import requests
import pandas as pd
import json
import urllib
import sqlalchemy as sa

pd.set_option('display.max_rows', 10)

# 1️⃣ Call API
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
data = response.json()

# 2️⃣ Save RAW JSON (optional but good practice)
with open("users_raw.json", "w") as f:
    json.dump(data, f, indent=4)

# 3️⃣ Normalize JSON → DataFrame
df = pd.json_normalize(data)
print("Rows fetched:", len(df))
print(df.head())

# 4️⃣ SQL Server connection
params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=.\\SQLEXPRESS;"
    "DATABASE=project;"
    "Trusted_Connection=yes;"
)

engine = sa.create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

# 5️⃣ Load into SQL
df.to_sql(
    "json_dirty_data",
    engine,
    if_exists="replace",
    index=False
)

print("✅ Data inserted successfully into SQL")