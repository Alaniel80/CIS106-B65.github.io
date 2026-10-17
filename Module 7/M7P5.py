#Iana Vasileva  CIS 160 B65    M7P5   10/16/26

#Prompt the user on whether they want to do this program
answer=str(input("Do you want to run this program?")).lower()
sum_amount=0
sum_discount=0

#Conditions and calculation:
while answer=="yes":
    quantity=int(input("Enter quantity of items:"))
    price=float(input("Enter price of an item:"))
    extended_price=quantity*price

    if extended_price>10000:
        discount=25
    else:
        discount=10
    discount_amount=extended_price*discount/100
    total_price=extended_price-discount_amount

    print("Extended price:", extended_price)
    print("Discount amount:",discount_amount)

    sum_amount+=extended_price
    sum_discount+=discount_amount

 # Ask again
    answer = str(input("Do you want to run this program again?")).lower()

 #Display
print("Sum ammount:",sum_amount)
print("Sum discount:",sum_discount)
