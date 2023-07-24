import streamlit as st
from db_conn import *
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


_="""

    Function Definations

"""

_=""" Supportive function """

# funtcion to get refress data
def refresh_data():
    video_file = open('video/dashboard_refresh.mp4', 'rb')
    video_bytes = video_file.read()
    return video_bytes    

# Function to get user table data
def user_table_data(user_table,connection):
    try:
        df = pd.read_sql_query("SELECT * FROM " + user_table, connection)
        names = list(df['id'])
        usernames = list(df['username'])
        hashed_passwords = list(df['password'])
        return names,usernames,hashed_passwords
    except:
        st.session_state["sq_cur_obj"]=0
        st.experimental_rerun()

# Function for :Reset Password
#@st.experimental_memo(suppress_st_warning=True,show_spinner=False)
def reset_password_mail_verfication(receiver_email,sender_mail=dashboard_mail_id,sender_password=dashboard_mail_password):
    import smtplib, ssl
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    import math
    import random
    digits="0123456789"
    OTP=""
    for i in range(6):
        OTP+=digits[math.floor(random.random()*10)]
    otp = OTP + " is your OTP"
    msg= otp
    print(msg)

    sender_email = sender_mail
    sender_password = sender_password


    message = MIMEMultipart("alternative")
    message["Subject"] = "Your OTP for password reset"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Welcome,to the Stock_analyser!

    Hello,
    Here is your OTP
    to reset password:
      {OTP}

    Best of luck, 
    for your best strategies for stock market.""".format(OTP=OTP)
    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with st.spinner("sending OTP to your Mail-Id"):
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, receiver_email, message.as_string())
                st.success("Sent")
                time.sleep(2)
                return OTP

        except Exception as e:
            st.error(e)
            return 0

# Functio to send user credentials after accounc creation

def password_mail(user_mail_id,username,password,sender_mail=dashboard_mail_id,sender_password=dashboard_mail_password):
        
        import smtplib, ssl
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        username = username
        password = password
        sender_email = sender_mail
        sender_password = sender_password
        receiver_email = user_mail_id

        message = MIMEMultipart("alternative")
        message["Subject"] = "Your Stock-analysers Password"
        message["From"] = sender_email
        message["To"] = receiver_email

        # Create the plain-text and HTML version of your message
        text = """\
        Hello,{user}
        Welcome,to the Stock_analyser!
        Here is your password:
        {password}

        Best of luck, 
        for your best strategies for stock market.""".format(user=username, password=password)
        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            with st.spinner("your password is sending to your mail..."):
                time.sleep(2)
                server.login(sender_email, sender_password)
                server.sendmail(
                        sender_email, receiver_email, message.as_string()
                    )
                time.sleep(3)
                st.success("sent")
                st.write("please cheak in you'r spam")
                st.experimental_rerun()
                
#Password Requirement
def password_requirements():
        t="Password must contains-\n Uppercase,lowercase,\n digits,special characters" 
        d="Must be 8 to 12 digit long" 
        s="Not allowed-\n Spaces"
        requirement="1.{} \n2.{} \n3.{}".format(t,d,s)
        return requirement

# User validation
def user_validate(u_mail_id=None,username=None,password=None):

    def mail_validation(mail_id=None):
        m="Sorry,mail-id doesn't exist!"
        isexists = validate_email(mail_id, verify=False)
        if isexists == True:
            return True, 0
        else:
            return False,m

    def mail_validation_2(u_mail_id=None):
        exist_error="Sorry,mail-id doesn't exist!"
        invalid_error="Sorry,mail-id is'nt valid!"
        email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
        if re.search(email_condition,u_mail_id):

            return True, 0
        else:
            return False,invalid_error

    def password_validate(password=None):
       
        t="Password must contains-\n Uppercase,lowercase,\n digits,special characters; \n Must be 8 to 12 digit long; \n Not allowed-\n Spaces"
        
        # Create a schema
        schema = PasswordValidator()
        # Add properties to it
        schema\
        .min(8)\
        .max(12)\
        .has().uppercase()\
        .has().lowercase()\
        .has().digits()\
        .has().no().spaces()\
        
        return schema.validate(password),t

    def username_validate(username=None):
            t='Username should contain-\n characters, special characters \n; Not allowed-\n alphanmeric'
            ALPHANUM=re.compile('^[a-zA-Z0-9_.-]+$')
            if ALPHANUM.match(username):
                return False,t
            else:
                return True,0
            
    
    if u_mail_id and username and password:
        mail_v,mail_e=mail_validation_2(u_mail_id)
        user_v,user_e=username_validate(username)
        pass_v,pass_e=password_validate(password)
        return mail_v,mail_e,user_v,user_e,pass_v,pass_e
    if u_mail_id:
        mail_v,mail_e=mail_validation_2(u_mail_id)
        return mail_v,mail_e
    if username:
        user_v,user_e=username_validate(username)
        return user_v,user_e
    if password:
        pass_v,pass_e=password_validate(password)
        return pass_v,pass_e


def auth_func(names,uernames,passwords):
    authenticator = stauth.Authenticate(names,uernames,passwords,"stocksalgo", "abcdef", cookie_expiry_days=30)
    names, authentication_status, username = authenticator.login("Login", "main")
    return names,authentication_status,username,authenticator


def sheet_names(_username,table_name,_connection):
    try:
        file_names_q='SELECT sheet_name FROM ' + table_name +' Where username="'+_username+'"'
        file_names_df=pd.read_sql_query(file_names_q,_connection).drop_duplicates()
        return file_names_df
    except:
        st.error("Something were wrong......")
        if not st.session_state["sq_cur_obj"]:
            st.session_state["sq_cur_obj"]=0   
            time.sleep(2)
            st.warning("Please check connection.....")
            st.experimental_rerun()


def filter_names(_username,table_name,_connection):
    try:
        file_names_q='SELECT name FROM ' + table_name +' Where username="'+_username+'"'
        file_names_df=pd.read_sql_query(file_names_q,_connection).drop_duplicates()
        return file_names_df
    except:
        st.error("Something were wrong......")
        if not st.session_state["sq_cur_obj"]:
            st.session_state["sq_cur_obj"]=0   
            time.sleep(2)
            st.warning("Please check connection.....")
            st.experimental_rerun()


def query_run(query,connection):
    try:
        df=pd.read_sql_query(query,connection)
        return df
    except:
        st.error("Something went wrong!!!")
        if not st.session_state["sq_cur_obj"]:
            st.session_state["sq_cur_obj"]=0   
            st.error("Connection lost")
            time.sleep(2)
            st.experimental_rerun()

    