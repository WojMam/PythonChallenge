"""
Console Application: Exchange

User can use this application to:
    - Get the Exchange information from the banking API
    - Calculate the exchange rates
"""

from tableA import *

if __name__ == "__main__":
    table_a = TableA()
    print(table_a.get_given_currency_by_code('EUR'))
    print(table_a.get_given_currency_rate_by_code('EUR'))
    print(table_a.get_all_currencies_codes())
