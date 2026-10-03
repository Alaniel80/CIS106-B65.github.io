#M4P3 CIS 106 B65 Vasileva Iana 10/3/26
#Users input
total_for_a_meal=float(input("Enter the total amount for a meal: "))

#Compute a tip at 15%, 18% and 20%
tip_15=total_for_a_meal*0.15
tip_18=total_for_a_meal*0.18
tip_20=total_for_a_meal*0.20
total_tip15=tip_15+total_for_a_meal
total_tip18=tip_18+total_for_a_meal
total_tip20=tip_20+total_for_a_meal

#Display results
print("With 15% Tip:")
print ("Total:",format(total_for_a_meal,".2f"))
print("Tip:", format(tip_15,".2f"))
print("Total with Tip ",format(total_tip15,".2f"))
print()
print("With 18% Tip:")
print ("Total:",format(total_for_a_meal,".2f"))
print("Tip:", format(tip_18,".2f"))
print("Total with Tip ",format(total_tip18,".2f"))
print()
print("With 20% Tip:")
print ("Total:",format(total_for_a_meal,".2f"))
print("Tip:", format(tip_20,".2f"))
print("Total with Tip ",format(total_tip20,".2f"))




