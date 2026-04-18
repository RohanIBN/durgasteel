# Final Steel Manufacturing ERP Flow Document

## Final Business Flow

```text
Procurement Need Identified
    -> Vendor
    -> PO
    -> GRN
    -> QC RM

QC RM Decision
    -> Approve -> RM Inventory
    -> Reject -> Stop
    -> Hold -> Pending

RM Inventory
    -> Product Master / Capability Check
    -> Sales Inquiry
    -> Quotation
    -> Sales Order

Sales Order Decision 1
    -> Credit Fail -> Block SO
    -> Credit Pass -> Continue

Sales Order Decision 2
    -> Stock Full Available -> SO Allocation -> Dispatch
    -> Stock Partial Available -> Partial Dispatch + Remaining -> MRP
    -> Stock Not Available -> MRP

MRP Decision
    -> RM Available YES -> Production
    -> RM Available NO -> Procurement Loop

Procurement Loop
    -> PO -> GRN -> QC RM -> RM Inventory -> Back to MRP

Production
    -> FG QC

FG QC Decision
    -> Approve -> FG Inventory
    -> Reject -> Rework -> Production -> FG QC
    -> Hold -> Pending

FG Inventory
    -> SO Allocation
    -> Dispatch
    -> Billing
    -> Delivery
    -> POD Upload
    -> Completion
```

---

## Final Stepper Sequence

```text
Procurement Need -> Vendor -> PO -> GRN -> QC -> RM -> Product -> Inquiry -> SO -> MRP -> Production -> FG -> Allocation -> Dispatch -> Billing -> Delivery
```

---

## Final Page Map

### 1. `procurement-need.html`
Purpose:

- starting point for procurement trigger
- captures low stock or manual procurement demand

Inputs:

- need source
- triggered by
- material
- required quantity
- priority

Next:

- `vendor.html`

---

### 2. `vendor.html`
Purpose:

- supplier master for raw material procurement

Inputs:

- vendor name
- GSTIN
- material category
- lead time
- approval status

Next:

- `po.html`

---

### 3. `po.html`
Purpose:

- create purchase order
- support regular procurement and MRP procurement loop

Inputs:

- PO number
- vendor
- material
- quantity
- rate

Statuses shown:

- Draft
- Approved
- Received

Next:

- `grn.html`

---

### 4. `grn.html`
Purpose:

- inward receipt against PO
- weighbridge validation

Inputs:

- PO selection
- truck number
- driver
- gross weight
- tare weight
- net weight

Next:

- `qc-rm.html`

---

### 5. `qc-rm.html`
Purpose:

- raw material quality check before stock release

Checks:

- chemical
- surface
- thickness

Decision:

- Approve -> `inventory-rm.html`
- Reject -> stop flow for lot
- Hold -> pending review

---

### 6. `inventory-rm.html`
Purpose:

- approved raw material stock visibility
- RM source for inquiry and MRP

Table:

- item
- batch
- weight
- status

Next:

- `product-master.html`
- or direct business navigation to `inquiry.html`

---

### 7. `product-master.html`
Purpose:

- capability validation before commercial commitment

Inputs:

- product
- grade
- thickness
- width
- process type

Process types:

- Slitting
- CTL

Next:

- `inquiry.html`

---

### 8. `inquiry.html`
Purpose:

- capture customer requirement
- check feasibility

Inputs:

- customer
- product
- grade
- width
- quantity

Action:

- Check Feasibility

Next:

- `quotation.html`

---

### 9. `quotation.html`
Purpose:

- commercial offer creation

Shows:

- quote number
- base price
- validity
- payment terms

Next:

- `sales-order.html`

---

### 10. `sales-order.html`
Purpose:

- order confirmation with decision logic

Shows:

- SO number
- customer
- product
- quantity
- SO status
- credit status

Sales Order statuses:

- Draft
- Confirmed
- Blocked
- Completed

Decision 1: Credit Check

- Fail -> Block SO and disable next actions
- Pass -> enable stock decision

Decision 2: Stock Check

- Full Available -> `allocation.html`
- Partial Available -> partial dispatch + balance to `mrp.html`
- Not Available -> `mrp.html`

---

### 11. `mrp.html`
Purpose:

- shortage planning and RM decision

Shows:

- required RM
- available RM
- shortage

Decision:

- RM Available YES -> `production.html`
- RM Available NO -> `po.html`

Note:

- this starts procurement loop:
  `po.html -> grn.html -> qc-rm.html -> inventory-rm.html -> mrp.html`

---

### 12. `production.html`
Purpose:

- execute manufacturing after MRP release

Inputs:

- work order
- machine
- planned output

Statuses shown:

- Planned
- Running
- Completed
- QC Pending
- Approved

Actions:

- Start
- Stop

Next:

- `qc-fg.html`

---

### 13. `qc-fg.html`
Purpose:

- finished goods quality decision

Decision:

