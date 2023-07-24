import streamlit as st
import pandas as pd
from Home import db_conn

sql=db_conn.sqlalchemy_connect("chetan")

tables=sql.tables
entry_conditions_tbl=tables["entry_conditions"]
order_log_table=tables["order_log_table"]

#st.write(tables)
edf=sql.fetch_tables(entry_conditions_tbl)


st.title("Entry Conditions")
st.write(edf)



ndf=sql.fetch_tables(order_log_table)

st.title("Net Conditions")
st.write(ndf.sort_values(by="createdate",ascending=False))
