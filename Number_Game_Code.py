# Basic Number Guessing Game.

# Importing Random_module
import random
num_list = range(1, 101)
com_seletion = random.choice(num_list)
# Displaying the rules to play the game.
def display_info():
    print("\n=================== Instrutions ===================")
    print("1] You have to Guess the number between 1-100.")
    print("2] Your have only 10 Attempt to Guess.")
    print("3] The Computer will selet the number, which you have to Guess.")
    print("4] Computer will give you hints at all attempts.")
    print("------------------------------------------------------")

display_info()

# For loop to ask Number again and again.
i = 1
while i <= 10:
    user_input = int(input("Guess the Computers seletion(1-100): "))
    if (user_input == com_seletion):
        print("\n------------------------------------------------------")
        print("Congratulations,\nYou Guessed it.")
        break
    elif ((user_input > 100) or (user_input < 0)):
        print("Guess The Number Between 1-100.")
    elif (user_input < com_seletion):
        print("Hint : Guess Higher Number\n")
    elif (user_input > com_seletion):
        print("Hint : Guess Lower Numeber\n")
    i += 1
print("------------------------------------------------------")

if (user_input != com_seletion):
    print("You Lose.\nTry again")
    print("------------------------------------------------------\n")
