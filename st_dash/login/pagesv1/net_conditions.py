import streamlit as st
import pandas as pd
from login import db_conn

sql=db_conn.sqlalchemy_connect("chetan")

st.write(sql)

tables=sql.tables
#st.write(tables)

entry_conditions_tbl=tables["entry_conditions"]
order_log_table=tables["order_log_table"]


df=sql.fetch_tables(order_log_table)

st.title("Net Conditions")
st.write(df.sort_values(by="createdate",ascending=False))

col=st.columns((1,1))
col[0].header("Failed Net Conditions")
col[0].write(df[df["status"]=="Failed"])

with col[1]:
    st.header("Successed Net Conditions")
    st.write(df[df["status"]=="Success"])