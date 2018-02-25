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

Run: `run.bat lloyds <input_file.csv>`

## Halifax (Dec 2017)

Reduces the CSV to the following columns:
* Date
* Description
* Amount

Converts positive amounts to negative and vice versa to represent credit
and debit amounts (credit card transactions).

Run: `run.bat halifax <input_file.csv>`

## N26 (Feb 2018)

Reduces the CSV to the following columns:
* Date
* Description
* Amount

Run: `run.bat n26 <input_file.csv>`