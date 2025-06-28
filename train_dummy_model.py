from sklearn.linear_model import LinearRegression
import joblib
import numpy as np

# Dummy data
X = np.array([[1, 5], [2, 7], [5, 8], [7, 10], [9, 15]])
y = np.array([500, 800, 1200, 2000, 3000])

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, 'model/pricing_model.pkl')
print("Dummy pricing model trained and saved.")
