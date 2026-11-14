#Iana Vasileva  CIS160 B65   M113P3 11/14/2026
#Load list of 10 Player Names and Batting Averages from a file into a dictionary.
# Write a function to print the dictionary contents in two columns with a header for the name and average.

#Variables
players={}

#Open the file
file=open("M12P4_players.txt","r")
#Load file into Dictionary
for line in file:
    data=line.split()
    players[data[0]]=float(data[1])

file.close()

#Define function to print the dictionary contentsdef display_stats(player_name, batting_average):
def display_info(players):
    print(f"{"Player_name":<15}{"Batting_average":>15}")
    for name,batting in players.items():
        print(f"{name:<15}{batting:>15.3f}")

#Call function
display_info(players)



