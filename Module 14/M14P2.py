#Iana Vasileva  CIS160 B65   M14P2 11/25/26
#Create a student class.
#This class should consist of student first name, student last name, district code (I or O) and enrolled credits.
#Create a method to compute tuition owed. Tuition owed should be enrolled credits times $250.00 per credit hour for in district students (district code of I) and or times $500.00 per credit hour for out of district students (district code of anything other than I).
#Test the class by instantiating the object and adding data.

#Define the object
class Student:
    def __init__(self,first,last,district_code,credits):
        self.first=first
        self.last=last
        self.district_code=district_code
        self.credit=credits

    tuition=0
    def tuition_owed(self):
        if self.district_code=="I":
            tuition=250.00*self.credit
        else:
            tuition=500.00*self.credit
        return tuition

#Instatiate the object
stud1=Student("Iana","Vasileva","I",12)

#Use the object
print(stud1.last)
print(stud1.first)
print(stud1.credit)
print(stud1.district_code)
print(stud1.tuition_owed())

