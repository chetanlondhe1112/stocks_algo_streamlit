import warnings
#pip install smartapi-python
from SmartApi.smartConnect import SmartConnect
import pdb
import requests
import pandas as pd
import datetime
import time
import mibian
import pyotp
import sys
from datetime import datetime,date
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
    


sql=sqlalchemy_connect(username="chetan",config_file_path="tls_config.toml")
#print(sql)
tables_dict=sql.read_config()
db_tables=tables_dict["db_tables"]
customer_tbl=db_tables["customer_table"]
candle_stick_tbl=db_tables["candle_stick_log_table"]
entry_conditions=db_tables["entry_conditions"]

# functions

def angelbrok_login(api_key,angel_user,angel_pwd,totp_key):   
	try:
                
		global feed_token, client_code, obj, obj3, obj4, obj5, obj6, obj7, obj8, obj9, obj10, obj11, obj12, obj13, obj14, obj16, obj17, obj20, obj21, obj22, obj23, password, refreshToken, accessToken, data
		
		countt = 0
		countt = countt+1

		apikey = api_key
		username = angel_user
		#pwd = 'KnsAng@12#'
		pwd = angel_pwd
		kiteSetupKeyForTOTP = totp_key
		totp = pyotp.TOTP(kiteSetupKeyForTOTP)
		totp = totp.now()
		obj=SmartConnect(api_key=apikey) # Sridharan
		data = obj.generateSession(username,pwd,totp)
		refreshToken= data['data']['refreshToken']
		#fetch the feedtoken
		feedToken=obj.getfeedToken()
		#fetch User Profile
		userProfile= obj.getProfile(refreshToken)
    	
		return totp, obj 
       	
	except Exception as e:
        
	    print("Error in login", e)
        


# defaults
countt = 0
apikey = 'DodjVpCE' # Sridharan knsridharan@winrich.in
kiteSetupKeyForTOTP = 'ZT4OKWGC3TXIRPRZJLDKX3IBCM'


#customer all data
all_cust={}

def customer_data():
	customer_table_df=sql.fetch_tables(table_name=customer_tbl)[["name","angel_user","angel_pwd"]]
	
	for i in range(len(customer_table_df)):
		cus_df=customer_table_df.iloc[i].to_dict()
		all_cust[cus_df['name']]=cus_df
                
	return all_cust

all_cust=customer_data()
print(all_cust)
for i in all_cust:
	username = all_cust[i]['angel_user']
	pwd = all_cust[i]["angel_pwd"]
	print(username,pwd)
	try:
		totp,obj=angelbrok_login(apikey,angel_user=username,angel_pwd=pwd,totp_key=kiteSetupKeyForTOTP)
		print(totp,obj)
		all_cust[i]["totp"]=int(totp)
		all_cust[i]["obj"]=obj
	except Exception as e:
		print(e)
		continue

print(all_cust)

        

#username = 'k31094'
#pwd = 'KnsAng@12#'
#pwd = '1985'
#kiteSetupKeyForTOTP = 'ZT4OKWGC3TXIRPRZJLDKX3IBCM'




#pdb.set_trace()

valid_acc={}
for i in all_cust:
    if "obj" in all_cust[i].keys():
         valid_acc[all_cust[i]['name']]=all_cust[i] 
print("valid acc\n",valid_acc)
obj_list =[] 
#obj_dict2={}
obj_dict ={}

for i in valid_acc:
     obj_list.append(valid_acc[i]['obj'])
     obj_dict[obj]=valid_acc[i]['name']
print("objlist\n",obj_list)
print("obj dict\n",obj_dict)


# Entry conditions read
#data1 = pd.read_csv('Entry_conditions.csv', index_col=0)
data1=sql.fetch_tables(entry_conditions)

expiry = date(2023, 6, 29) # For Future


