import pandas as pd
import urllib
import sqlalchemy as sa

df = pd.read_csv("dirty_data.csv")
print("CSV rows:", len(df))

params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=.\\SQLEXPRESS;"
    "DATABASE=project;"
    "Trusted_Connection=yes;"
)

engine = sa.create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

df.to_sql("dirty_data", engine, if_exists="replace", index=False)

print("Data inserted successfully")

