#Iana Vasileva  CIS106 B65   Final project 11/27/26
#Travel tracker application
#Stores up to 5 records about travel destinations
#The user can add, view, find, delete travel destinations and saves the record to a file when finished

from prettytable import PrettyTable

#Define main menu and get a correct user input
def menu():
    print()
    print("Travel Destinations")
    print("1. Add Destination")
    print("2. View Destinations")
    print("3. Find Destination")
    print("4. Delete Destination")
    print("5. Quit")

    choice = int(input("Enter your choice (1-5): "))

    while choice<1 or choice>5:
        print("Invalid input. Please enter a number from 1 to 5.")
        choice = int(input("Enter your choice (1-5): "))
    return choice

#Define main function. Create 2D List to store records
def main():
    destinations=[]      #For each destination enter Country, City, Days, travel By, Cost
    print("Travel Destination Application")

#The main menu loop
    while True:
        choice=menu()
        if choice==1:
            add_destination(destinations)
        elif choice==2:
            view_destinations(destinations)
        elif choice==3:
            find_destination(destinations)
        elif choice==4:
            delete_destination(destinations)
        elif choice==5:
            save_destinations(destinations)
            print ("Bye. Have a great day!")
            break

#Main menu:1. Add Destination
#Define the function
def add_destination(destinations):
    if len(destinations)>=5:
        print("Maximum of 5 destinations allowed")
        return

#Get user's input
    country=input("Enter the Country: ").title()
    city=input("Enter the City: ").title()
    days=int(input("Enter number of travel days: "))
    travel_by=(input("Enter travel type (plane/car/boat): ")).title()
    cost=float(input('Enter the cost: $'))

#Create a record and add in to the list
    destination=[country,city,days,travel_by,cost]
    destinations.append(destination)

#Print the result
    print("Destination was successfully added.")

#Main menu:2.View Destination.
#Define the function. Use Prettytable to view records
def view_destinations(destinations):
    if len(destinations)==0:
        print('There are no records to view')
        return
    table=PrettyTable()
    table.field_names=["Country","City","Days","Travel By","Cost"]

    for destination in destinations:
        table.add_row(destination)
    print(table)

#Main Menu: 3. Find Destination
#Define the function and get user's input
def find_destination(destinations):
    if len(destinations)==0:
        print("There are no records to find")
        return

    country=input("Enter country to find: ")

    for destination in destinations:
        if destination[0].lower()==country.lower():
            table=PrettyTable()
            table.field_names=["Country","City","Days","Travel By","Cost"]
            table.add_row(destination)
            print(table)
            return

    print("Country not found.")

#Main Menu: 4. Delete Destination
#Define the function and get user's input
def delete_destination(destinations):
    if len(destinations)==0:
        print("There are no records to delete")
        return

    country=input("Enter country to delete: ")
    for destination in destinations:
        if destination[0].lower()==country.lower():
            destinations.remove(destination)
            print(destination[0], "was successfully deleted.")
            return
    print("Country not found.")

#Save records to a file
def save_destinations(destinations):
    file=open("destinations.txt","w")
    for destination in destinations:
        file.write(str(destination)+"\n")
    file.close()
    print("Travel destination records saved to destinations.txt")

#Start the program
main()
