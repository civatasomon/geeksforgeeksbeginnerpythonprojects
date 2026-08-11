import sys, random as rnd, readchar

def hand(choice):
    if choice == 1:
        return "rock"
    elif choice == 2:
        return "paper"
    elif choice == 3:
        return "scissors"
    else:
        return "I don't know this game."

def computer_win():
    print("You lose.")
def player_win():
    print("You win!")
def tie(choice):
    print("It's a tie of", choice)

while True:
    try:
        computer = rnd.randint(1,3)
        sys.stdout.write("1- Rock\n2- Paper\n3- Scissors\nWhich one do you choose? Enter 1/2/3: ")
        sys.stdout.flush()
        player = int(input())
        if computer == 1:
            if player == 1:
                tie(hand(1))
            elif player == 2:
                player_win()
            elif player == 3:
                computer_win()
            else:
                print(hand(player))
        elif computer == 2:
                if player == 1:
                    computer_win()
                elif player == 2:
                    tie(hand(2))
                elif player == 3:
                    player_win()
                else:
                    print(hand(player))
        elif computer == 3:
                    if player == 1:
                        player_win()
                    elif player == 2:
                        computer_win()
                    elif player == 3:
                        tie(hand(3))
                    else:
                        print(hand(player))
        else:
            print(hand(computer))
    except ValueError:
        print("Invalid input! Choose either 1 or 2 or 3. Either way, you lose")
    sys.stdout.write("Do you wanna play again? y/n: ")
    sys.stdout.flush()
    ans = readchar.readchar()
    sys.stdout.write(ans+"\n")
    if ans != "y":
        break