#Iana Vasileva  CIS160 B65   M113P2 11/14/2026
# Expand the dictionary from M13P1 to have a list of three grades as the value.
# Create a function to create a list of three grade averages for the class. This list may be a dictionary, a list of lists ([name, average] as each element of the list
# Print the list of students and their grade averages.
# Print the class average for each of the three grades. Layout the output for ease of readability by the user

#Dictionary
student={"Iana":[100,93,92], "Laura":[95,91,88], "Jennifer":[98,90,89], "Emily":[96,97,99]}

#Function
def average_grade(student):
    averages={}

#For each student average
    for name,grades in student.items():
        average=sum(grades)/len(grades)
        averages[name]=average
#For class average for each of three grades
    grade1=0
    grade2=0
    grade3=0
    for grades in student.values():
        grade1+=grades[0]
        grade2+=grades[1]
        grade3+=grades[2]

    grade1_average=grade1/len(student)
    grade2_average=grade2/len(student)
    grade3_average=grade3/len(student)

#Display
    print("STUDENT AVERAGES")
    print("-" * 28)
    print(f"{"Student":<15}{"Grade Average":>10}")
    print("-" * 28)
    for name, average in averages.items():
        print(f"{name:<15}{average:>10.2f}")
    print()
    print("CLASS AVERAGES")
    print("-" * 28)
    print(f"Grade 1 Class Average: {grade1_average:.2f}")
    print(f"Grade 2 Class Average: {grade2_average:.2f}")
    print(f"Grade 3 Class Average: {grade3_average:.2f}")
#Call function
average_grade(student)
