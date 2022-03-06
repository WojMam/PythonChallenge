import config
from rich.table import Table
from rich.console import Console
import tableA


console = Console()


def start_application():
    show_welcome_msg()
    while config.APPLICATION_STATE:
        print("What you want to do?")
        user_input = input("Input: ")
        if valid_user_input(user_input):
            choose_action(user_input)
        else:
            print("Sorry, we don't support this action. Please try again. Type 'help' to list the possible actions.")


def show_welcome_msg():
    print("Welcome")


def choose_action(user_input):
    if user_input == 'table':
        print(pretty_print_json(tableA.get_all_exchange_rates()))
    elif user_input == 'calculate':
        print("nothing to see here")
        # tableA.calculate_exchange_rate(tableA.get_given_currency_rate_by_code(currency_code),user_ammount)
    elif user_input == 'exit':
        close_application()
    else:
        show_help_information()


def valid_user_input(user_input):
    if user_input in config.POSSIBLE_ACTIONS:
        return True
    else:
        return False


def valid_user_input_for_exchange(user_input):
    try:
        int(user_input)
        return True
    except ValueError:
        print()
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
        "exit", "Close the application."
    )

    console.print(table)


def pretty_print_json(json_object, crop=False):
    console.print(json_object)


def close_application():
    config.APPLICATION_STATE = False
