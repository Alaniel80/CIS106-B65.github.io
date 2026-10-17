#Iana Vasileva  CIS 160 B65    M7P4   10/16/26

#Prompt the user on whether they want to do this program
answer=str(input("Do you want to run this program?")).lower()
number_of_employees=0
total_gross_pay=0

#Conditions and calculation:
while answer=="yes":
    last_name=str(input("Enter your last name:"))
    hours_worked=float(input("Enter your hours worked:"))
    pay_rate= float(input("Enter your pay rate:"))

    if hours_worked>40:
        overtime_hours=hours_worked-40
        gross_pay=pay_rate*40+overtime_hours*pay_rate*1.5
    else:
        gross_pay=pay_rate*hours_worked

    print(last_name,gross_pay)

    number_of_employees+=1
    total_gross_pay+=gross_pay

    average_pay=total_gross_pay/number_of_employees

#ask again
    answer=str(input("Do you want to run this program again?")).lower()

# Display
print("Number of employees:",number_of_employees,"Total gross pay,",total_gross_pay)
print("Average pay:",average_pay)

