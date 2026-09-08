"""
Day 1 - Data Cleaning and Preprocessing
Practice project for a Data Analytics task.
"""
import pandas as pd

RAW_FILE = "data/raw_dataset.csv"
CLEAN_FILE = "data/cleaned_dataset.csv"

df = pd.read_csv(RAW_FILE)

print("Initial shape:", df.shape)
print("\nMissing values:\n", df.isna().sum())
print("\nDuplicate rows:", df.duplicated().sum())
print("\nData types:\n", df.dtypes)

# Trim whitespace
for col in ["Customer_Name", "Email", "Region", "Product", "Status"]:
    df[col] = df[col].astype("string").str.strip()

# Standardize text
for col in ["Customer_Name", "Region", "Product", "Status"]:
    df[col] = df[col].str.title()
df["Email"] = df["Email"].str.lower()

# Correct data types
df["Order_ID"] = pd.to_numeric(df["Order_ID"], errors="coerce").astype("Int64")
df["Order_Date"] = pd.to_datetime(
    df["Order_Date"], errors="coerce", format="mixed", dayfirst=True
)
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Unit_Price"] = pd.to_numeric(df["Unit_Price"], errors="coerce")

# Context-specific missing-value handling
df["Email"] = df["Email"].fillna("not_provided@example.com")
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median())
df["Unit_Price"] = df["Unit_Price"].fillna(df["Unit_Price"].median())

# Remove exact duplicates
df = df.drop_duplicates().reset_index(drop=True)

# Derived metric
df["Total_Sales"] = (df["Quantity"] * df["Unit_Price"]).round(2)

df.to_csv(CLEAN_FILE, index=False)

print("\nFinal shape:", df.shape)
print("Remaining missing values:", int(df.isna().sum().sum()))
print("Remaining duplicate rows:", int(df.duplicated().sum()))
print("\nCleaned dataset saved to:", CLEAN_FILE)
