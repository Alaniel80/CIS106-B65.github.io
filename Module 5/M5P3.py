#Iana Vasileva CIS 106 B65      M5P3 10/11/26
#User input
number_of_books=int(input("Enter number of books:"))
cost_per_book=float(input("Enter cost per book:"))

#Compute shipping charge and total cost
total_cost=cost_per_book*number_of_books
if total_cost>=50:
    shipping=0
else:
    shipping=25

#Output total cost and shipping
print(f"Order total cost: ${total_cost:.2f}")
print(f"Total shipping: ${shipping:.2f}")

