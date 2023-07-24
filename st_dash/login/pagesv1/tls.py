import streamlit as st
import pandas as pd
from login import db_conn

st.title("Tickers Data")

sql=db_conn.sqlalchemy_connect("chetan")

st.write(sql)

tables=sql.tables
#st.write(tables)

candle_stick_log_table=tables["candle_stick_log_table"]
@st.cache()
def fetch_values():
    return sql.fetch_tables(candle_stick_log_table).sort_values(by="date",ascending=False)
tickers_data=fetch_values()
st.dataframe(tickers_data,use_container_width=True)

_="""
trade_log=tickers_data.loc[:,"Entry Date":"stop loss value"].dropna(axis=0,how="all")
st.subheader("Trade Log")
st.dataframe(trade_log,use_container_width=True)

short_trades=trade_log[trade_log["Position"]=="short"]
long_trades=trade_log[trade_log["Position"]=="Long"]

col=st.columns((1,1))

with col[0]:
    st.subheader("Short Trades")
    st.dataframe(short_trades)

with col[1]:
    st.subheader("Long Trades")
    st.dataframe(long_trades)"""