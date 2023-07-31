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
    st.error("Please Login")
    st.stop()

if not st.session_state['sq_conn']:
    st.session_state['sq_conn']=reconnection(connection_object=sql)
    sq_conn=st.session_state['sq_conn']
else:
    sq_conn=st.session_state['sq_conn']

tables=sql.tables
customer_tbl=tables["customer_table"]
entry_conditions=tables["entry_conditions"]
order_log_table=tables["order_log_table"]
user_table=tables["user_table"]
access_token_table=tables["access_token_table"]
error_log_table=tables["error_log_table"]


dbm=sqlmethods(sq_conn,sql,st.session_state["authentication_status"])
def show_df(df):
    df.index = np.arange(1, len(df) + 1)
    return df
st.title("👨‍⚖️ Admin")
customer_tab,zerodha_tab,defaults,bnf_log,error_log=st.tabs(["📋 Customer Registration","🔐 Zerodha Credentials","📌 Set Values","🔖 BNF log","📑 Error Log"])
regi_tab,log_tab,upd_tab=customer_tab.tabs(['📝 Registration','📖 Register','✒️ Update'])
tls_error,st_tls_error=error_log.tabs(["📑 TLS Error Log","📑 Dashboard Error Log"])

with regi_tab:
    col=st.columns((1,1,1))

    col[1].header("📝 Registration")

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
                dbm.upload_to_table(df=df,table_name=customer_tbl,if_exists="append")
                st.success("Registration Successfull")
                time.sleep(1)
                st.experimental_rerun()
            except Exception as e:
                st.error("Registration Failed")
                st.error(e)

with log_tab:
    col2=st.columns((1,1,1))

    col2[1].header("📖 Register")
    #df=pd.read_sql_table(customer_tbl,con=sq_conn,index_col=['id'])
    df=dbm.fetch_tables(table_name=customer_tbl,)
    st.write(show_df(df))

with upd_tab:
    
    col=st.columns((1,1,1))

    col[1].header("✒️ Update")
    
    today=datetime.now()

    customers_names=dbm.fetch_customers_names()

    customer_name=st.selectbox("Select The Customer",options=customers_names)
    
    df=dbm.fetch_customer(customer_name=customer_name)

    with st.form("Customer Update"):

        st.header("Customer Personal Details")
        
        name=st.text_input("Enter Name",placeholder="Name",value=df['name'][0])

        password=st.text_input("Enter Password",placeholder="Password",type='password',value=df['pwd'][0])

        angel_username=st.text_input("Enter Angel Broking Username",placeholder="Username",value=df['angel_user'][0])

        angel_password=st.text_input("Enter Angel Broking Password",placeholder="Password",type='password',value=df['angel_pwd'][0])

        aadhar=st.number_input("Enter Adhar Number",value=df['aadhar'][0])

        pan=st.number_input("Enter Pan Number",value=df['pan'][0])

        mobile=st.number_input("Enter Mobile No.",value=df['mobileno'][0])

        st.header("Customer Trading Details")

        totp_key=st.text_input("Enter The TOTP Key",placeholder="TOTP Key",value=df['totpkey'][0])

        fin_q=st.number_input("Enter the fin quantity")

        lotsize=st.number_input("Enter Lot Size",value=df['lotsize'][0])

        initial_depo=st.number_input("Enter Initial Deposit",value=df['initialdeposit'][0])

        if st.form_submit_button("Update",use_container_width=True):

            dic={"name":name,"pwd":password,"pan":pan,"aadhar":aadhar,"mobileno":mobile,"initialdeposit":initial_depo,"lotsize":lotsize,
                "createdate":today,"angel_user":angel_username,"angel_pwd":angel_password,"totpkey":totp_key,"fin_q":fin_q}
            with st.spinner("Updating..."):
                try:
                    dbm.update_customer(update_values=dic,customr_name=customer_name)
                    st.success("Update Successfull")
                    st.experimental_rerun()
                except Exception as e:
                    st.error("Updates Failed")
                    st.error(e)

