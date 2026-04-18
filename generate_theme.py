from pathlib import Path

base = Path(r"c:\Users\Rohan.Sancheti\Documents\Durga Steel")

steps = [
    ("Need", "procurement-need.html"),
    ("Vendor", "vendor.html"),
    ("PO", "po.html"),
    ("GRN", "grn.html"),
    ("QC", "qc-rm.html"),
    ("RM", "inventory-rm.html"),
    ("Product", "product-master.html"),
    ("Inquiry", "inquiry.html"),
    ("SO", "sales-order.html"),
    ("MRP", "mrp.html"),
    ("Production", "production.html"),
    ("FG", "inventory-fg.html"),
    ("Allocation", "allocation.html"),
    ("Dispatch", "dispatch.html"),
    ("Billing", "billing.html"),
    ("Delivery", "delivery.html"),
]

menu_groups = [
    ("Overview", "bi-grid-1x2-fill", [
        ("Dashboard", "dashboard.html", "bi-grid-1x2-fill"),
        ("Reports", "reports.html", "bi-bar-chart-line"),
    ]),
    ("Procurement", "bi-cart-check", [
        ("Procurement Need", "procurement-need.html", "bi-exclamation-diamond"),
        ("Vendor", "vendor.html", "bi-building-add"),
        ("Procurement (PO)", "po.html", "bi-cart-check"),
        ("GRN", "grn.html", "bi-box-arrow-in-down"),
        ("QC (RM)", "qc-rm.html", "bi-clipboard2-check"),
        ("RM Inventory", "inventory-rm.html", "bi-box-seam"),
    ]),
    ("Sales", "bi-receipt-cutoff", [
        ("Product Master", "product-master.html", "bi-sliders"),
        ("Sales Inquiry", "inquiry.html", "bi-chat-left-dots"),
        ("Quotation", "quotation.html", "bi-file-earmark-richtext"),
        ("Sales Order", "sales-order.html", "bi-receipt-cutoff"),
        ("SO Allocation", "allocation.html", "bi-diagram-3"),
    ]),
    ("Planning & Production", "bi-gear-wide-connected", [
        ("MRP", "mrp.html", "bi-diagram-2"),
        ("Production", "production.html", "bi-gear-wide-connected"),
        ("FG QC", "qc-fg.html", "bi-patch-check"),
        ("FG Inventory", "inventory-fg.html", "bi-archive"),
    ]),
    ("Dispatch & Finance", "bi-truck", [
        ("Dispatch", "dispatch.html", "bi-truck"),
        ("Billing", "billing.html", "bi-cash-coin"),
        ("Delivery", "delivery.html", "bi-sign-turn-right"),
    ]),
]

css = r"""
:root {
  --bg-main: #eaf1fb;
  --bg-panel: #ffffff;
  --bg-soft: #edf4ff;
  --bg-tint: linear-gradient(135deg, #f6faff 0%, #e7effb 100%);
  --line: #c8d5e8;
  --text-main: #102a43;
  --text-soft: #4f627b;
  --accent: #2563eb;
  --accent-2: #1d4ed8;
  --ok: #22c55e;
  --warn: #f59e0b;
  --bad: #ef4444;
  --shadow: 0 10px 30px rgba(37, 99, 235, 0.10);
  --tr: all .28s ease;
}
* { box-sizing: border-box; }
html, body { height: 100%; }
body {
  margin: 0;
  font-family: Inter, sans-serif;
  color: var(--text-main);
  background: linear-gradient(180deg, #f2f7ff 0%, var(--bg-main) 100%);
  animation: pageFade .35s ease-out;
}
.app { display: flex; min-height: 100vh; }
.sidebar { position: fixed; inset: 0 auto 0 0; width: 282px; overflow-y: auto; background: #eef4fd; border-right: 1px solid var(--line); padding: 1rem .95rem; }
.brand { display:flex; align-items:center; justify-content:space-between; gap:.6rem; padding:.2rem .35rem 1rem; }
.brand-left { display:flex; align-items:center; gap:.7rem; }
.brand-mark { width:42px; height:42px; border-radius:12px; display:inline-flex; align-items:center; justify-content:center; background: #e8f1fb; border:1px solid #c8d8ea; box-shadow:none; }
.brand-mark i { color: var(--accent); }
.brand-title { font-weight:700; font-size:1.02rem; letter-spacing:.01em; }
.brand-sub { color: var(--text-soft); font-size:.78rem; }
.menu-group { margin-bottom: .85rem; }
.menu-group-label {
  width: 100%; display:flex; align-items:center; justify-content:space-between; gap:.55rem; padding:.8rem .84rem;
  color: #3e4c62; font-size:.8rem; font-weight:700; border-radius:12px; border:1px solid var(--line);
  background: #fff; text-transform:uppercase; letter-spacing:.04em;
}
.menu-group-label:hover {
  background: #e3edfc;
  color: var(--accent-2);
}
.menu-group-title {
  display:flex; align-items:center; gap:.55rem;
  min-width: 0;
}
.menu-group-title .txt { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.menu-group-links { padding-left: .15rem; margin-top: .4rem; display:none; }
.menu-group.open .menu-group-links { display:block; }
.menu-chevron { transition: var(--tr); }
.menu-group.open .menu-chevron { transform: rotate(90deg); }
.nav-link.erp-link { color:#334e68; border-radius:10px; padding:.68rem .82rem; margin-bottom:.28rem; display:flex; gap:.72rem; align-items:center; transition:var(--tr); font-size:.92rem; }
.nav-link.erp-link:hover { color:var(--accent-2); background:#e2ecfb; transform:translateX(2px); }
.nav-link.erp-link.active { color:var(--accent-2); background:#dbe8fb; border:1px solid #b8cde6; box-shadow:0 4px 12px rgba(37,99,235,.12); font-weight:700; }
.submenu-link { margin-left: .35rem; padding-left: .7rem; }
.sidebar-footer { margin-top:1rem; padding:.9rem; border:1px solid var(--line); border-radius:12px; background:#fff; }
.main { width: calc(100% - 282px); margin-left: 282px; padding:1.1rem 1.6rem 2.2rem; }
.app.sidebar-collapsed .sidebar { width: 84px; padding: .9rem .55rem; }
.app.sidebar-collapsed .brand-copy, .app.sidebar-collapsed .txt, .app.sidebar-collapsed .sidebar-footer, .app.sidebar-collapsed .menu-chevron { display:none; }
.app.sidebar-collapsed .menu-group-links { display:none !important; }
.app.sidebar-collapsed .menu-group-label { justify-content:center; padding:.72rem; }
.app.sidebar-collapsed .menu-group-title { justify-content:center; }
.app.sidebar-collapsed .submenu-link { margin-left:0; padding-left:.7rem; }
.app.sidebar-collapsed .main { width: calc(100% - 84px); margin-left: 84px; }
.topbar { background: var(--bg-tint); border:1px solid var(--line); border-radius:12px; padding:.85rem 1rem; margin-bottom:1rem; position:sticky; top:10px; z-index:10; box-shadow:0 6px 18px rgba(37,99,235,.08); animation: riseIn .35s ease-out; }
.topbar-label { font-size:.72rem; color:var(--text-soft); text-transform:uppercase; letter-spacing:.08em; font-weight:700; }
.topbar-title { font-weight:700; letter-spacing:.01em; font-size:1.15rem; }
.panel { background: var(--bg-panel); border:1px solid var(--line); border-radius:12px; box-shadow:var(--shadow); padding:1rem; transition:border-color .2s ease, box-shadow .2s ease, transform .2s ease; animation: riseIn .35s ease-out; }
.panel:hover { transform:translateY(-2px); border-color:#c5d6e7; box-shadow:0 14px 26px rgba(37,99,235,.10); }
.hero-grid .panel { background: var(--bg-tint); }
.hero-grid { display:grid; grid-template-columns: 1fr; gap:1rem; }
.metric-strip { display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:.85rem; }
.metric { border:1px solid var(--line); border-radius:10px; padding:.9rem; background:var(--bg-soft); transition:var(--tr); }
.metric:hover { border-color:#bfd2ef; background:#f1f7ff; }
.section-title { font-size:1.03rem; font-weight:700; margin-bottom:1rem; letter-spacing:.01em; }
.small-muted { font-size:.88rem; color:var(--text-soft); line-height:1.55; }
.input-group-text,.form-control,.form-select { background:#fff; border:1px solid #c8d4e3; color:var(--text-main); border-radius:8px; }
.form-control::placeholder { color:var(--text-soft); }
.form-control:focus,.form-select:focus { background:#fff; color:var(--text-main); border-color:#7fb1e3; box-shadow:0 0 0 .14rem rgba(10,110,209,.12); }
.form-label { font-size:.84rem; font-weight:700; color:var(--text-soft); text-transform:uppercase; letter-spacing:.05em; margin-bottom:.45rem; }
.btn.erp-primary { border:1px solid var(--accent-2); background:var(--accent); padding:.62rem .92rem; border-radius:8px; font-weight:700; }
.btn.erp-primary:hover { transform:translateY(-1px); box-shadow:0 8px 16px rgba(37,99,235,.18); background:var(--accent-2); }
.btn.glass-btn { border:1px solid #c8d4e3; background:#fff; color:var(--text-main); padding:.62rem .92rem; border-radius:8px; font-weight:600; }
.btn-sm { border-radius:8px; }
.table.erp { --bs-table-bg:transparent; --bs-table-color:var(--text-main); --bs-table-border-color:#dde6f0; }
.table.erp thead th { font-size:.75rem; text-transform:uppercase; letter-spacing:.06em; color:var(--text-soft); border-bottom-width:1px; background:#f5f8fc; }
.table.erp td { padding-top:.95rem; padding-bottom:.95rem; vertical-align:middle; }
.table.erp tbody tr:hover { background:#f7fbff; }
.badge-soft { border:1px solid transparent; font-weight:700; padding:.45rem .65rem; border-radius:999px; }
.badge-ok { background:#e8f7ee; color:#1f7a3d; border-color:#bfe3cb; }
.badge-pending { background:#fff4de; color:#9a6700; border-color:#f2d9a6; }
.badge-bad { background:#fdecec; color:#b42318; border-color:#f2c4c1; }
.workflow { display:flex; gap:.65rem; overflow-x:auto; padding-bottom:.2rem; }
.workflow-step { text-decoration:none; white-space:nowrap; border-radius:999px; padding:.5rem .88rem; border:1px solid #d4dfea; color:#4f637a; background:#fff; font-size:.8rem; font-weight:700; transition:var(--tr); }
.workflow-step.pending { opacity:.78; }
.workflow-step.done { color:#1f7a3d; border-color:#bfe3cb; background:#e8f7ee; }
.workflow-step.current { color:#0b3d6d; border-color:#9dc3e6; background:#e8f1fb; box-shadow:0 0 0 3px rgba(37,99,235,.08); animation: pulseSoft 2.2s infinite; }
.flow-grid { display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:.9rem; }
.flow-node { border:1px solid var(--line); border-radius:12px; padding:1rem; background:linear-gradient(180deg, #ffffff 0%, #f8fbff 100%); min-height:136px; }
.stat-image { border:1px solid var(--line); border-radius:12px; background:linear-gradient(180deg, #ffffff 0%, #f4f8ff 100%); padding:.8rem; }
.stat-image svg { width:100%; height:auto; display:block; }
.decision-card { border:1px solid #bcd1e6; border-radius:12px; padding:1rem; background:#f7fbff; }
.page-kicker { font-size:.78rem; text-transform:uppercase; letter-spacing:.08em; color:var(--accent); font-weight:700; margin-bottom:.35rem; }
.presenter-note { border-left:3px solid #a9c7e6; padding-left:.9rem; margin-top:.75rem; color:var(--text-soft); font-size:.86rem; }
.progress-track { display:flex; gap:.55rem; flex-wrap:wrap; }
.progress-pill { padding:.46rem .74rem; border-radius:999px; border:1px solid #d5dfeb; background:#fff; }
.progress-pill.done { background:#e8f7ee; border-color:#bfe3cb; color:#1f7a3d; }
.progress-pill.current { background:#e8f1fb; border-color:#b8d0e9; color:#0b3d6d; }
.machine-dot { width:10px; height:10px; display:inline-block; border-radius:50%; margin-right:.35rem; }
.machine-dot.run { background:var(--ok); animation:pulseDot 1.5s infinite; }
.machine-dot.stop { background:#64748b; }
.viz-grid { display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:.8rem; }
@keyframes pulseDot { 0% { box-shadow:0 0 0 0 rgba(34,197,94,.65);} 70% { box-shadow:0 0 0 9px rgba(34,197,94,0);} 100% { box-shadow:0 0 0 0 rgba(34,197,94,0);} }
@keyframes pageFade { from { opacity: .0; } to { opacity: 1; } }
@keyframes riseIn { from { opacity: .0; transform: translateY(6px);} to { opacity: 1; transform: translateY(0);} }
@keyframes pulseSoft { 0%,100% { box-shadow:0 0 0 0 rgba(37,99,235,.10);} 50% { box-shadow:0 0 0 4px rgba(37,99,235,.04);} }
@media (max-width:1100px) { .sidebar { width:92px; } .brand-copy,.txt,.sidebar-footer { display:none; } .main { width:calc(100% - 92px); margin-left:92px; } .hero-grid,.flow-grid,.viz-grid { grid-template-columns:1fr; } }
@media (max-width:768px) { .sidebar { width:100%; height:auto; inset:0 0 auto 0; border-right:0; border-bottom:1px solid var(--line); } .sidebar .nav { flex-direction:row !important; overflow-x:auto; white-space:nowrap; } .brand-copy,.sidebar-footer { display:none; } .main { width:100%; margin-left:0; padding-top:5.8rem; } .metric-strip { grid-template-columns:1fr; } }
"""

