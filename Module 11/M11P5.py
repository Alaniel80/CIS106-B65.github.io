#Iana Vasileva  CIS160 B65   M11P5
# Allow the user to enter quantity of an item and unit price.
# Write a function to compute total (qty * unit price) and tax (7% of total). Demonstrate your knowledge of global variables by making total and tax global scope.
# Display total land tax in main.

#define variables and function
unit_price=0
quantity=0
total_price=0
tax_amount=0

def compute_totals(unit_price,quantity):
    global total_price, tax_amount
    total_price=unit_price*quantity
    tax_amount=total_price*0.07

#Input from the user
quantity=int(input("Enter the quantity of items: "))
unit_price=float(input("Enter the unit price:$ "))

#Call function
compute_totals(unit_price,quantity)

#Display results
print(f"Total price: ${total_price:,.2f}")
print(f"Tax amount: ${tax_amount:,.2f}")



