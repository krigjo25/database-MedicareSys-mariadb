# Hospital Management System (HMS)

## 🚀 Tech Stack

- **Database:** MariaDB (SQL)
- **Backend:** Python 3 (ReportLab, MariaDB-connector)
- **Automation:** SQL Procedures, Triggers, Events, Views
- **PDF Generation:** ReportLab (Python)
- **BLOB Storage:** MariaDB

---

## 🏥 Project Overview
**Developer:** Kristoffer (@krigjo25)  
**Timeline:** Jan 2022 - April 2022  
**Core Stack:** MariaDB, Python (ReportLab, MariaDB-connector)  

A comprehensive hospital administration system designed to streamline medical records, staff scheduling, billing automation, and facility management.

---

## 📂 Database Architecture
The system is modularized into four primary databases to optimize maintenance and data integrity:

1. **patientRegistration**: Manages personal profiles and automated billing.
2. **patientRecords**: Contains dynamic, SSN-indexed tables for individualized health data.
3. **employment**: Tracks staff records, shifts (`Turnus`), and doctor-patient relations.
4. **hospitalManageSystem**: Handles infrastructure (rooms/floors), medicine inventory, and booking.
5. **Archive**: Stores historical data for terminated staff and processed invoices.

---

## 📚 Key Documentation

- [architecture.md](architecture.md): System architecture overview and directory structure
- [docs/TheCase.md](docs/TheCase.md): Project case description
- [lib/databasePython.py](lib/databasePython.py): Python database connector
- [lib/patientJournal.py](lib/patientJournal.py): PDF generation logic
- [lib/customFunctions.py](lib/customFunctions.py): Custom Python utilities
- [databases.sql](databases.sql): Database initialization script
- [accounting/docs/accounting-erdiagram.md](accounting/docs/accounting-erdiagram.md): Accounting ER diagram
- [archive/docs/archive-erdiagram.md](archive/docs/archive-erdiagram.md): Archive ER diagram
- [employeement/docs/employee-erdiagram.md](employeement/docs/employee-erdiagram.md): Employee ER diagram
- [HospitalManagementSystem/docs/hos-erdiagram.md](HospitalManagementSystem/docs/hos-erdiagram.md): Hospital ER diagram
- [patientRegistration/docs/patient-erdiagram.md](patientRegistration/docs/patient-erdiagram.md): Patient ER diagram

For additional diagrams and documentation, see each module's `docs/` subfolder.

---

## ⚙️ Key Technical Features

### SQL Automation
* **Procedures**: Automated registration of patients (`newpatient`), staff (`newemployee`), and room bookings (`bookRoom`).
* **Triggers**: Automated PDF generation upon registration and archive migration for billing status changes.
* **Events**: Automated "housekeeping" tasks, such as re-calculating salaries monthly and deleting obsolete records.
* **Views**: A unified `Rooms` view that merges multiple floor tables into a single interface.

### Python Integration
* **Data Connectivity**: Managed via `databasePython.py` using MariaDB-connector.
* **Document Generation**: Uses **ReportLab** to create standardized PDF journals, invoices, and salary slips.
* **BLOB Storage**: Efficiently stores and retrieves binary data (PDFs) directly within the database.

---

## 📊 Summary of Learned Lessons
* **Database Scaling**: Moving from a monolithic structure to multiple databases improved scalability and ease of use.
* **Constraint Management**: Resolved "Foreign Key Issue 150" by strategically using `UNIQUE` constraints where multiple references were required.
* **Code Cleanliness**: Adopted a class-based approach in Python to separate logic (SQL calls, PDF generation, and custom functions) into manageable files.

---

## 📜 Credits & Licensing
* **Dependencies**: `mariadb`, `python-dotenv`, `reportlab`.
* **License**: Open-Source.