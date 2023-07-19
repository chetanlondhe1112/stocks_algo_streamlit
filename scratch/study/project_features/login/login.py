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

from db_conn import *
from home_functions import *
from connection import db_conn

_=""" Defaults"""

current_date = datetime.now()

_="""
    Page layout design
"""
if "sidebar_state" not in st.session_state:
    st.session_state["sidebar_status"]="collapsed"

# Set page config
st.set_page_config(
        page_icon="📈",
        page_title="Stocks Algo",
        layout="wide",
        initial_sidebar_state=st.session_state["sidebar_status"],
        menu_items={
            #'Report a bug': "https://www.stockanalyser2022@gmail.com/",
            'About': "# Stocks Analyser!"
                    "\n ##### Report a bug on mail:"
                    "\n ##### https://www.stockanalyser2022@gmail.com/"
        }
    )

# CSS file
#with open('CSS/homestyle.css') as f:
#    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)



#Page columns layout
#if "Home_Image" not in st.session_state:
#    st.session_state["Home_Image"]=Image.open('stock3.png')


col1=st.columns((2,1))

with col1[0]:
    col1[0].markdown('# 📈:red[Stocks Algo ]')
    #col1[0].info("Username:chetan|Password:Chetan@3333")
    #col1[0].image(st.session_state["Home_Image"], caption='Stocks Analyser',use_column_width=True)


_=""" 

    Creating Connection 

"""
# Connection defaults
if "serverout_time" not in st.session_state:
    st.session_state["serverout_time"]=0


# Session state objects of database connection 
if "sq_connection_obj" not in st.session_state:                                 # session state SQL connection object         
    st.session_state["sq_connection_obj"]=0
if "sq_cur_obj" not in st.session_state:                                        # session state SQL cursor object
    st.session_state["sq_cur_obj"]=0

with col1[1]:
    if not st.session_state["sq_cur_obj"]:  
        
        reconnection()                                       # Check the SQL cursor object is present is session state or not

    else:
        sq_conn=st.session_state["sq_connection_obj"]
        sq_cur=st.session_state["sq_cur_obj"]        

   


_="""

    session state

"""

_="""SS_Variables"""

# 0.Image


# 1. User_table data
if "names" and "usernames" and "hashed_passwords" not in st.session_state:
    st.session_state["names"],st.session_state["usernames"],st.session_state["hashed_password"]=user_table_data(user_table,sq_conn)

# 2.Username
if "username" not in st.session_state:
    st.session_state["username"]=""
username=st.session_state["username"]

# 3.Authentication_status
if 'authentication_status' not in st.session_state:
    st.session_state['authentication_status'] =0
auth_status=st.session_state['authentication_status']

if 'authenticator' not in st.session_state:
    st.session_state['authenticator']=0

# 4.Lable
if "lable" not in st.session_state:
    st.session_state["lable"] = ""

# 5.User Id
if 'user_id' not in st.session_state:
    st.session_state["user_id"]=''

# 6.OTP
if 'OTP' not in st.session_state:
    st.session_state["OTP"]=0

# 7.Values
if 'values' not in st.session_state:
    st.session_state["values"]=pd.DataFrame()


_="""SS_Buttons"""
# 1. Loggin 
if 'login' not in st.session_state:
    st.session_state["login"]=False
def login_callback():
    st.session_state["login"] =True

# 2. Create acc
if 'create_acc' not in st.session_state:
    st.session_state["create_acc"]=False
def create_acc_callback():
    st.session_state["create_acc"] = True

# 3.Forget Password
if 'forget_password' not in st.session_state:
    st.session_state["forget_password"]=False
def forget_password_callback():
    st.session_state["forget_password"] = True

# 4.Send_OTP
if 'send_otp' not in st.session_state:
    st.session_state["send_otp"]=False
def send_otp_callback():
    st.session_state["send_otp"] = True

# 5.OTP_verify
if 'otp_verify' not in st.session_state:
    st.session_state["otp_verify"]=False
def otp_verify_callback():
    st.session_state["otp_verify"] = True

# 6.Reset Password
if 'reset_password' not in st.session_state:
    st.session_state["reset_password"]=False
def reset_password_callback():
    st.session_state["reset_password"] = True


