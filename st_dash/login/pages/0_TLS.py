import streamlit as st
import pandas as pd
from connection.db_conn import sqlalchemy_connect
from Home import sql


tables=sql.tables
entry_conditions_tbl=tables["entry_conditions"]
order_log_table=tables["order_log_table"]

try:
    if st.session_state['authentication_status']:
        print("logged in")
except:
    st.error("please login")
    st.stop()


st.title("TLS")

entry_cond_tab,net_cond_tab=st.tabs(["Entry Conditions","Net Conditons"])

with entry_cond_tab:

    edf=sql.fetch_tables(entry_conditions_tbl)

    st.title("Entry Conditions")

    st.write(edf)

with net_cond_tab:
    
    st.title("Net Conditions")
    ndf=sql.fetch_tables(entry_conditions_tbl)
    st.write(ndf.sort_values(by="createdate",ascending=False))

