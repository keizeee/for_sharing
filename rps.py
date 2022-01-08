# this is a rock paper scissors simulator
# the program will randomise between rock paper and scissors
# the player can choose best out of however many they want
import random
import re

selection_list = ["Rock", "Paper", "Scissors"]
try:
    nog = int(input ("Welcome to RPS simulator! Please select the number of games you wish to play: "))
except ValueError:
    print ("Please give an integer!")
    exit()
if nog % 2 == 0 or nog < 0:
    nog = int(input ("Welcome to RPS simulator! Please select the number of games you wish to play: "))

count_of_game = 0
win_count = 0
loss_count = 0
number_to_win = (nog+1)/2
while count_of_game <= nog:
    hand = input("Please choose Rock, Paper or Scissors: ")
    if not re.match("[rpsRPS]", hand) or len(hand) != 1:
        print ("Please only type in r, p or s!")
        # hand = input("Please choose Rock, Paper or Scissors: ")
    else:
        r = random.randint(0, 2)
        cpuhand = selection_list[r]
        if hand == "r" or hand == "R":
            hand = 0
        elif hand == "s" or hand == "S":
            hand = 2
        elif hand == "p" or hand == "P":
            hand = 1
        print (hand)
        if hand == r:
            print ("CPU played " + cpuhand)
            print ("Draw!")
        elif hand == 0 and r == 2:
            print ("CPU played " + cpuhand)
            print ("You win!")
            win_count += 1
        elif hand == 2 and r == 0:
            print("CPU played " + cpuhand)
            print("You lose!")
            loss_count += 1
        elif hand < r:
            print("CPU played " + cpuhand)
            print("You lose!")
            loss_count += 1
        elif hand > r:
            print("CPU played " + cpuhand)
            print("You win!")
            win_count += 1
        if win_count == number_to_win or loss_count == number_to_win:
            print("END OF MATCH")
            break

if win_count == number_to_win:
    print ("Congrats you won!")
elif loss_count == number_to_win:
    print("Too bad you lost!")

