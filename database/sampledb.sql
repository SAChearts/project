DROP TABLE IF EXISTS comments;
DROP TABLE IF EXISTS incedents;
DROP TABLE IF EXISTS punctuality;
DROP TABLE IF EXISTS department;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS company;

CREATE TABLE employees (
    empID           INTEGER PRIMARY KEY AUTOINCREMENT,
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
    deptID          INTEGER PRIMARY KEY AUTOINCREMENT,
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

INSERT INTO employees (
    fname,    
    lname,    
    username, 
    pass,     
    dob,      
    startdate,
    managerID )
VALUES
    -- PASSWORD == USERNAME1234
    ('Liam', 'Smith', 'lsmith', '2513f4b7667125c0c49775855c0e9af6', '1 March 1990', '15 February 2018', NULL),
    ('Noah', 'Johnson', 'njohnson', '0454b72ad059857b2f0863165f5d0962', '30 April 1991', '21 June 2018', 1),
    ('Oliver', 'Williams', 'owilliams', '73b50cd04d849f612b05a13299ffcefa', '19 June 1991', '14 May 2019', 1),
    ('Elijah', 'Jones', 'ejones', 'cddc28bef9bee2cba33748d4baa60ef8', '30 June 1991', '20 May 2019', 1),
    ('William', 'Brown', 'wbrown', '4b7b53b828e2bd92bd7433002e3e5efa', '4 September 1991', '27 June 2019', 1),
    ('James', 'Davis', 'jdavis', '6f6d4212ed2396f58a2971fc5c332a7e', '19 March 1992', '9 July 2019', 1),
    ('Benjam', 'Miller', 'bmiller', 'ce6fd11a72b347161df47597948a11a1', '31 July 1993', '19 September 2019', 1),
    ('Lucas', 'Wilson', 'lwilson', 'f06a57d20e8c37e428cd46fe8cc590a4', '29 September 1993', '6 December 2019', 1),
    ('Henry', 'Moore', 'hmoore', '8013f3f7ec2f17f636b2c21930ae5f99', '20 October 1993', '27 March 2020', 1),
    ('Alexand', 'Taylor', 'ataylor', '1f4fbbe507ffd212cf842d0be6d89615', '18 November 1993', '10 April 2020', 1),
    ('Mason', 'Anderson', 'manderson', '64d6392fe0772d6b3a13afb0634d2a92', '3 December 1993', '4 June 2020', 1),
    ('Michael', 'Thomas', 'mthomas', '5b891b67e3bb93df3b29bf75d80e82fa', '18 December 1993', '28 September 2020', 1),
    ('Ethan', 'Jackson', 'ejackson', 'a164ff99e26b2c4034c52a1a076cec23', '3 February 1994', '19 November 2020', 1),
    ('Daniel', 'White', 'dwhite', '9b0d6b257c425926539a0c9a3bbb4635', '15 February 1994', '31 March 2021', 1),
    ('Jacob', 'Harris', 'jharris', 'c39f9cc4324536d2ca51a0922d4060c0', '25 March 1994', '14 April 2021', 1),
    ('Logan', 'Martin', 'lmartin', 'e8f6273161ee47dff1d68ef0ba305abb', '17 April 1994', '15 April 2021', 1),
    ('Jackson', 'Thompson', 'jthompson', 'd72088ac23bb10715cbc42688d218de2', '31 May 1994', '21 May 2021', 1),
    ('Levi', 'Garcia', 'lgarcia', 'c88f225a3b4939fa298bfdd2516105e1', '3 June 1994', '5 November 2021', 1),
    ('Sebasti', 'Martinez', 'smartinez', '6a0fae29949c6df51ba1a19ad69a3b89', '10 June 1994', '9 December 2021', 1),
    ('Mateo', 'Robinson', 'mrobinson', 'f88eca96424b1500b857a7dd4f5ce1ef', '25 July 1994', '15 December 2021', 1),
    ('Olivia', 'Clark', 'oclark', '5e99e5289a13a56837bf9d0b551ac39a', '9 August 1994', '23 April 2018', 1),
    ('Emma', 'Rodriguez', 'erodriguez', 'dad35cab3a563d5e2189b718b07017d2', '30 August 1994', '1 June 2018', 1),
    ('Ava', 'Lewis', 'alewis', 'ffa1fa4ec0dce9f41c4916d902e2881a', '3 October 1998', '5 June 2018', 1),
    ('Charlotte', 'Lee', 'clee', 'a6fa6f611c297f36f1682951b2b1100a', '29 January 1999', '11 October 2018', 1),
    ('Sophia', 'Walker', 'swalker', '0cd0fb20675f9b2180d9c9b39b6348dd', '9 March 2000', '24 October 2018', 1),
    ('Amelia', 'Hall', 'ahall', 'c1d833e1f7fefb5411a1720f991aa61e', '10 January 2004', '2 April 2019', 1),
    ('Isabella', 'Allen', 'iallen', 'c52b00dee92d8c20104aed7b6a9aee0a', '28 February 2011', '14 May 2019', 1),
    ('Mia', 'Young', 'myoung', '3e811e9072dc9e844a0f64b89ac36aaf', '29 January 1999', '4 June 2019', 1),
    ('Evelyn', 'Hernandez', 'ehernandez', '184ae42c50580aad703803dbf6a0c141', '18 December 1993', '14 June 2019', 1),
    ('Harper', 'King', 'hking', 'e85639f024a7b207f31ca4896c1c9935', '3 February 1994', '14 August 2019', 1),
    ('Camila', 'Wright', 'cwright', '9720beda990486f276a504545b4046fa', '15 February 1994', '6 March 2020', 1),
    ('Gianna', 'Lopez', 'glopez', '95e870d9729c696f87f554351d33db10', '28 February 2011', '2 July 2020', 1),
    ('Abigail', 'Hill', 'ahill', '419cf32177b9af5d9c86dbeaa66abe7d', '1 March 1990', '21 July 2020', 1),
    ('Luna', 'Scott', 'lscott', 'e6c2837cda5ca1caa5c36403e86393ff', '9 March 2000', '7 October 2020', 1),
    ('Ella', 'Green', 'egreen', 'd85340c1676711bba930a8ec4cfd6a66', '19 March 1992', '9 October 2020', 1),
    ('Elizabeth', 'Adams', 'eadams', 'fb31f421200a4056ad6f87e0ccde6895', '25 March 1994', '26 January 2021', 1),
    ('Sofia', 'Baker', 'sbaker', '3d1de6b49696ea6bdf641130e4978f6c', '17 April 1994', '15 April 2021', 1),
    ('Emily', 'Gonzalez', 'egonzalez', '3a25ded32422cb5f1807c272f804b842', '30 April 1991', '23 April 2021', 1),
    ('Avery', 'Nelson', 'anelson', 'e359476d5c57de7927b014d3a8116cf6', '31 May 1994', '28 May 2021', 1),
    ('Mila', 'Carter', 'mcarter', 'fd0ac2607faaaa027031439eeb76a0ea', '3 June 1994', '20 September 2021', 1)
;
 
