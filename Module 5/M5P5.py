#Iana Vasileva  CIS 160B65    M5P2  10/11/26
#User's input
last_name=str(input("Enter last name:"))
number_of_depend=int(input("Enter number of dependents:"))
gross_income=float(input("Enter the gross income:"))

#Compute adjusted gross income and final income tax
adj_gross_income=gross_income-number_of_depend*12000
if adj_gross_income>50000:
    tax_rate=20
else:
    tax_rate=10
income_tax=adj_gross_income*tax_rate/100
if income_tax<0:
    income_tax=100

#Display last name, gross income, number of dependents, adjusted gross income, income tax.
print("Last name:",last_name)
print("Number of depends:",number_of_depend)
print("Gross income: $",gross_income)
print("Adjusted Gross Income: $",adj_gross_income)
print ("Income tax: $",income_tax)