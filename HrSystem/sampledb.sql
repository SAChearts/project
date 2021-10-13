DROP TABLE comments IF EXISTS;
DROP TABLE incedents IF EXISTS;
DROP TABLE punctuality IF EXISTS;
DROP TABLE department IF EXISTS;
DROP TABLE employees IF EXISTS;
DROP TABLE company IF EXISTS;

CREATE TABLE employees (
    empID           INTEGER PRIMARY KEY,
    fname           TEXT NOT NULL,
    lname           TEXT NOT NULL,
    username        TEXT NOT NULL,
    pass            TEXT NOT NULL,
    dob             TEXT NOT NULL,
    startdate       TEXT NOT NULL,
    managerID       INTEGER,
    CONSTRAINT employees_manager_fk FOREIGN KEY (managerID)
        REFERENCES employees(managerID)
);

CREATE TABLE department (
    deptID          INTEGER PRIMARY KEY,
    dept_name       TEXT NOT NULL,
    managerID       INTEGER NOT NULL,
    proj_goal       INTEGER,
    punc_goal       INTEGER,
    incedent_goal   INTEGER,
    CONSTRAINT department_manager_fk FOREIGN KEY (managerID)
        REFERENCES employees(managerID)

);

CREATE TABLE company (
    co_name    VARCHAR(100) PRIMARY KEY,
    co_mission  TEXT,
    co_tagline: TEXT,
    
);

CREATE TABLE comments (
    empID       INTEGER,
    comments    TEXT,
    magnitude   INTEGER,
);

CREATE TABLE punctuality (
    empID           INTEGER,
    incedent_date   TEXT,
    incedent_type   TEXT,
    magnitude       INTEGER,
);

CREATE TABLE incedents (
    empID           INTEGER,
    incedent_date   TEXT,
    incedent_type   TEXT,
    magnitude       INTEGER,
);