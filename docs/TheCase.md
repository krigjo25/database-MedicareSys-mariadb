# Project Case Summary: Hospital Management System

### 1. Database & Entity Scope
* **Comprehensive Records**: The system requires the creation of databases containing full details for both patients and employees.
* **Patient Profiles**: Patient tables must include personal details, work-related information, and specific health data.
* **Employee Identification**: Every employee will be assigned a unique `employeeID` for identification and tracking.

### 2. Clinical Relationships & Capacity
* **Doctor-Patient Mapping**: Doctors and patients will be linked via defined relationships.
* **Workload Constraints**: A strict limit is set where one doctor can treat a maximum of ten patients at a time.
* **Support Staff**: The hospital infrastructure includes nurses and ward boys dedicated to maintenance and direct patient care.

### 3. Hospital Infrastructure
* **Facility Zones**: The hospital must be organized into distinct functional areas, specifically:
    * Operation Theaters
    * Intensive Care Units (ICU)
    * Emergency Services

### 4. Billing & Financial Logic
* **Invoice Generation**: Bills are generated based on the duration of the hospital stay (number of days) and the specific treatments received.