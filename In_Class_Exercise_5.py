import streamlit as st
import pandas as pd


# load stock info and data
ticker_info = pd.read_csv("ticker_info.csv")
stock_data = pd.read_csv("stock_data.csv", parse_dates=['Date'])

# extract S&P 100 tickers from ticker_info
# fill in the code below
tickers_100 = 

# set page title
st.title("S&P 100 Stock Dashboard 📊")  

# Sidebar controls
# fill in the code below
with st.sidebar:
    # Header
    st.header("Sidebar Widgets")

    # Checkbox widget
    # fill in the code below
    show_sector = 

    # Multiselect widget
    # fill in the code below
    selected_tickers = 

    # Year range slider
    # fill in the code below
    selected_years = 

# a bar chart that visualizes the market cap of S&P 100 stocks by sector
# fill in the code below
if show_sector:
    st.header()
    st.bar_chart()

# display price and volme charts if stocks are selected; show error message otherwise
# fill in the code below
if selected_tickers:
    st.header()
    chart_data = stock_data.query()
 
    # Line chart for closing price
    st.subheader("Closing Prices")
    st.line_chart()

    
    # Bar chart for volume
    st.subheader("Trading Volume")
    st.bar_chart()

# display the error message
# fill in the code below
else:
    
    




