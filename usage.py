import pandas as pd
from sklearn.preprocessing import LabelEncoder

from main import users_df, items_df

# Load datasets
# users_df = pd.read_csv("users.csv")
# items_df = pd.read_csv("items.csv")

# Print datasets
print(users_df)
print(items_df)

# Encoding columns in users_df
username_encoder = LabelEncoder()
email_encoder = LabelEncoder()

users_df["username_encoded"] = username_encoder.fit_transform(users_df["username"])
users_df["email_encoded"] = email_encoder.fit_transform(users_df["email"])

# Verify the updated DataFrame
print(users_df)

# Extract features for analysis
X = users_df[["username_encoded", "email_encoded"]]
print("Features:\n", X)

# Extract item details for analysis
Y = items_df[["item_name", "quantity", "price"]]
print("Item Details:\n", Y)

# Perform any further ML tasks as needed
