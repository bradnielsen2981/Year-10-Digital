import random

def check_hand_value(hand):
    value = 0
    for number in hand:
        if number > 10:
            value = value + 10
        else:
            value = value + number
    if 1 in hand:
        total = value + 10
        if total <= 21:
            value = total
    return value

money = 1000

bet = int(input("How much do you wish to bet!!"))
#Dealt two cards from a randomised shuffle
playerhand = []
dealerhand = []
for i in range(2):
    card = random.randint(1,13)
    playerhand.append(card)
print(playerhand)
#Change playerhand to Ace, King, Queen, Jack
response = input("Do you wish to hit, or sit? ")
while response != 'sit':
    card = random.randint(1,13)
    playerhand.append(card)
    print(playerhand)
    #Check if persons goes bust
    if check_hand_value(playerhand) > 21:
        print("You busted!")
        break
    response = input("Do you wish to hit, or sit? ")
    #check that response is hit or sit
playervalue = check_hand_value(playerhand)
print(playervalue)
dealervalue = 0
while dealervalue < playervalue:
    card = random.randint(1,13)
    dealerhand.append(card)
    print(dealerhand)
    if check_hand_value(dealerhand) > 21:
        print("Dealer busted!")
        break
if dealervalue <= 21:
    print("Dealer Wins")
    money = money - bet
else:
    print("Player Wins")
    money = money + bet




