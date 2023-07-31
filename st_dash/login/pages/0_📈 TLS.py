import streamlit as st
import pandas as pd
from Home import sql,sqlmethods,reconnection
import numpy as np
# CSS file
with open('css/homestyle.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
_=""" 
    Refresh warning process
"""
if len(st.session_state) == 0:

    st.warning("Please! Don't Refresh your browser.")

    st.info("Always, use dashboard Default Refresh!")

    _="""with st.expander('Do This:'):

        video_file = open('video/dashboard_refresh.mp4', 'rb')

        video_bytes = video_file.read()

        st.video(video_bytes)"""

    st.stop()  
 
if not st.session_state["authentication_status"]:
    st.error("Please Login...")
    st.stop()

if not st.session_state['sq_conn']:
    st.session_state['sq_conn']=reconnection(connection_object=sql)
    sq_conn=st.session_state['sq_conn']
else:
    sq_conn=st.session_state['sq_conn']

tables=sql.tables
entry_conditions_tbl=tables["entry_conditions"]
order_log_table=tables["order_log_table"]
candle_sticks_table=tables["candle_stick_log_table"]

dbm=sqlmethods(sq_conn,sql,st.session_state["username"])
st.title("📈 TLS")


def show_df(df):
    df.index = np.arange(1, len(df) + 1)
    return df

ohlc_tab,entry_cond_tab,net_cond_tab=st.tabs(["📉 OHLC","🎯 Entry Conditions","📝 Order Log"])

with ohlc_tab:
    candlles=dbm.fetch_tables(table_name=candle_sticks_table).sort_values(by="date",ascending=False)
    st.header("📉 OHLC Values")
    st.dataframe(show_df(candlles),use_container_width=True)

with entry_cond_tab:

    edf=dbm.fetch_tables(entry_conditions_tbl).sort_values(by="Start Date",ascending=False)

    st.header("🎯 Entry Conditions")

    edf=edf.drop(columns=['id'])

    st.dataframe(show_df(edf),use_container_width=True)

with net_cond_tab:
    
    st.header("📝Order Log")
    ndf=dbm.fetch_tables(order_log_table)
    st.dataframe(show_df(ndf).sort_values(by="createdate",ascending=False),use_container_width=True)

