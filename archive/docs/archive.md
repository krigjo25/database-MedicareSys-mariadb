# Archive
This database is an archive for "paid billings", "billingCredit" and terminated employees.

When a bill gets paid a trigger will trigger a new row in "paidBillings"<br>
table, if its not paid untill overdue date, the bill will be moved into 'billCredited',<br>
then there will be added a fine.<br>

When the credit collectors has retrieved the payment the payment<br>
will be moved into paidBillings.

Whenever an employee resigns or gets fired the employee will be registered in the terminatedEmployee table.

[Visualization over Tables](./archive-erdiagram.md)
[Visualization over sequences](./archive-sequencediagram.md)

**Event**

* An event will be trigged to check wheter the patient has paid the given bill.