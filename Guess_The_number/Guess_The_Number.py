from random import randint

Guessing_number = 0
Attempts = 0
Player_number = 0

def Change_number():
    return randint(1, 100)

def Change_Dificalt():
    Diff = input("Choose The Difficulty: Hard: 'H', Easy 'E' : ").lower()
    if not (Diff == 'h' or Diff == 'e'):
        print("You pick wrong latter!")
        print("=" * 30)
        return Change_Dificalt()
    elif Diff == "h":
        return 5
    elif Diff == 'e':
        return 10

def Another_Game():
    Select = input("Another Round? [y] Yes, [n] No : ").lower()
    if not (Select == 'y' or Select == 'n'):
        print("You pick wrong latter!")
        print("=" * 30)
        return Another_Game()
    elif Select == "y":
        print("\n" * 100)
        return True
    elif Select == 'n':
        print("\n" * 100)
        return False

PlayGame = True
while(PlayGame):
    Attempts = Change_Dificalt()
    Guessing_number = Change_number()
    Player_number =  int(input("Pick a Number between 1 - 100 : "))
    while Attempts > 0:
        if Player_number == Guessing_number:
            print("****** You Got it ******")
            break
        elif Player_number > Guessing_number:
            Attempts -= 1
            print(f"Higher then {Player_number}")
        elif Player_number < Guessing_number:
            Attempts -= 1
            print(f"Lower Then {Player_number}")
        if (Attempts != 0):
            Player_number = int(input(f"{Attempts} Attempts lefts, Pick another Number : "))
        else:
            print("You run out of Attempts")

    if (Attempts == 0):
        print("****** YOU LOSE ******")
    else:
        print("****** YOU WIN ******")
    PlayGame = Another_Game()