#@st.cache(suppress_st_warning=True,show_spinner=False)
def main():

    with col1[1]:

        if st.session_state["authentication_status"]:

            authen=st.session_state['authenticator']

            st.session_state['active_heighlights']=1

            lg_but_col=st.columns((1,1))
            with lg_but_col[1].expander("🙎‍♂️{}".format(st.session_state["username"])):

                if authen.logout('Logout', 'main'):

                    for key in st.session_state.keys():
                        del st.session_state[key]
                    #st.experimental_rerun()  

        #authenticator = stauth.Authenticate(st.session_state["names"],st.session_state["usernames"],st.session_state["hashed_password"], "sfdb", "abcdef", cookie_expiry_days=30)
        elif not st.session_state["authentication_status"]:
            
            
            if st.session_state["login"]==True or st.session_state["create_acc"]==False and st.session_state["forget_password"]==False and  st.session_state["reset_password"]==False:
                
                names, st.session_state['authentication_status'], username, st.session_state["authenticator"]=auth_func(st.session_state["names"],st.session_state["usernames"],st.session_state["hashed_password"])
                
                #names, st.session_state['authentication_status'], username = authenticator.login("Login", "main")
                
                if st.session_state["authentication_status"]: 
                    
                    st.session_state["username"]=username
    
                    st.experimental_rerun()


                elif st.session_state["authentication_status"]==False:
                    with col1[1]:
                        sign_col=st.columns((1,1))
                        if len(username)>0:

                            st.error('Username/password is incorrect')  
                        
                        st.session_state["forget_password"]=sign_col[0].button("Forget Password ?",on_click=forget_password_callback,use_container_width=True)

                        st.session_state["create_acc"]=sign_col[1].button("Sign Up",on_click=create_acc_callback,use_container_width=True)

                else:
                    with col1[1]:
                        sign_col=st.columns((1,1))
                        st.session_state["forget_password"]=sign_col[0].button("Forget Password ?",on_click=forget_password_callback,use_container_width=True)

                        st.session_state["create_acc"]=sign_col[1].button("Sign Up",on_click=create_acc_callback,use_container_width=True)
                

            if st.session_state["create_acc"] :
                col1[1].subheader("Sign Up")
                with col1[1].form("sign up"):

                    values=[]

                    
                    full_name=st.text_input("Name",max_chars=50,placeholder="Full Name")
                    email = st.text_input("Email",placeholder="Email",max_chars=50)
                    username = st.text_input("Username",placeholder="Username",help="Eg. username=james@SA",max_chars=50)
                    password = st.text_input("Password",placeholder="Password", type='password',help=password_requirements(),max_chars=100)
                    
                    hashed_password = stauth.Hasher([str(password)]).generate()

                    

                    if st.form_submit_button("Sign Up",use_container_width=True):
                        acc_query = "SELECT * FROM '"+user_table+"' where username='" + username + "'and email='"+email+"'"

                        values =query_run(acc_query,connection=sq_conn)
                        mail_v, mail_e,user_v,user_e,pass_v,pass_e=user_validate(email,username,password)

                        if values:

                            if username in values['username'].to_list():
                                st.error("Username is already used,Please select another username!!")
                            elif user_id in values['id'].to_list():
                                st.error("User ID is already used,Please select another User ID!!")
                            else:
                                st.warning("User already exist!,Please try new username/user_id")

                        elif mail_v==False or user_v==False or pass_v==False:

                            if mail_v==False:
                                st.warning("1.invalid mail-id")
                                st.error(mail_e)
                            if user_v==False:
                                st.warning("2.invalid username")
                                st.error(user_e)
                            if pass_v==False:
                                st.warning("3.invalid password")
                                st.error(pass_e)

                        else:    
                            try:
                                with st.spinner("Creating account..."):
                                    time.sleep(2)
                                    signing_up_datetime = datetime.now()
                                    add_query = 'insert into `user`(`fullname`,`username`,`password`,`createdate`,`email`)VALUES(%s,%s,%s,%s,%s)'
                                    try:
                                        sq_cur.execute(add_query,(str(full_name),username,str(hashed_password[0]),signing_up_datetime,str(email)))
                                        st.success("Successfully created account.")
                                    except:
                                        st.error("Error to create account.")

                                with st.spinner("Sending username and password to mail-id"):
                                    try:
                                        time.sleep(2)
                                        password_mail(e, username, password, sender_mail=dashboard_mail_id, sender_password=dashboard_mail_password)
                                        st.session_state["create_acc"]=False
                                        st.experimental_rerun()
                                    except:
                                        st.error("Error to send mail.")
   
                                #st.balloons()
                                
                            except:
                                st.error("Please,cheak your network.")
                            st.experimental_rerun()
                login_col=st.columns((1.3,1))    
                login_col[0].markdown("##### Already registerd?")  

                if login_col[1].button("Login",use_container_width=True):
                    st.session_state["create_acc"]=False
                    st.experimental_rerun()

            if st.session_state["forget_password"]:

                #st.experimental_memo.clear()
                col1[1].subheader("Reset Password")
                col1[1].info("Please Verify your mail_id to reset your password")

                with col1[1].form("Email Verification"):
                    values=[]
                    st.subheader("Email Verification")
                    st.session_state["user_id"] = st.text_input("Enter your registered mail-id",placeholder="Email")

                    st.write(st.session_state["user_id"])
                    if (st.form_submit_button("Send OTP",on_click=send_otp_callback,use_container_width=True) or st.session_state["send_otp"]  ) and st.session_state["user_id"] :
                        #st.session_state["OTP"]=False
                        if st.session_state["user_id"]:
                            if st.form_submit_button("Resend",use_container_width=True):
                                st.session_state["OTP"]=0
                                st.experimental_memo.clear()
                                st.session_state["send_otp"]=True
                                st.experimental_rerun()
                            
                            mail_v, mail_e=user_validate(u_mail_id=st.session_state["user_id"])

                            if not mail_v:
                                st.error("Invlid Mail_id")
                                time.sleep(2)
                                st.session_state["forget_password"]=False
                                st.experimental_rerun()

                            elif mail_v==True:    
                                acc_query = "SELECT * FROM user where email='" + str(st.session_state["user_id"]) + "'" 
                                #sq_cur.execute(text(acc_query))      
                                st.session_state["values"] = query_run(acc_query,connection=sq_conn)
                                #st.experimental_rerun()
                                if len(st.session_state["values"]):
                                    if not st.session_state["OTP"]:
                                        st.session_state["OTP"]=reset_password_mail_verfication(st.session_state["user_id"],)
                                        #st.experimental_rerun()
                                    else:    
                                        check_otp=st.text_input("Enter OTP")
                                        #st.session_state["otp_verify"]=st.form_submit_button("Verify",on_click=otp_verify_callback)
                                        if( st.form_submit_button("Verify",on_click=otp_verify_callback) or st.session_state["otp_verify"] ):  
                                            if check_otp==st.session_state["OTP"]:
                                                with st.spinner():
                                                    st.session_state["reset_password"]=True
                                                    st.session_state["forget_password"]=False
                                                    st.session_state["login"]=False
                                                    st.success("Verified...")
                                                    time.sleep(2)
                                                    st.experimental_rerun()
                                            else:
                                                st.error("Incorrect OTP")                          
                                else:
                                    st.error("Sorry,mail_id is not registerd.")
                                    st.info("Please,Sign Up first.")
                        else:
                            st.error("Invalid email!") 

                forget_col=st.columns((1,1))
                if forget_col[0].button("Login",use_container_width=True):
                    st.session_state["forget_password"]=False
                    st.experimental_rerun()

                if forget_col[1].button("Sign Up",use_container_width=True):
                    st.session_state["forget_password"]=False
                    st.session_state["create_acc"]=True
                    st.experimental_rerun()

            if  st.session_state["reset_password"] :
                with col1[1].form("Email Verification"):
                    st.subheader("Reset Password")
                    new_pass=st.text_input(" New password",type="password")
                    conf_pass=st.text_input(" New password confirmation",type="password")
                                      
                    if st.form_submit_button("Save Password"):
                        pass_v,pass_e=user_validate(password=conf_pass)
                        
                        if new_pass==conf_pass:
                            if pass_v==False:
                                st.warning("3.invalid password")
                                st.error(pass_e)
                            elif pass_v==True:
                                hashed_password = stauth.Hasher([str(new_pass)]).generate()
                                reset_pass_q="UPDATE user_login SET password = '"+str(hashed_password[0])+"' WHERE id = '"+st.session_state["user_id"]+"'"
                                sq_cur.execute(text(reset_pass_q))
                                st.success("Password has reset")
                                time.sleep(2)
                                st.session_state["user_id"]=''
                                st.session_state["reset_password"]=False
                                st.experimental_rerun()
                        else:
                            st.error("The two password fields did'nt match.")       

if __name__ == '__main__':
        main()

 