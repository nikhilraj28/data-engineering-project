import pandas as pd
import urllib
import sqlalchemy as sa

df = pd.read_csv("cleaned_dirty_data_load.xlsx")


print("xlsx rows:", len(df))

params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=.\\SQLEXPRESS;"
    "DATABASE=project;"
    "Trusted_Connection=yes;"
)

engine = sa.create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

df.to_sql("cleaned_dirty_data_load", engine, if_exists="replace", index=False)

print("Data inserted successfully")

