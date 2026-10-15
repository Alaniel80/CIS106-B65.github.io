#Iana Vasileva CIS160 B65    M6P4 10/14/26
#User's input
quantity=int(input("Enter number of tickets: "))

#Determine price of the tickets and calculate the total cost
if quantity>=25:
    unit_cost=50
elif 10<=quantity<=24:
    unit_cost=60
elif 5<=quantity<=9:
    unit_cost=70
else:
    unit_cost=75
total_cost=quantity*unit_cost

#Display  the number of tickets, price per ticket and the total cost
print("Number of tickets: ",quantity)
print("Price per Ticket: $",unit_cost)
print("Total cost: $",total_cost)