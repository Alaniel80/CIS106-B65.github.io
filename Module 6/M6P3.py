#Iana Vasileva CIS160 B65    M6P3 10/14/26
#User's Input
principle_amount=int(input("Enter a principle amount: "))
year_to_maturity=int(input("Enter a year to maturity: "))

#Calculate first year interest and determine interest rate
if principle_amount>100000 and year_to_maturity==5:
    int_rate=6
elif 50000<=principle_amount<=100000 and year_to_maturity==5:
    int_rate=4
elif 50000<=principle_amount<=100000 and year_to_maturity==10:
    int_rate=5
else:
    int_rate=2
first_year_int=principle_amount*int_rate/100

#Display principle, interest rate and the interest amount for first year
print("Principle amount:$",principle_amount)
print("Interest rate:%",int_rate)
print("First year interest amount:$",first_year_int)
