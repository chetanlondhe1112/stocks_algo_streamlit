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
#db_section_name="mysql2"

# databse name
database=st.secrets[db_section_name]["database"]

# tables credentials

# Equity Tables
admin = st.secrets["admin_ch"]["admin_ch"]
master_table = st.secrets["db_table"]["master_table"]
filter_table = st.secrets["db_table"]["filter_table"]
query_table = st.secrets["db_table"]["query_table"]
user_table = st.secrets["db_table"]["user_table"]

#   Portfolio tables
portfolio_table = st.secrets["db_table"]["portfolio_table"]

#   Sentiment tables
news_table = st.secrets["db_table"]["news_table"]
sentiment_table = st.secrets["db_table"]["sentiment_table"]

#   Mutual Fund table credentials
mf_sheet_table=st.secrets["db_table"]["mf_sheet_table"]
mf_filter_table=st.secrets["db_table"]["mf_filter_table"]
mf_rolling_return_table=st.secrets["db_table"]["mf_rolling_return_table"]
mf_reports_table=st.secrets["db_table"]["mf_reports_table"]
#mail credential
dashboard_mail_id=st.secrets["mail"]["mail_id"]
dashboard_mail_password=st.secrets["mail"]["password_token"]


_=""" 
    Database connection Functions
"""

# 1.Database conection Function
def sqlalchemy_connection(db_section_name):

    """ 
        Function used to connect database using SQLALCHEMY ORM for python.
        From SqlAlchemy we use create engine method
    """

    try:
        connect_string = "mysql://{}:{}@{}:{}/{}".format(st.secrets[db_section_name]["user"],
                                            st.secrets[db_section_name]["password"],
                                            st.secrets[db_section_name]["host"],
                                            st.secrets[db_section_name]["port"],
                                            st.secrets[db_section_name]["database"])
        return create_engine(connect_string)
    except:
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
        names = list(df['id'])
        usernames = list(df['username'])
        hashed_passwords = list(df['password'])
        return names,usernames,hashed_passwords
    
    except:

        st.session_state["sq_cur_obj"]=0
        st.experimental_rerun()

# 2.Sheet name 
def sheet_names(username,table_name,connection):

    """ 
        Function to collect the uploaded sheets by user
    """

    try:

        file_names_q='SELECT sheet_name,date_time FROM ' + table_name +' Where username="'+username+'"'
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


def filter_names(username,table_name,connection):

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


def fetch_user_uploads(username,conn):


    """ 
        Collect the files of Equity FIlter module
    """
    st.session_state['users_sheets_names']=sheet_names(username,master_table,conn)
    st.session_state['users_filter_names']=filter_names(username,table_name=filter_table,connection=conn)
    
    """
        Collect the files OF Mutual Fund Module
    """
    st.session_state['main_file_names']=sheet_names(username,mf_sheet_table,conn)
    st.session_state['rr_file_names']=sheet_names(username,mf_rolling_return_table,conn)
    st.session_state['mf_filter_names']=filter_names(username,table_name=mf_filter_table,connection=conn)

    """
        Collect the files of Uploads Module
    """
    st.session_state['u_users_sheets_names']=sheet_names(username,master_table,conn)
    st.session_state['u_rr_file_names']=sheet_names(username,mf_rolling_return_table,conn)
    st.session_state['u_main_file_names']=sheet_names(username,mf_sheet_table,conn)

    """
        Collect the all saved querys
    """
    st.session_state['my_querys_names']=query_names(table_name=query_table,connection=conn,username=username)

    """
        Collect the all saved reports
    """
    st.session_state['mf_report_names'],st.session_state['mf_report_dates']=report_names(username=username)


def user_data_collection(username,conn):
    """
        This function is made to collect all the users data which,
        has stored by user.
        We collect only the names of the all names of the files,filters
        so the user can scroll through them to select the sepecific one
        from his own uploads.
    """
    with st.spinner("###### Please wait!!,\n###### dashboard is collecting your uploads..."):
        
        try:
            # Delete all the items in Session state
            #for key in st.session_state.keys():
            #    if key!="st.session_state['authentication_status']":
            #        del st.session_state[key]

            #reconnection()

            fetch_user_uploads(username=username,conn=conn)

            st.success("Collected your data....")

            ret="Enjoy your analysis..."

            time.sleep(2)

            return ret,1
        
        except:
            st.error("Dashboard gets problem \nto collect your data...")

            time.sleep(2)

            ret="Dashboard gets problem to collect your data..."

            return ret,0


