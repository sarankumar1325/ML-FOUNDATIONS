# Iris Classification - End to End Machine Learning Project

![Image](https://github.com/user-attachments/assets/9a94f942-ec19-4912-b6e6-50643ef52c33)

![Image](https://github.com/user-attachments/assets/96abed4e-00c3-43a2-946d-65e6bb39d674)


This project demonstrates a complete end-to-end machine learning pipeline for Iris flower classification, including model development, API deployment, and a web-based user interface.

## Project Structure
```
├── ModelBuilding.ipynb     # Jupyter notebook containing EDA and model development
├── app.py                  # Flask API for model serving
├── streamlit_app.py        # Streamlit web interface
├── iris_model.pkl          # Trained Random Forest model
├── scaler.pkl             # Fitted StandardScaler for feature scaling
├── prediction_log.json     # Log file for model predictions
└── requirements.txt        # Project dependencies
```

## Features

- **Data Analysis and Model Development**
  - Exploratory Data Analysis (EDA)
  - Feature scaling using StandardScaler
  - Model training using RandomForestClassifier
  - Model evaluation with accuracy metrics and confusion matrix

- **REST API (Flask)**
  - Endpoint for real-time predictions
  - JSON response with prediction and probabilities
  - Error handling and status reporting

- **Web Interface (Streamlit)**
  - User-friendly interface for making predictions
  - Interactive sliders for feature input
  - Visualization of prediction probabilities
  - Real-time model monitoring dashboard
  - Prediction history tracking

## Technologies Used

- Python 3.x
- Scikit-learn
- Flask
- Streamlit
- Pandas
- NumPy
- Seaborn
- Matplotlib
- Plotly

## Installation

1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask API:
```bash
python app.py
```

2. In a new terminal, start the Streamlit application:
```bash
streamlit run streamlit_app.py
```

3. Open your web browser and navigate to:
   - Web Interface: http://localhost:8501
   - API Endpoint: http://localhost:5000/predict

## API Usage

Make predictions using the API:

```python
import requests

# Example data
data = {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}

# Make prediction
response = requests.post("http://localhost:5000/predict", json=data)
print(response.json())
```

## Model Monitoring

The application includes a monitoring dashboard that shows:
- Prediction history
- Distribution of predictions
- Recent predictions table
- Real-time monitoring metrics

## Model Performance

The Random Forest model achieves high accuracy in classifying Iris flowers into their respective species. The model evaluation metrics, including accuracy score, classification report, and confusion matrix, can be found in the `ModelBuilding.ipynb` notebook.

## Future Improvements

- Add model retraining capability
- Implement A/B testing
- Add more advanced monitoring metrics
- Deploy to cloud platform
- Add user authentication
- Implement batch prediction functionality


