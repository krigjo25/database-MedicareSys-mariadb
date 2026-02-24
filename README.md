# Hospital Management System (HMS)

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
* **Contact**: Discord (krigjo25#5588).

*"Everything is perfect at all times."*