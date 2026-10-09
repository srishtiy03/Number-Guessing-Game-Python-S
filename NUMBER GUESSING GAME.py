import random

def easy():
    num = random.randint(1,100)
    while True:
        ans = int(input("Enter your choice between 0-100. "))
        if num == ans:
            print("Congratulations You Won!!")
            break
        else:
            print("Wrong guess. Please try again.")
            if ans < num:
                print("Think for something higher.")
            else:
                print("Think for something lower")

def medium():
    print("You have 10 chances to win this game.")
    i = 10
    num = random.randint(1,100)
    while i > 0:
        ans = int(input("Enter your choice between 0-100. "))
        if num == ans:
            print("Congratulations You Won!!")
            return
        else:
            i = i - 1
            print("Wrong guess.Please try again.")
            if ans < num:
                print("Think for something higher.")
            else:
                print("Think for something lower.")
            print("Now you are left with",i,"chances only.")
    print("Sorry, you have used all your chances. Better luck next time.")

def hard():
    print("You have 5 chances to win this game.")
    i = 5
    num = random.randint(1,100)
    while i > 0:
        ans = int(input("Enter your choice between 0-100. "))
        if num == ans:
            print("Congratulations You Won!!")
            return
        else:
            i = i - 1
            print("Wrong guess.Please try again.")
            if ans < num:
                print("Think for something higher.")
            else:
                print("Think for something lower")
            print("Now you are left with",i,"chances only.")
    print("Sorry, you have used all your chances. Better luck next time.")

def playgame():
    print("=====NUMBER GUESSING GAME=====")
    print("\nLet's go.....\n")
    print("LEVEL TYPE")
    print("1. EASY")
    print("2. MEDIUM")
    print("3. HARD")

    level = int(input("Select the level number you want to play. "))
    if level == 1:
        easy()
    elif level == 2:
        medium()
    else:
        hard()

while True:
    playgame()
    replay = input("Do you want to play again?(yes/no): ")
    if replay != "yes":
        print("Thank you for playing.")
        break
    else:
        playgame()






