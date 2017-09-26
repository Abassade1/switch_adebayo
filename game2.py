print ("==============WORD GUESS GAME==================") #random.choice()
print('You have 3 attempts to guess the right product in a Boutique')
print ("PICK FROM THE OPTIONS:""polo,", "belt,", "jeans,", "nike,", "top,", "suit.")
import random
from random import choice

boutique = choice (("polo", "belt", "jeans", "nike", "top", "suit"))
word_guess = ""
tries = ""
count = 0



while count < 2:
    user_guess = input("Guess your desire product:")
    count += 1
    
    if user_guess in boutique:
        print("===HURRAY CONGRATULATIONS===")
        tries += user_guess
##    elif user_guess != boutique and user_guess not in boutique:
##        print("Try again! You can do better")
    else:
        print("Try again! You can do better")


user_guess = input("Again! Guess your desire product:")

if user_guess == boutique:
    print ("===HURRAY CONGRATULATIONS===")
else:
    print("GAME OVER!! Thanks for trying")
    #break


input('Press Enter to leave the program ')

