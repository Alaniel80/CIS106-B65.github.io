#Iana Vasileva  CIS160 B65   M9P3    10/24/26
#define function
def compute_mile_per_gallon(miles_traveled,gallons):
    miles_per_gallon = miles_traveled/gallons
    return miles_per_gallon

#Define counter
entries=0

#Input from a user and loop while
dest_city=str(input("Enter the the destination city (Enter to stop):"))
while dest_city!='':
    miles_traveled=float(input("Enter the miles traveled:"))
    gallons=float(input("Enter the gallons used:"))

#Count number of trips
    entries=entries+1

#Display destination city, miles and mpg
    print("Destination city:",dest_city)
    print(f"Miles traveled:{miles_traveled:.2f}")
    print(f"Miles per gallon:{compute_mile_per_gallon(miles_traveled, gallons):.2f}")
    print()

#next entry
    dest_city = str(input("Enter the the destination city (Enter to stop):"))

#Display the number of entries made
print("Number of entries:",entries)
