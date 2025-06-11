import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Sample data: [Rating, Cost, Budget], and Target (1 = Will Stay, 0 = Won't Stay)
data = {
    'Rating': [5, 4, 3, 2, 1, 5, 4, 3, 2, 1],
    'Cost':   [5000, 4000, 3000, 2000, 1000, 4500, 4200, 2500, 1500, 800],
    'Budget': [5500, 4500, 3500, 3000, 2000, 4000, 4000, 2700, 2000, 1000],
    'Will_Stay': [1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Features and target
X = df[['Rating', 'Cost', 'Budget']]
y = df['Will_Stay']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create and train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Example prediction
example = pd.DataFrame([[4, 3800, 4000]], columns=['Rating', 'Cost', 'Budget'])
prediction = model.predict(example)
print("\nWill the customer stay? ", "Yes" if prediction[0] == 1 else "No")
