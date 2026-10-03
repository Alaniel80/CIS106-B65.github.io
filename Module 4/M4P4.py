#M4P4 CIS 106 B65 Vasileva Iana 10/3/26
#User's input
first_name=str(input("Enter your first name: "))
number_of_steps=int(input("Enter number of steps: "))

#Constant calories in one step
CALORIES=.25

#Calculate number of calories burned
number_of_calories=number_of_steps*CALORIES

#Display results
print(first_name)
print("calories burned:",number_of_calories)

