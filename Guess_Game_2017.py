import random

g_word_list = ["game", "car","plane","laptop","switch","civichive"]
g_game_count = 1


def pick_word():
    word = random.choice(g_word_list)
    return word


def get_guess():
    while True:
        guess = input("Guess a word: ")
        if guess != "":
            return guess
        print ("Word cannot be empty")


def evaluate_guess(word, attempts):
    while attempts:
        guess = get_guess()
        if guess == word:
            return True
        attempts -= 1
        print ("Wrong attempt, you have", attempts, "attempts left")
    return False


def play_game():
    global g_game_count
    word = pick_word()
    attempts = 5
    print ("=====WORD GUESS GAME SOLUTION=====")
    print("WELCOME TO WORD GUESS **SUPER** GAME")
    print()
    truth_var = evaluate_guess(word, attempts)
    if truth_var:
        print("CONGRATULATIONS")
        print("Your guess is correct!")
    else:
        g_game_count += 1
        print("Sorry there are no attempts left!")

    ask = input("Do you want to play another GAME y/n:")
    if ask == "y":
        play_game()
    else:
        print ("you played", g_game_count, "games")
        print ("Goodbye Thanks for Playing")
        exit()


play_game()