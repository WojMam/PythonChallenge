import config
from rich.table import Table
from rich.console import Console
import tableA, gold


console = Console()


def start_application():
    show_welcome_msg()
    while config.APPLICATION_STATE:
        print("What you want to do?")
        user_input = input("Input: ").lower()
        if valid_user_input_main_menu(user_input):
            choose_action(user_input)
        else:
            print("Sorry, we don't support this action. Please try again. Type 'help' to list the possible actions.")


def start_exchange_calculator():
    config.EXCHANGE_CALCULATOR_STATE = True
    print("Possible currencies codes that can be used for calculation:")
    print(tableA.get_all_currencies_codes())
    while config.EXCHANGE_CALCULATOR_STATE:
        print("You can always stop calculator and get back to menu by typing 'menu'.")
        print("Which currency you want to use for calculation?")
        user_input_currency = input("Currency code: ").upper()
        if user_input_currency == "MENU":
            config.EXCHANGE_CALCULATOR_STATE = False
            break
        if valid_user_input_for_exchange_currency_code(user_input_currency):
            while config.EXCHANGE_CALCULATOR_STATE:
                print("How much polish zlotys You want to exchange?")
                try:
                    user_input_money_ammount = input("Ammount of PLN: ")
                    if user_input_money_ammount.lower() == "menu":
                        config.EXCHANGE_CALCULATOR_STATE = False
                        break
                    money_ammount = int(user_input_money_ammount)
                    calculation_result = tableA.calculate_exchange_rate(
                        tableA.get_given_currency_rate_by_code(
                            user_input_currency), money_ammount)
                    print(f"The result of exchange would be: {calculation_result}")
                    config.EXCHANGE_CALCULATOR_STATE = False
                except ValueError:
                    print("Your ammount was not a number! Please use a number.")
        else:
            print("Sorry, we don't support this currency code. Please try again. Possible codes:")
            print(tableA.get_all_currencies_codes())


def show_welcome_msg():
    print("Welcome")
    show_help_information()


def choose_action(user_input):
    if user_input == 'table':
        pretty_print_json(tableA.get_all_exchange_rates())
    elif user_input == 'calculate':
        start_exchange_calculator()
    elif user_input == 'gold':
        pretty_print_json(gold.get_gold_price())
    elif user_input == 'exit':
        close_application()
    else:
        show_help_information()


def valid_user_input_main_menu(user_input):
    if user_input in config.POSSIBLE_ACTIONS:
        return True
    else:
        return False


def valid_user_input_for_exchange_money_ammount(user_input):
    try:
        int(user_input)
        return True
    except ValueError:
        print()
        return False


def valid_user_input_for_exchange_currency_code(user_input):
    if user_input in tableA.get_all_currencies_codes():
        return True
    else:
        return False


def show_help_information():
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Commands", style="dim", width=12)
    table.add_column("Description")
    table.add_row(
        "table", "Show whole Table A."
    )
    table.add_row(
        "calculate", "Go to calculate menu."
    )
    table.add_row(
        "help", "Show this beautiful table."
    )
    table.add_row(
        "gold", "Show gold price."
    )
    table.add_row(
        "exit", "Close the application."
    )

    console.print(table)


def pretty_print_json(json_object):
    console.print(json_object)


def close_application():
    config.APPLICATION_STATE = False
