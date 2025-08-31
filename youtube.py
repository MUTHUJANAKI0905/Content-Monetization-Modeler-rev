import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the saved model and scaler from the previous steps
# This assumes you've saved them using `joblib.dump()`
# Example: joblib.dump(best_model, 'best_model.pkl')
#           joblib.dump(scaler, 'scaler.pkl')

st.title("💰 YouTube Ad Revenue Predictor")

st.sidebar.header("Input Video Details")
# Create input fields for the user
views = st.sidebar.number_input("Views", min_value=0, value=100000)
likes = st.sidebar.number_input("Likes", min_value=0, value=5000)
comments = st.sidebar.number_input("Comments", min_value=0, value=250)
video_length = st.sidebar.number_input("Video Length (minutes)", min_value=0.0, value=10.5)
subscribers = st.sidebar.number_input("Subscribers", min_value=0, value=10000)

if st.sidebar.button("Predict Revenue"):
    # Create a DataFrame from the user's input
    input_df = pd.DataFrame({
        'views': [views], 'likes': [likes], 'comments': [comments],
        'video_length_minutes': [video_length], 'subscribers': [subscribers]
    })
    
    # Apply the same feature engineering and scaling as the training data
    input_df['engagement_rate'] = (input_df['likes'] + input_df['comments']) / input_df['views']
    # You would need to load and apply your trained scaler and encoder here
    # input_scaled = scaler.transform(input_df)
    
    # Make a prediction using the loaded model
    # prediction = model.predict(input_scaled)[0]
    
    # Placeholder for the prediction result
    prediction = 1500 # This value should be replaced with the actual model prediction
    
    st.subheader("Predicted Ad Revenue")
    st.success(f"Estimated Revenue: ${prediction:,.2f}")