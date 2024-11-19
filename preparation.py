from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

from main import users_df, items_df

# Example: Encode user data
encoder = LabelEncoder()
users_df["username_encoded"] = encoder.fit_transform(users_df["username"])

# Normalize item prices
scaler = StandardScaler()
items_df["price_scaled"] = scaler.fit_transform(items_df[["price"]])

# Split users into train/test
train_users, test_users = train_test_split(users_df, test_size=0.2, random_state=42)
