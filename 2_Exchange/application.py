"""
Console Application: Exchange

User can use this application to:
    - Get the Exchange information from the banking API
    - Calculate the exchange rates
"""

from tableA import *
from utils import *


def choose_action():
    pass


def exchange_calculator():
    utils.show_welcome_msg()
    while utils.APPLICATION_STATE:
        input(f"What you want to do?")
        input(f"Input: ")
        utils.valid_user_input()
        choose_action()


if __name__ == "__main__":
    table_a = TableA()
    utils = Utils()
    exchange_calculator()
