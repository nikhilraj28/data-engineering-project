# Project Title

End-to-End Data Cleaning, Validation, and SQL Analytics Pipeline

## Project Overview :

This project demonstrates an end-to-end data engineering workflow using Python and SQL Server.
The goal is to ingest raw CSV data, clean and validate it using Python, store clean data in SQL Server, and enforce data quality rules using SQL constraints.

## Tools & Technologies Used :

* Python (Pandas)
* SQL Server
* PyCharm
* CSV files
* SQL Server Management Studio (SSMS)

## Data Pipeline Flow :

Raw CSV Data
   ↓
Python Data Ingestion
   ↓
Data Cleaning (Python)
   ↓
Cleaned CSV Generation
   ↓
Load into SQL Server
   ↓
SQL Validation & Constraints
   ↓
SQL Queries / Analytics

## Project Structure :

dirty_data.csv              # Raw input data
dirty_data load.py          # Loads raw CSV into SQL Server
data_cleaning.py            # Cleans raw data and generates cleaned CSV
cleaned_dirty_data.csv      # Cleaned output data
cleaned_dirty_data_load.py  # Loads cleaned data into SQL Server

## Data Cleaning (Python) :

* The following cleaning operations were performed using Python:
* Filled missing age values with median
* Converted invalid salary values to numeric
* Replaced missing names and cities with "Unknown"
* Standardized city names
* Fixed inconsistent date formats
* Added audit columns:
    age_was_missing
    salary_was_missing

## Data Validation (SQL Server):

To ensure data quality, CHECK constraints were added in SQL Server:

Age validation:
Age must be between 0 and 100

Join date validation:
Join date cannot be in the future

Salary was stored as DECIMAL(10,2) to ensure financial accuracy.

## Key Learnings

* How to build an end-to-end data pipeline
* When to use Python vs SQL
* Importance of data validation rules
* Real-world data engineering best practices
* Handling dirty and inconsistent data

## Conclusion

This project simulates a real-world data engineering scenario where raw data is cleaned, validated, stored, and analyzed using industry-standard tools and practices.

## Note:
Data comes from different formate like CSV, Excel (.xlsx), JSON, XML and database
so i have practised from CSV,XLSX and json file.
