#Iana Vasileva  CIS160 B65   M14P1 11/25/26
#Create employee class and test it to make sure it works.
#Add a method to the class that accepts a bonus rate for the employee. It should then compute the employee bonus of rate x salary and return this value.
#Demonstrate this method works by entering a bonus rate and displaying the bonus.

#Define the object
class Employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+"."+last+"@company.org"

    def bonus(self,rate):
        b=float(rate)*float(self.pay)
        return b

# Instantiate the object
empl1=Employee("Iana","Vasileva",70000.00)

#Use the object
print(empl1.first)
print(empl1.last)
print(empl1.email)
print(empl1.pay)
print(empl1.bonus(0.05))


