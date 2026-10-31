#Iana Vasileva  CIS160 B65   M10P5 10/30/26
#Define variables
assessed_value=0
sum_market_values=0
sum_assessed_values=0

#Define function
def compute_assessed_value(county,market_value):
    if county=="COOK":
        market_value_percent=0.90
    elif county=="DUPAGE":
        market_value_percent=0.80
    elif county=="MCHENRY":
        market_value_percent=0.75
    elif county=="KANE":
        market_value_percent=0.60
    else:
        market_value_percent=0.70

    assessed_value=market_value_percent*market_value
    return assessed_value

#Ask user if they want to run the program
repeat=input("Do you want to run this program (Yes or No): ")

#Loop while
while repeat.upper()=="YES":
    county=input("Please enter county name: ").upper()
    market_value=float(input("Please enter market value:$ "))

#call on function
    assessed_value=compute_assessed_value(county,market_value)
    sum_market_values=sum_market_values+market_value
    sum_assessed_values=sum_assessed_values+assessed_value

#Display assessed value
    print(f"Assessed value: S{assessed_value:,.2f}")

# Ask user if they want to run the program
    repeat = input("Do you want to run this program again (Yes or No): ")

#Display display all market values and assessed values.
print(f"All market values: ${sum_market_values:,.2f}")
print(f"All assessed values: ${sum_assessed_values:,.2f}")


