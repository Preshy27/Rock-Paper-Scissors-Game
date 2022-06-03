import random

prompt = ("R is Rock", "P is Paper",
          "S is Scissors, Choose one of the options")
print(prompt)
options = ['R', 'P', 'S']
print(options)
full = ("Rock", "Paper", "Scissors")
computer = random.choice(options)
player = None

while player not in options:
    player = input("Choose from the options: ").upper()


while computer == player:
    print("Player " + "(" + player + ")")
    print("Computer " + "(" + computer + ")")
    print("Its a tie")
    player = input("Choose from the options: ").upper()


def is_win():
    if player == options[0] and computer == options[2]:
        print("Player " + "(" + options[0] + ")")
        print("Computer " + "(" + computer + ")")
        win = "Player wins"
        print(win)
    elif player == options[1] and computer == options[0]:
        print("Player " + "(" + options[1] + ")")
        print("Computer " + "(" + computer + ")")
        win = "Player wins!"
        print(win)
    elif player == options[2] and computer == options[1]:
        print("Player " + "(" + options[2] + ")")
        print("Computer " + "(" + computer + ")")
        win = "Player wins"
        print(win)


is_win()


def is_lose():
    if player == options[2] and computer == options[0]:
        print("Player " + "(" + options[2] + ")")
        print("Computer " + "(" + computer + ")")
        lose = "Computer wins"
        print(lose)
    elif player == options[0] and computer == options[1]:
        print("Player " + "(" + options[0] + ")")
        print("Computer " + "(" + computer + ")")
        lose = "Computer wins"
        print(lose)
    elif player == options[1] and computer == options[2]:
        print("Player " + "(" + options[1] + ")")
        print("Computer " + "(" + computer + ")")
        lose = "Computer wins"
        print(lose)


is_lose()
