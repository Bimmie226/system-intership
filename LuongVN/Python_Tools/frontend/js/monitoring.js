"use strict";

(() => {
    const byId = (id) => document.getElementById(id);
    const groups = ["pods", "deployments", "services", "replicasets", "statefulsets", "daemonsets"];
    let pending = false;
    const text = (value) => value === null || value === undefined || value === "" ? "—" : String(value);
    const count = (value) => Number.isInteger(value) && value >= 0;
    const join = (items) => Array.isArray(items) && items.length ? items.map(text).join("\n") : "—";
    const ratio = (ready, desired) => `${text(ready)} / ${text(desired)}`;

    function node(tag, content, className) {
        const result = document.createElement(tag);
        if (content !== undefined) result.textContent = text(content);
        if (className) result.className = className;
        return result;
    }

    function badge(label, tone = "neutral") {
        const result = node("span", label, "health-badge");
        result.dataset.tone = tone;
        return result;
    }

    function readiness(ready, desired) {
        if (!count(desired)) return badge("Chưa rõ");
        if (desired === 0) return badge("Desired = 0");
        if (!count(ready)) return badge("Chưa rõ");
        return ready >= desired ? badge("Đủ ready", "good") : badge("Chưa đủ ready", "warn");
    }

    function podStatus(pod) {
        if (pod.phase === "Succeeded") return badge("Succeeded", "good");
        if (pod.phase === "Failed") return badge("Failed", "bad");
        if (pod.phase === "Pending") return badge("Pending", "warn");
        if (pod.phase !== "Running") return badge(pod.phase || "Chưa rõ");
        if (!count(pod.total_containers) || pod.total_containers === 0 || !count(pod.ready_containers)) return badge("Running · chưa rõ readiness");
        return pod.ready_containers === pod.total_containers ? badge("Running · Ready", "good") : badge("Running · chưa Ready", "warn");
    }

    function nodeReady(item) {
        return (Array.isArray(item.conditions) ? item.conditions : []).find((condition) => condition?.condition_type === "Ready")?.condition_status;
    }

    function conditions(items) {
        if (!Array.isArray(items) || !items.length) return node("span", "Chưa có conditions");
        const list = node("ul", undefined, "condition-list");
        for (const condition of items) {
            if (!condition || typeof condition !== "object") continue;
            const item = node("li");
            const value = condition.condition_status;
            const type = condition.condition_type;
            const adverse = ["MemoryPressure", "DiskPressure", "PIDPressure", "NetworkUnavailable"].includes(type);
            let tone = "neutral";
            if (type === "Ready") tone = value === "True" ? "good" : value === "False" ? "bad" : "neutral";
            if (adverse) tone = value === "True" ? "warn" : value === "False" ? "good" : "neutral";
            item.append(node("strong", type), badge(value || "Unknown", tone));
            if (condition.reason || condition.message) {
                const details = node("details");
                details.append(node("summary", condition.reason || "Chi tiết"), node("p", condition.message || "Không có thông điệp."));
                item.append(details);
            }
            list.append(item);
        }
        return list;
    }

    function table(title, headers, rows) {
        if (!rows.length) return node("p", "Không có dữ liệu trong kết quả kiểm tra này.", "empty-state");
        const wrapper = node("div", undefined, "table-wrapper");
        wrapper.tabIndex = 0;
        wrapper.setAttribute("role", "region");
        wrapper.setAttribute("aria-label", `${title} — cuộn ngang để xem đủ cột`);
        const result = node("table");
        result.append(node("caption", title, "sr-only"));
        const head = node("thead");
        const heading = node("tr");
        for (const label of headers) {
            const cell = node("th", label);
            cell.scope = "col";
            heading.append(cell);
        }
        head.append(heading);
        const body = node("tbody");
        for (const values of rows) {
            const row = node("tr");
            for (const value of values) {
                const cell = node("td");
                if (value instanceof Node) cell.append(value);
                else cell.textContent = text(value);
                row.append(cell);
            }
            body.append(row);
        }
        result.append(head, body);
        wrapper.append(result);
        return wrapper;
    }

    const definitions = {
        pods: { title: "Pods", headers: ["Tên", "Phase / readiness", "Ready / total", "Restarts", "Tạo lúc"], row: (p) => [p.pod_name, podStatus(p), ratio(p.ready_containers, p.total_containers), p.restart_count, p.created_at] },
        deployments: { title: "Deployments", headers: ["Tên", "Readiness", "Ready / desired", "Current", "Updated", "Available"], row: (r) => [r.deployment_name, readiness(r.ready_replicas, r.desired_replicas), ratio(r.ready_replicas, r.desired_replicas), r.current_replicas, r.updated_replicas, r.available_replicas] },
        services: { title: "Services", headers: ["Tên", "Type", "Cluster IPs", "External IPs", "Ports / NodePort", "Kiểm tra kết nối"], row: (r) => [r.service_name, r.service_type, join(r.cluster_ips), join(r.external_ips), join((r.ports || []).map((p) => `${text(p.port)}/${text(p.protocol)}${p.node_port == null ? "" : ` → ${p.node_port}`}`)), "Chưa có dữ liệu"] },
        replicasets: { title: "ReplicaSets", headers: ["Tên", "Readiness", "Ready / desired", "Current"], row: (r) => [r.replicaset_name, readiness(r.ready_replicas, r.desired_replicas), ratio(r.ready_replicas, r.desired_replicas), r.current_replicas] },
        statefulsets: { title: "StatefulSets", headers: ["Tên", "Readiness", "Ready / desired", "Current"], row: (r) => [r.statefulset_name, readiness(r.ready_replicas, r.desired_replicas), ratio(r.ready_replicas, r.desired_replicas), r.current_replicas] },
        daemonsets: { title: "DaemonSets", headers: ["Tên", "Readiness", "Ready / desired", "Current scheduled", "Updated", "Available", "Node selector"], row: (r) => [r.daemonset_name, readiness(r.ready, r.desired_scheduled), ratio(r.ready, r.desired_scheduled), r.current_scheduled, r.updated_scheduled, r.available, join(Object.entries(r.node_selector || {}).map(([key, value]) => `${key}=${value}`))] }
    };

    function render(payload, namespace) {
        const data = payload?.data;
        if (!data || payload.namespace !== namespace || data.namespace !== namespace || !["nodes", ...groups].every((key) => Array.isArray(data[key]) && data[key].every((item) => item && typeof item === "object" && !Array.isArray(item))) || !groups.every((key) => data[key].every((item) => item.namespace === namespace))) {
            throw new Error("Dữ liệu backend không đúng định dạng hoặc không khớp namespace đã chọn.");
        }
        // Build detached content first so malformed nested fields cannot expose partial results.
        const nodeTable = table("Nodes toàn cluster", ["Node", "Ready", "Conditions"], data.nodes.map((item) => {
            const ready = nodeReady(item);
            return [item.node_name, badge(ready === "True" ? "Ready" : ready === "False" ? "NotReady" : "Unknown", ready === "True" ? "good" : ready === "False" ? "bad" : "neutral"), conditions(item.conditions)];
        }));
        const fragment = document.createDocumentFragment();
        for (const key of groups) {
            const definition = definitions[key];
            const group = node("details", undefined, "card resource-group");
            group.id = `group-${key}`;
            group.open = true;
            const heading = node("summary", definition.title);
            heading.append(node("span", data[key].length, "pill"));
            group.append(heading, table(`${definition.title} · ${namespace}`, definition.headers, data[key].map(definition.row)));
            fragment.append(group);
        }
        byId("node-content").replaceChildren(nodeTable);
        byId("resource-groups").replaceChildren(fragment);
        byId("node-total").textContent = data.nodes.length;
        byId("node-ready").textContent = data.nodes.filter((item) => nodeReady(item) === "True").length;
        byId("pod-total").textContent = data.pods.length;
        byId("resource-total").textContent = groups.reduce((sum, key) => sum + data[key].length, 0);
        byId("snapshot-namespace").textContent = namespace;
        byId("snapshot-received").textContent = new Date().toLocaleString("vi-VN");
        byId("snapshot-run").textContent = text(payload.check_run_id);
        byId("snapshot-status").textContent = text(payload.status);
        byId("snapshot-source").textContent = payload.source === "redis" ? "Redis · dữ liệu cache" : payload.source === "k8s-api" ? "Kubernetes API" : "Nguồn chưa rõ";
        byId("cache-note").textContent = payload.source === "redis" ? "Đây là dữ liệu cache; backend chưa cung cấp thời điểm lấy snapshot gốc. Trạng thái lần kiểm tra có thể vẫn là RUNNING; không dùng trạng thái này để suy ra sức khỏe resource." : "Trạng thái thu thập là trạng thái lần kiểm tra, không phải sức khỏe của toàn bộ resource. Thời gian nhận phản hồi không phải thời điểm thu thập từng resource.";
        byId("monitoring-results").hidden = false;
    }

    function feedback(state, message) {
        byId("monitoring-feedback").dataset.state = state;
        byId("monitoring-feedback").textContent = message;
    }

    byId("monitoring-form").addEventListener("submit", async (event) => {
        event.preventDefault();
        if (pending) return;
        byId("monitoring-results").hidden = true;
        const namespace = byId("namespace").value.trim();
        let api;
        try {
            if (!/^[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?$/.test(namespace)) throw new Error("Namespace cần 1–63 ký tự chữ thường, số hoặc dấu -, bắt đầu và kết thúc bằng chữ hoặc số.");
            api = new URL(byId("monitoring-api").value.trim());
            if (!["http:", "https:"].includes(api.protocol) || api.username || api.password || api.search || api.hash) throw new Error("Địa chỉ API phải là HTTP/HTTPS và không chứa thông tin đăng nhập, query hoặc fragment.");
        } catch (error) {
            feedback("error", error instanceof TypeError ? "Địa chỉ API không hợp lệ." : error.message);
            return;
        }
        pending = true;
        byId("namespace").value = namespace;
        byId("monitoring-controls").disabled = true;
        byId("check-button").textContent = "Đang kiểm tra…";
        byId("monitoring-results").setAttribute("aria-busy", "true");
        feedback("loading", `Đang kiểm tra namespace ${namespace} và node toàn cluster…`);
        const controller = new AbortController();
        const timer = setTimeout(() => controller.abort(), 60000);
        try {
            let response;
            try {
                response = await fetch(`${api.href.replace(/\/$/, "")}/api/monitoring/${encodeURIComponent(namespace)}/check`, { method: "POST", signal: controller.signal });
            } catch (error) {
                if (error.name === "AbortError") throw new Error("Chờ quá 60 giây. Backend có thể vẫn đang xử lý; hãy kiểm tra kết nối trước khi thử lại.");
                throw new Error("Không kết nối được backend. Kiểm tra địa chỉ API, mạng và CORS. Khi chạy local, mở frontend tại http://127.0.0.1:5500 hoặc http://localhost:5500.");
            }
            if (!response.ok) throw new Error(`Không lấy được trạng thái (HTTP ${response.status}). Kiểm tra namespace, quyền Kubernetes và các dịch vụ backend.`);
            let payload;
            try { payload = await response.json(); } catch { throw new Error("Backend không trả về JSON hợp lệ hoặc kết nối bị gián đoạn."); }
            render(payload, namespace);
            const resourceCount = groups.reduce((sum, key) => sum + payload.data[key].length, 0);
            feedback(resourceCount ? "success" : "empty", resourceCount ? `Đã nhận ${resourceCount} resource trong namespace ${namespace} và ${payload.data.nodes.length} node toàn cluster.` : `Không có resource thuộc sáu nhóm được theo dõi trong namespace ${namespace}. Danh sách node toàn cluster hiển thị riêng bên dưới.`);
        } catch (error) {
            feedback("error", error instanceof TypeError ? "Dữ liệu chi tiết từ backend không đúng định dạng." : error.message);
        } finally {
            clearTimeout(timer);
            pending = false;
            byId("monitoring-controls").disabled = false;
            byId("check-button").textContent = "Kiểm tra trạng thái";
            byId("monitoring-results").setAttribute("aria-busy", "false");
        }
    });
})();
