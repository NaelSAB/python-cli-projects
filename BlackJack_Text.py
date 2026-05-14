import random

cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

def playgame(check):
    if (check == None):
        playgame = input("Wanna play blackJack ? 'y' for Yes, 'n' for no: ").lower()
    else:
        playgame = input("Wanna play Another Round ? 'y' for Yes, 'n' for no: ").lower()
    while True:
        if (playgame != 'y' and playgame != 'n'):
            playgame = input("wrong input! Enter 'y' To yes, 'n' for no: ").lower()
            continue
        elif(playgame == 'y'):
            return True
        elif(playgame == 'n'):
            return False

def Draw():
    return random.choice(cards)

def TotalCards(Hand):
    intHand = []
    for card in Hand:
        if (card == 'J' or card == 'Q' or card == 'K'):
            intHand.append(10)
        elif (card == 'A'):
            intHand.append(11)
        else:
            intHand.append(card)

    intHand.sort()
    Total = 0
    for card in intHand:
        if (card == 11) and (Total + card > 21):
            Total += 1
        else:
            Total += card
    return Total


Startgame = playgame(None)
while Startgame:
    print("\n" * 100)
    BUST = False
    PlayerCards = [Draw(), Draw()]
    DealerCards = [Draw(), Draw()]
    print(f"Player Cards: [{PlayerCards[0]}, {PlayerCards[1]}] = {TotalCards(PlayerCards)}\nDealer Cards: [{DealerCards[0]}, ??] = {DealerCards[0]} + ??" )
    IsAdd = True
    while True:
        print("=" * 30)
        AddCard = input("Wanna Draw a Card? 'y' For yes 'n' for no: ")
        if (AddCard != 'y' and AddCard != 'n'):
            print("wrong input!")
            continue
        elif(AddCard == 'y'):
            PlayerCards.append(Draw())
            print(f"Player Cards: {PlayerCards} = {TotalCards(PlayerCards)}")
            if (TotalCards(PlayerCards) > 21):
                print("BUST")
                BUST = True
                break
            continue
        elif(AddCard == 'n'):
            break

    while not BUST:
        if (TotalCards(DealerCards) < 17):
            DealerCards.append(Draw())
        else:
            break
    TotalPlayer = TotalCards(PlayerCards)
    TotalDealer = TotalCards(DealerCards)
    print("=" * 30)
    print(f"Player Cards: {PlayerCards} = {TotalPlayer}\nDealer Cards: {DealerCards} = {TotalDealer}")
    if (TotalPlayer > TotalDealer and TotalPlayer <= 21) or (TotalPlayer <= 21 and TotalDealer > 21):
        print("********** PLAYER WIN **********")
    elif(TotalPlayer < TotalDealer and TotalDealer <= 21) or (TotalPlayer > 21):
        print("********** PLAYER LOSE **********")
    else:
        print("********** Draw **********")
    Startgame = playgame(Startgame)

print("=" * 30)
print("Thanks For using BlackJack App Game")