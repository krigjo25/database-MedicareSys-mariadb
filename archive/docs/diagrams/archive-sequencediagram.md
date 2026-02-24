```mermaid
---
title: "Archive Design for Employee and Billing Records"
---
sequenceDiagram
    participant EMP as Employee(Table)
    participant TERM as Terminated Employee(Table)
    participant ACC as Billing(Table)
    participant CRED as CreditedBillings(Table)
    participant PAID as paidBillings(Table)

    note over ACC: Status changes to 'Paid' or 'Credited'

    EMP->>TERM: TRIGGER: When an employee is terminated from the workplace.

    loop For each paid or credited billing record
        alt
            ACC->>PAID: TRIGGER : When a billing has been paid (using INDEX pID, invoiceID, status)
        else
            ACC->>CRED: TRIGGER : When a billing has been credited by Insurance / Hospital (using INDEX pID, invoiceID, status)
        end
    end
```
    classDef regular color: #f5f5f5, stroke: #555555, stroke-width:1px
    classDef default color: #f5f5f5, stroke: #D3D3D3, stroke-width:1px
    classDef highlight color: #f5f5f5, stroke: #007acc, stroke-width:3px

    Rooms ::: regular
    PATIENT::: highlight
    AvailableMedicines ::: highlight