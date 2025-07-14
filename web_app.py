import streamlit as st
from app import scan_stocks

st.set_page_config(page_title="Nifty 500 Screener", layout="centered")

st.title("📊 Nifty 500 Stock Screener")
st.markdown("This screener filters stocks based on 20 EMA > 30 SMA > 200 EMA on Daily chart.")

if st.button("🔍 Run Screener"):
    with st.spinner("Scanning... please wait"):
        result = scan_stocks()
        if result:
            st.success("📈 Matching Stocks Found:")
            for stock in result:
                st.write(f"- {stock}")
        else:
            st.warning("No stocks matched the criteria.")
