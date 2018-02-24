# YNAB CSV Conversion

Convert UK bank transactions CSV export files to a format that can be 
integrated with You Need A Budget's web app. Mainly renames headers and converts
amount values to positive/negative amounts.

## LLoyds (Dec 2017)

Reduces the CSV to the following columns and replaces headers:
* Transaction Date: **Date**
* Transaction Description: **Description**
* Debit Amount: **Outflow**
* Credit Amount: **Inflow**

Run: `python3 convert.py lloyds <input_file.csv>`

## Halifax (Dec 2017)

Reduces the CSV to the following columns:
* Date
* Description
* Amount

Converts positive amounts to negative and vice versa to represent credit
and debit amounts (credit card transactions).

Run: `python3 convert.py halifax <input_file.csv>`

## N26 (Feb 2018)

Reduces the CSV to the following columns:
* Date
* Description
* Amount

Run: `python3 convert.py n26 <input_file.csv>`