- Approve -> `inventory-fg.html`
- Reject -> rework -> `production.html` -> QC again
- Hold -> pending

---

### 14. `inventory-fg.html`
Purpose:

- approved FG stock visibility
- ready state before allocation

Table:

- item
- batch
- weight
- status

Next:

- `allocation.html`

---

### 15. `allocation.html`
Purpose:

- allocate FG batches to sales order

Features:

- select sales order
- view FG inventory batches
- allocate quantity
- show allocated quantity

Next:

- `dispatch.html`

---

### 16. `dispatch.html`
Purpose:

- outbound execution after allocation

Dispatch statuses:

- Packing
- Loading
- Verified
- Dispatched

Next:

- `billing.html`

---

### 17. `billing.html`
Purpose:

- tax and invoice closure

Shows:

- invoice number
- GST status
- IRN
- e-way bill

Next:

- `delivery.html`

---

### 18. `delivery.html`
Purpose:

- final customer delivery and closure

Features:

- shipment ID
- customer confirmation
- delivery status
- POD upload
- Mark as Completed button

End:

- Completion

---

## Final Decision Matrix

### QC RM

- Approve -> RM Inventory
- Reject -> Stop
- Hold -> Pending

### Sales Order Credit Check

- Fail -> Block SO
- Pass -> Continue

### Sales Order Stock Check

- Full Available -> Allocation -> Dispatch
- Partial Available -> Partial Dispatch + Remaining -> MRP
- Not Available -> MRP

### MRP RM Availability

- YES -> Production
- NO -> Procurement Loop

### FG QC

- Approve -> FG Inventory
- Reject -> Rework -> Production -> FG QC
- Hold -> Pending

---

## Status Flow Per Entity

### Sales Order Lifecycle

```text
Draft -> Confirmed -> In Progress -> Allocated -> Dispatched -> Completed
```

### Purchase Order Lifecycle

```text
Draft -> Approved -> Partially Received -> Fully Received
```

### Production Lifecycle

```text
Planned -> Running -> Completed -> QC Pending -> Approved
```

---

## Partial Flow Handling

### Stock Check Logic

```text
Full Available -> Allocation -> Dispatch
Partial Available -> Partial Dispatch + Remaining Quantity -> MRP
Not Available -> MRP
```

### Why This Matters

- steel orders are frequently fulfilled from multiple FG lots
- part of the order may ship immediately
- remaining quantity may still need planning and production

---

## Traceability Link

### End-to-End Traceability Chain

```text
Sales Order -> FG Batch -> Production Batch -> RM Batch -> Vendor
```

### Traceability Use Cases

- quality complaint tracing
- vendor-level defect analysis
- audit readiness
- production-to-customer batch mapping

---

## Rework Loop

### Closed-Loop FG Rejection Flow

```text
Production -> FG QC
Reject -> Rework -> Production -> FG QC
Approve -> FG Inventory
Hold -> Wait
```

This ensures the system is not open-ended and rejected finished goods can re-enter controlled production flow.

---

## Advanced Optional Concept

### Allocation Enhancements

- multi-entity allocation against one sales order
- weight-based cost allocation by FG batch

These are advanced features and can be added later without changing the core business flow.

---

## Final Finalized Flow

```text
Procurement Need
   ->
Vendor -> PO -> GRN -> QC RM
   ->
RM Inventory
   ->
Product Master
   ->
Inquiry -> Quotation -> Sales Order
   ->
Credit Check
   ->
Stock Check
   -> Full Available -> Allocation -> Dispatch
   -> Partial Available -> Partial Dispatch + MRP
   -> Not Available -> MRP

MRP
   ->
RM Available?
   -> YES -> Production
   -> NO -> Procurement Loop

Production -> FG QC
   ->
Approve -> FG Inventory
Reject -> Rework -> Production
Hold -> Wait

FG Inventory
   ->
Allocation
   ->
Dispatch -> Billing -> Delivery -> POD -> Completion
```

---

## Final Navigation Chain

```text
GRN -> QC RM
QC RM -> RM Inventory
RM Inventory -> Product Master
Product Master -> Inquiry
Inquiry -> Quotation
Quotation -> Sales Order
Sales Order -> Allocation / MRP
MRP -> Production or PO
Production -> FG QC
FG QC -> FG Inventory
FG Inventory -> Allocation
Allocation -> Dispatch
Dispatch -> Billing
Billing -> Delivery
Delivery -> POD -> Completion
```

---

## Final File List

- `dashboard.html`
- `procurement-need.html`
- `vendor.html`
- `po.html`
- `grn.html`
- `qc-rm.html`
- `inventory-rm.html`
- `product-master.html`
- `inquiry.html`
- `quotation.html`
- `sales-order.html`
- `mrp.html`
- `production.html`
- `qc-fg.html`
- `inventory-fg.html`
- `allocation.html`
- `dispatch.html`
- `billing.html`
- `delivery.html`

