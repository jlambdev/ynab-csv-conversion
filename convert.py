"""
Convert UK bank transactions CSV exports to a CSV import format
that is compatible with the You Need A Budget web app. Currently
converts for Lloyds/N26 current accounts and Halifax credit cards.

Run: python3 convert.py [lloyds|halifax|n26] <input_file.csv>
"""
from constants import BANK_NAMES, LLOYDS_OUTPUT, LLOYDS_HEADERS, \
    HALIFAX_OUTPUT, HALIFAX_HEADERS, N26_OUTPUT, N26_HEADERS, \
    MONZO_OUTPUT, MONZO_HEADERS
import argparse
import csv
import sys
import os

parser = argparse.ArgumentParser()
parser.add_argument("bank")
parser.add_argument("target_path")


def convert_lloyds_export(file_path):
    """
    Convert a Lloyds transactions CSV export to a CSV that is
    compatible with the import feature for You Need A Budget.

    Creates a new file with a subset of data and new headers.

    :param file_path: the CSV input file to convert
    """
    output_path = os.path.join('.', LLOYDS_OUTPUT)
    with open(file_path) as csv_file:
        with open(output_path, 'w', newline='') as output_file:
            reader = csv.reader(csv_file, delimiter=',')
            writer = csv.writer(output_file, delimiter=',')
            header_row = True
            for row in reader:
                if header_row:
                    writer.writerow(LLOYDS_HEADERS)
                    header_row = False
                else:
                    writer.writerow([row[0], row[4], row[5], row[6]])
    print("File created as '{}'.".format(output_path[2:]))


def convert_halifax_export(file_path):
    """
    Convert a Halifax credit card transactions CSV export to a CSV
    that is compatible with the import feature for You Need A Budget.

    Creates a new file with a subset of data and new headers.
    Changes positive values to negative and vice versa to indicate
    credit or debit amounts.

    :param file_path: the CSV input file to convert
    """
    output_path = os.path.join('.', HALIFAX_OUTPUT)
    with open(file_path) as csv_file:
        with open(output_path, 'w', newline='') as output_file:
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
    print("File created as '{}'.".format(output_path[2:]))


def convert_n26_export(file_path):
    """
    Convert an N26 debit card transactions CSV export to a CSV
    that is compatible with the import feature for You Need A Budget.

    Creates a new file with a subset of data and new headers.

    :param file_path: the CSV input file to convert
    """
    output_path = os.path.join('.', N26_OUTPUT)
    with open(file_path) as csv_file:
        with open(output_path, 'w', newline='') as output_file:
            reader = csv.reader(csv_file, delimiter=',')
            writer = csv.writer(output_file, delimiter=',')
            header_row = True
            for row in reader:
                if header_row:
                    writer.writerow(N26_HEADERS)
                    header_row = False
                else:
                    writer.writerow([row[0], row[1], row[6]])
    print("File created as '{}'.".format(output_path[2:]))


def convert_monzo_export(file_path):
    """
    Convert a Monzo debit card transactions CSV export to a CSV
    that is compatible with the import feature for You Need A Budget.

    Creates a new file with a subset of data and new headers.

    :param file_path: the CSV input file to convert
    """
    output_path = os.path.join('.', MONZO_OUTPUT)
    with open(file_path, encoding='latin1') as csv_file:
        with open(output_path, 'w', newline='') as output_file:
            reader = csv.reader(csv_file, delimiter=',')
            writer = csv.writer(output_file, delimiter=',')
            header_row = True
            for row in reader:
                if header_row:
                    writer.writerow(MONZO_HEADERS)
                    header_row = False
                else:
                    writer.writerow([row[1][:10], row[8], row[2]])
    print("File created as '{}'.".format(output_path[2:]))


if __name__ == '__main__':
    args = parser.parse_args()
    if args.bank not in BANK_NAMES:
        print("Conversion unavailable for '{}'".format(args.bank))
        sys.exit(1)

    if not os.path.isfile(args.target_path):
        print("Target file path '{}' is not a file".format(args.target_path))
        sys.exit(2)

    converter = {
        BANK_NAMES[0]: convert_lloyds_export,
        BANK_NAMES[1]: convert_halifax_export,
        BANK_NAMES[2]: convert_n26_export,
        BANK_NAMES[3]: convert_monzo_export
    }.get(args.bank)

    converter(args.target_path)
