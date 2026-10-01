#Get input from the user
make=str(input("Enter car make:"))
model=str(input("Enter car model:"))
msrp=float(input("Enter MSRP for the car:"))
discount=float(input("Enter Discount percent:"))
#Calculate amount off and discounted price
amount_off=msrp*discount
discounted_price=msrp-amount_off
#Display the results
print("Make:",make)
print("Model:",model)
print("MSRP:",msrp)
print("Discount percent:",discount)
print("Amount off:${:.2f}".format(amount_off))
print("Discounted price:$",discounted_price)
