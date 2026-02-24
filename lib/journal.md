# Summary: Patient Journal PDF Generation (Python Integration)

### 1. Design and Technology Stack
* **PDF Engine**: The project utilizes the **reportlab** library to generate standardized PDF files for patient journals.
* **Compatibility**: The generated journals are designed to be universally readable using standard tools like Google’s PDF reader or Adobe Acrobat.
* **Sample Layout**: A sample design for the document can be found in the `patientjournal.pdf` reference.

### 2. MariaDB Connector Logic
* **Database Access**: A dedicated Python class is implemented to manage the MariaDB connector, housing functions for both connecting to the database and extracting data.
* **Connection Management**: The system includes a specific function to securely close the database connection once it is no longer required.
* **Data Retrieval**: A function is designed to list medical details such as diagnoses, allergies, and suggested treatments to populate the report.

### 3. Dynamic Data Selection
* **Dynamic Table Access**: The script includes a function to specifically select tables from the **patientRecords** database.
* **Targeted Extraction**: This allows the Python script to access and process individualized patient data based on the unique table names assigned to each patient.

### 4. Technical Requirements (Responsibilities)
* **Libraries**: The core external dependencies are **reportlab** for document layout and **MariaDB** for data sourcing.