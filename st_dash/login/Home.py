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
from connection.db_conn import sqlalchemy_connect
 
username="chetan"
sql=sqlalchemy_connect(username)

tables_dict=sql.read_config()

db_tables=tables_dict["db_tables"]
customer_tbl=db_tables["customer_table"]
candle_stick_tbl=db_tables["candle_stick_log_table"]
entry_conditions=db_tables["entry_conditions"]
order_log_table=db_tables["order_log_table"]