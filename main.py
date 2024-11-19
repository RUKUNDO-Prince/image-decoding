from sqlalchemy import create_engine
import pandas as pd

# Connect to the database
engine = create_engine("postgresql://postgres:postgres@localhost/medic_db")

# Query the tables
users_query = "SELECT * FROM users"
items_query = "SELECT * FROM inventory"

# Load data into DataFrames
users_df = pd.read_sql(users_query, engine)
items_df = pd.read_sql(items_query, engine)

# # Save as CSV (optional)
# users_df.to_csv("users.csv", index=False)
# items_df.to_csv("items.csv", index=False)
#
# # Load from CSV
# users_df = pd.read_csv("users.csv")
# items_df = pd.read_csv("items.csv")

# Inspect the datasets
print(users_df.head())
print(items_df.head())