nav_script = """
<script>
(function () {
  document.addEventListener("DOMContentLoaded", function () {
    const app = document.querySelector(".app");
    const sidebarToggle = document.getElementById("sidebarToggle");
    const groups = document.querySelectorAll(".menu-group");
    const toggles = document.querySelectorAll("[data-menu-toggle]");

    if (sidebarToggle && app) {
      sidebarToggle.addEventListener("click", function () {
        app.classList.toggle("sidebar-collapsed");
        const collapsed = app.classList.contains("sidebar-collapsed");
        this.innerHTML = collapsed
          ? '<i class="bi bi-layout-sidebar"></i>'
          : '<i class="bi bi-layout-sidebar-inset"></i>';
      });
    }

    toggles.forEach(function (toggle) {
      toggle.addEventListener("click", function () {
        const target = this.getAttribute("data-menu-toggle");
        const group = document.querySelector('.menu-group[data-menu-group="' + target + '"]');
        const willOpen = group && !group.classList.contains("open");
        groups.forEach(function (g) { g.classList.remove("open"); });
        if (willOpen && group) {
          group.classList.add("open");
        }
      });
    });
  });
})();
</script>
"""


def render_sidebar(current_file: str) -> str:
    groups = []
    for idx, (group_label, group_icon, links) in enumerate(menu_groups):
        link_html = "".join(
            f'<li class="nav-item"><a class="nav-link erp-link submenu-link{" active" if file == current_file else ""}" href="{file}"><i class="bi {icon}"></i><span class="txt">{label}</span></a></li>'
            for label, file, icon in links
        )
        groups.append(
            f'<div class="menu-group" data-menu-group="{idx}"><button class="menu-group-label" type="button" data-menu-toggle="{idx}"><span class="menu-group-title"><i class="bi {group_icon}"></i><span class="txt">{group_label}</span></span><i class="bi bi-chevron-right menu-chevron"></i></button><ul class="nav flex-column menu-group-links">{link_html}</ul></div>'
        )
    return "".join(groups)


def render_stepper(current_file: str) -> str:
    if current_file not in [f for _, f in steps]:
        current_file = steps[0][1]
    idx = [f for _, f in steps].index(current_file)
    out = []
    for i, (label, file) in enumerate(steps):
        cls = "done" if i < idx else ("current" if i == idx else "pending")
        out.append(f'<a class="workflow-step {cls}" href="{file}">{label}</a>')
    return "".join(out)


def hero(title: str, subtitle: str, eyebrow: str, metrics: list[str]) -> str:
    metric_html = "".join(
        f'<div class="metric"><div class="small-muted">{a}</div><div class="fw-semibold mt-1">{b}</div></div>'
        for a, b in (m.split("|") for m in metrics)
    )
    return f"""
<section class="hero-grid mb-3">
  <div class="panel">
    <div class="page-kicker">{eyebrow}</div>
    <div class="d-flex justify-content-between align-items-start gap-3 flex-wrap">
      <div>
        <h2 class="mt-1 mb-2" style="font-size:1.75rem; font-weight:700; line-height:1.18;">{title}</h2>
        <p class="small-muted mb-0" style="max-width:720px;">{subtitle}</p>
      </div>
      <span class="badge badge-soft badge-ok">Enterprise View</span>
    </div>
    <div class="presenter-note">Standardized page summary with key operating indicators for review and decision-making.</div>
    <div class="metric-strip mt-3">{metric_html}</div>
  </div>
</section>
"""


def page(title: str, current_file: str, body: str, hero_block: str, scripts: str = "") -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} | SteelFlow ERP</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" />
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css" rel="stylesheet" />
  <style>{css}</style>
