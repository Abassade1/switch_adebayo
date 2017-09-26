print ("======WELCOME TO THE HANGMAN GAME 2017===")
import random
alphabet = (a, b, c, d, e, f, g, h, i, j, k, l, m, o, p, q, r, s, t, u, v, w ,x, y, z)
word = understanding
count = 5

def guess_letter ():
    letter = random.choice(alphabet)
    return letter

def letter_guess():
    while count > 0:
        answer = input("Guess a letter from A - Z: ")
        if answer != "":
            return answer
        else:
            max_attmepts = 5
            print ("TRY AGAIN NOTICE! You must insert a letter")
            letter_guess()

def evaluate_answer():
    while True
        for letter in range(len(word)):
            if print ()

