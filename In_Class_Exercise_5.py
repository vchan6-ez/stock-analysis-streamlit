import streamlit as st
import pandas as pd


# load stock info and data
ticker_info = pd.read_csv("ticker_info.csv")
stock_data = pd.read_csv("stock_data.csv", parse_dates=['Date'])

# extract S&P 100 tickers from ticker_info
# fill in the code below
tickers_100 = ticker_info['Ticker'].tolist()

# set page title
st.title("S&P 100 Stock Dashboard 📊")  

# Sidebar controls
# fill in the code below
with st.sidebar:
    # Header
    st.header("Sidebar Widgets")

    # Checkbox widget
    # fill in the code below
    show_sector = st.checkbox("Show market cap by sector", value=True)

    # Multiselect widget
    # fill in the code below
    selected_tickers = st.multiselect(
        "Select stocks to display",
        options=tickers_100,
        default=['TSLA', 'NVDA', 'AAPL']
    )
    # Year range slider
    # fill in the code below
    selected_years = st.slider(
        "Select year range",
        min_value=2020,
        max_value=2026,
        value=(2025, 2026),
        step=1
    )
# a bar chart that visualizes the market cap of S&P 100 stocks by sector
# fill in the code below
if show_sector:
    st.header("Market Capitalization by Sector")
    
    sector_col = 'Sector' if 'Sector' in ticker_info.columns else 'GICS Sector'
    market_cap_col = 'MarketCap' if 'MarketCap' in ticker_info.columns else ticker_info.columns[2]

    sector_market_cap = ticker_info.groupby(sector_col)[market_cap_col].sum().reset_index()
    sector_market_cap = sector_market_cap.sort_values(market_cap_col, ascending=False)
    
    st.bar_chart(sector_market_cap.set_index(sector_col))

# display price and volme charts if stocks are selected; show error message otherwise
# fill in the code below
if selected_tickers:
    st.header("Stock Price and Volume Analysis")
    start_year, end_year = selected_years
    query_str = f"Date.dt.year >= {start_year} and Date.dt.year <= {end_year} and Ticker in {selected_tickers}"
    chart_data = stock_data.query(query_str)
  if not chart_data.empty:
    # Line chart for closing price
    st.subheader("Closing Prices")
    price_pivot = chart_data.pivot(index='Date', columns='Ticker', values='Close')
    st.line_chart(price_pivot)

    
    # Bar chart for volume
    st.subheader("Trading Volume")
    volume_pivot = chart_data.pivot(index='Date', columns='Ticker', values='Volume')
    st.bar_chart(volume_pivot)
  else:
        st.warning("No data available for the selected stocks and year range.")

# display the error message
# fill in the code below
else:
    st.error("Please select at least one stock!")
    
    




