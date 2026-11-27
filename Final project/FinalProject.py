#Iana Vasileva  CIS160 B65   Final project 11/27/26
#Dog Rescue Application.
#Application stores up to 5 records about the rescued dogs
#The user can add, view, find, delete dogs and saves the record to a file when finished


from prettytable import PrettyTable

#Define main menu and get a correct user input
def menu():
    print()
    print("Dog Rescue Menu")
    print("1. Add Dog")
    print("2. View Dogs")
    print("3. Find Dog")
    print("4. Delete Dog")
    print("5. Quit")

    choice = int(input("Enter your choice (1-5): "))

    while choice<1 or choice>5:
        print("Invalid input. Please enter a number from 1 to 5.")
        choice = int(input("Enter your choice (1-5): "))
    return choice

#Define main function. Create 2D List to store records
def main():
    dogs=[]      #For each dog enter Name, Breed, Age, Weight
    print("Dog Rescue Application")

#The main menu loop
    while True:
        choice=menu()
        if choice==1:
            add_dog(dogs)
        elif choice==2:
            view_dogs(dogs)
        elif choice==3:
            find_dog(dogs)
        elif choice==4:
            delete_dog(dogs)
        elif choice==5:
            save_dogs(dogs)
            print ("Bye. Have a great day!")
            break

#Main menu:1.Add Dog.
#Define the function
def add_dog(dogs):
    if len(dogs)>=5:
        print("Maximum of 5 dogs allowed")
        return

#Get user's input
    name=input("Enter dog's name: ").title()
    breed=input("Enter dog's breed: ").title()
    age=int(input("Enter dog's age: "))
    weight=float(input("Enter dog's weight: "))

#Create a record and add in to the list
    dog=[name,breed,age,weight]
    dogs.append(dog)

#Print the result
    print(name, "was successfully added.")

#Main menu:2.View Dogs.
#Define the function. Use Prettytable to view records
def view_dogs(dogs):
    if len(dogs)==0:
        print('There are no records to view')
        return
    table=PrettyTable()
    table.field_names=["Name","Breed","Age","Weight"]

    for dog in dogs:
        table.add_row(dog)
    print(table)

#Main Menu: 3. Find Dog
#Define the function and get user's input
def find_dog(dogs):
    if len(dogs)==0:
        print("There are no records to find")
        return

    name=input("Enter dog's name to find: ")

    for dog in dogs:
        if dog[0].lower()==name.lower():
            table=PrettyTable()
            table.field_names=["Name","Breed","Age","Weight"]
            table.add_row(dog)
            print(table)
            return

    print("Dog not found.")

#Main Menu: 4. Delete Dog
#Define the function and get user's input
def delete_dog(dogs):
    if len(dogs)==0:
        print("There are no records to delete")
        return

    name=input("Enter dog's name to delete: ")
    for dog in dogs:
        if dog[0].lower()==name.lower():
            dogs.remove(dog)
            print(name, "was successfully deleted.")
            return
    print("Dog not found.")

#Save records to a file
def save_dogs(dogs):
    file=open("dogs.txt","w")
    for dog in dogs:
        file.write(str(dog)+"\n")
    file.close()
    print("Dog records saved to dogs.txt")

#Start the program
main()
