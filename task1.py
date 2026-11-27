employees=[[1, "Arjun", "Sales", 30000, "Pune"],
    [2, "Priya", "HR", 45000, "Chennai"],
    [3, "Rahul", "IT", 60000, "Bangalore"],
    [4, "Divya", "IT", 75000, "Chennai"],
    [5, "Karthik", "Finance", 90000, "Mumbai"],
    [6, "Meena", "Sales", 52000, "Bangalore"],
    [7, "Suresh", "IT", 68000, "Chennai"],
    [8, "Anitha", "HR", 48000, "Mumbai"]
]

print("Employee Data")

for emp in employees:
    print(emp)

def bonus(salary, rate=0.1, *extras, **options):
    total= salary*rate+sum(extras)
    cap=options.get("cap", total)
    return min(total,cap)
print("Bonus:", bonus(30000,0.1,500, cap=4000))

class Employee:
    def __init__(self, name, salary):
        self.name= name
        self.salary= salary
    def annual_salary(self):
            return self.salary*12
    def get_details(self):
            return self.name,self.salary
        
emp = Employee("Arjun", 30000)

print("Employee Name:", emp.get_details())
print("Annual Salary:", emp.annual_salary())

class Manager(Employee):

    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size=team_size
    def get_details(self):
        return self.name, self.salary, self.team_size
manager= Manager("Priya", 45000, 5)
print("Manager Details:", manager.get_details())
print("Manager Annual Salary:", manager.annual_salary())

class InvalidSalaryError(Exception):
     pass
class Employee:
     def __init__(self,name,salary):
          if salary < 0:
               raise InvalidSalaryError("Invalid salary")
          self.name = name
          self.salary = salary
try:
               emp=Employee("Arun", -500)
except InvalidSalaryError as e:
               print("Error:",e)
finally:
               print("Transaction fininshed")

above_50000=[emp[1] for emp in employees if emp[3]>50000]
print("Above 50000:", above_50000)

new_salary=list(
       map(
              lambda emp: emp[3]*1.10, employees
)
)
print("New Salary:", new_salary)

chennai= list(
       filter(
              lambda emp: emp[4]=="Chennai", employees
       )
)
print("Chennai Employees:")

for emp in chennai:
       print(emp[1])

for emp in employees:
       salary=emp[3]
       if salary == 0:
           continue 
       if salary < 85000:
              print(emp[1], "Salary:", salary)
              
             


