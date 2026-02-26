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
The system is modularized into five primary databases to optimize maintenance and data integrity:

1. **[patientRegistration](patientRegistration/)**: Manages personal profiles and automated billing.  
   - See [patientRegistration/docs/README.md](patientRegistration/docs/README.md) for details.
2. **[patientRecords](patientRecords/)**: Contains dynamic, SSN-indexed tables for individualized health data.
3. **[employeement](employeement/)**: Tracks staff records, shifts (`Turnus`), and doctor-patient relations.  
   - See [employeement/docs/Employee.md](employeement/docs/Employee.md) for details.
4. **[hos-system](hos-system/)**: Handles infrastructure (rooms/floors), medicine inventory, and booking.
5. **[archive](archive/)**: Stores historical data for terminated staff and processed invoices.  
   - See [archive/docs/README.md](archive/docs/README.md) for details.

For a visual overview and directory structure, see [docs/architecture.md](docs/architecture.md).

---

## 📚 Key Documentation
- [docs/architecture.md](docs/architecture.md): System architecture overview and directory structure
- [docs/TheCase.md](docs/TheCase.md): Project case description
- [lib/databasePython.py](lib/databasePython.py): Python database connector
- [lib/patientJournal.py](lib/patientJournal.py): PDF generation logic
- [lib/customFunctions.py](lib/customFunctions.py): Custom Python utilities
- [databases.sql](databases.sql): Database initialization script

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