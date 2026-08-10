import random as rnd
import sys

word_list = ["cluster", "dopamine", "hell", "governor", "fraternity", "language", "bisexual", "interior", "animal"]
guess_word = rnd.choice(word_list)
ltr_count = len(guess_word)

sys.stdout.write("There are 9 words to be randomly selected for you to guess. You have " + str(ltr_count) + " turns to guess a letter. If you guess correctly, you keep your turn.\n")

while True:
    for letter in range(ltr_count):
        sys.stdout.write("_ ")
    sys.stdout.write("\n")
    ltr_guess = (sys.stdin.readline())
    
    