# Database Archive Summary

### 1. Payment and Billing Lifecycle
* **Archive Purpose**: This database serves as a permanent archive for `paidBillings`, `billCredited`, and `terminatedEmployee` records.
* **Payment Trigger**: When a bill is settled, a database trigger automatically generates a new row in the `paidBillings` table.
* **Overdue Handling**: If a bill remains unpaid past the due date, it is moved to the `billCredited` table, and a fine is automatically applied.
* **Debt Collection**: Once payments are successfully retrieved by credit collectors, the record is moved back from `billCredited` into the `paidBillings` archive.

### 2. Employee Offboarding
* **Termination Records**: Whenever an employee resigns or is dismissed, their data is registered within the `terminatedEmployee` table for historical tracking.

### 3. Automated Monitoring
* **Payment Verification Event**: An automated event is scheduled to verify whether patients have paid their respective bills.
**Event**

* An event will be trigged to check wheter the patient has paid the given bill.
[Visualization over Tables](./archive-erdiagram.md)
[Visualization over sequences](./archive-sequencediagram.md)

