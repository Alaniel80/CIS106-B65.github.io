#Iana Vasileva  CIS160 B65   M112P5 11/8/26
#Copy and modify M12P4_players to display a message, “Name not found” when the name is not in the list.

player_name=[]
batting_average=[]

#Open file
file=open("M12P4_players.txt","r")
#Load data
for line in file:
    data=line.split()
    player_name.append(data[0])
    batting_average.append(float(data[1]))

file.close()

#Define function for arrays
def display_stats(player_name, batting_average):
    for i in range(len(player_name)):
        print(player_name[i], ":", format(batting_average[i],".3f"))

#define function for search
def search_player(player_name, batting_average, search_name):
    found=False
    for i in range(len(player_name)):
        if player_name[i].lower() == search_name:
            print("Player name; ", player_name[i], "Batting average:",format(batting_average[i],".3f"))
            found=True
    if found==False:
            print("Name not found")

#call function
display_stats(player_name, batting_average)
#Search loop
search_name=""
while search_name.lower()!="stop":
    search_name=input("Enter player's name or stop: ")
    if search_name.lower()!="stop":
        search_player(player_name, batting_average, search_name)
