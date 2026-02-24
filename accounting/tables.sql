/************************************* Billings **********************************************************/
CREATE TABLE billing (
                    --  Table Columns
                        id BIGINT NOT NULL UNIQUE AUTO_INCREMENT,
                        invoiceID INT NOT NULL UNIQUE, -- AUTO_INCREMENT PRIMARY KEY, AUTO_INCREMENT=300000 
                        patientID BIGINT SIGNED NOT NULL,
                        discount TINYINT NOT NULL,
                        incTax DECIMAL(11,2),
                        overDue DATE NOT NULL,
                        paymentStatus TINYINT NOT NULL DEFAULT 0,
                    
                    -- Table Constraints
                        INDEX (patientID),
                        CONSTRAINT patientID_FK FOREIGN KEY (patientID) REFERENCES patientRegistrations (patientID) ON DELETE CASCADE);
/*************************************************************************************************************/

/******************************** SalaryInfo **************************************************************/
CREATE OR REPLACE TABLE salaryInfo (
                        --  Table Columns
                        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                        occupation VARCHAR(255) NOT NULL, 
                        yearlySalary DECIMAL(10,2) NOT NULL,
                        monthlySalary DECIMAL(7,2) NOT NULL,
                        hourlySalary DECIMAL (5,2) NOT NULL,

                        --  Constraints
                        INDEX(occupation));
/*************************************************************************************************************/

