# Data Visualization Learning & Live Dashboard Project

![Image](https://github.com/user-attachments/assets/b7245bce-a7fe-4403-bd9e-cef46a2c1b4a)

![Image](https://github.com/user-attachments/assets/7e74aa22-410c-45df-91d1-b56026e90cf0)

![Image](https://github.com/user-attachments/assets/3d7452c7-dd3d-41e2-adcc-0a40b96201a5)

This project is designed to help you learn and practice data visualization in Python using Matplotlib, Seaborn, and Plotly, and to build a live dashboard for real-time stock data visualization.

## Contents

- **Matplotlib_Basics.ipynb**: Learn the basics of Matplotlib with hands-on examples for line, scatter, and bar plots.
- **Seaborn_Plotting_Practice.ipynb**: Practice Seaborn plotting, including distribution, categorical, and pair plots.
- **Plot_Types_and_Uses.ipynb**: Study different plot types (line, scatter, bar, histogram, boxplot, heatmap) and their use cases.
- **live_data_dashboard.py**: A Streamlit app that fetches live stock data (no API key required, uses Yahoo Finance via yfinance) and provides interactive visualizations using Plotly.
- **requirements.txt**: All required Python packages for notebooks and the dashboard.

## How to Use

1. **Install Requirements**
   ```
   pip install -r requirements.txt
   ```

2. **Explore the Notebooks**
   - Open the `.ipynb` files in Jupyter or VS Code to learn and practice data visualization with Matplotlib and Seaborn.

3. **Run the Live Dashboard**
   - Make sure you have `streamlit` and `yfinance` installed (included in requirements.txt).
   - In your terminal, run:
     ```
     streamlit run live_data_dashboard.py
     ```
   - Select a stock symbol to view its latest hourly data, volume, and high-low range with interactive Plotly charts.

## Features
- No API keys required for live data (uses Yahoo Finance via yfinance).
- Interactive and visually appealing dashboards with Plotly.
- Error handling for missing data or dependencies.
- Refresh button for live updates.


