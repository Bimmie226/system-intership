"use strict";

const element = (id) => document.getElementById(id);
const YAML_INDENT = "  ";
let inputMode = "text";
let pending = false;

function setMode(mode) {
    if (pending) return;
    inputMode = mode;
    for (const value of ["text", "file"]) {
        const selected = value === mode;
        element(`${value}-mode`).setAttribute("aria-pressed", String(selected));
        element(`${value}-mode`).classList.toggle("selected", selected);
        element(`${value}-panel`).hidden = !selected;
    }
}

function feedback(state, message, badge) {
    element("feedback").dataset.state = state;
    element("feedback").textContent = message;
    element("result-badge").textContent = badge;
}

function errorDetail(data, status) {
    // Validation messages are useful; arbitrary server errors may contain secrets
    // or echoed manifest bodies, so do not display their raw contents.
    if (status >= 500) return `Backend gặp lỗi (HTTP ${status}). Kiểm tra YAML, quyền truy cập và kết nối Kubernetes.`;
    const detail = data && data.detail;
    if (Array.isArray(detail)) {
        return detail.map((item) => typeof item.msg === "string" ? item.msg : "Dữ liệu không hợp lệ.").join("\n");
    }
    if (typeof detail === "string") {
        if (detail.startsWith("Invalid YAML:")) return "YAML không hợp lệ. Kiểm tra cú pháp và thụt dòng.";
        if (detail === "Manifest file is empty") return "File manifest không chứa resource.";
        if (detail === "Only .yaml and .yml files are allowed") return "Chỉ chấp nhận file .yaml hoặc .yml.";
    }
    return `Yêu cầu không thành công (HTTP ${status}). Kiểm tra nội dung manifest và cấu hình backend.`;
}

function renderResults(data) {
    if (!data || !Array.isArray(data.results) || !data.results.every((row) => row && typeof row === "object")) {
        throw new Error("Backend trả về kết quả không đúng định dạng. Kiểm tra trạng thái cluster trước khi gửi lại.");
    }
    const rows = element("result-rows");
    rows.replaceChildren();
    for (const result of data.results) {
        const row = document.createElement("tr");
        const values = [result.name, result.kind, result.namespace ?? "Cluster-scoped", result.api_version, result.status];
        values.forEach((value, index) => {
            const cell = document.createElement("td");
            if (index === 4 && value === "APPLIED") {
                const badge = document.createElement("span");
                badge.className = "resource-status";
                badge.textContent = "APPLIED";
                cell.append(badge);
            } else {
                cell.textContent = String(value ?? "—");
            }
            row.append(cell);
        });
        rows.append(row);
    }
    element("table-wrapper").hidden = data.results.length === 0;
    element("result-summary").textContent = `${data.results.length} resource được trả về · ${new Date().toLocaleTimeString("vi-VN")}`;
    if (data.results.length === 0) {
        feedback("empty", "Không có resource nào được áp dụng. Kiểm tra manifest có nội dung ngoài chú thích và dấu phân cách.", "Không có resource");
    } else {
        feedback("success", "Backend đã xử lý manifest. Xem trạng thái từng resource bên dưới; APPLIED không đồng nghĩa workload đã sẵn sàng.", "Đã xử lý");
    }
}

async function submitManifest(event) {
    event.preventDefault();
    if (pending) return;
    let baseUrl;
    let options;
    try {
        baseUrl = new URL(element("api-url").value.trim());
        if (!["http:", "https:"].includes(baseUrl.protocol) || baseUrl.username || baseUrl.password || baseUrl.search || baseUrl.hash) {
            throw new Error("Địa chỉ backend phải là HTTP/HTTPS, không chứa thông tin đăng nhập, query hoặc fragment.");
        }
        if (inputMode === "text") {
            const manifest = element("manifest").value;
            if (!manifest.trim()) throw new Error("Hãy nhập nội dung YAML trước khi apply.");
            options = { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ manifest }) };
        } else {
            const file = element("manifest-file").files[0];
            if (!file) throw new Error("Hãy chọn file manifest trước khi apply.");
            if (!/\.(yaml|yml)$/.test(file.name)) throw new Error("Tên file phải kết thúc bằng .yaml hoặc .yml (chữ thường).");
            if (file.size === 0) throw new Error("File đang trống. Hãy chọn file có nội dung YAML.");
            const body = new FormData();
            body.append("file", file);
            options = { method: "POST", body };
        }
    } catch (error) {
        element("table-wrapper").hidden = true;
        element("result-summary").textContent = "Chưa gửi yêu cầu mới đến backend.";
        feedback("error", error instanceof TypeError ? "Địa chỉ backend không hợp lệ." : error.message, "Kiểm tra dữ liệu");
        return;
    }

    pending = true;
    element("controls").disabled = true;
    element("results-section").setAttribute("aria-busy", "true");
    element("submit-label").textContent = "Đang apply…";
    element("table-wrapper").hidden = true;
    element("result-rows").replaceChildren();
    element("result-summary").textContent = "Đang chờ backend xử lý manifest.";
    feedback("loading", "Đang áp dụng manifest. Vui lòng chờ và không gửi lại yêu cầu.", "Đang xử lý");

    try {
        const endpoint = inputMode === "text" ? "/api/manifest/apply" : "/api/manifest/apply-file";
        let response;
        try {
            response = await fetch(`${baseUrl.href.replace(/\/$/, "")}${endpoint}`, options);
        } catch {
            throw new Error("Không nhận được phản hồi từ backend. Kiểm tra địa chỉ API, kết nối mạng và CORS. Khi chạy local, mở giao diện tại http://127.0.0.1:5500 hoặc http://localhost:5500.");
        }
        let data;
        try { data = await response.json(); } catch { data = null; }
        if (!response.ok) throw new Error(errorDetail(data, response.status));
        renderResults(data);
    } catch (error) {
        element("result-summary").textContent = "Không xác nhận được toàn bộ kết quả triển khai.";
        feedback("error", `${error.message}\nMột số resource có thể đã được áp dụng. Kiểm tra cluster trước khi gửi lại; nội dung nhập vẫn được giữ nguyên.`, "Không hoàn tất");
    } finally {
        pending = false;
        element("controls").disabled = false;
        element("results-section").setAttribute("aria-busy", "false");
        element("submit-label").textContent = "Apply Manifest";
    }
}

element("text-mode").addEventListener("click", () => setMode("text"));
element("file-mode").addEventListener("click", () => setMode("file"));
element("manifest-form").addEventListener("submit", submitManifest);
element("manifest").addEventListener("keydown", (event) => {
    if (event.key !== "Tab" || event.shiftKey || event.ctrlKey || event.altKey || event.metaKey) return;

    event.preventDefault();
    const editor = event.currentTarget;
    editor.setRangeText(YAML_INDENT, editor.selectionStart, editor.selectionEnd, "end");
});
element("manifest").addEventListener("input", () => {
    element("line-count").textContent = `${element("manifest").value.split("\n").length} dòng`;
});
element("manifest-file").addEventListener("change", () => {
    const file = element("manifest-file").files[0];
    element("file-info").textContent = file ? `${file.name} · ${(file.size / 1024).toFixed(1)} KB` : "Chưa chọn file.";
});