</head>
<body>
  <div class="app">
    <aside class="sidebar">
      <div class="brand"><div class="brand-left"><span class="brand-mark"><i class="bi bi-building-gear"></i></span><div class="brand-copy"><div class="brand-title">SteelFlow ERP</div><div class="brand-sub">Process-driven steel workflow</div></div></div></div>
      <ul class="nav flex-column">{render_sidebar(current_file)}</ul>
      <div class="sidebar-footer"><div class="small-muted text-uppercase">Operations Standard</div><div class="mt-2 fw-semibold">Source -> Plan -> Make -> Allocate -> Dispatch</div></div>
    </aside>
    <main class="main">
      <div class="topbar d-flex justify-content-between align-items-center gap-3">
        <div class="d-flex align-items-center gap-2"><button id="sidebarToggle" class="btn glass-btn" type="button" title="Hide or view sidebar"><i class="bi bi-layout-sidebar-inset"></i></button><div><div class="topbar-label">SteelFlow ERP</div><div class="topbar-title">{title}</div></div></div>
        <div class="d-flex align-items-center gap-2">
          <div class="input-group" style="max-width:340px;"><span class="input-group-text border-secondary"><i class="bi bi-search"></i></span><input class="form-control" placeholder="Search PO, SO, heat no, truck..." /></div>
          <button class="btn glass-btn" type="button"><i class="bi bi-bell"></i></button>
        </div>
      </div>
      <section class="panel mb-3">
        <div class="d-flex justify-content-between align-items-center mb-2"><div class="section-title mb-0">Workflow Stepper</div><span class="badge badge-soft badge-pending">Decision connected</span></div>
        <div class="workflow">{render_stepper(current_file)}</div>
      </section>
      {hero_block}
      {body}
    </main>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
  {scripts}
  {nav_script}
</body>
</html>
"""


pages = {
    "dashboard.html": page(
        "Management Dashboard",
        "dashboard.html",
        """
<section class="row g-3 mb-3">
  <div class="col-lg-3 col-md-6"><div class="panel h-100"><div class="small-muted">Monthly Revenue</div><div class="display-6 fw-bold mt-2">Rs. 8.42 Cr</div><div class="small-muted mt-2"><span class="text-success">+12.8%</span> vs last month</div></div></div>
  <div class="col-lg-3 col-md-6"><div class="panel h-100"><div class="small-muted">Open Sales Orders</div><div class="display-6 fw-bold mt-2">148</div><div class="small-muted mt-2">32 orders awaiting allocation</div></div></div>
  <div class="col-lg-3 col-md-6"><div class="panel h-100"><div class="small-muted">Production Attainment</div><div class="display-6 fw-bold mt-2">91.4%</div><div class="small-muted mt-2">3 lines running, 1 planned stop</div></div></div>
  <div class="col-lg-3 col-md-6"><div class="panel h-100"><div class="small-muted">OTIF Dispatch</div><div class="display-6 fw-bold mt-2">94.2%</div><div class="small-muted mt-2">6 trucks loading, 2 delayed</div></div></div>
</section>
<section class="row g-3 mb-3">
  <div class="col-lg-8"><div class="panel h-100">
    <div class="d-flex justify-content-between align-items-center mb-3"><div class="section-title mb-0">Executive Process Snapshot</div><a href="reports.html" class="btn glass-btn btn-sm">Open Reports</a></div>
    <div class="flow-grid">
      <div class="flow-node"><div class="fw-semibold">Procurement Health</div><div class="small-muted mt-2">12 open POs, 3 delayed GRNs, 1 RM lot on hold.</div></div>
      <div class="flow-node"><div class="fw-semibold">Demand Funnel</div><div class="small-muted mt-2">28 inquiries, 16 live quotations, 148 confirmed SOs.</div></div>
      <div class="flow-node"><div class="fw-semibold">Execution</div><div class="small-muted mt-2">Partial stock cases routed through allocation + MRP without breaking the flow.</div></div>
      <div class="flow-node"><div class="fw-semibold">Closure</div><div class="small-muted mt-2">Billing aging under control, 11 PODs pending customer upload.</div></div>
    </div>
  </div></div>
  <div class="col-lg-4"><div class="panel h-100">
    <div class="section-title">Management Attention</div>
    <div class="metric mb-2"><div class="small-muted">Critical RM</div><div class="fw-semibold mt-1 text-warning">HRC Coil E350 below reorder level</div></div>
    <div class="metric mb-2"><div class="small-muted">High Value SO</div><div class="fw-semibold mt-1">SO-2026-417 waiting credit release</div></div>
    <div class="metric"><div class="small-muted">FG Rework</div><div class="fw-semibold mt-1">2 batches returned from FG QC</div></div>
  </div></div>
</section>
<section class="row g-3 mb-3">
  <div class="col-lg-8"><div class="panel h-100">
    <div class="section-title">Management Statistical View (Last 6 Months)</div>
    <div class="stat-image">
      <svg viewBox="0 0 860 320" role="img" aria-label="Revenue and dispatch trend">
        <rect x="0" y="0" width="860" height="320" fill="#f8fbff"/>
        <line x1="60" y1="40" x2="60" y2="270" stroke="#c9d8ec"/>
        <line x1="60" y1="270" x2="820" y2="270" stroke="#c9d8ec"/>
        <line x1="60" y1="220" x2="820" y2="220" stroke="#e2ebf7"/>
        <line x1="60" y1="170" x2="820" y2="170" stroke="#e2ebf7"/>
        <line x1="60" y1="120" x2="820" y2="120" stroke="#e2ebf7"/>
        <line x1="60" y1="70" x2="820" y2="70" stroke="#e2ebf7"/>

        <polyline fill="none" stroke="#2563eb" stroke-width="4" points="90,210 210,198 330,182 450,166 570,148 690,132 810,118"/>
        <circle cx="810" cy="118" r="6" fill="#2563eb"/>
        <text x="818" y="110" font-size="12" fill="#1d4ed8">Revenue: Rs. 8.42 Cr</text>

        <polyline fill="none" stroke="#16a34a" stroke-width="4" points="90,236 210,228 330,212 450,201 570,188 690,176 810,160"/>
        <circle cx="810" cy="160" r="6" fill="#16a34a"/>
        <text x="818" y="154" font-size="12" fill="#15803d">Dispatch: 1,842 t</text>

        <text x="80" y="294" font-size="12" fill="#5f6f86">Nov</text>
        <text x="200" y="294" font-size="12" fill="#5f6f86">Dec</text>
        <text x="320" y="294" font-size="12" fill="#5f6f86">Jan</text>
        <text x="440" y="294" font-size="12" fill="#5f6f86">Feb</text>
        <text x="560" y="294" font-size="12" fill="#5f6f86">Mar</text>
        <text x="680" y="294" font-size="12" fill="#5f6f86">Apr</text>
        <text x="790" y="294" font-size="12" fill="#5f6f86">May</text>

        <text x="10" y="74" font-size="12" fill="#5f6f86">High</text>
        <text x="10" y="174" font-size="12" fill="#5f6f86">Mid</text>
        <text x="10" y="274" font-size="12" fill="#5f6f86">Low</text>
      </svg>
    </div>
  </div></div>
  <div class="col-lg-4"><div class="panel h-100">
    <div class="section-title">Management Highlights</div>
    <div class="metric mb-2"><div class="small-muted">Revenue trend</div><div class="fw-semibold mt-1 text-success">Consistent month-on-month growth</div></div>
    <div class="metric mb-2"><div class="small-muted">Dispatch trend</div><div class="fw-semibold mt-1">Throughput improving with planning stability</div></div>
    <div class="metric"><div class="small-muted">Action point</div><div class="fw-semibold mt-1">Protect OTIF while scaling high-value orders</div></div>
  </div></div>
</section>
<section class="row g-3">
  <div class="col-lg-7"><div class="panel h-100">
    <div class="section-title">Plant Performance Summary</div>
    <div class="table-responsive"><table class="table erp align-middle"><thead><tr><th>Area</th><th>Today</th><th>Status</th><th>Remark</th></tr></thead><tbody>
      <tr><td>Procurement</td><td>7 GRNs posted</td><td><span class="badge badge-soft badge-pending">Watch</span></td><td>3 supplier receipts delayed by 1 day</td></tr>
      <tr><td>Production</td><td>428 t processed</td><td><span class="badge badge-soft badge-ok">Stable</span></td><td>Slitter Line 02 above target</td></tr>
      <tr><td>Quality</td><td>96.8% pass</td><td><span class="badge badge-soft badge-ok">Good</span></td><td>2 FG lots in rework loop</td></tr>
      <tr><td>Dispatch</td><td>19 trucks planned</td><td><span class="badge badge-soft badge-pending">At Risk</span></td><td>2 trucks waiting loading clearance</td></tr>
    </tbody></table></div>
  </div></div>
  <div class="col-lg-5"><div class="panel h-100">
    <div class="section-title">Commercial Summary</div>
    <div class="metric mb-2"><div class="small-muted">Receivables at Risk</div><div class="fw-semibold mt-1">Rs. 1.18 Cr</div></div>
    <div class="metric mb-2"><div class="small-muted">Avg Contribution / ton</div><div class="fw-semibold mt-1">Rs. 6,840</div></div>
    <div class="metric mb-2"><div class="small-muted">Pending Invoices</div><div class="fw-semibold mt-1">9 dispatches awaiting invoice print</div></div>
    <div class="metric"><div class="small-muted">Top Customer</div><div class="fw-semibold mt-1">Apex Infra Steel | Rs. 2.14 Cr monthly run-rate</div></div>
  </div></div>
