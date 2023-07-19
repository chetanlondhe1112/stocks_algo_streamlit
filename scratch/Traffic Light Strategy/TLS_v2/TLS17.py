import pandas as pd
import pdb
import datetime
import os
import sys
import time

from datetime import datetime,date
# Read in the data
from sqlalchemy import create_engine,text
import time
import tomlkit
#import streamlit as st

class sqlalchemy_connect:

    def __init__(self,username,config_file_path=str):
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
        df=pd.read_sql_table(table_name,self.engine)
        return df

    def fetch_user_table(self,table_name=str):
        s="SELECT * FROM `"+table_name+"` WHERE username='"+str(self.user)+"'"
        df=pd.read_sql_query(s,self.engine)
        return df
    
    def upload_to_table(self,df=pd.DataFrame(),table_name=str):
        try:
            df.to_sql(table_name,con=self.engine,if_exists="replace",index=0)
            return True
        except Exception as e:
            print(e)

sql=sqlalchemy_connect(username="chetan",config_file_path="tls_config.toml")
#print(sql)
tables_dict=sql.read_config()
db_tables=tables_dict["db_tables"]
customer_tbl=db_tables["customer_table"]
candle_stick_tbl=db_tables["candle_stick_log_table"]
entry_conditions=db_tables["entry_conditions"]


candle_data=sql.fetch_tables(candle_stick_tbl)
candle_data.index=candle_data["date"]
print(candle_data)

