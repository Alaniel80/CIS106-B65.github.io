#Iana Vasileva  CIS160 B65   M11P1    11/3/26
#Define 2 functions and assign variables
price=0
discount_rate=0
quantity=0

def compute_discount(price,discount_rate):
    discount_amount=price*discount_rate
    discounted_price=price-discount_amount
    return discount_amount, discounted_price


#User's input
quantity=int(input("Enter the quantity: "))
price=float(input("Enter the price: $"))
discount_rate=float(input("Enter the discount rate: "))/100

#Call function
discount_amount, discounted_price=compute_discount(price,discount_rate)

#Display results
print("Quantity: ",quantity)
print(f"The price is: ${price:,.2f}")
print(f"Discount amount is: ${discount_amount:,.2f}")
print(f"Discounted price is: ${discounted_price:,.2f}")



