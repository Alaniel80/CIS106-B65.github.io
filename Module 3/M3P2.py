# Get information from the user
lastname = input ("enter the last name:")
midterm = float(input("Enter the Midterm Exam Score: "))
final=float(input("Enter the Final Exam Score: "))
# Calculate total exam points
total_exam_points=0.40*midterm+0.60*final
# Display the result
print("Total Exam points for ",lastname,"are ",total_exam_points)
