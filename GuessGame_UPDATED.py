print ("=====WORD GUESS GAME SOLUTION=====")
WORD_LIST =["game", "car", "plane", "laptop", "switch", "civichive"]
import random

def pick_word(list_word):
    word = random.choice(list_word)
    return word

def get_guess():
    #print("running the get_guess function")
    guess = input("Guess a word: ")
    if not guess == "":
        return guess
    else:
        max_attempt = 5
        print ("word cannot be empty")
        get_guess ()#get_guess should call the function!

def evaluate_guess(word, attempts):
    guess = get_guess()
    print(word)
    while attempts > 0:
        guess = get_guess()
        if guess != word:
            attempts -=1
            print ("Wrong attempt, you have", attempts, "attempts left")
            evaluate_guess(word,attempts)
        elif guess == word:
            print ("CONGRATULATIONS YOU JUST WON 1 MILLION USD")

        else:
            print("your guess is correct")
            return True
        break
    if guess == word:
       # print ("you have used up your attempts")
        return False

#evaluate_guess (word, attempts)

def play_game(game_count):
    game_count +=1
    word = pick_word(WORD_LIST)
    print ("WELCOME TO WORD GUESS **SUPER** GAME")
    print()
    truth_var = evaluate_guess(word, 5)
    if truth_var == True:
        print ("CONGRATUALATIONS")
        ask = input("Do you want to play another GAME y/n:")
        if ask == "y":
            play_game(game_count)
        else:
            print ("you played", game_count,"games")
            print ("Goodbye")
            exit()
    elif truth_var != True:
        #print ("oops you missed that one")
        retry = input("Do you want to try another word y/n?")
        if retry == "y":
            play_game(game_count)
        else:
            print ("Goodbye Thanks for Playing")


play_game(0)