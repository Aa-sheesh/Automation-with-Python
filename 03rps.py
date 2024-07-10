import random

tie,win,lose=0,0,0
while(input("Do you want to play rock, paper, scissors? (y/n)")==('y' or 'Y')):
    print("Choose rock, paper or scissors")
    playerChoice = input()

    choices = ["rock","paper","scissors"]
    computerChoice = random.choice(choices)

    #GAME LOGIC
    if playerChoice == computerChoice:
        tie+=1
    elif ((playerChoice=='rock' and computerChoice=='scissors') or (playerChoice=='paper' and computerChoice=='rock') or (playerChoice=='scissors' and computerChoice=='paper')):
        win+=1
    else:
        lose+=1

    print("You chose",playerChoice)
    print("Computer chose",computerChoice)
    print ("Wins:",win,"Losses:",lose,"Ties:",tie)