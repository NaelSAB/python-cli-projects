from pydoc import describe
import random
from game_data import data

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

def dataformate(data):
    name = data["name"]
    desc = data["description"]
    country = data["country"]
    return f"{name}, a {desc}, from {country}, Follower {data['follower_count']}"

def Compare(data1, data2, selection):
    Follower1 = data1["follower_count"]
    Follower2 = data2["follower_count"]
    if ((Follower1 > Follower2 and selection == 1) or (Follower2 > Follower1 and selection == 2)):
        return True
    elif not (selection == 1 or selection == 2):
        print(f"Score: {score}")
        print(f"First Compare : {dataformate(First_Select)}")
        print(vs)
        print(f"Second Compare : {dataformate(Second_Select)}")
        selection = int(input(f"You enter a wrong number! I will give you another Try. Pick a number 1 or 2: "))
        print("\n" * 100)
        print(logo)
        return Compare(data1, data2, selection)
    else:
        return False

print(logo)
score = 0
Game_keep = True
First_Select = {}
Second_Select = random.choice(data)
while (Game_keep):
    First_Select = Second_Select
    Second_Select = random.choice(data)
    print(f"First Compare : {dataformate(First_Select)}")
    print(vs)
    print(f"Second Compare : {dataformate(Second_Select)}")
    Guess = int(input("Who is higher follower? First '1' or '2': "))
    print("\n" * 100)
    print(logo)
    if (Compare(First_Select, Second_Select, Guess)):
        score += 1
        print(f"You are Right! Score: {score}")
    else:
        print(f"You are Wrong! Game Over Score: {score}")
        Game_keep = False


