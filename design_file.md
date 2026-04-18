# 🏭 Steel ERP SaaS — Design System (Frontend HTML + Bootstrap)

---

# 1. 🎯 DESIGN PRINCIPLES

### Core Philosophy

* Process-first (not dashboard-first)
* Data clarity over decoration
* Industrial + modern SaaS feel
* Minimal but functional

---

### Design Goals

* Clean enterprise UI
* Fast readability
* Low cognitive load
* Consistent across modules

---

# 2. 🎨 COLOR SYSTEM

## Primary Palette

| Token      | Color   | Usage                  |
| ---------- | ------- | ---------------------- |
| Primary    | #3B82F6 | Buttons, active states |
| Secondary  | #64748B | Labels, muted text     |
| Background | #F8FAFC | Main background        |
| Surface    | #FFFFFF | Cards, tables          |
| Border     | #E2E8F0 | Dividers               |

---

## Status Colors

| Status  | Color   | Usage               |
| ------- | ------- | ------------------- |
| Success | #22C55E | Approved, Completed |
| Warning | #F59E0B | Pending, Hold       |
| Danger  | #EF4444 | Rejected, Blocked   |
| Info    | #0EA5E9 | Active processes    |

---

## Dark Mode (Optional Future)

| Token      | Color   |
| ---------- | ------- |
| Background | #0F172A |
| Surface    | #1E293B |
| Text       | #E2E8F0 |

---

# 3. 🧱 TYPOGRAPHY

## Font

* Primary: `Inter`, `Poppins`
* Fallback: `sans-serif`

---

## Font Scale

| Type  | Size | Weight |
| ----- | ---- | ------ |
| H1    | 24px | 600    |
| H2    | 20px | 600    |
| H3    | 18px | 500    |
| Body  | 14px | 400    |
| Small | 12px | 400    |

---

## Usage Rules

* Titles → bold, dark
* Labels → medium, muted
* Data → normal, clear

---

# 4. 📐 LAYOUT SYSTEM

## Grid

* Use Bootstrap Grid (12-column)
* Container: `container-fluid`

---

## Spacing Scale

| Token | Size |
| ----- | ---- |
| xs    | 4px  |
| sm    | 8px  |
| md    | 16px |
| lg    | 24px |
| xl    | 32px |

---

## Layout Structure

```text
Sidebar (fixed)
Top Navbar
Main Content Area
    → Stepper
    → Page Content
```

---

# 5. 🧭 NAVIGATION

## Sidebar

### Behavior

* Fixed left
* Collapsible
* Icon + label

---

### Menu Order (STRICT FLOW)

```text
Procurement Need
Vendor
PO
GRN
QC RM
RM Inventory
Product Master
Inquiry
Quotation
Sales Order
MRP
Production
FG QC
FG Inventory
Allocation
Dispatch
Billing
Delivery
```

---

## Top Navbar

Include:

* Search bar
* Notifications
* User profile
* Sync status toggle

---

# 6. 🔁 WORKFLOW STEPPER (CRITICAL COMPONENT)

## Purpose

Represents **ERP flow progression**

---

## Structure

```html
<div class="stepper">
  <div class="step completed">Vendor</div>
  <div class="step active">PO</div>
  <div class="step">GRN</div>
</div>
```

---

## States

| State     | Style |
| --------- | ----- |
| Completed | Green |
| Active    | Blue  |
| Pending   | Grey  |

---

## Rules

* Must appear on EVERY page
* Clickable navigation
* Horizontal scroll on small screens

---

# 7. 🧩 CORE COMPONENTS

---

## 7.1 Cards

### Usage

* Summary info
* KPIs

### Style

* White background
* Rounded (12px)
* Shadow: subtle

---

## 7.2 Tables (MOST USED)

### Structure

| Column  | Description        |
| ------- | ------------------ |
| ID      | Primary identifier |
| Name    | Entity             |
| Status  | Badge              |
| Actions | Buttons            |

---

### Rules

* Zebra rows optional
* Hover highlight
* Sticky header (optional)

---

## 7.3 Forms

### Style

* Label above input
* Full-width inputs
* Consistent spacing

---

### Input Types

* Text
* Dropdown
* Number
* Date

---

## 7.4 Buttons

| Type      | Style |
| --------- | ----- |
| Primary   | Blue  |
| Secondary | Grey  |
| Danger    | Red   |
| Success   | Green |

---

## 7.5 Badges (VERY IMPORTANT)

### Examples

```html
<span class="badge bg-success">Approved</span>
<span class="badge bg-danger">Blocked</span>
<span class="badge bg-warning">Pending</span>
```

---

# 8. 🔀 DECISION UI (ERP LOGIC)

## Example: Stock Check

```html
<div class="decision-box">
  <h5>Is Stock Available?</h5>
  <button class="btn btn-success">Yes → Dispatch</button>
  <button class="btn btn-danger">No → MRP</button>
</div>
```

---

## Rules

* Always visible
* Clear actions
* Color-coded

---

# 9. 📊 STATUS SYSTEM

## Sales Order

```text
Draft → Confirmed → In Progress → Allocated → Dispatched → Completed
```

---

## Purchase Order

```text
Draft → Approved → Partially Received → Fully Received
```

---

## Production

```text
Planned → Running → Completed → QC Pending → Approved
```

---

# 10. 🎬 ANIMATIONS

## Allowed

* Hover lift
* Fade-in
* Progress bar animation
* Stepper transition

---

## Avoid

* Heavy JS libraries
* Complex motion
* Distracting effects

---

# 11. 🏭 ERP-SPECIFIC UI PATTERNS

---

## 11.1 Allocation Screen

* Left: Sales Order
* Right: FG Inventory
* Action: Allocate quantity

---

## 11.2 Dispatch Tracker

```text
Packing → Loading → Verified → Dispatched
```

Use progress bar or stepper

---

## 11.3 MRP Screen

Show:

* Required RM
* Available RM
* Shortage

---

# 12. 🔗 NAVIGATION FLOW RULES

* GRN → QC RM
* QC RM → RM Inventory
* SO → Allocation / MRP
* MRP → Production / PO
* Production → FG QC
* FG Inventory → Allocation
* Allocation → Dispatch
* Dispatch → Billing
* Billing → Delivery

---

# 13. 📦 FILE STRUCTURE

```text
/pages
  dashboard.html
  procurement-need.html
  vendor.html
  po.html
  grn.html
  qc-rm.html
  inventory-rm.html
  product-master.html
  inquiry.html
  quotation.html
  sales-order.html
  mrp.html
  production.html
  qc-fg.html
  inventory-fg.html
  allocation.html
  dispatch.html
  billing.html
  delivery.html

/assets
  css/
  js/
  icons/
```

---

# 14. 🚀 DEVELOPMENT RULES

* Use Bootstrap 5 only
* No heavy frameworks
* Reusable components (sidebar, navbar)
* Clean semantic HTML
* Keep JS minimal

---

# 15. 🧠 FINAL DESIGN PRINCIPLE

> “This is not a dashboard.
> This is a workflow system.”

---

## ✔ Every screen must answer:

* Where am I in the process?
* What is the current status?
* What is the next action?

---

# ✅ END OF DESIGN SYSTEM
