#Iana Vasileva  CIS160 B65   M10P1    10/28/26
#Define function
def compute_forecast(month,sales):
    forecast_percent = 1
    if month in["Jan","Feb","Mar"]:
        forecast_percent=.10
    elif month in["Apr","May","Jun"]:
        forecast_percent=.15
    elif month in["Jul","Aug","Sep"]:
        forecast_percent=.20
    elif month in["Oct","Nov","Dec"]:
        forecast_percent=.25
    else:
        print("Please enter a valid month")
        return 0

    next_month_forecast=sales*(1+forecast_percent)
    return next_month_forecast

#Ask user if they want to run the program
repeat=input("Do you want to run this program (Yes or No): ")

#While
while repeat.upper()=="YES":
    last_name=str(input("Enter your last name:"))
    month=input("Enter month(Jan,Feb,Mar,etc.):").title()
    sales=float(input("Enter sales: $"))

#Call on next month forecast
    next_month_forecast=compute_forecast(month,sales)

#Display results
    print(f"Next month sales: ${next_month_forecast:,.2f}")

#Ask user if they want to run the program again
    repeat=input("Do you want to run this program again (Yes or No): ")

