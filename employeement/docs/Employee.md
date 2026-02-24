#   Summary: Employee Management & Automated System Design
1. Database Architecture & Organization
   - Dedicated Database: Employee-related information is managed in its own database to streamline administration and enhance security.
   - Central Employee Table: The Employee table serves as the primary repository for both personal details (name, address) and work-specific data (status, hire date).
   - Static Reference Tables: Tables like Occupation store static values such as job titles and salary tiers, ensuring data consistency across the system.

2. Rostering & Leave Management
    -   Automated Rostering (Turnus): A dedicated procedure generates a 3-month medical roster by selecting necessary data from the Employee table.
    -   Sick Day Administration: The system includes a procedure to manage sickDays within the Employee table.
    -   Annual Renewal Event: A scheduled event automatically resets sickDays back to their default value once a year has passed for the employee.

3. Patient Assignment & Recovery Logic
    -   Doctor-Patient Mapping: The system generates specific patient lists assigned to doctors to improve memory and workflow efficiency.
    -   Recovery Event: An automated event monitors patient status and terminates the relationship in the Patient_relationship table once a patient is marked as recovered.
    -   Capacity Management: Terminating a relationship automatically frees up a slot, allowing doctors to receive new assignments if their patient limit was previously reached.

4. Financial Procedures & Calculations
   - The Occupation table utilizes stored procedures to automate all salary-related mathematics:
   - Creation Procedure (addNewOccupation): This procedure accepts a yearly salary as input and automatically calculates the corresponding monthly and hourly rates .
   - Update Procedure (editYearlySalary): When a yearly salary is modified, this procedure recalculates the monthly and hourly rates instantly to ensure all financial data remains synchronized .

[Visualization of Tables](./employee-erdiagram.md)
[Visualization of Sequences](./employee-sequencediagram.md)
[Visualization of state](./employee-statediagram.md)
