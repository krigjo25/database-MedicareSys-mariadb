CREATE OR REPLACE TRIGGER salaryChanges AFTER UPDATE ON salaryInfo
    FOR EACH ROW BEGIN

        /************ salaryChanges ********************'
            When yearly salary is updated, the trigger will
            recalculate the necsessary values in monthly
            and hourly salary.

        ************************************************/

        --  Declare variables
        DECLARE mSalary DECIMAL(7.2);
        DECLARE hSalary DECIMAL(6.2);
        DECLARE ySalary DECIMAL(9.2);

        --  Set values to the variables using a function

        SELECT yearlyRate into ySalary FROM salaryInfo;
    
        SET hSalary = ySalary / 1950;
        SET mSalary = ySalary = mSalary / 163.5;

        --  Inserting values into the table
        UPDATE salaryInfo SET hourlyRate = hSalary;
        UPDATE salaryInfo SET monthlyRate = mSalary;

    END x