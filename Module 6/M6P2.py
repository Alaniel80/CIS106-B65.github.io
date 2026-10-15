#Iana Vasileva CIS160 B65    M6P1 10/14/26

#User's input
part_number=str(input("Enter the part number: "))
quantity=int(input("Enter the quantity: "))

#Calculate total cost
if part_number=="10" or part_number=="55":
    unit_cost=1
elif part_number=="99":
    unit_cost=2
elif part_number=="80" or part_number=="70":
    unit_cost=3
else:
    unit_cost=5
total=quantity*unit_cost

#Display
print("The part number is: ",part_number)
print("Cost per unit: ",unit_cost)
print("Total cost: ",total)
