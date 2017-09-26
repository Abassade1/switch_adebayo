print ("=====WORD GUESS GAME SOLUTION=====")
import random
WORD_LIST =["name", "car", "plane", "laptop", "switch"]

def pick_word(list_word):
    word = random.choice(list_word)
    print ("The word is", word)
    return word

pick_word(WORD_LIST)
def get_guess():
    #print("running the get_guess function")
    guess = input("Guess a word?")
    if not guess == "":
        return guess
    else:
        print ("word cannot be empthy")
get_guess ()

def evaluate_guess():
    #print("running an evaluate function")
    word = pick_word(WORD_LIST)
    guess = get_guess()
    if guess == word:
        print ("your guess is correct")
        return True
    else:
        return False
evaluate_guess()

def play_game():
    if evaluate_guess() == True:
        print ("Your guess is correct")
        resp = input ("Do you want to play again? Y/N")
        if resp == "Y":
            play_game()
        else:
            print ("Goodbye")
    else:
        evaluate_game()
    
play_game()

        
