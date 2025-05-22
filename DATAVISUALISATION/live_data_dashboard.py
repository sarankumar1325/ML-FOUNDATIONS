import streamlit as st
import pandas as pd
import time
import plotly.express as px

# Requirements: yfinance
# If not installed, run: pip install yfinance
try:
    import yfinance as yf
except ImportError:
    st.error('yfinance is not installed. Please run: pip install yfinance')
    st.stop()

st.title('Live Stock Price Dashboard')

stock = st.selectbox('Select Stock Symbol', ['AAPL', 'GOOGL', 'MSFT', 'TSLA', 'AMZN'])

# Fetch last 2 days of hourly data
try:
    df = yf.download(stock, period='2d', interval='60m', progress=False)
    if not df.empty:
        df = df.reset_index()

        # Fix for multi-index columns from yfinance
        # Flatten columns if needed
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = ['_'.join(col).strip() if col[1] else col[0] for col in df.columns.values]
        # Handle yfinance column naming
        time_col = 'Datetime' if 'Datetime' in df.columns else df.columns[0]
        close_col = [col for col in df.columns if 'Close' in col][0]
        volume_col = [col for col in df.columns if 'Volume' in col][0]
        high_col = [col for col in df.columns if 'High' in col][0]
        low_col = [col for col in df.columns if 'Low' in col][0]

        st.subheader(f'{stock} Stock Price (Last 2 Days, Hourly)')
        fig = px.line(df, x=time_col, y=close_col, title=f'{stock} Close Price', markers=True)
        fig.update_traces(line_color='royalblue')
        fig.update_layout(xaxis_title='Time', yaxis_title='Close Price (USD)')
        st.plotly_chart(fig, use_container_width=True)

        st.subheader('Volume Traded')
        fig2 = px.bar(df, x=time_col, y=volume_col, title=f'{stock} Volume', labels={'Volume': 'Volume'})
        st.plotly_chart(fig2, use_container_width=True)

        st.subheader('High-Low Range')
        fig3 = px.area(df, x=time_col, y=[high_col, low_col], title=f'{stock} High-Low Range')
        st.plotly_chart(fig3, use_container_width=True)
    else:
        st.error('No data available for the selected stock.')
except Exception as e:
    st.error(f'Failed to fetch data: {e}')

st.write('Data updates every time you rerun the app.')

if st.button('Refresh Data'):
    st.experimental_set_query_params(refresh=str(time.time()))
    st.rerun()