</section>
""",
        hero("Management Dashboard For Daily Review", "This dashboard is designed for leadership review across procurement, sales, production, dispatch, and financial closure, with immediate visibility into operational risk and throughput.", "Overview", ["Revenue|Rs. 8.42 Cr", "Open SO|148", "OTIF|94.2%"]),
    ),
    "reports.html": page(
        "Management Reports",
        "reports.html",
        """
<section class="panel mb-3">
  <div class="d-flex justify-content-between align-items-center flex-wrap gap-2 mb-3"><div class="section-title mb-0">Report Filters</div><div class="d-flex gap-2"><button class="btn glass-btn btn-sm" onclick="exportPdf()">Download PDF</button><button class="btn erp-primary btn-primary btn-sm" onclick="exportCsv()">Download CSV</button></div></div>
  <form class="row g-3" onsubmit="applyReportFilters(event)">
    <div class="col-lg-3 col-md-6"><label class="form-label">Report Type</label><select id="reportType" class="form-select"><option>Management Summary</option><option>Sales Performance</option><option>Production Efficiency</option><option>Dispatch OTIF</option></select></div>
    <div class="col-lg-3 col-md-6"><label class="form-label">Plant</label><select id="plantFilter" class="form-select"><option>Nagpur Plant</option><option>Raipur Plant</option><option>All Plants</option></select></div>
    <div class="col-lg-3 col-md-6"><label class="form-label">From Date</label><input id="fromDate" type="date" class="form-control" value="2026-04-01" /></div>
    <div class="col-lg-3 col-md-6"><label class="form-label">To Date</label><input id="toDate" type="date" class="form-control" value="2026-04-16" /></div>
    <div class="col-lg-3 col-md-6"><label class="form-label">Customer Segment</label><select id="segmentFilter" class="form-select"><option>All Segments</option><option>Infrastructure</option><option>Automotive</option><option>OEM</option></select></div>
    <div class="col-lg-3 col-md-6"><label class="form-label">Material Family</label><select id="materialFilter" class="form-select"><option>All Materials</option><option>CR Sheet</option><option>HR Coil</option><option>GP Coil</option></select></div>
    <div class="col-lg-3 col-md-6"><label class="form-label">Order Status</label><select id="statusFilter" class="form-select"><option>All Statuses</option><option>Confirmed</option><option>Allocated</option><option>Dispatched</option><option>Completed</option></select></div>
    <div class="col-lg-3 col-md-6 d-flex align-items-end"><button class="btn erp-primary btn-primary w-100" type="submit">Apply Filters</button></div>
  </form>
  <div id="reportFilterSummary" class="presenter-note mt-3">Showing Management Summary for Nagpur Plant from 2026-04-01 to 2026-04-16.</div>
</section>
<section class="row g-3 mb-3">
  <div class="col-lg-3 col-md-6"><div class="panel h-100"><div class="small-muted">Booked Revenue</div><div class="display-6 fw-bold mt-2">Rs. 12.6 Cr</div><div class="small-muted mt-2">Filtered report value</div></div></div>
  <div class="col-lg-3 col-md-6"><div class="panel h-100"><div class="small-muted">Dispatch Qty</div><div class="display-6 fw-bold mt-2">1,842 t</div><div class="small-muted mt-2">Across 94 dispatch notes</div></div></div>
  <div class="col-lg-3 col-md-6"><div class="panel h-100"><div class="small-muted">Avg Realization</div><div class="display-6 fw-bold mt-2">Rs. 68.4k</div><div class="small-muted mt-2">Per ton billed</div></div></div>
  <div class="col-lg-3 col-md-6"><div class="panel h-100"><div class="small-muted">Production Yield</div><div class="display-6 fw-bold mt-2">97.1%</div><div class="small-muted mt-2">Based on reported batches</div></div></div>
</section>
<section class="panel">
  <div class="section-title">Management Report Table</div>
  <div class="table-responsive"><table id="reportTable" class="table erp align-middle"><thead><tr><th>Period</th><th>Order Count</th><th>Dispatch Qty (t)</th><th>Revenue</th><th>OTIF</th><th>Contribution</th></tr></thead><tbody>
    <tr><td>Week 1</td><td>34</td><td>428</td><td>Rs. 2.94 Cr</td><td><span class="badge badge-soft badge-ok">95.1%</span></td><td>Rs. 28.6 L</td></tr>
    <tr><td>Week 2</td><td>39</td><td>462</td><td>Rs. 3.12 Cr</td><td><span class="badge badge-soft badge-ok">94.7%</span></td><td>Rs. 31.2 L</td></tr>
    <tr><td>Week 3</td><td>41</td><td>489</td><td>Rs. 3.38 Cr</td><td><span class="badge badge-soft badge-pending">92.9%</span></td><td>Rs. 33.1 L</td></tr>
    <tr><td>Week 4</td><td>32</td><td>463</td><td>Rs. 3.16 Cr</td><td><span class="badge badge-soft badge-ok">94.4%</span></td><td>Rs. 29.4 L</td></tr>
  </tbody></table></div>
</section>
""",
        hero("Management Reports With Export Controls", "Filter report views by time range, plant, segment, material family, and order status, then export the report for review in PDF or CSV format.", "Reports", ["Report Type|Management Summary", "Filters|Multi-dimensional", "Export|PDF + CSV"]),
        """<script>
function applyReportFilters(event){
  event.preventDefault();
  const type = document.getElementById('reportType').value;
  const plant = document.getElementById('plantFilter').value;
  const from = document.getElementById('fromDate').value;
  const to = document.getElementById('toDate').value;
  document.getElementById('reportFilterSummary').textContent = `Showing ${type} for ${plant} from ${from} to ${to}.`;
}
function exportPdf(){
  window.print();
}
function exportCsv(){
  const rows = [
    ['Period','Order Count','Dispatch Qty (t)','Revenue','OTIF','Contribution'],
    ['Week 1','34','428','Rs. 2.94 Cr','95.1%','Rs. 28.6 L'],
    ['Week 2','39','462','Rs. 3.12 Cr','94.7%','Rs. 31.2 L'],
    ['Week 3','41','489','Rs. 3.38 Cr','92.9%','Rs. 33.1 L'],
    ['Week 4','32','463','Rs. 3.16 Cr','94.4%','Rs. 29.4 L']
  ];
  const csv = rows.map(row => row.join(',')).join('\\n');
  const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url;
  link.download = 'management-report.csv';
  link.click();
  URL.revokeObjectURL(url);
}
</script>""",
    ),
    "procurement-need.html": page(
        "Procurement Need",
        "procurement-need.html",
        """
<section class="row g-3">
  <div class="col-lg-7"><div class="panel"><div class="section-title">Demand Trigger</div><form class="row g-3">
    <div class="col-md-6"><label class="form-label">Need Source</label><select class="form-select"><option>Low RM stock</option><option>Planned sales demand</option><option>Manual plant request</option></select></div>
    <div class="col-md-6"><label class="form-label">Triggered By</label><input class="form-control" value="Planning Team" /></div>
    <div class="col-md-4"><label class="form-label">Material</label><input class="form-control" value="HRC Coil E350" /></div>
    <div class="col-md-4"><label class="form-label">Required Qty</label><input class="form-control" value="120 t" /></div>
    <div class="col-md-4"><label class="form-label">Priority</label><select class="form-select"><option>High</option><option>Medium</option></select></div>
    <div class="col-12 d-flex gap-2"><button type="button" class="btn erp-primary btn-primary">Manual Procurement Trigger</button><a href="vendor.html" class="btn glass-btn">Continue to Vendor</a></div>
  </form></div></div>
  <div class="col-lg-5"><div class="panel h-100"><div class="section-title">Low Stock Alert</div>
    <div class="metric mb-2"><div class="small-muted">Critical Item</div><div class="fw-semibold mt-1">HRC Coil E350</div></div>
    <div class="metric mb-2"><div class="small-muted">Available RM</div><div class="fw-semibold mt-1 text-warning">38 t</div></div>
    <div class="metric"><div class="small-muted">Reorder Threshold</div><div class="fw-semibold mt-1">100 t</div></div>
  </div></div>
</section>
""",
        hero("Procurement Need Identified", "Start the process when raw material demand is triggered by low stock or upcoming order pressure.", "Need Trigger", ["Current Alert|HRC below threshold", "Trigger Type|Manual + system", "Next Step|Vendor selection"]),
    ),
    "vendor.html": page(
        "Vendor Management",
        "vendor.html",
        """
