import streamlit as st
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine,text
import time

_="""
    Database credentials
"""  
# database connection credentials: Hostnames

db_section_name="mysql"

# databse name
database=st.secrets[db_section_name]["database"]
user_table=st.secrets["db_tables"]["user_table"]
access_token_table=st.secrets["db_tables"]["access_token_table"]
customer_table=st.secrets["db_tables"]["customer_table"]
# tables credentials

#mail credential
dashboard_mail_id=st.secrets["mail"]["mail_id"]
dashboard_mail_password=st.secrets["mail"]["password_token"]


_=""" 
    Database connection Functions
"""
if "sq_connection_obj" not in st.session_state:
    st.session_state["sq_connection_obj"]=''
# 1.Database conection Function
def sqlalchemy_connection(db_section_name):
    """ 
        Function used to connect database using SQLALCHEMY ORM for python.
        From SqlAlchemy we use create engine method
    """
    #try:
    connect_string = "mysql://{}:{}@{}:{}/{}".format(st.secrets[db_section_name]["user"],
                                        st.secrets[db_section_name]["password"],
                                        st.secrets[db_section_name]["host"],
                                        st.secrets[db_section_name]["port"],
                                        st.secrets[db_section_name]["database"])
    return create_engine(connect_string)
    #except:
    error="No database passed to function!!!"
    return error


sq_conn=sqlalchemy_connection(db_section_name=db_section_name)
sq_cur=sq_conn.connect()

regi_tab,log_tab=st.tabs(['Registration','Register'])


with regi_tab:
    col=st.columns((0.5,2,0.5))

    col[1].title("Customer Registration")

    today=datetime.now()
    with st.form("Customer registration"):


        st.header("Customer Personal Details")
        
        name=st.text_input("Enter Name",placeholder="Name")

        password=st.text_input("Enter Password",placeholder="Password",type='password')

        angel_username=st.text_input("Enter Angel Broking Username",placeholder="Username")

        angel_password=st.text_input("Enter Angel Broking Password",placeholder="Password",type='password')

        aadhar=st.number_input("Enter Adhar Number")

        pan=st.number_input("Enter Pan Number")

        mobile=st.number_input("Enter Mobile No.")

        st.header("Customer Trading Details")

        lotsize=st.number_input("Enter Lot Size")

        initial_depo=st.number_input("Enter Initial Deposit")

        if st.form_submit_button("Register",use_container_width=True):
            dic={"name":name,"pwd":password,"pan":pan,"aadhar":aadhar,"mobileno":mobile,"initialdeposit":initial_depo,"lotsize":lotsize,"createdate":today,"angel_user":angel_username,"angel_pwd":angel_password}
            df=pd.DataFrame(dic,index=[0])

            try:
                df.to_sql(customer_table,con=sq_conn,if_exists="append",index=False)
                st.success("Registration Successfull")
                time.sleep(1)
                st.experimental_rerun()
            except Exception as e:
                st.error("Registration Failed")
                st.error(e)

with log_tab:
    col2=st.columns((0.5,2,0.5))

    col2[1].title("Customer Register")
    df=pd.read_sql_table(customer_table,con=sq_conn,index_col=['id'])

    st.write(df)
