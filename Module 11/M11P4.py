#Iana Vasileva  CIS160 B65   M11P4    11/3/26
#define variables and function to compute average score and average score with handicap
score_game_1=0
score_game_2=0
score_game_3=0
handicap=0

def players_average(score_game_1,score_game_2,score_game_3,handicap):
    average_score=(score_game_1+score_game_2+score_game_3)/3
    average_handicap=average_score+handicap
    return average_handicap,average_score

#Enter bowler’s last name, 3 game scores and handicap
last_name=input("Enter player's last name: ")
score_game_1=int(input("Enter score game 1: "))
score_game_2=int(input("Enter score game 2: "))
score_game_3=int(input("Enter score game 3: "))
handicap=float(input("Enter handicap: "))

#Call function
average_handicap,average_score=players_average(score_game_1,score_game_2,score_game_3,handicap)

#Display the results
print("Player's last name: ", last_name)
print(f"Average score is: {average_score:.2f}")
print(f"Average score with handicap is: {average_handicap:.2f}")
