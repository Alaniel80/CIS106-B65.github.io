#Iana Vasileva CIS 106 B65      M5P1 10/11/26

#Users input
quantity=int(input("Enter quantity: "))

#Compute Extended price and total price


if quantity>=1000:
    unit_price=3
    extended_price = quantity * unit_price
else:
    unit_price=5
    extended_price = quantity * unit_price
tax=extended_price*.07
total=tax+extended_price

#Output: quantity, unit price, extended price, tax and total
print("Unit quantity: ",quantity)
print("Unit price: $",unit_price)
print("Extended price: $",extended_price)
print(f"Tax: $ {tax:.2f}")
print ("Total cost: $",total)

