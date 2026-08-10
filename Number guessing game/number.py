import random as rnd

while True:
    try: 
        user_range = int(input("Select your guessing range from 1 to ?: "))
        if isinstance(user_range, int):
            break
    except: 
        print("You entered an invalid value. Please enter a number.")
    
guess_num = rnd.randint(1, user_range)

counter = 0

print("Enter your guess below: ")

cond = True

while cond:
    try:
        counter += 1
        user_guess = input()
        if user_guess == "exit":
            break
        else:
            user_guess = int(user_guess)
        if user_guess == 67 and user_guess == guess_num:
            print("⣿⣿⡿⣛⠽⠛⠓⠒⠒⠒⠫⢟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
            print("⣿⣫⠊⠁⠀⠀⠀⡀⠀⠀⠀⠀⠱⡽⣿⡍⠛⠛⠛⠛⠿⠭⠭⠭⠭⠽⢟⣛⣛⠻")
            print("⣯⠁⠀⠀⠀⢰⠁⢀⡱⠤⠔⠒⠋⠁⣹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡃")
            print("⢸⠀⠀⠀⠀⠠⢀⡿⠯⠄⠤⢖⡾⣿⣿⠧⠤⠤⢤⣀⣀⣀⡀⠀⠀⠀⠀⠀⡠⠁")
            print("⢸⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠉⢪⣻⣶⣤⣤⣤⣤⢄⠜⠁⠀⠀⠀⡠⠊⠀⣤")
            print("⣼⠀⠀⠀⠀⠀⡴⠚⣒⢄⠀⠀⠀⠀⢳⢻⣿⣿⣿⢯⠃⠀⠀⠀⢀⠜⠁⣰⣿⣿")
            print("⣗⡄⠀⠀⠀⠘⡄⣾⣿⣧⡇⠀⠀⠀⢸⠀⣿⣿⣳⠃⠀⠀⠀⢀⡎⠀⣼⣿⣿⣿")
            print("⣿⡙⡄⠀⠀⠀⠙⠯⠿⠵⠃⠀⠀⢀⡎⢀⣿⣏⠇⠀⠀⠀⠀⡜⠀⣼⣿⣿⣿⣿")
            print("⣿⣿⣜⠦⣀⠀⠀⠀⠀⠀⠀⣀⡤⠊⢀⣼⡿⡼⠀⠀⠀⠀⢠⠁⢸⣿⣿⣿⣿⣿")
            print("⣿⣿⣿⣷⣤⣉⠑⠒⠒⠋⠉⢀⣀⣴⣿⣿⡗⠧⠀⢄⣀⣀⡸⠀⣿⣿⣿⣿⣿⣿")
            print("⣿⣿⡿⣫⣭⣽⣟⣛⣒⢿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣤⣤⣤⣄⣼⣿⣿⣿⣿⣿⣿")
            print("⡿⣹⣾⣿⢻⣿⣿⣿⣿⣷⡽⣿⣿⣿⣿⣿⣿⣿⣿⡿⢛⣭⣾⣿⣿⣭⡛⢿⣿⣿")
            print("⣜⣛⡛⣡⣽⣿⠿⣏⣼⣿⣧⠹⡿⠿⣿⣿⣿⣿⡿⣱⣿⡟⢿⣿⣿⣿⡿⣿⣦⢿")
            print("⣿⣿⡇⣿⣷⣒⢿⡷⠞⣫⡉⣾⠆⡖⣼⣿⡿⣿⡇⣿⣿⣿⠮⠟⠛⣿⣦⢙⠿⣣")
            print("⣿⣿⣿⣜⣿⡽⣡⣎⣋⠷⢇⣏⡸⣧⣿⣏⢒⣈⡢⢛⠽⠻⣭⡛⢯⣿⣿⢸⣿⣿")
            print("⣿⣿⣿⣿⣎⣻⠿⡣⡾⢟⣚⣵⣿⣿⣿⣿⣞⢧⢻⣯⢽⣧⡳⢿⣶⣽⢇⣿⣿⣿")
            print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣻⣆⡺⠿⣆⣭⣵⣿⣿⣿⣟")
            break
        elif user_guess > guess_num:
            print("\x1b[31mLOWER\x1b[0m")
        elif user_guess < guess_num:
            print("\x1b[32mHIGHER\x1b[0m")
        else:
            if counter == 1:
                print("You guessed it correct on your first try!")
            else:
                print("You guessed it correct! It only took you", counter, "tries.")
            break
    except:
        print("You entered an invalid value. Please enter a number.")
        counter -= 1
