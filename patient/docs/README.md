# Summary: Patient Management, Billing, and Dynamic Health Records

### 1. Patient Database and Core Information
* **Database Isolation**: Patient details are stored in a dedicated database to ensure easier maintenance and organized data management.
* **Data Content**: The database captures general information, health history, and the patient's profession to assist assigned doctors in treatment.
* **Management Procedures**:
    * `newPatient()`: Registers a new patient into the database.
    * `modifyPatient()`: Updates existing patient information.
    * `newTable()`: Creates a new record entry within the `patientInfo` section.
* **Data Processing**: Functions are used to convert SSN and phone digits, while BMI calculations are handled externally via Python code.

### 2. Automated Documentation and PDF Events
* **Registration Trigger**: A trigger fires upon the first registration to create a PDF containing personal info, allergies, and diagnosis-based treatments.
* **Dynamic PDF Updates**: An event automatically regenerates the patient's PDF document whenever their information is updated.
* **Recovery Event**: A specific event triggers the creation of a final PDF once the patient has recovered.



### 3. Dynamic Patient Health Records (Patient Info DB)
* **SSN-Based Tables**: This database uses a unique naming convention for health data tables (first 3 letters of name + last 4 digits of SSN) to identify patients.
* **Dynamic Updates**: Tables are updated automatically every time a patient undergoes a procedure at the hospital.
* **Cross-Database Trigger**: Registering a patient in the main `patient` table automatically triggers the creation of their specific health data table.

### 4. Billing System and Financial Logic
* **Invoice Composition**: The system fetches data on visited rooms, procedures performed, and extra treatments to calculate the final bill.
* **Billing Table Structure**: Tracks `patientID`, `invoiceID`, tax status (`incTax`), reminders, and overdue status.
* **Financial Procedures**:
    * `newBilling(vpID)`: Inserts the necessary values required to generate the invoice PDF.
    * `updateBilling()`: Allows for the correction of billing values if they were added incorrectly.
* **Overdue and Payment Triggers**:
    * **Automation**: An event monitors the due date; if missed, it triggers a new overdue notice and adds a fine.
    * **Archiving**: Records are triggered into the `credited` table if overdue, or the `paidBillings` table upon successful payment.

---

## 📊 Diagrams & Documents

- [patient-erdiagram.md](patient-erdiagram.md): Entity Relationship Diagram for patient tables
- [patient-flowchartdiagram.md](patient-flowchartdiagram.md): Flowchart Diagram for patient processes
- [patient-sequencediagram.md](patient-sequencediagram.md): Sequence Diagram for patient operations
- [patientJournal.odt](patientJournal.odt): Patient Journal (OpenDocument)
- [patientJournal.pdf](patientJournal.pdf): Patient Journal (PDF)