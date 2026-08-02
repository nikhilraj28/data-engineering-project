import pandas as pd
from datetime import datetime
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.width', 1000)        # Wider display

# Load data
df = pd.read_csv("dirty_data.csv")

# Inspect data
print("Original Data:")
print(df)
print(df.info())

# Step 1: Remove duplicates #Fewer rows → faster calculations for mean/median
# Example: If you have 1000 rows with 200 duplicates, you do 40% less work
# df = df.drop_duplicates()
# df = df.drop_duplicates(inplace=True)

# Ignore 'id' and maybe 'join_date' if they differ slightly
df = df.drop_duplicates(subset=['id'])

# Step 2: Handle missing values
df['name'] = df['name'].fillna('').astype(str).str.strip().replace('', 'Unknown')

# step 3: For Age column
# 1. First, create a new column that remembers which ages were originally missing
df['age_was_missing'] = df['age'].isna()   # True if it was NaN, False if it had a value

# 2. Now fill the missing ages with median
df['age'] = df['age'].fillna(df['age'].median())  # First fill missing ages
df.loc[df['age'] > 100, 'age'] = df['age'].median()   # Then fix outliers


#  Optional: Convert the flag to something more readable
df['age_was_missing'] = df['age_was_missing'].map({True: 'Yes (filled)', False: 'No (original)'})

# step 4: Handle missing salaries
# 1. Convert to numeric first (so any bad values become NaN)
df['salary'] = pd.to_numeric(df['salary'], errors='coerce')

# 2. Create the flag BEFORE filling
df['salary_was_missing'] = df['salary'].isna()   # This captures the TRUE missing values

# 3. Now fill with median
df['salary'] = df['salary'].fillna(df['salary'].median())

# 4. Optional: Make it readable
df['salary_was_missing'] = df['salary_was_missing'].map({True: 'Yes (filled)', False: 'No (original)'})

# Step 5: Standardize city names
df['city'] = df['city'].str.strip().str.title()  # Title case
df['city'] = df['city'].replace('', 'Unknown').fillna('Unknown')

# Step 6: Fix date format option 1:
# def parse_join_date(date_value):
#     for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%d-%m-%Y"):
#         try:
#             return datetime.strptime(str(date_value), fmt)
#         except ValueError:
#             continue
#     return pd.NaT
# df['join_date'] = df['join_date'].apply(parse_join_date)
# df['join_date'] = df['join_date'].dt.strftime('%Y-%m-%d')

#option 2:
# normalize separators
s = df['join_date'].str.replace('/', '-', regex=False)

# first pass: YYYY-MM-DD
d1 = pd.to_datetime(s, errors='coerce', format='%Y-%m-%d')

# second pass: DD-MM-YYYY (only where first failed)
d2 = pd.to_datetime(s, errors='coerce', format='%d-%m-%Y')

# combine results
df['join_date'] = d1.fillna(d2).dt.strftime('%Y-%m-%d')

# Step 7: Final cleaned data
print("\nCleaned Data:")
print(df)

# Step 8 : Save Clean Data
df.to_csv("cleaned_dirty_data.csv", index=False)