def refresh_dashboard(username,conn):
    
    """
        to refresh the dashboard so it will update his lists of files and filters.
    """

    with st.spinner("Refreshing Dashboard..."):
    
        try:
            
            fetch_user_uploads(username=username,conn=conn)

            st.success("Dashboard Updated")

            time.sleep(1)
        
        except:
            st.error("Unable to Refresh dashboard")

            time.sleep(1)


def fetch_table(table_name,connection,sheet_name=None,username=None):

    """
        To fetch the tables of users,with specific sheet name or file names 
        which was given by user at the time of upload.
    """

    if sheet_name and username:

        try:

            selected_file_q='SELECT * FROM '+ table_name+' WHERE username="'+username+'" and sheet_name="'+sheet_name+'"'
            selected_file_df=pd.read_sql(selected_file_q,connection).drop_duplicates().dropna(axis=1,how='all')
            selected_file_datetime=selected_file_df['date_time'][0]
            return selected_file_df.drop(columns=['username','sheet_name','lable','date_time'],axis=1),selected_file_datetime
        
        except:

            st.error("Server lost.....")
            st.error("Please check connection.....")
            if not st.session_state["sq_cur_obj"]:
                st.session_state["sq_cur_obj"]=0   
                time.sleep(2)
                st.experimental_rerun()

    else:

        try:    

            selected_file_q="SELECT * FROM " + table_name
            selected_file_df=pd.read_sql(selected_file_q,connection).dropna(axis=1,how='all')
            lenght_of_selected_file_df=len(selected_file_df)
            return selected_file_df,lenght_of_selected_file_df
        
        except:

            st.error("Server lost.....")
            st.error("Please check connection.....")
            st.session_state["sq_cur_obj"]=0
            time.sleep(2)
            st.experimental_rerun()


def fetch_filter(table_name,connection,name,username):
    """
        To fetch the filter 
    """
    try:
        selected_file_q='SELECT * FROM '+ table_name+' WHERE username="'+username+'" and name="'+name+'"'
        selected_file_df=pd.read_sql(selected_file_q,connection).drop_duplicates().dropna(axis=1,how='all')
        selected_file_datetime=selected_file_df['date_time'][0]
        return selected_file_df.drop(columns=['username','name','lable','date_time'],axis=1),selected_file_datetime
    except:
        st.error("Server lost.....")
        st.error("Please check connection.....")
        if not st.session_state["sq_cur_obj"]:
            st.session_state["sq_cur_obj"]=0   
            time.sleep(2)
            st.experimental_rerun()


def fetch_query(table_name,connection,name,username):

    """
        To fetch query
    """
    try:
        selected_query_q='SELECT query,date_time FROM '+ table_name+' WHERE username="'+username+'" and name="'+name+'"'
        selected_query_df=pd.read_sql_query(selected_query_q,connection).drop_duplicates().dropna(axis=1,how='all')
        selected_query=selected_query_df['query'][0]
        selected_query_datetime=selected_query_df['date_time'][0]
        return selected_query,selected_query_datetime
    except:
        st.error("Something were wromg,please try again!")
        st.error("Please check your network!")
        if not st.session_state["sq_cur_obj"]:
            st.session_state["sq_cur_obj"]=0   
            time.sleep(2)
    st.experimental_rerun()


def delete_query(table_name,cursor,username,name,date_time):
    """
        To delete query
    """
    delete_query_q="DELETE FROM " + table_name + " WHERE username='" + username + "' and name='" +name+ "' and date_time='"+str(date_time)+"'"
    
    with st.spinner("deleting..."):
        try:
            cursor.execute(text(delete_query_q))
            st.success("Query Deleted..")
            time.sleep(1)
        except:
            st.error("Something were wrong,please try again!")
            st.error("Please check your network!")
            if not st.session_state["sq_cur_obj"]:
                st.session_state["sq_cur_obj"]=0   
                time.sleep(2)

