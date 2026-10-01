#Input information
amount1=float(input("Enter amount received by 1st person: "))
amount2=float(input("Enter amount received by 2nd person: "))
amount3=float(input("Enter amount received by 3rd person: "))
#Calculate total amount and split amount
Total_amount_received=amount1+amount2+amount3
Split_amount=Total_amount_received/3
#Display the result
print("Each person received: ${:.2f}".format(Split_amount))
