#Iana Vasileva  CIS160 B65   M116P1 11/26/26
#Choose a problem from previous sessions that has user input. It must also have computed results.
#Reimplement the user prompt with a window for the input. Verify that it works as before with respect to calculations and output.

#Copied from Iana Vasileva  CIS160 B65   M8P1    10/21/26

import tkinter as tk

#Calculate the interest
def calculate():
    #Get user's input from the window
    principal = float(principal_entry.get())
    int_rate = float(rate_entry.get())
    int_rate = int_rate / 100

    #Display 1: principal amount and rate
    print("Principal amount:", principal)
    print("Interest rate:", int_rate)

    balance = principal
    total_interest = 0

    #Display 2: year, beginning and ending balances
    print()
    print(f"{'Year':<8}{'Beginning Balance':<22}{'Ending Balance':<20}")
    print("-" * 50)

    #Loop for 5 years
    for i in range(1, 6):
        beginning_balance = balance
        interest = beginning_balance * int_rate
        ending_balance = beginning_balance + interest
        total_interest = total_interest + interest

        #Display 3: year, beginning balance and ending balance
        print(f"{i:<8}${beginning_balance:<21,.2f}${ending_balance:<20,.2f}")

        #The new balance by year
        balance = ending_balance

    #Display 4: total interest earned
    print("-" * 50)
    print(f"Total interest earned: ${total_interest:,.2f}")


#Create the window
window = tk.Tk()
window.title("Interest Calculator")

#Principal input
principal_label = tk.Label(window, text="Enter the principal amount:")
principal_label.pack()

principal_entry = tk.Entry(window)
principal_entry.pack()

#Interest rate input
rate_label = tk.Label(window, text="Enter the interest rate:")
rate_label.pack()

rate_entry = tk.Entry(window)
rate_entry.pack()

#Calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()

window.mainloop()