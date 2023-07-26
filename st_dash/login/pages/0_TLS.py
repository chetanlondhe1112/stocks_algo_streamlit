import streamlit as st
import pandas as pd
from Home import sql,sqlmethods


tables=sql.tables
entry_conditions_tbl=tables["entry_conditions"]
order_log_table=tables["order_log_table"]
if not st.session_state["authentication_status"]:
    st.error("Please Login")
    st.stop()

dbm=sqlmethods(sql,st.session_state["authentication_status"])
st.title("TLS")

entry_cond_tab,net_cond_tab=st.tabs(["Entry Conditions","Net Conditons"])

with entry_cond_tab:

    edf=dbm.fetch_tables(entry_conditions_tbl)

    st.title("Entry Conditions")

    st.write(edf)

with net_cond_tab:
    
    st.title("Net Conditions")
    ndf=dbm.fetch_tables(order_log_table)
    st.write(ndf.sort_values(by="createdate",ascending=False))

