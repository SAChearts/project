DROP TABLE IF EXISTS comments;
DROP TABLE IF EXISTS incedents;
DROP TABLE IF EXISTS punctuality;
DROP TABLE IF EXISTS completed_projects;
DROP TABLE IF EXISTS department;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS company;

CREATE TABLE employees (
    empID           INTEGER PRIMARY KEY AUTOINCREMENT,
    fname           TEXT NOT NULL,
    lname           TEXT NOT NULL,
    username        TEXT NOT NULL,
    pass            TEXT NOT NULL,
    phone           TEXT,
    email           TEXT,
    dob             TEXT NOT NULL,
    startdate       TEXT NOT NULL,
    managerID       INTEGER,
    FOREIGN KEY (managerID) REFERENCES employees(empID)
);


CREATE TABLE department (
    deptID          INTEGER PRIMARY KEY AUTOINCREMENT,
    dept_name       TEXT NOT NULL,
    managerID       INTEGER NOT NULL,
    proj_goal       INTEGER,
    punc_goal       INTEGER,
    incedent_goal   INTEGER,
    FOREIGN KEY (managerID) REFERENCES employees(empID)

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

CREATE TABLE completed_projects (
    empID       INTEGER,
    proj_name   TEXT,
    magnitude   INTEGER
);

CREATE TABLE punctuality (
    empID           INTEGER,
    incedent_date   TEXT,
    incedent_type   TEXT,
    magnitude       INTEGER,
    CONSTRAINT punctuality_type_ck
        CHECK (incedent_type IN ('late', 'excused', 'unexcused'))
);

CREATE TABLE incedents (
    empID           INTEGER,
    incedent_date   TEXT,
    incedent_desc   TEXT,
    magnitude       INTEGER
);

INSERT INTO employees (
    fname,    
    lname,    
    username, 
    pass,    
    phone, 
    email,
    dob,      
    startdate,
    managerID )
VALUES
    -- pass == md5("username1234")
    ('Liam', 'Smith', 'lsmith', '2513f4b7667125c0c49775855c0e9af6', '000-000-0001', 'lsmith@work.com', '1 March 1990', '15 February 2018', NULL),
    ('Noah', 'Johnson', 'njohnson', '0454b72ad059857b2f0863165f5d0962', '000-000-0002', 'njohnson@work.com', '30 April 1991', '21 June 2018', 1),
    ('Oliver', 'Williams', 'owilliams', '73b50cd04d849f612b05a13299ffcefa', '000-000-0003', 'owilliams@work.com', '19 June 1991', '14 May 2019', 1),
    ('Elijah', 'Jones', 'ejones', 'cddc28bef9bee2cba33748d4baa60ef8', '000-000-0004', 'ejones@work.com', '30 June 1991', '20 May 2019', 1),
    ('William', 'Brown', 'wbrown', '4b7b53b828e2bd92bd7433002e3e5efa', '000-000-0005', 'wbrown@work.com', '4 September 1991', '27 June 2019', 1),
    ('James', 'Davis', 'jdavis', '6f6d4212ed2396f58a2971fc5c332a7e', '000-000-0006', 'jdavis@work.com', '19 March 1992', '9 July 2019', 1),
    ('Benjam', 'Miller', 'bmiller', 'ce6fd11a72b347161df47597948a11a1', '000-000-0007', 'bmiller@work.com', '31 July 1993', '19 September 2019', 1),
    ('Lucas', 'Wilson', 'lwilson', 'f06a57d20e8c37e428cd46fe8cc590a4', '000-000-0008', 'lwilson@work.com', '29 September 1993', '6 December 2019', 1),
    ('Henry', 'Moore', 'hmoore', '8013f3f7ec2f17f636b2c21930ae5f99', '000-000-0009', 'hmoore@work.com', '20 October 1993', '27 March 2020', 1),
    ('Harper', 'King', 'hking', 'e85639f024a7b207f31ca4896c1c9935', '000-000-0010', 'hking@work.com', '3 February 1994', '14 August 2019', 1),
    ('Camila', 'Wright', 'cwright', '9720beda990486f276a504545b4046fa', '000-000-0011', 'cwright@work.com', '15 February 1994', '6 March 2020', 1),
    ('Gianna', 'Lopez', 'glopez', '95e870d9729c696f87f554351d33db10', '000-000-0012', 'glopez@work.com', '28 February 2011', '2 July 2020', 1),
    ('Abigail', 'Hill', 'ahill', '419cf32177b9af5d9c86dbeaa66abe7d', '000-000-0013', 'ahill@work.com', '1 March 1990', '21 July 2020', 1),
    ('Luna', 'Scott', 'lscott', 'e6c2837cda5ca1caa5c36403e86393ff', '000-000-0015', 'lscott@work.com', '9 March 2000', '7 October 2020', 1),
    ('Ella', 'Green', 'egreen', 'd85340c1676711bba930a8ec4cfd6a66', '000-000-0016', 'egreen@work.com', '19 March 1992', '9 October 2020', 1),
    ('Elizabeth', 'Adams', 'eadams', 'fb31f421200a4056ad6f87e0ccde6895', '000-000-0017', 'eadams@work.com', '25 March 1994', '26 January 2021', 1),
    ('Sofia', 'Baker', 'sbaker', '3d1de6b49696ea6bdf641130e4978f6c', '000-000-0018', 'sbaker@work.com', '17 April 1994', '15 April 2021', 1),
    ('Emily', 'Gonzalez', 'egonzalez', '3a25ded32422cb5f1807c272f804b842', '000-000-0019', 'egonzalez@work.com', '30 April 1991', '23 April 2021', 1),
    ('Avery', 'Nelson', 'anelson', 'e359476d5c57de7927b014d3a8116cf6', '000-000-0020', 'anelson@work.com', '31 May 1994', '28 May 2021', 1),
    ('Mila', 'Carter', 'mcarter', 'fd0ac2607faaaa027031439eeb76a0ea', '000-000-0021', 'mcarter@work.com', '3 June 1994', '20 September 2021', 1)
;
 
INSERT INTO department (
    dept_name,    
    managerID,    
    proj_goal,    
    punc_goal,    
    incedent_goal)
VALUES
    ('main', 1, 500, 100, 50)
;

INSERT INTO company (co_name, co_mission, co_tagline)
VALUES (
    'Super Service', 
    'Our mission is to provide the best service experience for our customers',
    'Simple Services Made Super!')
;

INSERT INTO comments (empID, comments, magnitude)
VALUES
    (1, 'I am so proud of your sympathetic heart.', 5),
    (3, 'I feel safe with you.', 5),
    (4, 'That thing you don''t like about yourself is what makes you so interesting.', 5),
    (5, 'I appreciate our friendship.', 5),
    (7, 'Our community is better because you’re in it.', 5),
    (9, 'Would you like to be my child’s godmother/godfather?', 5),
    (10, 'I value your opinion.', 5),
    (11, 'I appreciate you.', 5),
    (15, 'I am so proud that you always stand your ground.', 5),
    (17, 'Our family is complete because of you.', 5)
;

INSERT INTO completed_projects (empID, proj_name, magnitude)
VALUES
    (2, 'Fool With A Hat', 5),
    (4, 'Kicked Me Out', 3),
    (6, 'Raven Exploit', 8),
    (8, 'Wife Delusion', 5),
    (10, 'Baker And Soldier', 5),
    (12, 'Hunter And Raven', 1),
    (14, 'Antics Lives With Me', 2),
    (16, 'Parody Prophecy', 7),
    (18, 'Climax Of My Teacher', 5),
    (20, 'Favorite Of My Trick', 3)
;

INSERT INTO punctuality (empID, incedent_date, incedent_type, magnitude)
VALUES
    (1, '22 December 2020', 'late', 5),
    (2, '22 February 2021', 'excused', 5),
    (3, '24 February 2021', 'late', 5),
    (4, '3 March 2021', 'late', 5),
    (5, '17 March 2021', 'unexcused', 5),
    (20, '31 March 2021', 'unexcused', 5),
    (19, '3 September 2021', 'late', 5),
    (18, '7 September 2021', 'late', 5),
    (17, '15 September 2021', 'excused', 5),
    (16, '22 September 2021', 'excused', 5)
;

INSERT INTO incedents (empID, incedent_date, incedent_desc, magnitude)
VALUES
    (1, '22 December 2020', 'Reported wrong hours worked', 5),
    (2, '22 February 2021', 'Stormed out of meeting', 5),
    (3, '24 February 2021', 'Failed to report malfunction', 5),
    (4, '3 March 2021', 'Instigated an argument', 5),
    (5, '17 March 2021', 'Broke office door', 5),
    (20, '31 March 2021', 'Failed to file paperwork', 5),
    (19, '3 September 2021', 'Left out confidential documents', 5),
    (18, '7 September 2021', 'Failed to lock storage room', 5),
    (17, '15 September 2021', 'Distributed inappropriate email', 5),
    (16, '22 September 2021', 'Personal phone call during work hours', 5)
;
