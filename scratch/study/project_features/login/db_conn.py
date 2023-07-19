import streamlit as st
from sqlalchemy import create_engine,text
import pandas as pd
import time
import numpy as np


_="""
    Database credentials
"""  
# database connection credentials: Hostnames

db_section_name="mysql"

# databse name
database=st.secrets[db_section_name]["database"]
user_table=st.secrets["db_tables"]["user_table"]
access_token_table=st.secrets["db_tables"]["access_token_table"]
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
    st.write(connect_string)
    return create_engine(connect_string)
    #except:
    error="No database passed to function!!!"
    return error
    
def reconnection():  
    try: 

        # Creating Connection       
        st.session_state["sq_connection_obj"] = sqlalchemy_connection(db_section_name=db_section_name)
        sq_conn=st.session_state["sq_connection_obj"]
        st.session_state["sq_cur_obj"]=sq_conn.connect()
        st.experimental_rerun()

    except:
        
        st.info("Reconnecting.............")
        time.sleep(1)
        st.experimental_rerun()
        st.stop() 
                    
_="""
    Data fetching functions
"""

# 1.Function to get user table data
def user_table_data(users_table,connection):

    """
        This function collects all users credentials for login process.
    """

    try:

        df = pd.read_sql_query("SELECT * FROM " + users_table, connection)
        emails = list(df['email'])
        usernames = list(df['username'])
        hashed_passwords = list(df['password'])
        return emails,usernames,hashed_passwords
    
    except:

        st.session_state["sq_cur_obj"]=0
        st.experimental_rerun()

# 2.Sheet name 
def fetch_table(username,table_name,connection):

    """ 
        Retrive whole table from database
    """

    try:

        file_names_q='SELECT * FROM ' + table_name +' Where username="'+username+'"'
        file_names_df=pd.read_sql_query(file_names_q,connection).drop_duplicates()
        file_names_df=file_names_df.sort_values(by='date_time',ascending=False).drop(columns=['date_time'])
        return file_names_df
    
    except:

        st.error("Something were wrong......")
        if not st.session_state["sq_cur_obj"]:
            st.session_state["sq_cur_obj"]=0   
            time.sleep(2)
            st.warning("Please check connection.....")
    st.experimental_rerun()


def filter_names(username,table_name):

    """
        to collect the filters names by given user.
    """
    try:

        file_names_q='SELECT name,date_time FROM ' + table_name +' Where username="'+username+'"'
        file_names_df=pd.read_sql_query(file_names_q,connection).drop_duplicates()
        
        file_names_df=file_names_df.sort_values(by='date_time',ascending=False).drop(columns=['date_time'])
        return file_names_df
    
    except:
        st.error("Something were wrong......")

        if not st.session_state["sq_cur_obj"]:
            st.session_state["sq_cur_obj"]=0   
            time.sleep(2)
            st.warning("Please check connection.....")
    st.experimental_rerun()


def query_names(table_name,connection,username):

    """
        To fetch query names
    """
    try:
        query_names_q='SELECT name,date_time FROM '+ table_name+' WHERE username="'+username+'"'
        query_names_df=pd.read_sql_query(query_names_q,connection).drop_duplicates().dropna(axis=1,how='all')
        if len(query_names_df):
            query_names_df=query_names_df.sort_values(by='date_time',ascending=False)
            return query_names_df
        else:
            return pd.DataFrame()
    except:
        st.error("Something were wromg,please try again!")
        if not st.session_state["sq_cur_obj"]:
            st.session_state["sq_cur_obj"]=0   
            time.sleep(2)
            st.warning("Please check connection.....")

    st.experimental_rerun()

def fetch_access_tokens(connection=st.session_state["sq_connection_obj"],table_name=access_token_table):
    """
        To fetch all access tokens
    """
    query_names_q='SELECT id,access_token,creatdate FROM '+ table_name+'"'
    query_names_df=pd.read_sql_query(query_names_q,connection).drop_duplicates().dropna(axis=1,how='all')
    if len(query_names_df):
        query_names_df=query_names_df.sort_values(by='date_time',ascending=False)
        return query_names_df
    else:
        return pd.DataFrame()
     