#Iana Vasileva  CIS160 B65   M112P1 11/8/26
# Assign 10 last names to an array.
# Write a function to display the names.
# Write another function to display the names in reverse order.

last_names=["John","Smith","Malone","Barrington","King","Anderson","Townsend","Lee","Miller","Robinson"]

#Define functions
def display_names():
    for name in last_names:
        print(name)

def display_names_reverse():
    i=len(last_names)-1
    while i>=0:
        print(last_names[i])
        i-=1

#Call function
display_names()
print()
display_names_reverse()






