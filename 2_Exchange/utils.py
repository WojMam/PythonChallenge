import config
from rich.table import Table
from rich.console import Console



def show_welcome_msg():
    print("Welcome")


class Utils:
    console = Console()

    def valid_user_input(self, user_input):
        if user_input in config.POSSIBLE_ACTIONS:
            return True
        else:
            return False

    def show_help_information(self):
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

        self.console.print(table)
        print("Possible Actions: table, calculate, help, exit")

    def close_application(self):
        config.APPLICATION_STATE = False

    def pretty_print_json(self, json_object, crop=False):
        self.console.print(json_object)
