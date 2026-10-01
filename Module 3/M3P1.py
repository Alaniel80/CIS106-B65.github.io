# Get information from user
stock=input("Enter stock symbol: ")
shares=float(input("Enter number of shares: "))
cost=float(input("Enter number of sdhares: "))
#Compute amount invested
amount_invested=shares*cost
#Display the result
print("Amount invested into ",stock,"is ${:.2f}".format(amount_invested))
            
