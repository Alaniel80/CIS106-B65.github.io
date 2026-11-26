#Iana Vasileva  CIS160 B65   M8P1    10/21/26
#User's input
principal=float(input("Enter the principle amount:"))
int_rate=float(input("Enter the interest rate:"))
int_rate=int_rate/100

#Display 1: principal amount and rate
print("Principal amount:", principal)
print("Interest rate:", int_rate)

balance = principal
total_interest = 0

# Display 2: year, beginning and ending balances.
print()
print(f"{'Year':<8}{'Beginning Balance':<22}{'Ending Balance':<20}")
print("-" * 50)

# Loop for 5 years
for i in range(1, 6):
    beginning_balance = balance
    interest = beginning_balance * int_rate
    ending_balance = beginning_balance + interest
    total_interest = total_interest + interest

    # Display 3: year, beginning balance and ending balance
    print(f"{i:<8}${beginning_balance:<21,.2f}${ending_balance:<20,.2f}")

    # The new balance by year
    balance = ending_balance

# Display 4: total interest earned
print("-" * 50)
print(f"Total interest earned: ${total_interest:,.2f}")