with zerodha_tab:
    # Module to generate zerodha access token to continuews data generation of tickers values

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
    tit_col=st.columns((0.7,1,0.5))
    tit_col[1].header("🔐 Access Token Manager")
    col=st.columns((0.5,1,0.5))
    #image = Image.open('scratch\study\project_features\login\kite logo.png')
    if 'tkn_df' not in st.session_state:
        st.session_state['tkn_df']=dbm.fetch_access_tokens(table_name=access_token_table)
    with col[1]:
        
        im_col=st.columns((3,1,5))
        #im_col[1].image(image,width=70)

        if "acctkn"  not in st.session_state:
            st.session_state['acctkn']='' 

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
                if st.form_submit_button("Generate",use_container_width=True):
                    
                    with st.spinner("Generating access token..."):
                        
                        try:
                            # Try to generte session
                            data = kite.generate_session(request_tkn, api_secret=api_s)
                            kite.set_access_token(data["access_token"])
                            kws = KiteTicker(api_k, data["access_token"])
                            time.sleep(2)
                            st.session_state['acctkn']=data['access_token']
                            st.success(st.session_state['acctkn'])

                        except Exception as e:
                            # Validation for its operation fails
                            print(e)
                            st.error("Sorry,error to generate the access token!!")
                
        with dbacctok_tab:
            
            with st.form("Update Token"):
                st.header("Update Token")
                st.write("Today : "+str(dt.date.today()))
                today=dt.datetime.now()

                gen_tab,add_tab=st.tabs(["Generated Token","Replace Your Token"])
                with gen_tab:
                    st.subheader("New access token")
                    
                    st.success(st.session_state['acctkn'])
                    if st.form_submit_button("Update",use_container_width=True):
                        state,error=dbm.update_access_token(access_token=st.session_state['acctkn'],api_key=api_k,api_secret=api_s)

                        if state==True:
                            st.success("Token Updated")
                            time.sleep(2)
                            st.experimental_rerun()
                        else:
                            st.error("Sorry,error to update token")
                            st.error(error)
                with add_tab:
                    st.subheader("Replace access token")
                    
                    add_token=st.text_input("Give Your Token",placeholder="Access Token")
                    if st.form_submit_button("Replace",use_container_width=True):
                        current_time=datetime.now()
                        table_name=dbm.tables["access_token_table"]
                        df=pd.DataFrame(data={'id':1,'api_key':api_k,'api_secret':api_s,'access_token':add_token,'createdate':current_time},index=[0])
                        df.to_sql(table_name,dbm.engine,if_exists="replace",index=False)
                        
                        _='''
                        dbm.update_access_token(access_token=add_token,api_key=api_k,api_secret=api_s)
                        '''
                        st.success("Updated")
                        st.session_state['tkn_df']=dbm.fetch_access_tokens(table_name=access_token_table)
                        st.experimental_rerun()

                st.subheader("Token Log")
                st.dataframe(st.session_state['tkn_df'],use_container_width=True)

with defaults:
    st.header("📌 Set Values")

with bnf_log:
    
    def read_ltp():
        return pd.read_csv("D:\Arkonet Project\Project-06\Code\stocks_algo_streamlit\stocks_algo_streamlit\st_dash\login\csv\ltp_data.csv")
    st.header("🔖 BNF LTP Log")
    bnf=read_ltp()
    bnf.columns=['Date','LTP Value']
    st.dataframe(show_df(bnf).sort_values(by='Date',ascending=False),use_container_width=True)

with tls_error:
    st.header("📑 TLS Error Log")

    tls_error_df=dbm.fetch_tables(table_name=error_log_table,index_col='id')
    tls_error_df.index=tls_error_df['id']
    st.dataframe(tls_error_df,use_container_width=True)
    
