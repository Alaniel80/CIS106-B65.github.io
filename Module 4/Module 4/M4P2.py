#M4P2 CIS 106 B65 Vasileva Iana 10/3/26
#User's input
price_per_share=float(input("Enter the price per share: "))
current_stock_price=float(input("Enter the current stock price: "))
quantity_of_shares=float(input("Enter the quantity of shares: "))

#Calculate Value of stock
value_of_stock=(current_stock_price-price_per_share)*quantity_of_shares

#Display Value of Stock
print("Total price: ", value_of_stock)
if value_of_stock<0:
                    print("You are loosing money")
else: print("You are gaining money")


