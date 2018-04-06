"""
Test conversion of UK bank CSV exports to files that can be imported into YNAB.
"""
from convert import convert_lloyds_export, convert_halifax_export, \
    convert_n26_export, convert_monzo_export
from constants import BANK_NAMES
import unittest
import csv
import os


class BaseConversionTest(unittest.TestCase):
    """
    Base class that compares 2 CSV files
    """
    def assert_conversion(self, output_path, assertion_path):
        self.assertTrue(os.path.exists(output_path))
        with open(assertion_path) as assertion_csv:
            with open(output_path) as actual_csv:
                assertion_reader = csv.reader(assertion_csv, delimiter=',')
                actual_reader = csv.reader(actual_csv, delimiter=',')
                for assert_row in assertion_reader:
                    actual_row = actual_reader.__next__()
                    self.assertEqual(assert_row, actual_row)


class LloydsConversionTest(BaseConversionTest):
    """
    Test conversion of Lloyds CSV exports

    Assert header changes:
     - Transaction Date -> Date
     - Transaction Description -> Description
     - Debit Amount -> Outflow
     - Credit Amount -> Inflow
    """
    OUTPUT_PATH = os.path.join('.', 'lloyds_import.csv')
    INPUT_PATH = os.path.join('.', 'data', 'lloyds_download_example.csv')
    ASSERTION_PATH = os.path.join('.', 'data', 'lloyds_conversion_example.csv')

    def tearDown(self):
        if os.path.exists(self.OUTPUT_PATH):
            os.remove(self.OUTPUT_PATH)

    def test_conversion(self):
        convert_lloyds_export(self.INPUT_PATH)
        self.assert_conversion(self.OUTPUT_PATH, self.ASSERTION_PATH)


class HalifaxConversionTest(BaseConversionTest):
    """
    Test conversion of Halifax CSV exports

    Amount value modification:
    - Convert positive values to negative and vice versa
    """
    OUTPUT_PATH = os.path.join('.', 'halifax_import.csv')
    INPUT_PATH = os.path.join('.', 'data', 'halifax_download_example.csv')
    ASSERTION_PATH = os.path.join('.', 'data', 'halifax_conversion_example.csv')

    def tearDown(self):
        if os.path.exists(self.OUTPUT_PATH):
            os.remove(self.OUTPUT_PATH)

    def test_conversion(self):
        convert_halifax_export(self.INPUT_PATH)
        self.assert_conversion(self.OUTPUT_PATH, self.ASSERTION_PATH)


class N26ConversionTest(BaseConversionTest):
    """
    Test conversion of N26 CSV exports

    Assert header changes:
     - Payee -> Description
     - Amount (EUR) -> Amount
    """
    OUTPUT_PATH = os.path.join('.', 'n26_import.csv')
    INPUT_PATH = os.path.join('.', 'data', 'n26_download_example.csv')
    ASSERTION_PATH = os.path.join('.', 'data', 'n26_conversion_example.csv')

    def tearDown(self):
        if os.path.exists(self.OUTPUT_PATH):
            os.remove(self.OUTPUT_PATH)

    def test_conversion(self):
        convert_n26_export(self.INPUT_PATH)
        self.assert_conversion(self.OUTPUT_PATH, self.ASSERTION_PATH)


class MonzoConversionTest(BaseConversionTest):
    """
    Test conversion of Monzo CSV exports
    """
    OUTPUT_PATH = os.path.join('.', 'monzo_import.csv')
    INPUT_PATH = os.path.join('.', 'data', 'monzo_download_example.csv')
    ASSERTION_PATH = os.path.join('.', 'data', 'monzo_conversion_example.csv')

    def tearDown(self):
        if os.path.exists(self.OUTPUT_PATH):
            os.remove(self.OUTPUT_PATH)

    def test_conversion(self):
        convert_monzo_export(self.INPUT_PATH)
        self.assert_conversion(self.OUTPUT_PATH, self.ASSERTION_PATH)


class BankNamesTest(unittest.TestCase):
    """
    Simple contractual test for banks to map to methods.
    """
    EXPECTED_BANK_NAMES = ['lloyds', 'halifax', 'n26', 'monzo']

    def test_bank_names(self):
        self.assertEqual(BANK_NAMES, self.EXPECTED_BANK_NAMES)

if __name__ == '__main__':
    unittest.main()
