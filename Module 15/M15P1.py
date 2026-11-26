#Iana Vasileva  CIS160 B65   M11P1 11/25/26
#Starting with the Employee class you created in the previous assignment, create a Manager class.
#This class should use the previously created employee class as the base class and make a derived class called Manager.
#This class should include a long term bonus method that computes the long term bonus to be 40% of the manager salary.
#Create a program to instantiate the new class and show that it works for at least two employees and two managers.

#Define the object
class Employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+"."+last+"@company.org"
class Manager(Employee):
    def __init__(self,first,last,pay):
        super().__init__(first,last,pay)

    def long_term_bonus(self):
        b=self.pay*.40
        return b

# Instantiate the object
empl1=Employee("Iana","Vasileva",70000)
empl2=Employee("Jane","Smith",80000)
manag1=Manager("Vicky","Jones",100000)
manag2=Manager("Tim","Crane",150000)

#Use the object
print(f"{'First':<10}{'Last':<12}{'Pay':<15}{'Bonus':<12}")
print("-" * 50)

print(f"{empl1.first:<10}{empl1.last:<12}${empl1.pay:<14,.2f}")
print(f"{empl2.first:<10}{empl2.last:<12}${empl2.pay:<14,.2f}")
print(f"{manag1.first:<10}{manag1.last:<12}${manag1.pay:<14,.2f}${manag1.long_term_bonus():,.2f}")
print(f"{manag2.first:<10}{manag2.last:<12}${manag2.pay:<14,.2f}${manag2.long_term_bonus():,.2f}")


