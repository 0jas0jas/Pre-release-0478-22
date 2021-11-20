# A python program for pre-release material for computer science 0478/22
# Made by Ojas.


#constants
player_names = []
no_players = 0
no_holes = 0
par = 0


#task 1

#SCORE ARRAYS
player1 = []
player2 = []
player3 = []
player4 = []

#Inputting and validating no_players
while True:
    no_players = int(input("How many players are playing? (Please enter give a number between 2 to 4): "))
    if (no_players >= 2 and no_players <= 4):
        break
    else: print("Invalid input. Please try again.")

#Inputting and storing player names to player_names array
for player in range(no_players):
    player_name = input("Player " + str(player + 1) + ", please enter your name: ")
    player_names.append(player_name)

#inputing the number of holes to be played
while True:
    no_holes = int(input("Choose your preffered number of holes (Enter either 9 or 18): "))
    if (no_holes == 9 or no_holes == 18):
        break
    else: print("Invalid input. Please try again.")

#Inputting  par for the course
par = int(input("What would be the par for this course?: "))


#Printing all the inputs
print(""" 
The information that you've entered is as follows:

----------------------------------------------------""")
for player in range(no_players):
    print("Player" + str(player + 1) + ": " + player_names[player])
print("The number of holes that will be played: " + str(no_holes))
print("The par for the course: " + str(par))
print("----------------------------------------------------")

#initialising arrays
for hole in range(no_holes): 
    player1.append(0)
    player2.append(0)
    player3.append(0)
    player4.append(0)

#TASK 2

for hole in range(no_holes):
    print("HOLE " + str(hole + 1))
    print("----------------------------------------------------")
    for player in range(no_players):
        while True:
            strokes = int(input("Player " + player_names[player] + ", enter the number of strokes you played for this hole: "))
            strokesVerification = int(input("Please enter your score again for verification: "))
            if strokes == strokesVerification:
                break
            else: print("Sorry, the scores don't match. Please try again.")
        if player == 0: 
            player1[hole] = strokes
        elif player == 1:
            player2[hole] = strokes
        elif player == 2:
            player3[hole] = strokes
        elif player == 3:
            player4[hole] = strokes

#TASK 3
player1Score = 0
player2Score = 0
player3Score = 0
player4Score = 0

totalScores = []
for score in player1:
    player1Score = player1Score + score
totalScores.append(player1Score)

for score in player2:
    player2Score = player1Score + score
totalScores.append(player2Score)

for score in player3:
    player3Score = player1Score + score
totalScores.append(player3Score)

for score in player4:
    player4Score = player1Score + score
totalScores.append(player4Score)

print("The game has ended. The results are as follows: ")
for player in range(no_players):
    print("Player " + str(player + 1) + ": " + str(totalScores[player]))


#options
