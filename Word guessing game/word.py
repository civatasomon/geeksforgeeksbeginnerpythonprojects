import random as rnd
import sys

word_list = ["cluster", "dopamine", "hell", "governor", "fraternity", "language", "bisexual", "interior", "animal"]
guess_word = rnd.choice(word_list)
ltr_count = len(guess_word)


counter = 0
blanks = "_" * ltr_count

while counter < ltr_count:
    blanks_prvs = blanks
    sys.stdout.write("Hello. You have " + str(ltr_count - counter) + " tries to guess the word. You guess a character each turn. If you guess it right, you keep your guessing right.\n")
    sys.stdout.write(blanks)
    sys.stdout.write("\n\nGuess the letter: ")
    guessed_letter = str(input())
    sys.stdout.write("\033[F\033[K\033[F\033[F\033[K\033[F\033[K")
    for idx in range(ltr_count):
        if guessed_letter == guess_word[idx]:
            blanks = blanks[:idx] + guessed_letter + blanks[idx + 1:]
    if blanks_prvs.count("_") == blanks.count("_"):
        counter += 1
    if blanks.count("_") == 0:
        sys.stdout.write("You win!!")
        break
