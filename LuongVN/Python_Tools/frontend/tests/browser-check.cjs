// No dependencies. Run: node frontend/tests/browser-check.cjs
// Uses an installed Chrome/Edge and a local mock API; never contacts Kubernetes.
const assert = require('node:assert/strict');
const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');
const os = require('node:os');
const { spawn } = require('node:child_process');

const root = path.resolve(__dirname, '..');
const browserPath = process.env.BROWSER_PATH || [
    'C:/Program Files/Google/Chrome/Application/chrome.exe',
    'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'
].find(fs.existsSync);
if (!browserPath) throw new Error('Set BROWSER_PATH to an installed Chrome or Edge executable.');
const profile = fs.mkdtempSync(path.join(os.tmpdir(), 'k8s-frontend-browser-'));
let mode = 'success';
const requests = [];
const errors = [];
const pause = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
function monitoringFixture(namespace) {
    const workload = { namespace, desired_replicas: 2, current_replicas: 2, ready_replicas: 1 };
    const data = {
        namespace,
        nodes: [
            { node_name: '<img src=x onerror=alert(1)>', conditions: [{ condition_type: 'Ready', condition_status: 'True', reason: 'KubeletReady', message: '<script>unsafe()</script>' }, { condition_type: 'DiskPressure', condition_status: 'True' }] },
            { node_name: 'worker-2', conditions: [{ condition_type: 'Ready', condition_status: 'False' }] },
            { node_name: 'worker-unknown', conditions: [] }
        ],
        pods: [
            { namespace, pod_name: 'web-pod', phase: 'Running', ready_containers: 1, total_containers: 2, restart_count: 3 },
            { namespace, pod_name: 'job-pod', phase: 'Succeeded', ready_containers: 0, total_containers: 1, restart_count: 0 }
        ],
        deployments: [{ ...workload, deployment_name: 'web', updated_replicas: 1, available_replicas: 1 }],
        services: [{ namespace, service_name: 'web-svc', service_type: 'NodePort', cluster_ips: ['10.0.0.1'], external_ips: [], ports: [{ port: 80, node_port: 30080, protocol: 'TCP' }] }],
        replicasets: [{ ...workload, replicaset_name: 'web-rs', ready_replicas: null }],
        statefulsets: [{ ...workload, statefulset_name: 'db', desired_replicas: 0, ready_replicas: null }],
        daemonsets: [{ namespace, daemonset_name: 'agent', desired_scheduled: 2, current_scheduled: 2, ready: 2, updated_scheduled: 2, available: 2, node_selector: { 'kubernetes.io/os': 'linux' } }]
    };
    if (mode === 'empty') for (const key of Object.keys(data)) if (Array.isArray(data[key])) data[key] = [];
    if (mode === 'mismatch') data.namespace = 'other-namespace';
    return { namespace, source: mode === 'cache' ? 'redis' : 'k8s-api', check_run_id: 42, status: mode === 'cache' ? 'RUNNING' : 'SUCCESS', data };
}
const server = http.createServer(async (req, res) => {
    if (req.url.startsWith('/api/')) {
        let body = '';
        for await (const chunk of req) body += chunk;
        requests.push({ url: req.url, method: req.method, headers: req.headers, body });
        await pause(150);
        if (mode === 'network') return req.socket.destroy();
        if (mode === 'nonjson') { res.writeHead(502); return res.end('upstream unavailable'); }
        res.setHeader('Content-Type', 'application/json');
        if (req.url.startsWith('/api/monitoring/')) {
            if (mode === 'error') { res.writeHead(500); return res.end(JSON.stringify({ detail: 'secret-value' })); }
            if (mode === 'invalidjson') return res.end('not json');
            if (mode === 'malformed') return res.end(JSON.stringify({ data: {} }));
            return res.end(JSON.stringify(monitoringFixture(decodeURIComponent(req.url.split('/')[3]))));
        }
        if (mode === 'error') { res.writeHead(400); return res.end(JSON.stringify({ detail: 'Invalid YAML: secret-value' })); }
        if (mode === 'malformed') return res.end(JSON.stringify({ message: 'unexpected' }));
        return res.end(JSON.stringify({ total: mode === 'empty' ? 0 : 1, results: mode === 'empty' ? [] : [
            { name: '<img src=x onerror=alert(1)>', kind: 'ConfigMap', namespace: null, api_version: 'v1', status: 'APPLIED' }
        ] }));
    }
    const files = { '/': ['index.html', 'text/html'], '/index.html': ['index.html', 'text/html'], '/css/styles.css': ['css/styles.css', 'text/css'], '/js/app.js': ['js/app.js', 'text/javascript'], '/monitoring.html': ['monitoring.html', 'text/html'], '/css/monitoring.css': ['css/monitoring.css', 'text/css'], '/js/monitoring.js': ['js/monitoring.js', 'text/javascript'] };
    const file = files[req.url];
    if (!file) { res.writeHead(404); return res.end(); }
    res.setHeader('Content-Type', `${file[1]}; charset=utf-8`);
    res.end(fs.readFileSync(path.join(root, file[0])));
});

