#Iana Vasileva  CIS160 B65   M11P3    11/3/26
# Produce a sales report.
# Input salesperson last name and sales. Write a function that computes commission which is 10% for sales over $100, 000 and 5% for sales at or under $100,000.
# The function should also computer next year’s target, which is 5% of the sales. This function should return both commission and next year’s target.
# Display salesperson name, commission and next year’s target.

#Define variables and function
sales=0
next_year_target=0

def compute_commission(sales):
    if sales>100000:
        commission=sales*0.10
    else:
        commission=sales*0.05
    next_year_target=sales*0.05
    return commission,next_year_target

#Input from the user
last_name=input("Enter your last name: ")
sales=float(input("Enter your sales:$ "))

#call function
commission,next_year_target=compute_commission(sales)

#Display results
print("Last name: ", last_name)
print(f"Total commission: {commission:,.2f}")
print(f"Total next year target: {next_year_target:,.2f}")