# Token Genearation
url = 'https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json'
d = requests.get(url).json()
token_df = pd.DataFrame.from_dict(d)
token_df['expiry'] = pd.to_datetime(token_df['expiry']).apply(lambda x: x.date())
token_df = token_df.astype({'strike': float})
# token_df
token_df1= token_df[(token_df['name'] == 'BANKNIFTY') & (token_df['instrumenttype'] == 'OPTIDX') & (token_df['expiry']==expiry) ]


def getTokenInfo (symbol, exch_seg ='NSE',instrumenttype='OPTIDX',strike_price = '',pe_ce = '',expiry_day = None):
	# pass
	df = token_df
	strike_price = strike_price*100
	if exch_seg == 'NSE':
		eq_df = df[(df['exch_seg'] == 'NSE') ]
		return eq_df[eq_df['name'] == symbol]
	elif exch_seg == 'NFO' and ((instrumenttype == 'FUTSTK') or (instrumenttype == 'FUTIDX')):
		return df[(df['exch_seg'] == 'NFO') & (df['instrumenttype'] == instrumenttype) & (df['name'] == symbol)].sort_values(by=['expiry'])
	elif exch_seg == 'NFO' and (instrumenttype == 'OPTSTK' or instrumenttype == 'OPTIDX'):
		return df[(df['exch_seg'] == 'NFO') & (df['expiry']==expiry_day) &  (df['instrumenttype'] == instrumenttype) & (df['name'] == symbol) & (df['strike'] == strike_price) & (df['symbol'].str.endswith(pe_ce))].sort_values(by=['expiry'])


# token1 = getTokenInfo ('BANKNIFTY', 'NFO','FUTIDX','','',expiry_day = None).iloc[0] # For Future
token1 = getTokenInfo ('BANKNIFTY', 'NSE','','','',expiry_day = None).iloc[0] # For Index
symbol = token1['symbol']
token = token1['token']
lot = token1['lotsize']

print("check obj")
#time_15_15 = datetime.time(15,15)
#pdb.set_trace()
data1['Start Date']=pd.to_datetime(data1['Start Date'])
while True:
	today = date.today()
	obj=obj_list[0]
	#for obj in obj_list:
	if  data1.iloc[-1]['Start Date'].date()==today:
		bnf_ltp = obj.ltpData("NSE", "BANKNIFTY", "26009")['data']['ltp']
		#bnf_ltp=44262
		print(bnf_ltp)
		time.sleep(1)
		if bnf_ltp>data1.iloc[-1]['Entry Above High']:
			print("buying BANKNIFTY")
			print(data1.iloc[-1]['Entry Above High'])
			stop_loss_buy=data1.iloc[-1]['Stop Loss Above Entry']
			target_buy=data1.iloc[-1]['Target Profit Above Entry']
			choice='1'
			break
		if bnf_ltp<data1.iloc[-1]['Entry Below Low']:
			print("selling BANKNIFTY")
			print(data1.iloc[-1]['Entry Below Low'])
			stop_loss_sell=data1.iloc[-1]['Stop Loss Below Entry']
			target_sell=data1.iloc[-1]['Target Profit Below Entry']
			choice='2'
			break
	else:
		break


try:
    historicParam={
    "exchange": "NSE",
    "symboltoken": "3045",
    "interval": "ONE_MINUTE",
    "fromdate": "2023-01-23 09:00", 
    "todate": "2023-01-27 15:29"
    }
    dat = obj.getCandleData(historicParam)
except Exception as e:
    print("Historic Api failed: {}".format(e.message))

new = pd.DataFrame.from_dict(dat['data'])

def get_instruments():
	global instrument_df
	url = 'https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json'
	request = requests.get(url=url, verify=False)
	data = request.json()
	instrument_df = pd.DataFrame(data)
	instrument_df.to_csv("instruments.csv")
	instrument_df.set_index("symbol", inplace=True)
	return instrument_df

