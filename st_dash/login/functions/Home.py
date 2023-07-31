import time
import streamlit as st
import pandas as pd
from PIL import Image
from datetime import datetime
import streamlit_authenticator as stauth
from sqlalchemy import create_engine,text
from validate_email_address import validate_email
from password_validator import PasswordValidator
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re
# User defined functions import
from db_conn import *
from home_functions import *


_=""" Defaults"""

current_date = datetime.now()


_=""" Page layout design """

# Set page config
st.set_page_config(
        page_icon="📈",
        page_title="Stocks Algo",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            #'Report a bug': "https://www.stockanalyser2022@gmail.com/",
            'About': "# Stocks Analyser!"
                    "\n ##### Report a bug on mail:"
                    "\n ##### https://www.stockanalyser2022@gmail.com/"
        }
    )


_=""" Creating Connection """

# Session state objects of database connection 
if "sq_connection_obj" not in st.session_state:         # session state SQL connection object         
    st.session_state["sq_connection_obj"]=0
    
if "sq_cur_obj" not in st.session_state:                           # session state SQL cursor object
    st.session_state["sq_cur_obj"]=0

with col1[1]:
    if not st.session_state["sq_cur_obj"]:  
        
        reconnection()                                       # Check the SQL cursor object is present is session state or not
        st.write("Welcome")
    else:
        sq_conn=st.session_state["sq_connection_obj"]
        sq_cur=st.session_state["sq_cur_obj"]        

