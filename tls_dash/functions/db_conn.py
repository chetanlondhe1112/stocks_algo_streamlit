from datetime import datetime,date
from sqlalchemy import create_engine,text
import time
import tomlkit
import pandas as pd
import os

config_file_path="config/tls_config.toml"

class sqlalchemy_connect:

    def __init__(self,username):
        self.user=username
        self.file_path=config_file_path
        self.config=self.read_config()
        self.cred=self.config['db_server']
        self.tables=self.config['db_tables']
        self.engine=self.engine()
       
    def now_time(self):
      curr_time = datetime.now()
      return str(curr_time).split(".")[0]


    def read_config(self):

        #print(str(self.now_time())+" = Reading Configuration File....")
        try:
          with open(self.file_path, mode="rt", encoding="utf-8") as fp:
              config=dict(tomlkit.load(fp))
              #print(str(self.now_time())+" = File Read: Success :)")
              #self.config_info(config)
              return config
        except Exception as e:
          print(str(self.now_time())+" = File Read: Failed :(")
          time.sleep(2)
          print(e)

    def read_tables(self):
        return self.tables


    def config_info(self,config=dict):
        #print(str(self.now_time())+" = Collecting File Information...")
        time.sleep(1)
        print("="*50)
        time.sleep(1)
        print("Name: "+str(config['file_info']['file_name']))
        print("Info: "+str(config['file_info']['info']))
        print("Version: "+str(config['file_info']['version']))
        time.sleep(1)
        print("*"*22+"Auther"+"*"*22)
        print("Auther Name: "+str(config['auther']['name']))
        print("Auther Mail: "+str(config['auther']['mail']))
        print("="*50)
        time.sleep(2)


    def sqlalchemy_connection(self,credential_dict=dict):
        """
        function to establish the sqlalchemy connection to the database
        -Argument passed to function should be the dictionary of database configuration
        """
        user=credential_dict["user"]
        password=credential_dict["password"]
        host=credential_dict["host"]
        port=credential_dict["port"]
        database=credential_dict["database"]
        status_str=" = Connection Object Build :"

        #print(str(self.now_time())+" = Generating Connection Object...")
        time.sleep(2)
        try:
            engine=create_engine("mysql://{}:{}@{}:{}/{}".format(user,password,host,port,database))
            #print(str(self.now_time())+status_str+"Success")
            print(str(self.now_time())+" = Connection Object :"+str(engine))
            time.sleep(2)
            return engine
        except Exception as e:
            print(str(self.now_time())+status_str+"Failed")
            print(str(self.now_time())+" = Error : "+str(e))
            return ''

    def engine(self):
        """
          Function to create the connection with database
        """
        return self.sqlalchemy_connection(self.cred)

    def fetch_tables(self,table_name=str):
        """
            Function to fetch all the data from table
        """
        try:
            df=pd.read_sql_table(table_name,self.engine)
            return df
        except Exception as e:
            print(e)

    def fetch_table_u(self,table_name=str):
        """
            Retrives the tables data w.r.t user
        """
        s="SELECT * FROM `"+table_name+"` WHERE username='"+str(self.user)+"'"
        try:
            df=pd.read_sql_query(s,self.engine)
            return df
        except Exception as e:
            print(e)

    def upload_to_table(self,df=pd.DataFrame(),table_name=str,if_exists=str):
        """
            Uploads dataframe to table
        """
        try:
            df.to_sql(table_name,con=self.engine,if_exists=if_exists,index=0)
            return True
        except Exception as e:
            print(e)

    def ohlc_validation(self):
        """
            Validationn ffor getdata.py code to  upload ohlc value
        """
        candle_stick_tbl=self.tables["candle_stick_log_table"]
        last_date=self.fetch_tables(table_name=candle_stick_tbl)['date']
        
    def fetch_access_tokens(self):
        """
            To fetch all access tokens
        """
        table_name=self.tables["access_token_table"]
        connection=self.engine
        query_names_q='SELECT id,api_key,api_secret,access_token,createdate FROM `'+ table_name+'`'
        query_names_df=pd.read_sql_query(query_names_q,connection,index_col=['id']).drop_duplicates().dropna(axis=1,how='all')
        if len(query_names_df):
            query_names_df=query_names_df.sort_values(by='createdate',ascending=False,ignore_index=True)
            return query_names_df
        else:
            return pd.DataFrame()
        
    def fetch_query(self,query=str):
        try:
            return pd.read_sql_query(sql=query,con=self.engine)
        except Exception as e:
            print(e)
            return 0
            
    def upload_ohlc(self,df):

        """
            Validationn ffor getdata.py code to  upload ohlc value
        """
        candle_stick_tbl=self.tables["candle_stick_log_table"]
        #last_date=self.fetch_tables(table_name=candle_stick_tbl).iloc[-1]['date'].to_datetime64()
        today=date.today()
        try:
            #print(type(str(last_date).split("T")[0]),type(last_date))
            oq='SELECT date FROM `'+ candle_stick_tbl+'` WHERE DATE(date)="'+str(today)+'"'
            old_rows=len(self.fetch_query(oq))
            if old_rows<18:
                print("removing Old record : {}rows".format(old_rows))
                dq='DELETE FROM `'+ candle_stick_tbl+'` WHERE DATE(date)="'+str(today)+'"'
                self.engine.execute(text(dq))
                print("uploading new OHLC")
                self.upload_to_table(df, table_name=candle_stick_tbl, if_exists='append')
            else:
                print("Todays Ohlc collected")
                return 1
        except Exception as e:
            print(e)
        
    def upload_entry_conditions(self,df):
        today=date.today()
        entry_conditions=self.tables["entry_conditions"]

        oq='SELECT `Start Date` FROM `'+ entry_conditions+'` WHERE DATE(`Start Date`)="'+str(today)+'"'
        print(oq)
        old_rows=len(self.fetch_query(oq))
        print("removing Old Entry : {}rows".format(old_rows))
        dq='DELETE FROM `'+ entry_conditions+'` WHERE DATE(`Start Date`)="'+str(today)+'"'
        self.engine.execute(text(dq))
        print("uploading new Entry")
        self.upload_to_table(df, table_name=entry_conditions, if_exists='append')
        
            #status=.upload_to_table(df=df_pairs_up,table_name=entry_conditions,if_exists="append")

        