DROP TABLE IF EXISTS comments;
DROP TABLE IF EXISTS incedents;
DROP TABLE IF EXISTS punctuality;
DROP TABLE IF EXISTS department;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS company;

CREATE TABLE employees (
    empID           INTEGER PRIMARY KEY,
    fname           TEXT NOT NULL,
    lname           TEXT NOT NULL,
    username        TEXT NOT NULL,
    pass            TEXT NOT NULL,
    dob             TEXT NOT NULL,
    startdate       TEXT NOT NULL,
    managerID       INTEGER,
    FOREIGN KEY (managerID) REFERENCES employees(managerID)
);

CREATE TABLE department (
    deptID          INTEGER PRIMARY KEY,
    dept_name       TEXT NOT NULL,
    managerID       INTEGER NOT NULL,
    proj_goal       INTEGER,
    punc_goal       INTEGER,
    incedent_goal   INTEGER,
    FOREIGN KEY (managerID) REFERENCES employees(managerID)

);

CREATE TABLE company (
    co_name    VARCHAR(100) PRIMARY KEY,
    co_mission  TEXT,
    co_tagline TEXT
    
);

CREATE TABLE comments (
    empID       INTEGER,
    comments    TEXT,
    magnitude   INTEGER
);

CREATE TABLE punctuality (
    empID           INTEGER,
    incedent_date   TEXT,
    incedent_type   TEXT,
    magnitude       INTEGER
);

CREATE TABLE incedents (
    empID           INTEGER,
    incedent_date   TEXT,
    incedent_type   TEXT,
    magnitude       INTEGER
);