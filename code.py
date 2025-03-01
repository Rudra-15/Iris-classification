import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the dataset
df = pd.read_csv("Iris.csv")

# Display basic information
print(df.head())
print(df.info())
print(df.describe())

# Checking for missing values
print("Missing Values:\n", df.isnull().sum())

# Visualizing the dataset
sns.pairplot(df, hue="Species")
plt.show()

# Encoding categorical target variable
df["Species"] = df["Species"].astype("category").cat.codes

# Splitting dataset into features and target
X = df.drop(columns=["Species", "Id"], axis=1)
y = df["Species"]

# Splitting into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Model training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Model predictions
y_pred = model.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Saving the trained model
import joblib
joblib.dump(model, "iris_model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("Model and scaler saved successfully.")
