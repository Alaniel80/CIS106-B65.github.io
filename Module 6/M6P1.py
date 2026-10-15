#Iana Vasileva CIS160 B65    M6P1 10/14/26

#User's input
quantity=int(input("Enter the quantity of widgets: "))

#Calculate extended price and total price
if quantity>10000:
    price=10
elif 5000<=quantity<10000:
    price=20
else:
    price=30
tax_rate = 0.07
extended_price=price*quantity
tax_amount=extended_price*tax_rate
total=extended_price+tax_amount

#Display extended price, tax amount and total
print(f"Extended price: ${extended_price:,.2f}")
print(f"Tax amount: $ {tax_amount:,.2f}")
print(f"Total price: $ {total:,.2f}")