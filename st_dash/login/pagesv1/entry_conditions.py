import streamlit as st
import pandas as pd
from login import db_conn

sql=db_conn.sqlalchemy_connect("chetan")

st.write(sql)

tables=sql.tables
#st.write(tables)

entry_conditions_tbl=tables["entry_conditions"]

df=sql.fetch_tables(entry_conditions_tbl)

st.title("Entry Conditions")
st.write(df)