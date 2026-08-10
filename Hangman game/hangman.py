import sys
import random as rnd
import pandas as pd
import os
repo_path = os.path.abspath("8510732aa9a80a03c829b09f12e20d9c")
if repo_path not in sys.path:
    sys.path.append(repo_path)
from hangmanwordbank import HANGMANPICS, words

alphabet = [["A", "B", "C", "D", "E", "F", "G"],
            ["H", "I", "J", "K", "L", "M", "N"],
            ["O", "P", "Q", "R", "S", "T", "U"],
            ["V", "W", "X", "Y", "Z", "", ""]]

df = pd.DataFrame(alphabet)

sys.stdout.write(df.to_string(index=False, header=False))

# test etmek için bi yorum satırı

