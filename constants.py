"""
Constants for the Conversion scripts.
"""
DATE = 'Date'
DESCRIPTION = 'Description'
OUTFLOW = 'Outflow'
INFLOW = 'Inflow'
AMOUNT = 'Amount'

BANK_NAMES = ['lloyds', 'halifax', 'n26', 'monzo']

LLOYDS_OUTPUT_PATH = '.\\lloyds_import.csv'
LLOYDS_HEADERS = [DATE, DESCRIPTION, OUTFLOW, INFLOW]

HALIFAX_OUTPUT_PATH = '.\\halifax_import.csv'
HALIFAX_HEADERS = [DATE, DESCRIPTION, AMOUNT]

N26_OUTPUT_PATH = '.\\n26_import.csv'
N26_HEADERS = [DATE, DESCRIPTION, AMOUNT]

MONZO_OUTPUT_PATH = '.\\monzo_import.csv'
MONZO_HEADERS = [DATE, DESCRIPTION, AMOUNT]