# 2.Sheet name 
def report_names(username,table_name=mf_reports_table):

    """ 
        Function to collect the uploaded sheets by user
    """
    try:
        connection=st.session_state["sq_connection_obj"]
        file_names_q='SELECT mf_main_sheet,date_time FROM ' + table_name +' Where username="'+username+'"'
        file_names_df=pd.read_sql_query(file_names_q,connection).drop_duplicates()
        file_names_df=file_names_df.sort_values(by='date_time',ascending=False)
        #.drop(columns=['username','lable','date_time','mf_main_sheet','mf_rr_sheet','mf_filter_name'],axis=1)
        return file_names_df,file_names_df['date_time']

    except:

        st.error("Something were wrong......")
        if not st.session_state["sq_cur_obj"]:
            st.session_state["sq_cur_obj"]=0   
            time.sleep(2)
            st.warning("Please check connection.....")
            st.experimental_rerun()


def fetch_report(main_file_name,username,table_name=mf_reports_table):
    """
        To fetch the filter 
    """
    try:
        connection=st.session_state["sq_connection_obj"]
        file_q='SELECT * FROM ' + table_name +' Where username="'+username+'" and mf_main_sheet="'+main_file_name+'"'
        file_df=pd.read_sql_query(file_q,connection).drop_duplicates()
        file_df=file_df.sort_values(by='Result',ascending=False)
        file_df.index = np.arange(1, len(file_df) + 1)
        return file_df.drop(columns=['username','lable','date_time','mf_main_sheet','mf_rr_sheet','mf_filter_name'],axis=1),file_df.iloc[0]['date_time']
    except:
        st.error("Server lost.....")
        st.error("Please check connection.....")
        if not st.session_state["sq_cur_obj"]:
            st.session_state["sq_cur_obj"]=0   
            time.sleep(2)
            st.experimental_rerun()

def fetch_user_uploads_v2(username,conn):
    """ 
        Collect the files of Equity FIlter module
    """
    st.session_state['users_sheets_names']=sheet_names(username,master_table,conn)
    st.session_state['users_filter_names']=filter_names(username,table_name=filter_table,connection=conn)
    
    """
        Collect the files OF Mutual Fund Module
    """
    st.session_state['main_file_names']=sheet_names(username,mf_sheet_table,conn)
    st.session_state['rr_file_names']=sheet_names(username,mf_rolling_return_table,conn)
    st.session_state['mf_filter_names']=filter_names(username,table_name=mf_filter_table,connection=conn)

    """
        Collect the files of Uploads Module
    """
    st.session_state['u_users_sheets_names']=sheet_names(username,master_table,conn)
    st.session_state['u_rr_file_names']=sheet_names(username,mf_rolling_return_table,conn)
    st.session_state['u_main_file_names']=sheet_names(username,mf_sheet_table,conn)

    """
        Collect the filters
    """
    #Equity filters
    #st.session_state['users_filter_names']=filter_names(username=username,table_name=filter_table,connection=conn)
    
    #Mutual Fund Filters
    #st.session_state['mf_filter_names']=filter_names(username=username,table_name=mf_filter_table,connection=conn)


def user_data_collection_v2(username,conn):
    """
        This function is made to collect all the users data which,
        has stored by user.
        We collect only the names of the all names of the files,filters
        so the user can scroll through them to select the sepecific one
        from his own uploads.
    """
    #with st.spinner("###### Please wait!!,\n###### dashboard is collecting your uploads..."):
        
        #try:
                            
    """ 
        Collect the files of Equity FIlter module
    """
    st.session_state['users_sheets_names']=sheet_names(username,master_table,conn)
    st.session_state['users_filter_names']=filter_names(username,table_name=filter_table,connection=conn)
    
    """
        Collect the files OF Mutual Fund Module
    """
    st.session_state['main_file_names']=sheet_names(username,mf_sheet_table,conn)
    st.session_state['rr_file_names']=sheet_names(username,mf_rolling_return_table,conn)
    st.session_state['mf_filter_names']=filter_names(username,table_name=mf_filter_table,connection=conn)

    """
        Collect the files of Uploads Module
    """
    st.session_state['u_users_sheets_names']=sheet_names(username,master_table,conn)
    st.session_state['u_rr_file_names']=sheet_names(username,mf_rolling_return_table,conn)
    st.session_state['u_main_file_names']=sheet_names(username,mf_sheet_table,conn)

    #st.success("Collected your data....")

    ret="Enjoy your analysis..."

    #time.sleep(2)

    return ret,1
        
        #except:
            #st.error("Dashboard gets problem \nto collect your data...")

        #    time.sleep(2)

        #    ret="Dashboard gets problem to collect your data..."

        #    return ret,0
    