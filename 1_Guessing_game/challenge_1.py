"""
Aplikacja konsolowa "zgadnij liczbę" 

Aplikacja losuje liczbę (przedział wprowadza uytkownik).
Uzytkownik zgaduje liczbe, a aplikacja podpowiada 
czy liczba jest za mala/ za duza.

Wynikiem działania aplikacji jest wyświetlany wynik i statystyki.
"""

from pickle import FALSE, TRUE
import random
import sys

gameLowerLimit = 0
gameUpperLimit = 0
drawnNumber = 0
numberChoosedByPlayer = 0
isPlayerInputCorrect = False
gameIsOn = True

def setGameRange(lowerLimit = 0, upperLimit = 100):
    global gameLowerLimit
    global gameUpperLimit
    global drawnNumber
    
    gameLowerLimit = lowerLimit
    gameUpperLimit = upperLimit
    drawnNumber = random.randint(lowerLimit, upperLimit)

def inputRange():
    #TODO
    pass

def inputNumber():
    global numberChoosedByPlayer
    global isPlayerInputCorrect

    while isPlayerInputCorrect==False:
        numberChoosedByPlayer = input("Guess what number is drawn [0-100]: ")
        checkPlayerInputCorrectness(numberChoosedByPlayer)
    print(f"Ok- so you choose {numberChoosedByPlayer} !")
    isPlayerInputCorrect=False
    return int(numberChoosedByPlayer)

def checkPlayerInputCorrectness(playerInput):
    global gameUpperLimit
    global gameLowerLimit
    global isPlayerInputCorrect

    try:
        number = int(playerInput)
        if gameLowerLimit <= number <= gameUpperLimit:
            isPlayerInputCorrect = True
        else:
            print("You choose number that is not in the game range!")
            isPlayerInputCorrect = False
    except ValueError:
        print("It is not a number!")
        isPlayerInputCorrect = False

def checkGivenNumber(number):
    global drawnNumber
    global gameIsOn

    if number == drawnNumber:
        gameIsOn = True
        print(f"You've won! The number was {drawnNumber}.")
    elif number > drawnNumber:
        print("Your number is too high! Let's try one more time.")
    else:
        print("Your number is too low! Let's try one more time.")

def guessingGame():
    while(gameIsOn==True):
        checkGivenNumber(inputNumber())


if __name__ == "__main__":
    setGameRange()
    guessingGame()