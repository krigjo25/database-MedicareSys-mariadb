CREATE OR REPLACE PROCEDURE newSalary (IN vName VARCHAR(255), IN ySalary DECIMAL(8.2))
    BEGIN

        /************ calculateSalary(vSalary) ********************'

            Inserting a new record for occupation, and salary
            information for the occupation.

        *****************************************************************/

        --  Declare variables
        DECLARE mSalary DECIMAL(7.2);
        DECLARE hSalary DECIMAL (6.2);

        --  Set values to the variables using a function
        SET mSalary = ySalary / 162.5;
        SET hSalary = ySalary / 1950;

        --  Inserting values into the table
        INSERT INTO salaryInfo(occupation, yearlySalary, monthlySalary, hourlySalary)
            VALUES (vName, ySalary, mSalary, hSalary);

    END x

