#Iana Vasileva  CIS160 B65   M9P2    10/24/26
#Define the function
def compute_batting_avg(number_of_hits,at_bats):
    batting_avg=number_of_hits/at_bats
    return batting_avg
#Define counter
players_num=0

#Input from a user
last_name=str(input("Enter the last name (Enter to stop):"))
while last_name!="":
    number_of_hits=int(input("Enter the number of hits:"))
    at_bats=int(input("Enter the number of at bats:"))

#Count players
    players_num=players_num+1

#display last name and batting average
    print("Last name:",last_name)
    print(f"Batting average:{compute_batting_avg(number_of_hits, at_bats):.3f}")

#next entry
    last_name=str(input("Enter the last name (Enter to stop):"))

#Dispay number of players
print("Players batted:",players_num)