while True:
        #data = pd.read_csv('NIFTY BANK.csv', index_col=0)
    if len(candle_data):
        data = candle_data.iloc[:-1 , :]
            
    else:
        os.system('get_data.py')
        candle_data=sql.fetch_tables(candle_stick_tbl)
        candle_data.index=candle_data["date"]
        data = candle_data.iloc[:-1 , :]

    # pdb.set_trace() 
    # Remove rows corresponding to the opening minute of trading day
    print(data)
    print(data.to_csv("datav1.csv"))
    data = data.loc[~data.index.contains('09:15:00')]
    print(data.to_csv("datav2.csv"))



    # Create a new column that indicates whether each candlestick is red or green
    data['Color'] = 'Green'
    data.loc[data['close'] < data['open'], 'Color'] = 'Red'

    # Find pairs of red and green candlesticks
    pairs = []
    for i in range(1, len(data)):
        if data['Color'][i] == 'Green' and data['Color'][i-1] == 'Red':
            prev_time = pd.to_datetime(data.index[i-1])
            if prev_time.strftime('%H:%M') != '15:15' and prev_time.strftime('%H:%M') != '14:45':
                pairs.append((data.index[i-1],data.index[i]))
        elif data['Color'][i] == 'Red' and data['Color'][i-1] == 'Green':
            prev_time = pd.to_datetime(data.index[i-1])
            if prev_time.strftime('%H:%M') != '15:15' and prev_time.strftime('%H:%M') != '14:45':
                pairs.append((data.index[i-1], data.index[i]))

    # Store pairs in a DataFrame
    df_pairs = pd.DataFrame(pairs, columns=['Start Date', 'End Date'])
    df_pairs.to_csv("df_pairsv1.csv")
    print(df_pairs)
    
    # Calculate entry, stop loss, and target profit levels for each pair
    print(data)
    for i in range(len(df_pairs)):
        high = max(data.loc[df_pairs['Start Date'][i]:df_pairs['End Date'][i], 'high'])
        print(high)
        low = min(data.loc[df_pairs['Start Date'][i]:df_pairs['End Date'][i], 'low'])
        print(low)
        entry_above_high = high 
        entry_below_low = low 
        # stop_loss_above_entry = entry_above_high - 30
        # stop_loss_below_entry = entry_below_low + 30
        # stop_loss_above_entry = entry_above_high - 55
        # stop_loss_below_entry = entry_below_low + 55
        stop_loss_above_entry = entry_below_low 
        stop_loss_below_entry = entry_above_high
        df_pairs.loc[i, 'High'] = high
        df_pairs.loc[i, 'Low'] = low
        df_pairs.loc[i, 'Entry Above High'] = entry_above_high
        df_pairs.loc[i, 'Entry Below Low'] = entry_below_low
        # df_pairs.loc[i, 'Stop Loss Above Entry'] = stop_loss_above_entry
        # df_pairs.loc[i, 'Stop Loss Below Entry'] = stop_loss_below_entry
        df_pairs.loc[i, 'Stop Loss Above Entry'] = stop_loss_above_entry
        df_pairs.loc[i, 'Stop Loss Below Entry'] = stop_loss_below_entry
        
        target_diff=(high-low)
        target_profit=target_diff*1.5
        target_profit_above_entry = entry_above_high + target_profit
        target_profit_below_entry = entry_below_low - target_profit
        # target_profit_above_entry = entry_above_high + 140
        # target_profit_below_entry = entry_below_low - 140
        df_pairs.loc[i, 'Target Profit Above Entry'] = target_profit_above_entry
        df_pairs.loc[i, 'Target Profit Below Entry'] = target_profit_below_entry
        print(df_pairs.to_csv("df_pairsv2  .csv"))
        
        #pdb.set_trace()
    # Initialize the date as the start date of the data
    ref_date = data.index[0]
   
    for i in range(len(df_pairs)-1):
        # Check if the pair's start date is after the reference date
        if df_pairs['Start Date'][i] >= ref_date :

            # Get the index of the next candlestick after the pair's end date
            next_candle_index = data.index.get_loc(df_pairs['End Date'][i]) + 1 
        
            # Get the candlestick data for the next candlestick
            next_candle = data.iloc[next_candle_index]
            
            # Check if the next candlestick's high or low crosses the entry level
            if next_candle['high'] >= df_pairs['Entry Above High'][i] and (pd.to_datetime(next_candle.name).time()<pd.to_datetime(['12:00:00']).time):
                print(f"Pair {i}:Trade executed at entry level on date: ", pd.to_datetime(next_candle.name), " at price: ", df_pairs['Entry Above High'][i])
                df_pairs.loc[i, 'Entry Date'] = next_candle.name 
                df_pairs.loc[i, 'Position'] = 'Long'
                df_pairs.loc[i,'Entry_value']= df_pairs['Entry Above High'][i]
                # Check if the stop loss or target levels are hit
                # Check if the stop loss or target levels are hit
                for j in range(next_candle_index, len(data)): 
                    # Get the candlestick data for the next candlestick
                    next_candle = data.iloc[j]
                
                # Check if the next candlestick's high or low crosses the stop loss or target levels
                    if next_candle['low'] <= df_pairs['Stop Loss Above Entry'][i]:
                        # Execute the trade at the stop loss level
                        print(f"Pair {i}:Trade executed at stop loss level on date: ", pd.to_datetime(next_candle.name), " at price: ", df_pairs['Stop Loss Above Entry'][i])
                        df_pairs.loc[i, 'Exit Date'] = next_candle.name
                        df_pairs.loc[i, 'Result'] = 'Stop Loss'
                        df_pairs.loc[i, 'Profit/Loss'] = df_pairs['Stop Loss Above Entry'][i] - df_pairs['Entry Above High'][i]
                        #df_pairs.loc[i, 'Profit/Loss'] = -60 
                        #pdb.set_trace()
                        df_pairs.loc[i,'stop loss value']=df_pairs['Stop Loss Above Entry'][i]
                        break

                    elif next_candle['high'] >= df_pairs['Target Profit Above Entry'][i]:
                        # Execute the trade at the target profit level
                        print(f"Pair {i}:Trade executed at target profit level on date: ", pd.to_datetime(next_candle.name), " at price: ", df_pairs['Target Profit Above Entry'][i])
                        df_pairs.loc[i, 'Exit Date'] = next_candle.name
                        df_pairs.loc[i, 'Result'] = 'Target Profit'
                        df_pairs.loc[i, 'Profit/Loss'] =df_pairs['Target Profit Above Entry'][i] - df_pairs['Entry Above High'][i]
                        df_pairs.loc[i,'Target Profit value']= df_pairs['Target Profit Above Entry'][i]
                        break
                    elif pd.to_datetime(next_candle.name).time()==pd.to_datetime(['15:15:00']).time:
                        # Execute the trade at the target profit level
                        print(f"Pair {i}:Trade executed at target profit_Loss level on date: ", pd.to_datetime(next_candle.name), " at price: ", next_candle['close'])
                        df_pairs.loc[i, 'Exit Date'] = next_candle.name
                        df_pairs.loc[i, 'Result'] = 'Target Profit_loss'
                        target_profit_below_entry1= next_candle['close']
                        df_pairs.loc[i, 'Profit/Loss'] = df_pairs['Entry Above High'][i] - target_profit_below_entry1
                        df_pairs.loc[i,'Target Profit value']= target_profit_below_entry1
                        # df_pairs.loc[i, 'Profit/Loss'] = 0
                        # df_pairs.loc[i,'Target Profit value']= 0
                        #pdb.set_trace()
                        break
                # else:
                #     # Execute the trade at the entry level
                #     print(f"Pair {i}:Trade executed at entry level on date: ", pd.to_datetime(next_candle.name), " at price: ", df_pairs['Entry Above High'][i])
            elif next_candle['low'] <= df_pairs['Entry Below Low'][i] and (pd.to_datetime(next_candle.name).time()<pd.to_datetime(['12:00:00']).time):
                print(f"Pair {i}:Trade executed at entry level on date: ", pd.to_datetime(next_candle.name), " at price: ", df_pairs['Entry Below Low'][i])
                df_pairs.loc[i, 'Entry Date'] = next_candle.name
                df_pairs.loc[i, 'Position'] = 'short'
                df_pairs.loc[i,'Entry_value']= df_pairs['Entry Below Low'][i]
                # Check if the stop loss or target levels are hit
                for j in range(next_candle_index, len(data)): 
                    # Get the candlestick data for the next candlestick
                    next_candle = data.iloc[j]
                    
                    
                    # Check if the next candlestick's high or low crosses the stop loss or target levels
                    if next_candle['high'] >= df_pairs['Stop Loss Below Entry'][i]:
                        # Execute the trade at the stop loss level
                        print(f"Pair {i}:Trade executed at stop loss level on date: ", pd.to_datetime(next_candle.name), " at price: ", df_pairs['Stop Loss Below Entry'][i])
                        df_pairs.loc[i, 'Exit Date'] = next_candle.name
                        df_pairs.loc[i, 'Result'] = 'Stop Loss'
                        df_pairs.loc[i, 'Profit/Loss'] = df_pairs['Entry Below Low'][i] -  df_pairs['Stop Loss Below Entry'][i]
                        #df_pairs.loc[i, 'Profit/Loss'] = -60
                        df_pairs.loc[i,'stop loss value']=  df_pairs['Stop Loss Below Entry'][i]
                        break
                    elif next_candle['low'] <= df_pairs['Target Profit Below Entry'][i]:
                        # Execute the trade at the target profit level
                        print(f"Pair {i}:Trade executed at target profit level on date: ", pd.to_datetime(next_candle.name), " at price: ", df_pairs['Target Profit Below Entry'][i])
                        df_pairs.loc[i, 'Exit Date'] = next_candle.name
                        df_pairs.loc[i, 'Result'] = 'Target Profit'
                        df_pairs.loc[i, 'Profit/Loss'] =df_pairs['Entry Below Low'][i] - df_pairs['Target Profit Below Entry'][i]
                        df_pairs.loc[i,'Target Profit value']= df_pairs['Target Profit Below Entry'][i]
                        break
                    elif pd.to_datetime(next_candle.name).time()==pd.to_datetime(['15:15:00']).time:
                        # Execute the trade at the target profit level
                        print(f"Pair {i}:Trade executed at target profit_Loss level on date: ", pd.to_datetime(next_candle.name), " at price: ", next_candle['close'])
                        df_pairs.loc[i, 'Exit Date'] = next_candle.name
                        df_pairs.loc[i, 'Result'] = 'Target Profit_loss'
                        target_profit_below_entry2= next_candle['close']
                        df_pairs.loc[i, 'Profit/Loss'] = df_pairs['Entry Below Low'][i] - target_profit_below_entry2
                        df_pairs.loc[i,'Target Profit value']= target_profit_below_entry2
                        # df_pairs.loc[i, 'Profit/Loss'] = 0
                        # df_pairs.loc[i,'Target Profit value']= 0
                        #pdb.set_trace()
                        break


                # else:
                #     # Execute the trade at the entry level
                #     print(f"Pair {i}:Trade executed at entry level on date: ", pd.to_datetime(next_candle.name), " at price: ", df_pairs['Entry Below Low'][i])
            else:
                # No trade executed
                print("No trade executed")
            
            # Update the reference date to the exit date of the current pair
            ref_date = next_candle.name


    print(df_pairs)
    #df_pairs.to_csv('new3.csv')
    df_pairs.to_csv('new3.csv')

    df_pairs.tail(2).to_csv('Entry_conditions.csv')
    
    #df_pairs = pd.read_csv('new3.csv', index_col=0)
    df_pairs_up=df_pairs.tail(2)
    df_pairs_up.insert(0,"tradingstreategy",1)
    status=sql.upload_to_table(df=df_pairs_up,table_name=entry_conditions)
    print(status)

    # = pd.read_csv('Entry_conditions.csv', index_col=0)


    #data1 = pd.read_csv('Entry_conditions.csv', index_col=0)
    data1=df_pairs_up
    # pdb.set_trace()
    today = date.today()
    data1['Start Date']=pd.to_datetime(data1['Start Date'])
    if data1.iloc[-1]['Start Date'].date()==today:
        print("I am going to run the execution code")
        time.sleep(5)
        #import angel_session_test_Sridharan.py
    #pdb.set_trace()
    else:
    
        # delete nifty bank csv , 
        os.system('get_data.py')
        #check gap is 5 mins
        #if gap is not 5mins, again get_data

        #pdb.set_trace()
        time.sleep(5)
