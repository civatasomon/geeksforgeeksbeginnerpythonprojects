import readchar, sys, random as rnd

wants = True

list21 = []

print("Welcome to 21 game. You and your opponent will count to 21 together. Each player can say 1-3 numbers in consecutive order.")
print("Example: It is P1's turn and the count is 1 2 3 4. Now P1 has the options to say 5, 5 6, or 5 6 7. Whoever is left to say 21 loses.")
print("If you say the wrong number in your turn, you are disqualified. Press enter after each number and '.' afterwards to stop if you will not say 3 numbers, but 1 or 2.")

def lose():
    print("You lose.")
def win():
    print("You win!!")

def user_turn(list21):
    for i in range(3):
        try:
            ans = int(input("Player   > "))
            if list21:
                if ans - 1 == list21[-1]:
                    list21.append(ans)
                else:
                    return lose()
            else:
                if ans != 1:
                    return lose()
                else:
                    list21.append(ans)
        except ValueError:
            break   
    if list21[-1] == 20:
        return win()
    for i in list21:
        sys.stdout.write(str(i) + " ")
    sys.stdout.write("\n")
    return pc_turn(list21)

def pc_turn(list21):
    try:
        turns = list21[-1] % 4
    except IndexError:
        turns = 0
    try:
        if turns == 0:
            if list21[-1] < 12:
                for i in range(1, 4):
                    print("Computer > ", list21[-1] + 1)
                    list21.append(list21[-1] + 1)
            elif list21[-1] <= 16 and list21[-1] >= 12:
                for i in range(1, 3):
                    print("Computer > ", list21[-1] + 1)
                    list21.append(list21[-1] + 1)
            else:
                for i in range(1, 3):
                    print("Computer > ", list21[-1] + 1)
                    list21.append(list21[-1] + 1)
        else:
            for i in range((4 - turns) % 4):
                print("Computer > ", list21[-1] + 1)
                list21.append(list21[-1] + 1)
    except IndexError:
        for i in range(3):
            print("Computer > ", i + 1)
            list21.append(i + 1)
    if list21[-1] == 20:
        return lose()
    for i in list21:
        sys.stdout.write(str(i) + " ")
    sys.stdout.write("\n")
    return user_turn(list21)

def wants():
    sys.stdout.write("Do you want to play? y/n: ")
    sys.stdout.flush()
    while True:
        cevap = readchar.readchar()
        sys.stdout.write(cevap + "\n")
        if cevap == "y":
            return True
        elif cevap == "n":
            return False
        else:
            sys.stdout.write("y ya da n harflerinden birine tıklayın. y/n: ")
            sys.stdout.flush()

while wants():
    list21 = []
    sys.stdout.write("Do you wanna start first? y/n: ")
    sys.stdout.flush()
    cevap = readchar.readchar()
    sys.stdout.write(cevap + "\n")
    if cevap == "y":
        user_turn(list21)
    elif cevap == "n":
        pc_turn(list21)
    else:
        sys.stdout.write("\nUnclear Intention.")
        who_start = rnd.choice((True, False))
        if who_start:
            user_turn(list21)
        else:
            pc_turn(list21)
    