<section class="panel mb-3">
  <div class="section-title">Vendor Selection Decision</div>
  <div class="small-muted mb-3">Choose one path: select an existing approved vendor, or create a new vendor and move it through onboarding before PO.</div>
  <div class="row g-3 mb-3">
    <div class="col-md-8"><label class="form-label">Select Approved Vendor for PO</label><select id="vendorForPo" class="form-select"><option value="Durga Metal Source Pvt Ltd">Durga Metal Source Pvt Ltd | HRC | Approved</option><option value="Blue Zinc Alloys">Blue Zinc Alloys | Zinc | Pending</option></select></div>
    <div class="col-md-4 d-flex align-items-end"><button type="button" class="btn erp-primary btn-primary w-100" onclick="goToPoWithVendor()">Select Vendor & Create PO</button></div>
  </div>
  <div class="d-flex gap-2 flex-wrap">
    <button type="button" class="btn erp-primary btn-primary btn-sm" onclick="setVendorPath('existing')">Use Existing Vendor</button>
    <button type="button" class="btn glass-btn btn-sm" onclick="setVendorPath('new')">Vendor Not Present - Create New</button>
    <a href="po.html" class="btn glass-btn btn-sm">Continue to PO (manual)</a>
  </div>
  <div id="vendorPathMsg" class="presenter-note mt-3">Current path: Existing Vendor. Select approved vendor from list and continue to PO.</div>
</section>
<section class="row g-3 mb-3">
  <div class="col-lg-6"><div class="panel h-100">
    <div class="section-title">Existing vendors (operational flow)</div>
    <p class="small-muted mb-3">Approved suppliers are reused on every cycle. They do not re-enter onboarding unless master data changes or compliance is renewed.</p>
    <div class="progress-track mb-3"><span class="progress-pill done">Vendor master</span><span class="progress-pill done">Approved</span><span class="progress-pill done">Active on PO</span><span class="progress-pill current">GRN &amp; QC loop</span></div>
    <div class="small-muted">Example: <span class="fw-semibold">Durga Metal Source Pvt Ltd</span> is already on the procurement path. Next touchpoint is PO selection, then GRN and RM QC as material arrives.</div>
    <div class="mt-3 d-flex flex-wrap gap-2"><a href="po.html" class="btn erp-primary btn-primary btn-sm">Raise PO against vendor</a><a href="grn.html" class="btn glass-btn btn-sm">View GRN path</a></div>
  </div></div>
  <div class="col-lg-6"><div class="panel h-100">
    <div class="section-title">New vendor (onboarding flow)</div>
    <p class="small-muted mb-3">A newly created vendor follows master data and compliance steps before it can appear as an approved source on purchase documents.</p>
    <div class="progress-track mb-3"><span class="progress-pill current">Create / Draft</span><span class="progress-pill">Due diligence</span><span class="progress-pill">Compliance</span><span class="progress-pill">Approval</span><span class="progress-pill">Activate for PO</span></div>
    <div class="small-muted">Example: <span class="fw-semibold">Blue Zinc Alloys</span> is still in onboarding. Until status is Approved, procurement should not release PO except as a controlled exception.</div>
    <div class="metric mt-3"><div class="small-muted">Gate</div><div class="fw-semibold mt-1">PO creation allowed only after Approved + Active for PO</div></div>
  </div></div>
</section>
<section id="vendorCreationPanel" class="panel mb-3"><div class="section-title">Vendor Creation</div><form class="row g-3">
  <div class="col-md-6"><label class="form-label">Vendor Name</label><input class="form-control" value="Durga Metal Source Pvt Ltd" /></div>
  <div class="col-md-6"><label class="form-label">GSTIN</label><input class="form-control" value="27AAACD1122P1ZV" /></div>
  <div class="col-md-4"><label class="form-label">Material Category</label><select class="form-select"><option>HRC Coil</option><option>Zinc</option></select></div>
  <div class="col-md-4"><label class="form-label">Lead Time</label><input class="form-control" value="7 Days" /></div>
  <div class="col-md-4"><label class="form-label">Status</label><div class="pt-2"><span class="badge badge-soft badge-ok">Approved</span></div></div>
  <div class="col-12"><a href="po.html" class="btn erp-primary btn-primary">Save Vendor & Continue to PO</a></div>
</form></section>
<section id="vendorListPanel" class="panel"><div class="section-title">Vendor List</div><div class="table-responsive"><table class="table erp align-middle"><thead><tr><th>Vendor</th><th>Material</th><th>Location</th><th>Status</th></tr></thead><tbody>
  <tr><td>Durga Metal Source Pvt Ltd</td><td>HRC Coil</td><td>Nagpur</td><td><span class="badge badge-soft badge-ok">Approved</span></td></tr>
  <tr><td>Blue Zinc Alloys</td><td>Zinc</td><td>Raipur</td><td><span class="badge badge-soft badge-pending">Pending</span></td></tr>
</tbody></table></div></section>
""",
        hero("Approved Suppliers for Procurement", "Separate the operational path for existing approved vendors from the onboarding path for newly created vendors, so procurement and audit teams see the same lifecycle story.", "Vendor Step", ["Existing|PO ready", "New|Onboarding", "Next|PO creation"]),
        """<script>
function setVendorPath(path){
  const msg = document.getElementById('vendorPathMsg');
  const creation = document.getElementById('vendorCreationPanel');
  const list = document.getElementById('vendorListPanel');
  if(path === 'existing'){
    list.style.display = 'block';
    creation.style.display = 'none';
    msg.textContent = 'Current path: Existing Vendor. Select approved vendor from list and continue to PO.';
  } else {
    list.style.display = 'none';
    creation.style.display = 'block';
    msg.textContent = 'Current path: New Vendor Creation. Fill vendor master, complete checks, approve, then continue to PO.';
  }
}
function goToPoWithVendor(){
  const selected = document.getElementById('vendorForPo').value;
  if(selected === 'Blue Zinc Alloys'){
    alert('Selected vendor is pending approval. Complete onboarding/approval before PO release.');
    return;
  }
  window.location.href = 'po.html?vendor=' + encodeURIComponent(selected);
}
document.addEventListener('DOMContentLoaded', function(){
  setVendorPath('existing');
});
</script>""",
    ),
    "po.html": page(
        "Procurement PO",
        "po.html",
        """
<section class="panel"><div class="section-title">Purchase Order</div><form class="row g-3">
  <div class="col-md-4"><label class="form-label">PO Number</label><input class="form-control" value="PO-2026-0416-14" /></div>
  <div class="col-md-4"><label class="form-label">Vendor</label><select id="poVendorSelect" class="form-select"><option>Durga Metal Source Pvt Ltd</option><option>Blue Zinc Alloys</option></select></div>
  <div class="col-md-4"><label class="form-label">PO Lifecycle</label><div class="pt-2"><span class="badge badge-soft badge-pending">Draft</span> <span class="badge badge-soft badge-ok">Approved</span> <span class="badge badge-soft badge-pending">Partially Received</span> <span class="badge badge-soft badge-ok">Fully Received</span></div></div>
  <div class="col-md-4"><label class="form-label">Material</label><select class="form-select"><option>HRC Coil E350</option></select></div>
  <div class="col-md-4"><label class="form-label">Quantity (t)</label><input class="form-control" value="650" /></div>
  <div class="col-md-4"><label class="form-label">Rate / ton</label><input class="form-control" value="59400" /></div>
  <div class="col-12 d-flex gap-2"><span class="badge badge-soft badge-pending">Partially Received</span><a href="grn.html" class="btn erp-primary btn-primary">Proceed to GRN</a></div>
</form></section>
""",
        hero("Purchase Order Commitment", "Issue procurement against approved supplier and procurement need or MRP procurement loop.", "PO Stage", ["PO Status|Approved", "Qty|650 t", "Next|GRN"]),
        """<script>
document.addEventListener('DOMContentLoaded', function(){
  const params = new URLSearchParams(window.location.search);
  const vendor = params.get('vendor');
  const select = document.getElementById('poVendorSelect');
  if(vendor && select){
    const exists = Array.from(select.options).some(o => o.value === vendor);
    if(exists){ select.value = vendor; }
  }
});
</script>""",
    ),
    "grn.html": page(
        "GRN Receipt",
        "grn.html",
        """
<section class="panel"><div class="section-title">GRN + Weighbridge</div><form class="row g-3">
  <div class="col-md-4"><label class="form-label">PO Selection</label><select class="form-select"><option>PO-2026-0416-14</option></select></div>
  <div class="col-md-4"><label class="form-label">Truck No</label><input class="form-control" value="MH40AZ7812" /></div>
  <div class="col-md-4"><label class="form-label">Driver</label><input class="form-control" value="Mukesh Yadav" /></div>
  <div class="col-md-4"><label class="form-label">Gross Weight</label><input class="form-control" value="41.8 t" /></div>
  <div class="col-md-4"><label class="form-label">Tare Weight</label><input class="form-control" value="9.6 t" /></div>
  <div class="col-md-4"><label class="form-label">Net Weight</label><input class="form-control" value="32.2 t" /></div>
  <div class="col-12"><a href="qc-rm.html" class="btn erp-primary btn-primary">GRN -> QC RM</a></div>
