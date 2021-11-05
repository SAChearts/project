# from db import *


# class Employee:
#     def __init__(self, emp_id):
#         fname, lname = load_employee(emp_id)
#         self.fname = fname
#         self.lname = lname
#         self.emp_id = emp_id

#     def comments(self):
#         return load_comments(self.emp_id)

#     def incedents(self):
#         return load_incedents(self.emp_id)

#     def punctuality(self):
#         return load_punctuality(self.emp_id)

#     def completed_projects(self):
#         return load_projects(self.emp_id)


# class Manager(Employee):
#     def get_employees(self):
#         return load_employees(self.emp_id)


# if __name__ == "__main__":
#     m = Manager(1)
#     print(m.get_employees())

#     e = Employee(3)
#     print(e.fname)
#     print(e.comments())
