* step by step process

Raw Data → Clean → Validate → Transform → Store

1. Raw Data:
collected the data from sources like Excel, CSV, APIs, or databases exactly as received.
No changes are made so the original data is preserved for audit and comparison.

2. Clean:
We Fix missing values, duplicates, invalid formats, and obvious errors.
To ensure data is consistent, standardized, and usable for downstream processing.

3. Validate:
Checked for data quality rules like ranges, data types, null limits, and uniqueness.
Confirm the data meets business and technical expectations before moving forward.

4. Transform:
Applied business logic such as (age should between 18 and 60), (salary has to be with 2 decimals),
(joining date should not be > present date), we created another age and salary column for reference.
Convert data into structures optimized for analytics and reporting.

5. Store:
Loaded cleaned and transformed data into SQL tables or warehouses.
Separate staging and final tables to keep raw and processed data organized (to know the difference).

   
* pandas - Pandas is a fast, powerful, and flexible open-source Python library used for data manipulation, analysis, and cleaning. It provides high-performance, easy-to-use data structures like DataFrames and Series, allowing users to efficiently handle tabular, time-series, and heterogeneous data. It is essential for loading, cleaning, and transforming data. 

* import urllib - To use the urllib package in Python, you can import it or its specific submodules to handle URLs, perform HTTP requests, and parse data.

* sqlalchemy - SQLAlchemy is a powerful Python SQL toolkit and Object Relational Mapper (ORM) that provides a flexible, high-performance interface for interacting with relational databases.

* df means dataframe  -   A DataFrame is a two-dimensional, size-mutable, and tabular data structure commonly used in programming and data science to store and manipulate data in rows and columns. 

* len(df): This is the core part of the command. The len() function returns the row count of the DataFrame.
* csv file  - comma separating file

* params = urllib.parse.quote_plus - 
* params - variable name , urllib.parse - In Python, urllib.parse is a module used for manipulating URLs and their component parts. It allows you to either break a URL string into components (parsing) or combine components back into a single URL string (quoting). 

* quote_plus - What quote_plus Does:
* Replaces spaces with +: For example, "Hello World" becomes "Hello+World". This is the standard for application/x-www-form-urlencoded data, which is commonly used in GET request query strings.

* pyodbc - pyodbc (Python ODBC) is an open-source Python library that allows Python code to connect to and interact with various relational database management systems (DBMS) using the ODBC (Open Database Connectivity) standard. 

* Correct Folder Setup (Very Important)

 Make sure both files are in the SAME folder:

 data_cleaning_project/
 │
 ├── dirty_data.csv
 └── data_cleaning.py


 📌 This avoids 90% of “file not found” errors.