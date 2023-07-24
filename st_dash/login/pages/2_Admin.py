import streamlit as st
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine,text
import time
# Library imports
import streamlit as st
from kiteconnect import KiteConnect
from kiteconnect import KiteTicker
import datetime as dt
import time
import pdb
import pandas as pd
from sqlalchemy import create_engine,text
from Home import sql,db_tables

customer_tbl=db_tables["customer_table"]
entry_conditions=db_tables["entry_conditions"]
order_log_table=db_tables["order_log_table"]
user_table=db_tables["user_table"]
access_token_table=db_tables["access_token_table"]

st.title("Admin")
customer_tab,zerodha_tab=st.tabs(["Customer Registration","Zerodha Credentials"])
regi_tab,log_tab,update_tab=customer_tab.tabs(['Registration','Register'])


with regi_tab:
    col=st.columns((1,1,1))

    col[1].title("Registration")

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

        totp_key=st.text_input("Enter The TOTP Key",placeholder="TOTP Key")

        fin_q=st.number_input("Enter the fin quantity")

        lotsize=st.number_input("Enter Lot Size")

        initial_depo=st.number_input("Enter Initial Deposit")

        if st.form_submit_button("Register",use_container_width=True):
            dic={"name":name,"pwd":password,"pan":pan,"aadhar":aadhar,"mobileno":mobile,"initialdeposit":initial_depo,"lotsize":lotsize,
                "createdate":today,"angel_user":angel_username,"angel_pwd":angel_password,"totpkey":totp_key,"fin_q":fin_q}
            
            df=pd.DataFrame(dic,index=[0])

            try:
                sql.upload_to_table(df=df,table_name=customer_tbl,if_exists="append")
                st.success("Registration Successfull")
                time.sleep(1)
                st.experimental_rerun()
            except Exception as e:
                st.error("Registration Failed")
                st.error(e)

with log_tab:
    col2=st.columns((1,1,1))

    col2[1].title("Register")
    #df=pd.read_sql_table(customer_tbl,con=sq_conn,index_col=['id'])
    df=sql.fetch_tables(table_name=customer_tbl)
    st.write(df)



with zerodha_tab:
    # Module to generate zerodha access token to continuews data generation of tickers values

    _="""
        Database credentials
    """  
    # database connection credentials: Hostnames

    db_section_name="mysql"

    # databse name
    database=st.secrets[db_section_name]["database"]

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

    def fetch_access_tokens(connection=sq_conn,table_name=access_token_table):
        """
            To fetch all access tokens
        """
        query_names_q='SELECT id,access_token,createdate FROM `'+ table_name+'`'
        query_names_df=pd.read_sql_query(query_names_q,connection,index_col=['id']).drop_duplicates().dropna(axis=1,how='all')
        if len(query_names_df):
            query_names_df=query_names_df.sort_values(by='createdate',ascending=False,ignore_index=True)
            return query_names_df
        else:
            return pd.DataFrame()

    def update_access_token(access_token,api_key,api_secret,connection=sq_conn,table_name=access_token_table):
        """
            To fetch all access tokens
        """
        current_time=dt.datetime.now()
        
        df=pd.DataFrame(data={'id':1,'api_key':api_key,'api_secret':api_secret,'access_token':access_token,'createdate':current_time},index=[0])
        try:
            df.to_sql(access_token_table,con=connection,if_exists="replace",index=False)

            return True,''
        except Exception as e:
            return False,e     

    # Deafualts
    kws = ""
    kite = ""

    api_k = "m8lqe0lp92mndpzw"
    api_s = "lhg6sx4g3etshuleybete974h3voo8gz"
    
    #temp_access_token="2WcfyrIF67WtSxNNfUL8zVKnw0510Tn5"



    # log in to zerodha API panel
    def get_login(api_k, api_s):  
        """
            Generating the request token for zerodha account.
            -Function will generate link for access token
            -After collecting request token paste it in cmd and get your Access token
        """

        global kws, kite

        kite = KiteConnect(api_key=api_k)

        st.write("[*] Generate access Token : ", kite.login_url())
        #https://kite.trade/connect/login?api_key=a43v7sh3hkekai7u for request token https://kite.trade/connect/login?api_key=a43v7sh3hkekai7u&v=3

        request_tkn = st.text_input("[*] Enter Your Request Token Here : ")
        if st.button("Access Token"):
            try:
                # Try to generte session
                data = kite.generate_session(request_tkn, api_secret=api_s)
                kite.set_access_token(data["access_token"])
                kws = KiteTicker(api_k, data["access_token"])
                print(data['access_token'])
                st.success(data['access_token'])

            except Exception as e:
                # Validation for its operation fails
                print(e)

        # kite.set_access_token(access_token)
        # kws = KiteTicker(api_k, access_token)


    #get_login(api_k, api_s)

    from PIL import Image
    tit_col=st.columns((0.3,1,0.2))
    tit_col[1].title("Access Token Manager")
    col=st.columns((0.5,1,0.5))
    #image = Image.open('scratch\study\project_features\login\kite logo.png')

    access_tk_df=fetch_access_tokens(connection=sq_conn)
    with col[1]:
        
        im_col=st.columns((3,1,5))
        #im_col[1].image(image,width=70)
        acctok_tab,dbacctok_tab=st.tabs(["Access Token","Update Token"])



        with acctok_tab:
            kite = KiteConnect(api_key=api_k)
            #pdb.set_trace()
            
            with st.form("Access Token"):
                st.header("Creat Access Token")

                rq_col=st.columns((1,3,1))
                kit_url=kite.login_url()
                rq_col[1].write('''
                <a target="new" href={}>
                    <button>
                        Get Your Request Token
                    </button>
                </a>
                '''.format(kit_url),
                unsafe_allow_html=True)
            

                #https://kite.trade/connect/login?api_key=a43v7sh3hkekai7u for request token https://kite.trade/connect/login?api_key=a43v7sh3hkekai7u&v=3

                request_tkn=st.text_input("",placeholder="Enter your request token")
                temp_access_token=st.text_input("",placeholder="temporary token")
                if st.form_submit_button("Generate",use_container_width=True):
                    with st.spinner("Generating access token..."):
                        try:
                            # Try to generte session
                            #data = kite.generate_session(request_tkn, api_secret=api_s)
                            #kite.set_access_token(data["access_token"])
                            #kws = KiteTicker(api_k, data["access_token"])
                            time.sleep(2)
                            #st.success(data['access_token'])
                            #print(data['access_token'])
                            st.success(temp_access_token)

                        except Exception as e:
                            # Validation for its operation fails
                            print(e)
                            st.error("Sorry,error to generate the access token!!")
                
        with dbacctok_tab:
            with st.form("Update Token"):
                st.header("Update Token")
                st.write("Today : "+str(dt.date.today()))
                today=dt.datetime.now()
                st.subheader("New access token")
                
                st.success(temp_access_token)
                if st.form_submit_button("Update",use_container_width=True):
                    state,error=update_access_token(access_token=temp_access_token,api_key=api_k,api_secret=api_s)

                    if state==True:
                        st.success("Token Updated")
                        time.sleep(2)
                        st.experimental_rerun()
                    else:
                        st.error("Sorry,error to update token")
                        st.error(error)
                    
                st.subheader("Token Log")
                st.dataframe(access_tk_df,use_container_width=True)

