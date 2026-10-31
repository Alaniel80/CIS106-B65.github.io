#Iana Vasileva  CIS160 B65   M10P2  10/30/26
#Define variables
square_feet=0
square_footage_walls=0
square_footage_ceiling=0

#Define function 1 - walls
def compute_square_footage_walls(length,width,height):
    square_footage_walls=(length*height* 2)+(width*height*2)
    return square_footage_walls

#Define function 2 - ceiling or floor
def compute_square_footage_ceiling(length,width):
    square_footage_ceiling=length*width
    return square_footage_ceiling

#Define function 3 - walls
def compute_number_of_gallons_walls(square_feet):
    number_of_gallons_walls=square_feet/50
    return number_of_gallons_walls

#Define function 3 - ceiling
def compute_number_of_gallons_ceiling(square_feet):
    number_of_gallons_ceiling=square_feet/50
    return number_of_gallons_ceiling

#Ask user if they want to run the program
repeat=input("Do you want to run this program (Yes or No:): ").upper()

#loop while fot input
while repeat.upper()=="YES":
    choice=input("Do you want to run this program for walls, ceiling or floor: ").upper()

#loop IF for walls
    if choice=="WALLS":
        length=float(input("Enter the length of the walls: "))
        width=float(input("Enter the width of the walls: "))
        height=float(input("Enter the height of the walls: "))

#call function walls
        square_footage_walls = compute_square_footage_walls(length, width, height)
        number_of_gallons_walls = compute_number_of_gallons_walls(square_footage_walls)

# Display the number of gallons needed
        print("Gallons needed for walls: ",number_of_gallons_walls)

#loop IF for ceiling/floor
    elif choice=="CEILING" or choice=="FLOOR":
        length=float(input("Enter the lenght of the ceiling/floor: "))
        width=float(input("Enter the width of the ceiling/floor: "))

#call function ceiling/floor
        square_footage_ceiling = compute_square_footage_ceiling(length, width)
        number_of_gallons_ceiling = compute_number_of_gallons_ceiling(square_footage_ceiling)

#Display the number of gallons for the ceiling or floor
        print("Gallons needed for ceiling/floor: ",number_of_gallons_ceiling)

#Ask user if they want to run the program
    repeat=input("Do you want to run this program again (Yes or No): ").upper()









