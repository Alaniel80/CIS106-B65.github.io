#Iana Vasileva  CIS 160 B65    M7P3   10/16/26

#Prompt the user on whether they want to do this program
answer=str(input("Do you want to run this program?")).lower()
count=0

#Conditions and calculation:
while answer=="yes":
    last_name=str(input("Enter your last name:"))
    exam_score_1=float(input("Enter your 1st exam score:"))
    exam_score_2=float(input("Enter your 2nd exam score:"))

    average=(exam_score_1+exam_score_2)/2

    print(last_name,average)

    count=count+1

#ask again
    answer=str(input("Do you want to run this program again?")).lower()

# Display
print("Number of students who entered data:",count)








