#Iana Vasileva  CIS160 B65   M10P4 10/30/26
#Define variables
ticket_price=0
entries=0

#Define function
def copmute_ticket_price(miles):
    if miles>=30:
        ticket_price=12
    elif miles>=20 and miles<=29:
        ticket_price=10
    elif miles>=10 and miles<=19:
        ticket_price=8
    else:
        ticket_price=5
    return ticket_price

# Ask user if they want to run the program
repeat=input("Do you want to run this program (Yes or No): ")

#Loop while
while repeat.upper()=="YES":
    last_name=input("Enter your Last name: ")
    miles=float(input("Enter miles from downtown Chicago: "))

#call on function
    ticket_price=copmute_ticket_price(miles)

    entries=entries+1

#Display results
    print("Last Name:",last_name)
    print(f"Ticket price: ${ticket_price:.2f}")

# Ask user if they want to run the program
    repeat=input("Do you want to run this program again (Yes or No): ")

#Display total entries
print("Total entries: ",entries)

















