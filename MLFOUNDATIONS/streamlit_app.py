import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime
import json
import os

# Set up page config
st.set_page_config(page_title="Iris Classifier", layout="wide")

# Title
st.title("🌸 Iris Flower Classification")
st.markdown("---")

# Create columns for input
col1, col2 = st.columns(2)

with col1:
    st.subheader("Enter Flower Measurements")
    sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.4, 0.1)
    sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.4, 0.1)
    petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 4.7, 0.1)
    petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 1.4, 0.1)

    # Create predict button
    if st.button("Predict"):
        # Prepare data for API request
        data = {
            "sepal_length": sepal_length,
            "sepal_width": sepal_width,
            "petal_length": petal_length,
            "petal_width": petal_width
        }

        try:
            # Make prediction request to Flask API
            response = requests.post("http://localhost:5000/predict", json=data)
            result = response.json()

            if result['status'] == 'success':
                # Display prediction
                st.success(f"Predicted Iris Type: {result['prediction'].title()}")

                # Create probability chart
                prob_df = pd.DataFrame({
                    'Class': ['Setosa', 'Versicolor', 'Virginica'],
                    'Probability': result['probability']
                })

                # Plot probability chart
                fig = px.bar(prob_df, x='Class', y='Probability',
                           title='Prediction Probabilities',
                           color='Probability',
                           color_continuous_scale='viridis')
                st.plotly_chart(fig)

                # Log prediction
                log_entry = {
                    'timestamp': str(datetime.now()),
                    'input': data,
                    'prediction': result['prediction'],
                    'probabilities': result['probability']
                }

                # Save to log file
                with open('prediction_log.json', 'a') as f:
                    f.write(json.dumps(log_entry) + '\n')

            else:
                st.error("Prediction Error: " + result.get('error', 'Unknown error'))

        except Exception as e:
            st.error(f"Error connecting to API: {str(e)}")

with col2:
    st.subheader("Model Monitoring")
    
    # Read and display recent predictions
    if os.path.exists('prediction_log.json'):
        predictions = []
        with open('prediction_log.json', 'r') as f:
            for line in f:
                predictions.append(json.loads(line))
        
        if predictions:
            # Convert to DataFrame
            df_predictions = pd.DataFrame(predictions)
            df_predictions['timestamp'] = pd.to_datetime(df_predictions['timestamp'])
            
            # Show recent predictions
            st.write("Recent Predictions")
            st.dataframe(df_predictions[['timestamp', 'prediction']].tail())
            
            # Show prediction distribution
            pred_counts = df_predictions['prediction'].value_counts()
            fig_dist = px.pie(values=pred_counts.values, 
                            names=pred_counts.index, 
                            title='Prediction Distribution')
            st.plotly_chart(fig_dist)
    else:
        st.info("No prediction history available yet.")