def get_ohlc(name, exchange): # get_ohlc('BANKBEES-EQ',"NSE") # get_ohlc('BANKNIFTY24NOV2238000PE',"NFO") ,  get_ohlc('BANKNIFTY',"NSE")
	symboltoken = instrument_df.loc[name]['token']
	ohlc_data = obj.ltpData(exchange, name, symboltoken)
	ohlc_data = ohlc_data['data']
	return ohlc_data


def make_straddle(name, exipry, gap): #  make_straddle('BANKNIFTY', '25JAN23', 100)
	ltpd = obj.ltpData("NSE", "BANKNIFTY", "26009")['data']['ltp']
	atm_strike = round(ltpd/gap)*gap
	call_name = name + exipry + str(atm_strike) + 'CE'
	put_name = name + exipry + str(atm_strike) + 'PE'
	return [call_name, put_name,ltpd]
	
xval = make_straddle('BANKNIFTY', '29MAR23', 100)

instrument_df = get_instruments()

def get_token_and_exchange(name): # get_token_and_exchange('BANKNIFTY27OCT22FUT') # token, exchange = get_token_and_exchange('BANKNIFTY27OCT22FUT')
	symboltoken = instrument_df.loc[name]['token']
	exchange = instrument_df.loc[name]['exch_seg']
	return symboltoken, exchange
# pdb.set_trace()


for name in obj_list:
	
	try:
		Trade_net = name.position()['data'] # Angel Trade Net Positions
		nobj = obj_dict[name]
		Trade_df=pd.DataFrame(Trade_net)
		Angel_net_df = Trade_df[Trade_df['symbolname']=='BANKNIFTY']
		Angel_net_df.to_csv("Angel_net_positions_" + obj_dict[name]+".csv")
		print("angel trade\n")
		print(Angel_net_df)
	except Exception as e:
		print(obj_dict[name], " ---> Order net positions subset csv file creation failed for :  ", nobj)
		print("\n")


