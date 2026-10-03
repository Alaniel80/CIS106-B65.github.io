#M4P4 CIS 106 B65 Vasileva Iana 10/3/26
#User's input
import math

fixed_cost=float(input("Enter your fixed cost: "))
price_per_unit=float(input("Enter your price per unit: "))
cost_per_unit=float(input("Enter your cost per unit: "))

#Compute the break-even point
break_even=fixed_cost/(price_per_unit-cost_per_unit)
break_even_units=math.ceil(break_even)

#Display results
print("You need to sell",break_even_units, "units to break-even")
