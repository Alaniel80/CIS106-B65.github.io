#Iana Vasileva CIS 106B65     M5P4  10/11/26
#User Input
appl_name=str(input("Enter appl name: "))
appl_cost=float(input("Enter appl cost: "))

#Compute warranty cost if/else
if appl_cost>1000:
    warranty_cost=appl_cost*0.10
    total = appl_cost + warranty_cost
else:
    warranty_cost=appl_cost*0.05
    total=appl_cost+warranty_cost

#Display name, warranty cost and total
print("Name of the appliance: ", appl_name)
print(f"Applaiamce cost: $,{appl_cost:.2f}")
print(f"Warranty cost: $,{warranty_cost:.2f}")
print("Total: $", total)
