#Iana Vasileva  CIS160 B65   M14P3 11/25/26
#Modify problem 2 to use a dictionary for the district code pair.
#Expand the dictionary to include X for international students whose tuition is $800.00 per credit hour and G for reciprocity students whose tuition the same as an I student.
#Instantiate at least one student of each district code.

#Define the object
class Student:
    def __init__(self,first,last,district_code,credits):
        self.first=first
        self.last=last
        self.district_code=district_code
        self.credit=credits

    district_rate={
        "I":250.00,
        "O":500.00,
        "X":800.00,
        "G":250.00}

    def tuition_owed(self):
        tuition=self.credit*self.district_rate[self.district_code]
        return tuition

#Instatiate the object
stud1=Student("Iana","Vasileva","I",12)
stud2=Student("Laura","Townsend","O",10)
stud3=Student("Emily","Smith","X",12)
stud4=Student("Kathy","Jones","G",8)


#Use the object
print(f"{'First':<10}{'Last':<12}{'District':<10}{'Credits':<10}{'Tuition':<10}")
print("-" * 50)

print(f"{stud1.first:<10}{stud1.last:<12}{stud1.district_code:<10}{stud1.credit:<10}${stud1.tuition_owed():,.2f}")
print(f"{stud2.first:<10}{stud2.last:<12}{stud2.district_code:<10}{stud2.credit:<10}${stud2.tuition_owed():,.2f}")
print(f"{stud3.first:<10}{stud3.last:<12}{stud3.district_code:<10}{stud3.credit:<10}${stud3.tuition_owed():,.2f}")
print(f"{stud4.first:<10}{stud4.last:<12}{stud4.district_code:<10}{stud4.credit:<10}${stud4.tuition_owed():,.2f}")
