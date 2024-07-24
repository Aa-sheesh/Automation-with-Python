import random

randomNumber = random.randint(1,10)
print("Choose a number between 1 and 10")
chosenNumber = int(input())
if(chosenNumber==randomNumber):
    print("You guessed it right")
else:
    print("Sorry, the number was",randomNumber)