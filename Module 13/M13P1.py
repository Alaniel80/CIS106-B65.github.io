#Iana Vasileva  CIS160 B65   M113P1 11/14/2026
# Create a dictionary with student name as the key and the grade as the value.
# Print student names and grades and class average grade in two columns with a header for each column.

#Dictionary
student={"Iana":100, "Laura":95,"Jennifer":98,"Emily": 96}

#headings
print(f"{"Student Name":<15}{"Grade":>15}")

#Display
for name,grade in student.items():
    print(f"{name:<15}{grade:>15}")

#Average score
average_score=sum(student.values())/len(student)
print(f"Average score: {average_score:.2f}")