</form></section>
""",
        hero("Incoming Receipt Validation", "Record actual receipt against purchase order before quality clearance.", "GRN Stage", ["Receipt|32.2 t", "Truck|MH40AZ7812", "Next|QC RM"]),
    ),
    "qc-rm.html": page(
        "RM Quality Control",
        "qc-rm.html",
        """
<section class="row g-3 mb-3">
  <div class="col-md-4"><div class="panel h-100"><div class="section-title">Chemical</div><div class="small-muted">Pass within tolerance.</div></div></div>
  <div class="col-md-4"><div class="panel h-100"><div class="section-title">Surface</div><div class="small-muted">No scale or edge damage.</div></div></div>
  <div class="col-md-4"><div class="panel h-100"><div class="section-title">Thickness</div><div class="small-muted">3.19 mm average.</div></div></div>
</section>
<section class="panel"><div class="section-title">QC RM Decision</div><div class="d-flex gap-2 flex-wrap">
  <a href="inventory-rm.html" class="btn btn-success">Approve</a>
  <button class="btn btn-danger" onclick="rmDecision('reject')">Reject</button>
  <button class="btn btn-warning" onclick="rmDecision('hold')">Hold</button>
</div><div id="rmDecisionMsg" class="mt-3"></div></section>
""",
        hero("Incoming RM Quality Gate", "RM must be approved before inventory release; reject stops the flow and hold keeps it pending.", "QC RM", ["Approve|Move to RM stock", "Reject|Stop", "Hold|Pending"]),
        """<script>
function rmDecision(type){
  const el=document.getElementById('rmDecisionMsg');
  if(type==='reject'){el.innerHTML='<div class="alert alert-danger mb-0">Rejected: flow stopped for this lot.</div>';}
  else{el.innerHTML='<div class="alert alert-warning mb-0">Held: material pending review.</div>';}
}
</script>""",
    ),
    "inventory-rm.html": page(
        "RM Inventory",
        "inventory-rm.html",
        """
<section class="panel"><div class="section-title">Raw Material Inventory</div><div class="table-responsive"><table class="table erp align-middle"><thead><tr><th>Item</th><th>Batch</th><th>Weight</th><th>Status</th></tr></thead><tbody>
  <tr><td>HRC Coil E350</td><td>RM-HRC-6612</td><td>920 t</td><td><span class="badge badge-soft badge-ok">Available</span></td></tr>
  <tr><td>Zinc Ingot</td><td>RM-ZN-1904</td><td>44 t</td><td><span class="badge badge-soft badge-pending">Low Stock</span></td></tr>
  <tr><td>Flux Compound</td><td>RM-FLX-2811</td><td>118 t</td><td><span class="badge badge-soft badge-ok">Available</span></td></tr>
</tbody></table></div><div class="d-flex gap-2"><a href="product-master.html" class="btn erp-primary btn-primary">Product Master / Capability</a><a href="inquiry.html" class="btn glass-btn">Direct to Inquiry</a></div></section>
""",
        hero("RM Released for Planning", "Approved material becomes visible to product capability checks, inquiry feasibility, and MRP.", "RM Stock", ["Available RM|3 categories", "Low Stock|Zinc", "Next|Product capability"]),
    ),
    "product-master.html": page(
        "Product Master / Capability",
        "product-master.html",
        """
<section class="panel"><div class="section-title">Product Capability Check</div><form class="row g-3">
  <div class="col-md-4"><label class="form-label">Product</label><select class="form-select"><option>CR Sheet</option><option>HR Coil</option></select></div>
  <div class="col-md-4"><label class="form-label">Grade</label><input class="form-control" value="IS513" /></div>
  <div class="col-md-4"><label class="form-label">Thickness</label><input class="form-control" value="1.2 mm" /></div>
  <div class="col-md-4"><label class="form-label">Width</label><input class="form-control" value="1250 mm" /></div>
  <div class="col-md-4"><label class="form-label">Process Type</label><select class="form-select"><option>Slitting</option><option>CTL</option></select></div>
  <div class="col-md-4"><label class="form-label">Capability</label><div class="pt-2"><span class="badge badge-soft badge-ok">Capable</span></div></div>
  <div class="col-12"><a href="inquiry.html" class="btn erp-primary btn-primary">Proceed to Sales Inquiry</a></div>
</form></section>
""",
        hero("Capability Before Commercial Commitment", "Validate product, grade, thickness, width and process path before customer inquiry proceeds.", "Product Master", ["Process|Slitting", "Capability|Capable", "Next|Inquiry"]),
    ),
    "inquiry.html": page(
        "Sales Inquiry",
        "inquiry.html",
        """
<section class="panel"><div class="section-title">Customer Inquiry</div><form class="row g-3">
  <div class="col-md-6"><label class="form-label">Customer Name</label><input class="form-control" value="Apex Infra Steel" /></div>
  <div class="col-md-6"><label class="form-label">Product</label><select class="form-select"><option>CR Sheet 1.2mm</option></select></div>
  <div class="col-md-4"><label class="form-label">Grade</label><input class="form-control" value="IS513" /></div>
  <div class="col-md-4"><label class="form-label">Width</label><input class="form-control" value="1250 mm" /></div>
  <div class="col-md-4"><label class="form-label">Quantity</label><input class="form-control" value="110 t" /></div>
  <div class="col-12 d-flex gap-2 align-items-center"><button type="button" class="btn erp-primary btn-primary" onclick="feasibility()">Check Feasibility</button><span id="feasibilityBadge" class="badge badge-soft badge-pending">Pending</span></div>
  <div class="col-12"><a href="quotation.html" class="btn glass-btn">Continue to Quotation</a></div>
</form></section>
""",
        hero("Customer Requirement Capture", "Inquiry follows product capability validation and becomes the commercial input for quotation.", "Inquiry", ["Customer|Apex Infra Steel", "Demand|110 t", "Next|Quotation"]),
        """<script>
function feasibility(){const b=document.getElementById('feasibilityBadge'); b.className='badge badge-soft badge-ok'; b.textContent='Feasible';}
</script>""",
    ),
    "quotation.html": page(
        "Quotation",
        "sales-order.html",
        """
<section class="panel"><div class="section-title">Quotation Terms</div><div class="viz-grid">
  <div class="metric"><div class="small-muted">Quote No</div><div class="fw-semibold mt-1">QT-2026-221</div></div>
  <div class="metric"><div class="small-muted">Base Price</div><div class="fw-semibold mt-1">Rs. 66,800 / t</div></div>
  <div class="metric"><div class="small-muted">Validity</div><div class="fw-semibold mt-1">Till 30 Apr 2026</div></div>
</div><div class="metric mt-3"><div class="small-muted">Terms</div><div class="fw-semibold mt-1">30 days credit, dispatch against release clearance.</div></div><div class="mt-3"><a href="sales-order.html" class="btn erp-primary btn-primary">Convert to Sales Order</a></div></section>
""",
        hero("Commercial Offer Ready", "Quotation sits between inquiry and sales order but does not alter the main stepper logic.", "Quotation", ["Quote|QT-2026-221", "Commercial|Approved", "Next|Sales order"]),
    ),
    "sales-order.html": page(
        "Sales Order",
        "sales-order.html",
        """
<section class="panel mb-3"><div class="section-title">Sales Order Snapshot</div><div class="table-responsive"><table class="table erp align-middle"><thead><tr><th>SO No</th><th>Customer</th><th>Product</th><th>Qty</th><th>Status</th><th>Credit</th></tr></thead><tbody>
  <tr><td>SO-2026-417</td><td>Apex Infra Steel</td><td>CR Sheet 1.2mm</td><td>110 t</td><td><span class="badge badge-soft badge-pending">Draft</span> <span class="badge badge-soft badge-ok">Confirmed</span> <span class="badge badge-soft badge-pending">In Progress</span> <span class="badge badge-soft badge-pending">Allocated</span> <span class="badge badge-soft badge-ok">Dispatched</span> <span class="badge badge-soft badge-ok">Completed</span></td><td><span id="creditBadge" class="badge badge-soft badge-bad">Blocked</span></td></tr>
