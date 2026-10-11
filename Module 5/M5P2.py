#Iana Vasileva  CIS 160B65    M5P2  10/11/26
#User's input
item_name=str(input("Enter item name:"))
quantity=int(input("Enter quantity:"))

#Compute extendAed price if/else
if item_name=="A":
    unit_price=10.00
else:
    unit_price=20.00
extended_price=unit_price*quantity

#Output item, unit price and extended price
print("Item Name:",item_name)
print("Unit Price:",unit_price)
print("Extended Price:",extended_price)

