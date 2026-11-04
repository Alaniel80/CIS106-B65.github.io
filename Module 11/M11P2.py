#Iana Vasileva  CIS160 B65   M11P2   11/3/26
#Define variables and function to compute the average and total points
exam_score_1=0
exam_score_2=0
exam_score_3=0
total_points=0

def average(exam_score_1,exam_score_2,exam_score_3):
    average_score=(exam_score_1 + exam_score_2 + exam_score_3)/3
    total_points=exam_score_3+exam_score_2+exam_score_1
    return average_score,total_points

# Input from user- Enter the student’s last name and 3 exam scores
last_name=input("Enter your last name: ")
exam_score_1=float(input("Enter your first exam score: "))
exam_score_2=float(input("Enter your second exam score: "))
exam_score_3=float(input("Enter your third exam score: "))

#Call function
average_score, total_points=average(exam_score_1,exam_score_2,exam_score_3)

#Display results
print("Student's last name: ", last_name)
print(f"Student's average score: {average_score:.2f}")
print("Student's total points: ", total_points)



