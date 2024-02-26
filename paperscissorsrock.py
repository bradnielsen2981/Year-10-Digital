# player choose a move from paper,scissor,rock
# computer choose a random move from paper,scissor,rock
# decides who wins
# repeat until player chooses exit
import random
playerscore = 0
computerscore = 0
movelist = ['paper','scissors','rock']
playermove = input("Please choose paper, scissors, rock, or exit: ")
while playermove != 'exit':
    if playermove not in movelist:
        playermove = input("Please choose paper, scissors, rock, or exit: ")
        continue
    index = random.randint(0,2)
    computermove = movelist[index]
    print(computermove)
    # decides who wins
    if computermove == playermove:
        print("Draw")
    elif (computermove == 'paper' and playermove == 'rock') or (computermove == 'scissors' and playermove == 'paper') or (computermove == 'rock' and playermove == 'scissors'):
        print("Computer wins")
        computerscore = computerscore + 1
    else:
        print("Player wins")
        playerscore = playerscore + 1
    print("PLAYER score: ",playerscore," COMPUTER score: ",computerscore)
    playermove = input("Please choose paper, scissors, rock, or exit: ")