# pdb.set_trace()
"""
def angel_place_order(transaction_type, tsymbol, ttoken): # Change Product type to MIS ----> INTRADAY (from ---> CARRYFORWARD )
	global orderparams
	
	orderparams = {"variety": "NORMAL", "tradingsymbol": tsymbol, "symboltoken": ttoken, "transactiontype": transaction_type, 
	"exchange": exch_seg, "ordertype": "MARKET", "producttype": "CARRYFORWARD", "duration": "DAY", "price": "0", "squareoff": "0", 
	"stoploss": "0", "quantity": fin_q }
 
		
	
	# pdb.set_trace()
	for name in obj_list:
		try:					
												
			orderId=name.placeOrder(orderparams)
			print(obj_dict[name])
			print(tsymbol, " The order id is: {}".format(orderId))
			time_now = datetime.datetime.now().time().replace(microsecond=0)
			trade_dict_11 = {"time": time_now}
			print(trade_dict_11)
			print(time_now)
			print("\n")
						

		except Exception as e:			
			print("\n")
			print(obj_dict[name], " ---> Order placement subset failed: for ", tsymbol)
			time_now = datetime.datetime.now().time().replace(microsecond=0)
			order_fail={"time":time_now, "name":obj_dict[name], "symbol":tsymbol}
			print(time_now)
			print("\n")



# pdb.set_trace()
exch_seg = "NFO"
fin_quantity = 25
# fin_quantity = 125
fin_q = str(fin_quantity)

df_log = pd.read_csv('angel_trade_log_list.csv') # Take the source fike for Strikes symbol  and Token selected
CE_Symbol = df_log.iloc[0]['CE_Symbol']
CE_Token = str(df_log.iloc[0]['CE_Token'])

PE_Symbol = df_log.iloc[0]['PE_Symbol']
PE_Token = str(df_log.iloc[0]['PE_Token'])

#pdb.set_trace()
while True:	
	print("\n")
	# pdb.set_trace()
	print(CE_Symbol, " , ",  PE_Symbol)
	#val = input("Enter your trade action value (1)Buy Call , (2)Buy Put,  (3)Sell Call , (4)Sell Put , (5) EXIT loop : ----> ")
	print("Enter your trade action value (1)Buy Call , (2)Buy Put,  (3)Sell Call , (4)Sell Put , (5) EXIT loop : ----> ")
	val=choice
	
	print("You have chosen ---> ", val)
	print("\n")
	# pdb.set_trace()

	if val == "1":	
		# transaction_type = "BUY"
		print('Buying CALL ----> ')
		# pdb.set_trace()
		#angel_place_order("BUY", CE_Symbol, CE_Token)
		break
	elif val == "2":	
		# transaction_type = "BUY"
		print('Buying PUT ----> ')
		#angel_place_order("BUY", PE_Symbol, PE_Token)
		break
	elif val == "3":	
		# transaction_type = "SELL"
		print('Selling CALL ----> ')
		#angel_place_order("SELL", CE_Symbol, CE_Token)
		break
	elif val == "4":	
		# transaction_type = "SELL"
		print('Selling PUT ----> ')
		#angel_place_order("SELL", PE_Symbol, PE_Token)
		break
	elif val == "1" or val == "2" or val == "3" or val == "4":
		print("\n")
		print("exiting Loop")
		break
		#break	
	else:
		print("\n")
		print("Wrong Entry  ---> Please retry ")
		# break
		# pdb.set_trace()


while True:
	bnf_ltp = obj.ltpData("NSE", "BANKNIFTY", "26009")['data']['ltp']
	#bnf_ltp=44263
	print("bnf_ltp"+str(bnf_ltp))
	time.sleep(1)
	#check if current time is 12:15 and no position has been entered, then sys exit
	#check whether the time is 44:30 sec or time is 14:30 sec, delete nifty bank csv and then invoke tls17

	if choice=='1':
		time_now = datetime.datetime.now().time().replace(microsecond=0)
		print(time_now)
		print("\n")
		print("Choice is --> ",choice)
		print("stop loss =",stop_loss_buy)
		print("Target Profit =",target_buy)
		current_value=bnf_ltp>target_buy
		current_stop=bnf_ltp<stop_loss_buy
		EOD=time_now>time_15_15
		print("BANKNIFTY LTP is hitting profit-------> ", current_value)
		print("BANKNIFTY LTP is hitting loss-------> ", current_stop)
		if current_value:
			print("Profit Reached")
			print('Selling CALL ----> ')
			#angel_place_order("SELL", CE_Symbol, CE_Token)
			break
		if current_stop:
			print("Stop Loss Reached")
			print('Selling CALL ----> ')
			#angel_place_order("SELL", CE_Symbol, CE_Token)
			break
		if EOD:
			print("EOD Reached")
			#angel_place_order("SELL", CE_Symbol, CE_Token)
			break
	if choice=='2':
		time_now = datetime.datetime.now().time().replace(microsecond=0)
		print(time_now)
		print("\n")
		print("Choice is --> ",choice)
		print("stop loss =",stop_loss_sell)
		print("Target Profit =",target_sell)
		current_value=bnf_ltp<target_sell
		current_stop=bnf_ltp>stop_loss_sell
		EOD=time_now>time_15_15
		print("BANKNIFTY LTP is hitting profit-------> ", current_value)
		print("BANKNIFTY LTP is hitting loss-------> ", current_stop)	
		if current_value:
			print("Profit Reached")
			print('Selling PUT ----> ')
			#angel_place_order("SELL", PE_Symbol, PE_Token)
			break
		if current_stop:
			print("Stop Loss Reached")
			print('Selling PUT ----> ')
			#angel_place_order("SELL", PE_Symbol, PE_Token)
			break
		if EOD:
			print("EOD Reached")
			#angel_place_order("SELL", PE_Symbol, PE_Token)
			break
sys.exit()



"""