</tbody></table></div><div class="mt-2"><button class="btn btn-sm glass-btn" onclick="creditPass()">Recheck Credit</button></div></section>
<section class="row g-3 mb-3">
  <div class="col-lg-4"><div class="panel h-100"><div class="section-title">Commercial Readiness</div><div class="small-muted">Credit must clear before the system allows fulfilment path selection. This mimics a real order release gate.</div></div></div>
  <div class="col-lg-4"><div class="panel h-100"><div class="section-title">Fulfilment Logic</div><div class="small-muted">Full stock goes directly to allocation. Partial stock permits immediate dispatch for available quantity and routes the balance to MRP.</div></div></div>
  <div class="col-lg-4"><div class="panel h-100"><div class="section-title">Audit Confidence</div><div class="small-muted">Every order keeps a traceable link to FG batch, production batch, RM batch, and supplier source.</div></div></div>
</section>
<section class="panel decision-card"><div class="section-title">Stock Check Decision</div><p class="small-muted">Choose the business path after credit is approved.</p><div class="d-flex gap-2 flex-wrap mb-3">
  <a id="stockFull" href="allocation.html" class="btn btn-success disabled" aria-disabled="true">Full Available -> Allocation</a>
  <button id="stockPartial" class="btn btn-warning disabled" aria-disabled="true" onclick="handlePartial()">Partial Available</button>
  <a id="stockNo" href="mrp.html" class="btn btn-danger disabled" aria-disabled="true">Not Available -> MRP</a>
</div><div id="creditHelp" class="small-muted">Credit failed: next actions are blocked until credit passes.</div><div id="partialHelp" class="small-muted mt-2"></div></section>
<section class="panel"><div class="section-title">Traceability Link</div><div class="metric"><div class="small-muted">Chain</div><div class="fw-semibold mt-1">SO-2026-417 -> FG-CR-9021 / FG-CR-9022 -> PROD-WO-2026-910 -> RM-HRC-6612 -> Durga Metal Source Pvt Ltd</div></div></section>
""",
        hero("Order Release With Business Decisions", "This is the best page to present the ERP logic. The order is commercially blocked first, then released into full, partial, or no-stock fulfilment depending on availability.", "Sales Order", ["Credit|Blocked", "Partial Flow|Dispatch + MRP", "Traceability|Enabled"]),
        """<script>
function creditPass(){
  const b=document.getElementById('creditBadge');
  b.className='badge badge-soft badge-ok';
  b.textContent='OK';
  ['stockFull','stockPartial','stockNo'].forEach(id => { const el=document.getElementById(id); el.classList.remove('disabled'); el.removeAttribute('aria-disabled'); });
  document.getElementById('creditHelp').textContent='Credit passed: choose full, partial, or no-stock path.';
}
function handlePartial(){
  const el = document.getElementById('partialHelp');
  el.textContent = 'Partial available: dispatch available FG first, then route remaining quantity to MRP.';
  setTimeout(function(){ window.location.href = 'mrp.html'; }, 700);
}
</script>""",
    ),
    "mrp.html": page(
        "MRP Planning",
        "mrp.html",
        """
<section class="panel mb-3"><div class="section-title">RM Requirement Summary</div><div class="viz-grid">
  <div class="metric"><div class="small-muted">Required RM</div><div class="fw-semibold mt-1">HRC 76 t / Zinc 2.8 t</div></div>
  <div class="metric"><div class="small-muted">Available RM</div><div class="fw-semibold mt-1">HRC 38 t / Zinc 1.2 t</div></div>
  <div class="metric"><div class="small-muted">Shortage</div><div class="fw-semibold mt-1 text-warning">HRC 38 t / Zinc 1.6 t</div></div>
</div><div class="metric mt-3"><div class="small-muted">Partial Dispatch Handling</div><div class="fw-semibold mt-1">Only remaining quantity after partial dispatch should be planned in MRP.</div></div></section>
<section class="row g-3 mb-3">
  <div class="col-lg-6"><div class="panel h-100"><div class="section-title">Planning Narrative</div><div class="small-muted">MRP is not just shortage math here. It is the decision engine that checks what remains after current stock allocation and determines whether production can start or procurement must loop.</div></div></div>
  <div class="col-lg-6"><div class="panel h-100"><div class="section-title">Procurement Loop</div><div class="small-muted">If RM is not sufficient, the user is deliberately sent back into PO -> GRN -> QC RM -> RM Inventory before production release.</div></div></div>
</section>
<section class="panel decision-card"><div class="section-title">Is RM Available?</div><div class="d-flex gap-2 flex-wrap">
  <a href="production.html" class="btn btn-success">YES -> Production</a>
  <a href="po.html" class="btn btn-warning">NO -> Procurement Loop</a>
</div><div class="small-muted mt-3">Procurement loop: PO -> GRN -> QC RM -> RM Inventory -> back to MRP -> Production.</div></section>
""",
        hero("MRP That Explains The Next Move", "MRP decides whether the remaining requirement is manufacturable with current RM or must re-enter procurement. That makes the planning page easy to explain to a client.", "MRP", ["Shortage|Visible", "Decision|Produce or procure", "Loop|Controlled"]),
    ),
    "production.html": page(
        "Production Execution",
        "production.html",
        """
<section class="panel mb-3"><div class="section-title">Work Order</div><div class="row g-3">
  <div class="col-md-4"><label class="form-label">Work Order No</label><input class="form-control" value="WO-2026-910" /></div>
  <div class="col-md-4"><label class="form-label">Machine</label><select class="form-select"><option>Slitter Line 02</option></select></div>
  <div class="col-md-4"><label class="form-label">Production Lifecycle</label><div class="pt-2"><span class="badge badge-soft badge-pending">Planned</span> <span class="badge badge-soft badge-ok">Running</span> <span class="badge badge-soft badge-ok">Completed</span> <span class="badge badge-soft badge-pending">QC Pending</span> <span class="badge badge-soft badge-ok">Approved</span></div></div>
</div></section>
<section class="row g-3 mb-3">
  <div class="col-lg-4"><div class="panel h-100"><div class="section-title">Operational Control</div><div class="small-muted">Planner releases the work order, machine starts, and the lifecycle visibly moves from planned to running to QC pending.</div></div></div>
  <div class="col-lg-4"><div class="panel h-100"><div class="section-title">Traceability Ready</div><div class="small-muted">Every production batch can be traced backward to the RM lot and supplier, and forward to finished goods batches and customer orders.</div></div></div>
  <div class="col-lg-4"><div class="panel h-100"><div class="section-title">Closed Loop Quality</div><div class="small-muted">If FG QC rejects output, the system loops back into production for rework and then returns to QC again.</div></div></div>
</section>
<section class="panel"><div class="d-flex justify-content-between align-items-center mb-3"><div class="section-title mb-0">Machine Status</div><div id="machineState"><span class="machine-dot stop"></span>Idle</div></div>
<div class="d-flex gap-2 flex-wrap"><button class="btn btn-success" onclick="startMachine()">Start</button><button class="btn glass-btn" onclick="stopMachine()">Stop</button><a href="qc-fg.html" class="btn erp-primary btn-primary">Production -> FG QC</a></div></section>
<section class="panel mt-3"><div class="section-title">Batch Traceability</div><div class="metric"><div class="small-muted">Production Batch Link</div><div class="fw-semibold mt-1">PROD-WO-2026-910 consumes RM-HRC-6612 from Durga Metal Source Pvt Ltd and produces FG-CR-9021 / FG-CR-9022.</div></div></section>
""",
        hero("Production Execution With Traceability", "This page now reads like a manufacturing control screen: active lifecycle, machine state, traceability, and clear next action into FG quality.", "Production", ["WO|WO-2026-910", "Lifecycle|Running", "Next|FG QC"]),
        """<script>
function startMachine(){document.getElementById('machineState').innerHTML='<span class="machine-dot run"></span>Running';}
function stopMachine(){document.getElementById('machineState').innerHTML='<span class="machine-dot stop"></span>Idle';}
</script>""",
    ),
    "qc-fg.html": page(
        "FG Quality Control",
        "inventory-fg.html",
        """
<section class="row g-3 mb-3">
  <div class="col-md-4"><div class="panel h-100"><div class="section-title">Surface Finish</div><div class="small-muted">Customer finish quality pass.</div></div></div>
  <div class="col-md-4"><div class="panel h-100"><div class="section-title">Width Tolerance</div><div class="small-muted">Within process specification.</div></div></div>
  <div class="col-md-4"><div class="panel h-100"><div class="section-title">Coil Edge</div><div class="small-muted">No damage or burr exception.</div></div></div>
</section>
<section class="panel"><div class="section-title">FG QC Decision</div><div class="d-flex gap-2 flex-wrap">
  <a href="inventory-fg.html" class="btn btn-success">Approve</a>
  <button class="btn btn-danger" onclick="fgDecision('reject')">Reject</button>
  <button class="btn btn-warning" onclick="fgDecision('hold')">Hold</button>
</div><div id="fgDecisionMsg" class="mt-3"></div></section>
""",
        hero("Finished Goods Release Gate", "FG approval sends stock to inventory. Reject starts a rework loop back to production. Hold keeps the lot pending.", "FG QC", ["Approve|FG Inventory", "Reject|Rework Loop", "Hold|Pending"]),
        """<script>
