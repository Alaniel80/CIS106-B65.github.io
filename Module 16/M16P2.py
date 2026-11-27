#Iana Vasileva  CIS160 B65   M116P1 11/26/26
#Modify the above program to save the results to a file in addition to printing/displaying the results.
#If the file does not exist, it must be created. If the file does exist results must be appended. Make sure the program handles both cases.

import tkinter as tk
import os
def calculate():
    #Get user's input from the window
    principal = float(principal_entry.get())
    int_rate = float(rate_entry.get())
    int_rate = int_rate / 100

    balance = principal
    total_interest = 0

    #Create results
    results = ""
    results += f"Principal amount: ${principal:,.2f}\n"
    results += f"Interest rate: {int_rate:.2%}\n"
    results += "\n"
    results += f"{'Year':<8}{'Beginning Balance':<22}{'Ending Balance':<20}\n"
    results += "-" * 50 + "\n"

    #Loop for 5 years
    for i in range(1, 6):
        beginning_balance = balance
        interest = beginning_balance * int_rate
        ending_balance = beginning_balance + interest
        total_interest = total_interest + interest

        #Add each year's results
        results += f"{i:<8}${beginning_balance:<21,.2f}${ending_balance:<20,.2f}\n"

        #The new balance by year
        balance = ending_balance

    #Add total interest
    results += "-" * 50 + "\n"
    results += f"Total interest earned: ${total_interest:,.2f}\n"

    #Display results
    print(results)

    #Save results to file
    with open("interest_results.txt", "a") as file:
        file.write(results)
        file.write("\n")

    print("File saved to:", os.path.abspath("interest_results.txt"))

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