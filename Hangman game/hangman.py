import sys
import random as rnd
import pandas as pd
import os
repo_path = os.path.abspath("./8510732aa9a80a03c829b09f12e20d9c")
if repo_path not in sys.path:
    sys.path.append(repo_path)
from hangmanwordbank import HANGMANPICS, words #type: ignore

alphabet = [["A", "B", "C", "D", "E", "F", "G"],
            ["H", "I", "J", "K", "L", "M", "N"],
            ["O", "P", "Q", "R", "S", "T", "U"],
            ["V", "W", "X", "Y", "Z", "", ""]]

df = pd.DataFrame(alphabet)


guess_word = rnd.choice(words)
ltr_count = len(guess_word)

counter = 0
blanks = "_" * ltr_count

while counter < 6:
    blanks_prvs = blanks
    sys.stdout.write("Hello. You have " + str(6 - counter) + " tries left to guess the word. You guess a character each turn. If you guess it correct, you keep your guessing right.\n")
    sys.stdout.write(HANGMANPICS[counter] + "\n")
    sys.stdout.write(blanks + "\n\n")
    sys.stdout.write(df.to_string(index=False, header=False))
    sys.stdout.write("\033[4FGuess the letter: ")
    guessed_letter = str(input())
    df = df.replace(guessed_letter.capitalize(), " ")
    sys.stdout.write("\033[3B\n")
    for idx in range(ltr_count):
        if guessed_letter == guess_word[idx]:
            blanks = blanks[:idx] + guessed_letter + blanks[idx + 1:]
    if blanks_prvs.count("_") == blanks.count("_"):
        counter += 1
    if blanks.count("_") == 0:
        sys.stdout.write("You win!!")
        break
    sys.stdout.write("\033[15F\033[J")
if 6 - counter == 0:
    sys.stdout.write("You lost! LMAO")
