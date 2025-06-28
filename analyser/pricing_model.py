import joblib

model = joblib.load('model/pricing_model.pkl')

def predict_price(features):
    return model.predict([features])[0]
