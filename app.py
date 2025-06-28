import streamlit as st
from analyser.market_demand import get_trending_keywords
from analyser.pricing_model import predict_price
from analyser.utils import clean_input
import pandas as pd

st.set_page_config(page_title="Market Fit Analyser", page_icon="📊")

st.title("📊 AI-Powered Market Fit Analyser")

product_name = st.text_input("Product Name")
description = st.text_area("Product Description")
price = st.number_input("Proposed Price (₹)", min_value=0.0, step=100.0)

if st.button("Fetch Trending News Headlines"):
    if product_name:
        headlines = get_trending_keywords(product_name)
        st.write("📰 Top related news headlines:")
        for i, headline in enumerate(headlines, 1):
            st.write(f"{i}. {headline}")
    else:
        st.warning("Please enter a product name.")

# Dummy feature inputs for ML price predictor
feature1 = st.slider("Feature Score 1 (Product Quality, 0-10)", 0, 10, 5)
feature2 = st.slider("Feature Score 2 (Brand Value, 0-10)", 0, 10, 5)

if st.button("Predict Ideal Price"):
    pred_price = predict_price([feature1, feature2])
    st.success(f"💸 AI Recommended Price: ₹{pred_price:.2f}")
    st.info(f"Your Proposed Price: ₹{price:.2f}")
