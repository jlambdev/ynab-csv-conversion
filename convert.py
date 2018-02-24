"""
Convert UK bank transactions CSV exports to a CSV import format
that is compatible with the You Need A Budget web app. Currently
converts for Lloyds current accounts and Halifax credit cards.

Run: python3 convert.py [lloyds|halifax] <input_file.csv>
"""
import argparse
import csv
import sys
import os

parser = argparse.ArgumentParser()
parser.add_argument("bank")
parser.add_argument("target_path")

BANK_NAMES = ["lloyds", "halifax", "n26"]

LLOYDS_OUTPUT_PATH = '.\\lloyds_import.csv'
LLOYDS_HEADERS = ['Date', 'Description', 'Outflow', 'Inflow']

HALIFAX_OUTPUT_PATH = '.\\halifax_import.csv'
HALIFAX_HEADERS = ['Date', 'Description', 'Amount']

N26_OUTPUT_PATH = '.\\n26_import.csv'
N26_HEADERS = ['Date', 'Description', 'Amount']


def convert_lloyds_export(file_path):
    """
    Convert a Lloyds transactions CSV export to a CSV that is
    compatible with the import feature for You Need A Budget.

    Creates a new file with a subset of data and new headers.

    :param file_path: the CSV input file to convert
    """
    with open(file_path) as csv_file:
        with open(LLOYDS_OUTPUT_PATH, 'w', newline='') as output_file:
            reader = csv.reader(csv_file, delimiter=',')
            writer = csv.writer(output_file, delimiter=',')
            header_row = True
            for row in reader:
                if header_row:
                    writer.writerow(LLOYDS_HEADERS)
                    header_row = False
                else:
                    writer.writerow([row[0], row[4], row[5], row[6]])


def convert_halifax_export(file_path):
    """
    Convert a Halifax credit card transactions CSV export to a CSV
    that is compatible with the import feature for You Need A Budget.

    Creates a new file with a subset of data and new headers.
    Changes positive values to negative and vice versa to indicate
    credit or debit amounts.

    :param file_path: the CSV input file to convert
    """
    with open(file_path) as csv_file:
        with open(HALIFAX_OUTPUT_PATH, 'w', newline='') as output_file:
            reader = csv.reader(csv_file, delimiter=',')
            writer = csv.writer(output_file, delimiter=',')
            header_row = True
            for row in reader:
                if header_row:
                    writer.writerow(HALIFAX_HEADERS)
                    header_row = False
                else:
                    amount = row[4]
                    amount = amount[1:] if '-' in amount else '-{}'.format(amount)
                    writer.writerow([row[0], row[3], amount])


def convert_n26_export(file_path):
    """
    Convert an N26 debit card transactions CSV export to a CSV
    that is compatible with the import feature for You Need A Budget.

    Creates a new file with a subset of data and new headers.

    :param file_path: the CSV input file to convert
    """
    with open(file_path) as csv_file:
        with open(N26_OUTPUT_PATH, 'w', newline='') as output_file:
            reader = csv.reader(csv_file, delimiter=',')
            writer = csv.writer(output_file, delimiter=',')
            header_row = True
            for row in reader:
                if header_row:
                    writer.writerow(HALIFAX_HEADERS)
                    header_row = False
                else:
                    writer.writerow([row[0], row[1], row[6]])


if __name__ == '__main__':
    args = parser.parse_args()
    if args.bank not in BANK_NAMES:
        print("Conversion unavailable for '{}'".format(args.bank))
        sys.exit(1)

    if not os.path.isfile(args.target_path):
        print("Target file path '{}' is not a file".format(args.target_path))
        sys.exit(2)

    if args.bank == BANK_NAMES[0]:
        convert_lloyds_export(args.target_path)
    elif args.bank == BANK_NAMES[1]:
        convert_halifax_export(args.target_path)
