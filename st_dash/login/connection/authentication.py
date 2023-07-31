import time
import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
from validate_email_address import validate_email
from password_validator import PasswordValidator
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re
from sqlalchemy import text
import math
import random


class messages:
    def __init__(self):
        pass

class authenticate:
    """
        authenticate class is build to provide the streamlit authentication for dashboard   
    """  

    def __init__(self,connection_link=str,connection_object=object):
        self.sql=connection_object
        self.engine=connection_link
        self.mail_info=self.sql.st_algo_mail
        self.sender_mail=self.mail_info['mail']
        self.sender_mail_password=self.mail_info['password']
        self.tables=self.sql.tables

    def user_table_data(self):
        """
            This function collects all users credentials for login process.
        """
        user_table = self.tables['user_table']
        try:
            q="SELECT * FROM " + user_table
            df = pd.read_sql_query(q,self.engine)
            emails = list(df['email'])
            usernames = list(df['username'])
            hashed_passwords = list(df['password'])
            return emails,usernames,hashed_passwords
        except Exception as e:
            print(e)

    # Function for :Reset Password
    #@st.experimental_memo(suppress_st_warning=True,show_spinner=False)
    def reset_password_mail_verfication(self,receiver_email=str):
        
        digits="0123456789"
        OTP=""
        for i in range(6):
            OTP+=digits[math.floor(random.random()*10)]
        otp = OTP + " is your OTP"
        msg= otp
        print(msg)

        sender_email = self.sender_mail
        sender_password = self.sender_mail_password


        message = MIMEMultipart("alternative")
        message["Subject"] = "Your OTP for password reset"
        message["From"] = sender_email
        message["To"] = receiver_email

        # Create the plain-text and HTML version of your message
        text = """\
        Welcome,to the Stock Algo!

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
    def password_mail(self,user_mail_id=str,username=str,password=str):
            
            import smtplib, ssl
            from email.mime.text import MIMEText
            from email.mime.multipart import MIMEMultipart

            username = username
            password = password
            sender_email = self.sender_mail
            sender_password = self.sender_mail_password
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
                    print("sent")
                    print("please cheak in you'r spam")
                    
    #Password Requirement
    def password_requirements(self):
            t="Password must contains-\n Uppercase,lowercase,\n digits,special characters" 
            d="Must be 8 to 12 digit long" 
            s="Not allowed-\n Spaces"
            requirement="1.{} \n2.{} \n3.{}".format(t,d,s)
            return requirement

    # User validation
    def user_validate(self,u_mail_id=None,username=None,password=None):

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

    def auth_func(self,emails,uernames,passwords):
        authenticator = stauth.Authenticate(emails,uernames,passwords,"stocksalgo", "ghijk", cookie_expiry_days=30)
        names, authentication_status, username = authenticator.login("Login", "main")
        return names,authentication_status,username,authenticator

    def fetch_query(self,query=str):
        try:
            return pd.read_sql_query(sql=query,con=self.engine)
        except Exception as e:
            print(e)
            return 0

    def check_user(self,username=str,email=str):
        user_table=self.sql.tables['user_table']
        acc_query = "SELECT * FROM '"+user_table+"' where username='" + username + "'and email='"+email+"'"
        return self.fetch_query(acc_query)
    
    def sign_up_user(self,data=dict):
        """INSERT INTO BOOKS (book_id, book_price,
        genre, book_name) VALUES(:book_id, :book_price,
        :genre, :book_name)"""
        user_table=self.tables["user_table"]
        add_query = "INSERT INTO `"+user_table+"` (fullname, username, password, createdate, email)VALUES(:fullname,:username,:password,:createdate,:email)"
        self.engine.execute(text(add_query),**data)