let browser;
let socket;
async function run() {
    await new Promise((resolve) => server.listen(0, '127.0.0.1', resolve));
    const origin = `http://127.0.0.1:${server.address().port}`;
    browser = spawn(browserPath, ['--headless=new', '--disable-gpu', '--no-first-run', '--no-default-browser-check', '--remote-debugging-port=0', `--user-data-dir=${profile}`, 'about:blank'], { windowsHide: true, stdio: 'ignore' });
    browser.on('error', (error) => errors.push(error.message));
    const portFile = path.join(profile, 'DevToolsActivePort');
    for (let i = 0; !fs.existsSync(portFile) && i < 100; i++) await pause(100);
    const port = fs.readFileSync(portFile, 'utf8').split('\n')[0];
    const pages = await (await fetch(`http://127.0.0.1:${port}/json`)).json();
    socket = new WebSocket(pages.find((page) => page.type === 'page').webSocketDebuggerUrl);
    await new Promise((resolve, reject) => { socket.onopen = resolve; socket.onerror = reject; });
    let sequence = 0;
    const waiting = new Map();
    socket.onmessage = ({ data }) => {
        const message = JSON.parse(data);
        if (message.method === 'Runtime.exceptionThrown') errors.push(message.params.exceptionDetails.text);
        if (message.id) {
            const callback = waiting.get(message.id);
            waiting.delete(message.id);
            if (callback) callback(message);
        }
    };
    const command = (method, params = {}) => new Promise((resolve, reject) => {
        const id = ++sequence;
        const timeout = setTimeout(() => { waiting.delete(id); reject(new Error(`CDP timeout: ${method}`)); }, 10000);
        waiting.set(id, (message) => { clearTimeout(timeout); message.error ? reject(new Error(message.error.message)) : resolve(message.result); });
        socket.send(JSON.stringify({ id, method, params }));
    });
    const evaluate = async (expression) => {
        const result = await command('Runtime.evaluate', { expression, returnByValue: true, awaitPromise: true });
        if (result.exceptionDetails) throw new Error(result.exceptionDetails.text);
        return result.result.value;
    };
    const until = async (expression) => {
        for (let i = 0; i < 100; i++) { if (await evaluate(expression)) return; await pause(50); }
        throw new Error(`Timed out: ${expression}`);
    };
    await command('Runtime.enable');
    await command('Page.enable');
    await command('Page.navigate', { url: origin });
    await until('document.readyState === "complete" && typeof submitManifest === "function"');
    await evaluate(`element('api-url').value = ${JSON.stringify(origin)}`);
    assert.equal(requests.length, 0, 'No automatic apply on page load');
    await evaluate("element('submit-button').click()");
    assert.equal(requests.length, 0, 'Empty YAML must not be submitted');
    const tabBehavior = await evaluate(`(() => {
        const editor = element('manifest');
        editor.value = 'metadata:';
        editor.focus();
        editor.setSelectionRange(editor.value.length, editor.value.length);
        editor.dispatchEvent(new KeyboardEvent('keydown', { key: 'Tab', bubbles: true, cancelable: true }));
        return { value: editor.value, cursor: editor.selectionStart, focused: document.activeElement === editor };
    })()`);
    assert.deepEqual(tabBehavior, { value: 'metadata:  ', cursor: 11, focused: true }, 'Tab inserts two spaces and retains editor focus');
    const yaml = 'apiVersion: v1\nkind: ConfigMap\nmetadata:\n  name: example';
    await evaluate(`element('manifest').value = ${JSON.stringify(yaml)}; element('submit-button').click(); element('submit-button').click()`);
    assert.equal(await evaluate("element('controls').disabled"), true);
    await until('!pending');
    assert.equal(requests.length, 1, 'Duplicate submissions blocked');
    assert.equal(requests[0].url, '/api/manifest/apply');
    assert.deepEqual(JSON.parse(requests[0].body), { manifest: yaml });
    assert.equal(await evaluate("element('feedback').dataset.state"), 'success');
    assert.equal(await evaluate("element('result-rows').querySelectorAll('img').length"), 0, 'Resource values must be text');
    assert.ok(await evaluate("element('result-rows').textContent.includes('Cluster-scoped')"));
    for (const width of [375, 768, 1440]) {
        await command('Emulation.setDeviceMetricsOverride', { width, height: 1000, deviceScaleFactor: 1, mobile: false });
        assert.equal(await evaluate('document.documentElement.scrollWidth <= innerWidth'), true, `No page overflow at ${width}px`);
        assert.equal(await evaluate("element('submit-button').getBoundingClientRect().width > 0"), true);
        const screenshot = await command('Page.captureScreenshot', { format: 'png', captureBeyondViewport: true });
        fs.writeFileSync(path.join(profile, `viewport-${width}.png`), Buffer.from(screenshot.data, 'base64'));
    }
    await evaluate("element('file-mode').click(); const transfer = new DataTransfer(); transfer.items.add(new File(['kind: ConfigMap'], 'example.yaml', {type: 'application/yaml'})); element('manifest-file').files = transfer.files; element('manifest-file').dispatchEvent(new Event('change')); element('submit-button').click()");
    await until('!pending');
    assert.equal(requests[1].url, '/api/manifest/apply-file');
    assert.match(requests[1].headers['content-type'], /^multipart\/form-data; boundary=/);
    assert.match(requests[1].body, /name="file"; filename="example.yaml"/);
    await evaluate("element('text-mode').click()");
    for (const state of ['empty', 'error', 'nonjson', 'malformed', 'network']) {
        mode = state;
        await evaluate("element('submit-button').click()");
        await until('!pending');
        assert.equal(await evaluate("element('feedback').dataset.state"), state === 'empty' ? 'empty' : 'error');
        assert.equal(await evaluate("element('manifest').value"), yaml, 'Preserve user input');
        assert.equal(await evaluate("element('controls').disabled"), false);
        assert.equal(await evaluate("element('table-wrapper').hidden"), true);
        assert.equal(await evaluate("element('feedback').textContent.includes('secret-value')"), false);
    }
    mode = 'success';
    const beforeMonitoring = requests.length;
    await evaluate("document.querySelector('a[href=\"monitoring.html\"]').click()");
    await until('document.readyState === "complete" && !!document.getElementById("monitoring-form")');
    assert.equal(requests.length, beforeMonitoring, 'Monitoring must wait for explicit submit');
    await evaluate(`document.getElementById('monitoring-api').value = ${JSON.stringify(origin)}; document.getElementById('namespace').value = 'bad/name'; document.getElementById('check-button').click()`);
    assert.equal(requests.length, beforeMonitoring, 'Reject invalid namespace locally');
    await evaluate("document.getElementById('namespace').value = 'demo'; document.getElementById('check-button').click(); document.getElementById('check-button').click()");
    assert.equal(await evaluate("document.getElementById('monitoring-feedback').dataset.state"), 'loading');
    assert.equal(await evaluate("document.getElementById('monitoring-controls').disabled"), true);
    await until("!document.getElementById('monitoring-controls').disabled");
    assert.equal(requests.length, beforeMonitoring + 1, 'Monitoring duplicate submissions blocked');
    assert.equal(requests.at(-1).url, '/api/monitoring/demo/check');
    assert.equal(requests.at(-1).method, 'POST');
    assert.equal(requests.at(-1).body, '');
    assert.equal(await evaluate("document.getElementById('monitoring-feedback').dataset.state"), 'success');
    assert.equal(await evaluate("document.getElementById('node-total').textContent"), '3');
    assert.equal(await evaluate("document.getElementById('node-ready').textContent"), '1');
    assert.equal(await evaluate("document.getElementById('resource-total').textContent"), '7');
    assert.equal(await evaluate("document.querySelectorAll('#resource-groups > details').length"), 6);
    assert.equal(await evaluate("document.querySelectorAll('#monitoring-results img, #monitoring-results script').length"), 0);
    assert.ok(await evaluate("document.getElementById('node-content').textContent.includes('Unknown')"));
    assert.ok(await evaluate("document.getElementById('node-content').textContent.includes('NotReady')"));
    assert.ok(await evaluate("document.querySelector('#group-replicasets .health-badge').textContent.includes('Chưa rõ')"));
    assert.equal(await evaluate("document.querySelector('#group-statefulsets .health-badge').textContent"), 'Desired = 0');
    assert.ok(await evaluate("document.getElementById('group-services').textContent.includes('30080')"));
    assert.ok(await evaluate("document.getElementById('group-services').textContent.includes('Chưa có dữ liệu')"));
    assert.equal(await evaluate("document.querySelector('#group-pods .health-badge').dataset.tone"), 'warn');
    assert.equal(await evaluate("document.querySelector('#group-daemonsets .health-badge').dataset.tone"), 'good');
    for (const width of [375, 768, 1440]) {
        await command('Emulation.setDeviceMetricsOverride', { width, height: 1000, deviceScaleFactor: 1, mobile: false });
        assert.equal(await evaluate('document.documentElement.scrollWidth <= innerWidth'), true, `Monitoring page overflow at ${width}px`);
        assert.ok(await evaluate("document.getElementById('check-button').getBoundingClientRect().width > 0"));
        const screenshot = await command('Page.captureScreenshot', { format: 'png', captureBeyondViewport: true });
        fs.writeFileSync(path.join(profile, `monitoring-${width}.png`), Buffer.from(screenshot.data, 'base64'));
    }
    mode = 'cache';
    await evaluate("document.getElementById('check-button').click()");
    await until("!document.getElementById('monitoring-controls').disabled");
    assert.ok(await evaluate("document.getElementById('snapshot-source').textContent.includes('Redis')"));
    assert.equal(await evaluate("document.getElementById('snapshot-status').textContent"), 'RUNNING');
    assert.equal(await evaluate("document.getElementById('monitoring-results').hidden"), false, 'Cached RUNNING does not suppress snapshot');
    for (const state of ['empty', 'error', 'nonjson', 'invalidjson', 'malformed', 'mismatch', 'network']) {
        mode = state;
        await evaluate("document.getElementById('check-button').click()");
        assert.equal(await evaluate("document.getElementById('monitoring-results').hidden"), true, 'Hide old namespace snapshot while loading');
        await until("!document.getElementById('monitoring-controls').disabled");
        assert.equal(await evaluate("document.getElementById('monitoring-feedback').dataset.state"), state === 'empty' ? 'empty' : 'error');
        assert.equal(await evaluate("document.getElementById('monitoring-results').hidden"), state !== 'empty');
        assert.equal(await evaluate("document.getElementById('namespace').value"), 'demo');
        assert.equal(await evaluate("document.getElementById('monitoring-feedback').textContent.includes('secret-value')"), false);
        if (state === 'empty') assert.equal(await evaluate("document.querySelectorAll('#resource-groups .empty-state').length"), 6);
    }
    await evaluate("document.querySelector('nav a[href=\"index.html\"]').click()");
    await until('document.readyState === "complete" && typeof submitManifest === "function"');
    assert.deepEqual(errors, [], 'No uncaught browser JavaScript exceptions');
    console.log('PASS: manifest and monitoring API contracts, keyboard input, navigation, duplicate prevention, safe rendering, readiness/unknown/scaled-zero states, cache metadata, loading/empty/errors, namespace validation, responsive widths, browser exceptions.');
    console.log(`Screenshots: ${profile}`);
}

run().catch((error) => { console.error(error); process.exitCode = 1; }).finally(async () => {
    if (socket) socket.close();
    if (browser) browser.kill();
    server.closeAllConnections();
    server.close();
});
