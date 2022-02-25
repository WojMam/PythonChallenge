"""
Aplikacja konsolowa "zgadnij liczbę" 

Aplikacja losuje liczbę (przedział wprowadza uytkownik).
Uzytkownik zgaduje liczbe, a aplikacja podpowiada 
czy liczba jest za mala/ za duza.

Wynikiem działania aplikacji jest wyświetlany wynik i statystyki.
"""

import random

game_lower_limit = 0
game_upper_limit = 0
drawn_number = 0
number_choosed_by_player = 0
is_player_input_correct = False
game_is_on = True
number_of_player_steps = 0


def set_game_range(lower_limit=0, upper_limit=100):
    global game_lower_limit
    global game_upper_limit
    global drawn_number

    game_lower_limit = lower_limit
    game_upper_limit = upper_limit
    drawn_number = random.randint(lower_limit, upper_limit)


def input_range():
    # TODO
    pass


def input_number():
    global number_choosed_by_player
    global is_player_input_correct
    global number_of_player_steps

    while not is_player_input_correct:
        number_choosed_by_player = input("Guess what number is drawn [0-100]: ")
        number_of_player_steps += 1
        check_player_input_correctness(number_choosed_by_player)
    print(f"Ok- so you choose {number_choosed_by_player} !")
    is_player_input_correct = False
    return int(number_choosed_by_player)


def check_player_input_correctness(player_input):
    global game_upper_limit
    global game_lower_limit
    global is_player_input_correct

    try:
        number = int(player_input)
        if game_lower_limit <= number <= game_upper_limit:
            is_player_input_correct = True
        else:
            print("You choose number that is not in the game range!")
            is_player_input_correct = False
    except ValueError:
        print("It is not a number!")
        is_player_input_correct = False


def check_given_number(number):
    global drawn_number
    global game_is_on

    if number == drawn_number:
        game_is_on = False
        print(f"You've won! The number was {drawn_number}.")
    elif number > drawn_number:
        print("Your number is too high! Let's try one more time.")
    else:
        print("Your number is too low! Let's try one more time.")


def show_scores():
    global number_of_player_steps

    print(f"You managed to finish the game in {number_of_player_steps} steps. Congrats!")


def guessing_game():
    while game_is_on:
        check_given_number(input_number())
    show_scores()


if __name__ == "__main__":
    set_game_range()
    guessing_game()
