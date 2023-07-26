# import zrd_login as zl
from zrd_login_sridharan import zrd_login 
from kiteconnect import KiteConnect
import os
from datetime import datetime, timedelta,date
import datetime as dt
import pandas as pd
import time
import sys
import pdb
import pytz
from sqlalchemy import create_engine,text
from datetime import datetime,date
import pandas as pd
from functions.get_data_func import fetchOHLCExtended,live_zone_time
from functions.db_conn import sqlalchemy_connect

sql=sqlalchemy_connect(username="chetan")

tables_dict=sql.read_config()
db_tables=tables_dict["db_tables"]
customer_tbl=db_tables["customer_table"]
candle_stick_tbl=db_tables["candle_stick_log_table"]
entry_conditions=db_tables["entry_conditions"]

today=datetime.today().strftime('%d-%m-%Y')

# cwd = os.chdir("C:\\PythonL")
ohlc_intraday = {}

# tickers list
tickers=['NIFTY BANK']
#tickers = ['NIFTY BANK', 'NIFTY 50']


# Logger
kite = zrd_login(connection_object=sql)

# Collect Live OHLC Values in dataframe
for i in tickers:

    start = time.time()
    
    #try:
    ohlc_intraday[i] = fetchOHLCExtended( kite,i,today, "30minute")
    #ohlc_intraday[i].to_csv(i + '.csv')
    df_ohlc_intraday=ohlc_intraday[i]
    print("first")
    print(df_ohlc_intraday)
    print(ohlc_intraday[i])


    ohlc_intraday[i].to_csv(i + '.csv')
    sql.upload_ohlc(df=df_ohlc_intraday)
    #except Exception as e:    
    #    print(e)
    
    end = time.time()
    print(end - start) #     <-----NOTE Hashed
    print(i,"done") #       <-----NOTE Hashed


#time_check = dt.time(9,47)
#time_check = dt.time(15,29)

# Live Zone time
now_aware=live_zone_time()

tickers_v=[]
tickers_check=[]

print("Checking baseline time now , is the latest candle equal or greater than this time ---> ", now_aware)

print("done")

# To collect continues updating data
while True:  
    time.sleep(5)
    # For every ticker
    for i in tickers:

        if len(tickers_v) == 1:
        # if len(tickers_v) == 2:
            break

        if os.path.isfile(i + '.csv'):

            df = pd.read_csv(i + '.csv')
            df['date'] = pd.to_datetime(df['date'])
            time_now = dt.datetime.now().time().replace(microsecond=0)
            # starttime = pd.to_datetime(df.iloc[-1]['date']).time() # https://stackoverflow.com/questions/49554491/not-supported-between-instances-of-datetime-date-and-str
            starttime = (df.iloc[-1]['date'])
            # validate = starttime >=time_check
            str1 = str(starttime)
            datetime_obj = dt.datetime.strptime(str1,"%Y-%m-%d %H:%M:%S+05:30")
            datetime_obj =  datetime_obj.replace(tzinfo=pytz.timezone(('Asia/Kolkata')))
            # datetime_obj > now_aware

            validate = datetime_obj >= now_aware # Validate Previous candle is formed
            # validate = datetime_obj <= now_aware # Validate Previous candle is formed # For TESTING ONLY ---> Remember to HASH this line
            # pdb.set_trace()
            
            print(validate)

            if validate:
                tickers_check=[i]
                tickers_v += tickers_check
                tickers_v = list(set(tickers_v)) # https://stackoverflow.com/questions/66952798/how-do-i-update-a-list-using-the-for-loop
                print(tickers_v)
                time.sleep(2)
                # if len(tickers_v) == 2:
                if len(tickers_v) == 1:
                    # sys.exit()
                    print("COMPLETED downloading both tickers --->", tickers_v)
                    # break                
            else:
                try:
                    ohlc_intraday[i] = fetchOHLCExtended( kite,i,today, "30minute")
                    print(ohlc_intraday[i])
                    ohlc_intraday[i].to_csv(i + '.csv')
                    sql.upload_ohlc(df=df_ohlc_intraday)
                    print(time_now)
                    print("downloaded the get_data file for ticker again--->" , i)
                    print("\n")
                    print("latest candle 1 min downloaded time stamp is ----> ", datetime_obj)
                    print("Validate , is the latest candle time stamp equal or greater than this time ---> ", now_aware)
                    time.sleep(2)
                except Exception as e:
                    print(e)
    if len(tickers_v) == 1:
        break



