DROP TABLE employees IF EXISTS;
DROP TABLE company IF EXISTS;

CREATE TABLE employees (
    empID           SEQUENCE PRIMARY KEY,
    fname           VARCHAR(25) NOT NULL,
    lname           VARCHAR(25) NOT NULL,
    username        VARCHAR(100) NOT NULL,
    pass            VARCHAR(20) NOT NULL,
    dob             DATE NOT NULL,
    startdate       DATE  NOT NULL,
    incedents       INT DEFAULT 0,
    tardiness       INT DEFAULT 0,
    proj_completed  INT DEFAULT 0,
    managerID       INT REFERENCES employees
        ON DELETE SET NULL
);

CREATE TABLE company (
    company_name    VARCHAR(100) PRIMARY KEY,
    
)