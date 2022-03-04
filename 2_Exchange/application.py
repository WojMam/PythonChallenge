"""
Console Application: Exchange

User can use this application to:
    - Get the Exchange information from the banking API
    - Calculate the exchange rates
"""

from tableA import *
from utils import *


def choose_action(user_input):
    if user_input == 'table':
        print(utils.pretty_print_json(table_a.get_all_exchange_rates()))
    elif user_input == 'calculate':
        print("I will do the calculation next time, ok?")
    else:
        utils.show_help_information()


def exchange_calculator():
    show_welcome_msg()
    while utils.APPLICATION_STATE:
        print("What you want to do?")
        user_input = input(f"Input: ")
        if utils.valid_user_input(user_input):
            choose_action(user_input)
        else:
            print("Sorry, we don't support this action. Please try again. Type 'help' to list the possible actions.")


if __name__ == "__main__":
    table_a = TableA()
    utils = Utils()
    exchange_calculator()