function fgDecision(type){
  const el=document.getElementById('fgDecisionMsg');
  if(type==='reject'){el.innerHTML='<div class="alert alert-danger mb-0">Rejected: rework triggered. Returning to Production for correction and QC again.</div>'; setTimeout(function(){ window.location.href = 'production.html'; }, 900);}
  else{el.innerHTML='<div class="alert alert-warning mb-0">Held: FG pending QA review.</div>';}
}
</script>""",
    ),
    "inventory-fg.html": page(
        "FG Inventory",
        "inventory-fg.html",
        """
<section class="panel"><div class="section-title">Finished Goods Inventory</div><div class="table-responsive"><table class="table erp align-middle"><thead><tr><th>Item</th><th>Batch</th><th>Weight</th><th>Status</th></tr></thead><tbody>
  <tr><td>CR Sheet 1.2mm</td><td>FG-CR-9021</td><td>75 t</td><td><span class="badge badge-soft badge-ok">Ready</span></td></tr>
  <tr><td>CR Sheet 1.2mm</td><td>FG-CR-9022</td><td>35 t</td><td><span class="badge badge-soft badge-ok">Ready</span></td></tr>
</tbody></table></div><div class="metric mt-3"><div class="small-muted">Traceability</div><div class="fw-semibold mt-1">FG-CR-9021 / FG-CR-9022 -> PROD-WO-2026-910 -> RM-HRC-6612 -> Durga Metal Source Pvt Ltd</div></div><div class="d-flex gap-2 mt-3"><a href="allocation.html" class="btn erp-primary btn-primary">Go to SO Allocation</a><a href="sales-order.html" class="btn glass-btn">Back to Sales Order</a></div></section>
""",
        hero("FG Ready for Order Allocation", "Finished goods move to allocation before dispatch. This is now an explicit step in the process.", "FG Inventory", ["FG Batches|2", "Ready Qty|110 t", "Next|Allocation"]),
    ),
    "allocation.html": page(
        "Sales Order Allocation",
        "allocation.html",
        """
<section class="row g-3">
  <div class="col-lg-6"><div class="panel"><div class="section-title">Select Sales Order</div><div class="mb-3"><label class="form-label">Sales Order</label><select class="form-select"><option>SO-2026-417 | Apex Infra Steel | 110 t</option></select></div><div class="metric"><div class="small-muted">Allocated Quantity</div><div class="fw-semibold mt-1" id="allocatedQty">0 t</div></div></div></div>
  <div class="col-lg-6"><div class="panel"><div class="section-title">FG Inventory Batches</div><div class="table-responsive"><table class="table erp align-middle"><thead><tr><th>Batch</th><th>Weight</th><th>Action</th></tr></thead><tbody>
    <tr><td>FG-CR-9021</td><td>75 t</td><td><button class="btn btn-sm btn-success" onclick="allocate(75, 5130000)">Allocate</button></td></tr>
    <tr><td>FG-CR-9022</td><td>35 t</td><td><button class="btn btn-sm btn-success" onclick="allocate(35, 2394000)">Allocate</button></td></tr>
  </tbody></table></div><div class="metric mt-3"><div class="small-muted">Weight-Based Cost Allocation</div><div class="fw-semibold mt-1" id="allocatedCost">Rs. 0</div></div><div class="metric mt-3"><div class="small-muted">Traceability</div><div class="fw-semibold mt-1">SO -> FG Batch -> Production Batch -> RM Batch -> Vendor</div></div><div class="mt-3"><a href="dispatch.html" class="btn erp-primary btn-primary">Allocation -> Dispatch</a></div></div></div>
</section>
""",
        hero("Allocate FG to Sales Order", "Select order, assign FG batches, review traceability, and calculate weight-based cost before dispatch.", "Allocation", ["SO|SO-2026-417", "FG Batches|2", "Route|Dispatch"]),
        """<script>
let totalAllocated = 0;
let totalCost = 0;
function allocate(qty, cost){
  totalAllocated += qty;
  totalCost += cost;
  document.getElementById('allocatedQty').textContent = totalAllocated + ' t';
  document.getElementById('allocatedCost').textContent = 'Rs. ' + totalCost.toLocaleString();
}
</script>""",
    ),
    "dispatch.html": page(
        "Dispatch Control",
        "dispatch.html",
        """
<section class="panel mb-3"><div class="section-title">Dispatch Tracker</div><div class="progress-track"><span class="progress-pill done">Packing</span><span class="progress-pill current">Loading</span><span class="progress-pill">Verified</span><span class="progress-pill">Dispatched</span></div></section>
<section class="row g-3 mb-3">
  <div class="col-lg-4"><div class="panel h-100"><div class="section-title">What Client Sees</div><div class="small-muted">Allocation is already complete, so dispatch is focused on execution status only: packing, loading, verification, and dispatch confirmation.</div></div></div>
  <div class="col-lg-4"><div class="panel h-100"><div class="section-title">Operational Gate</div><div class="small-muted">The user should understand at a glance whether the truck can move or whether a verification step is still pending.</div></div></div>
  <div class="col-lg-4"><div class="panel h-100"><div class="section-title">Commercial Handover</div><div class="small-muted">Once dispatch is confirmed, the process moves directly into invoice, GST, IRN, and e-way documentation.</div></div></div>
</section>
<section class="panel"><div class="row g-3">
  <div class="col-md-4"><label class="form-label">Packing Status</label><div class="pt-2"><span class="badge badge-soft badge-pending">Packing</span></div></div>
  <div class="col-md-4"><label class="form-label">Loading Status</label><div class="pt-2"><span class="badge badge-soft badge-pending">Loading</span></div></div>
  <div class="col-md-4"><label class="form-label">Verification Status</label><div class="pt-2"><span class="badge badge-soft badge-ok">Verified</span> <span class="badge badge-soft badge-ok">Dispatched</span></div></div>
</div><div class="mt-3"><a href="billing.html" class="btn erp-primary btn-primary">Dispatch -> Billing</a></div></section>
""",
        hero("Dispatch Execution, Not Just A Link", "Dispatch is now presented as an operational stage with a clear sequence and commercial handover, which makes it more convincing in a client walkthrough.", "Dispatch", ["Current Stage|Loading", "Allocated|Yes", "Next|Billing"]),
    ),
    "billing.html": page(
        "Billing & GST",
        "billing.html",
        """
<section class="panel"><div class="section-title">Invoice Processing</div><div class="row g-3">
  <div class="col-md-3"><label class="form-label">Invoice No</label><input class="form-control" value="INV-2026-7102" /></div>
  <div class="col-md-3"><label class="form-label">GST Status</label><div class="pt-2"><span class="badge badge-soft badge-ok">Filed</span></div></div>
  <div class="col-md-3"><label class="form-label">IRN</label><div class="pt-2"><span class="badge badge-soft badge-ok">Generated</span></div></div>
  <div class="col-md-3"><label class="form-label">E-way Bill</label><div class="pt-2"><span class="badge badge-soft badge-pending">Pending Print</span></div></div>
</div><div class="mt-3"><a href="delivery.html" class="btn erp-primary btn-primary">Billing -> Delivery</a></div></section>
""",
        hero("Commercial Closure", "Billing follows dispatch and captures invoice, tax, IRN and e-way state before delivery.", "Billing", ["Invoice|INV-2026-7102", "GST|Filed", "Next|Delivery"]),
    ),
    "delivery.html": page(
        "Delivery Completion",
        "delivery.html",
        """
<section class="panel"><div class="section-title">Delivery Finalization</div><div class="row g-3">
  <div class="col-md-4"><label class="form-label">Shipment ID</label><input class="form-control" value="SHP-2026-2281" /></div>
  <div class="col-md-4"><label class="form-label">Customer Confirmation</label><select class="form-select"><option>Confirmed</option><option>Pending</option></select></div>
  <div class="col-md-4"><label class="form-label">Delivery Status</label><select class="form-select"><option>Delivered</option><option>In Transit</option></select></div>
  <div class="col-md-12"><label class="form-label">POD Upload</label><input type="file" class="form-control" /></div>
  <div class="col-12 d-flex gap-2"><button type="button" class="btn erp-primary btn-primary" onclick="markCompleted()">Mark as Completed</button><span id="completionBadge" class="badge badge-soft badge-pending">Pending Completion</span></div>
</div></section>
""",
        hero("POD and Completion", "Delivery closes the ERP flow after POD upload and customer confirmation.", "Delivery", ["Shipment|SHP-2026-2281", "POD|Required", "Final State|Completion"]),
        """<script>
function markCompleted(){ const badge = document.getElementById('completionBadge'); badge.className = 'badge badge-soft badge-ok'; badge.textContent = 'Completed'; }
</script>""",
    ),
}

for name, html in pages.items():
    (base / name).write_text(html, encoding="utf-8")

print(f"Generated {len(pages)} themed pages.")
