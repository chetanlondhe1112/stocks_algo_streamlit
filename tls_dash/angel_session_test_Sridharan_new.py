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
from functions.db_conn import sqlalchemy_connect
import datetime as dt



# Database Connection 
sql=sqlalchemy_connect(username="chetan")

tables_dict=sql.read_config()

db_tables=tables_dict["db_tables"]
customer_tbl=db_tables["customer_table"]
candle_stick_tbl=db_tables["candle_stick_log_table"]
entry_conditions=db_tables["entry_conditions"]
order_log_table=db_tables["order_log_table"]
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
        
def customer_data():
	all_cust={}
	customer_table_df=sql.fetch_tables(table_name=customer_tbl)[["name","angel_user","angel_pwd"]]
	
	for i in range(len(customer_table_df)):
		cus_df=customer_table_df.iloc[i].to_dict()
		all_cust[cus_df['name']]=cus_df
    
	print("\n All customers data\n",all_cust)  
	return all_cust

def get_obj(customer_dict=dict):

	for i in customer_dict:
		username = customer_dict[i]['angel_user']
		pwd = customer_dict[i]["angel_pwd"]
		print(username,pwd)
		try:
			totp,obj=angelbrok_login(apikey,angel_user=username,angel_pwd=pwd,totp_key=kiteSetupKeyForTOTP)
			print(totp,obj)
			customer_dict[i]["totp"]=int(totp)
			customer_dict[i]["obj"]=obj
			
		except Exception as e:
			all_cust[i]["obj"]=str(username+'_noobj')
			print(e)
			continue
	
	print("\nCustomer dictionary with object and totp\n",customer_dict)
	return customer_dict

def getTokenInfo (token_df,symbol, exch_seg ='NSE', instrumenttype='OPTIDX',strike_price = '',pe_ce = '',expiry_day = None):
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

def historic_data(object):
	try:
		historicParam={
		"exchange": "NSE",
		"symboltoken": "3045",
		"interval": "ONE_MINUTE",
		"fromdate": "2023-01-23 09:00", 
		"todate": "2023-01-27 15:29"
		}
		dat = obj.getCandleData(historicParam)
		print("\nHistoric data\n",dat)
		return dat
	except Exception as e:
		print("Historic Api failed: {}".format(e.message))
		return 0

def get_key(val):
	for key,value in obj_dict.items():
		if str(val)==str(value):
			return key
		

def obj_ls_di(cus_obj_dict=dict):
	obj_list =[] 
	obj_dict ={}
	for i in all_cust:
		obj_list.append(all_cust[i]['obj'])
		obj_dict[all_cust[i]['name']]=all_cust[i]['obj']
	print("\nobjlist\n",obj_list)
	print("\nobj dict\n",obj_dict)
	return obj_list,obj_dict

# Token Genearation
def token_generation():
	url = 'https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json'
	d = requests.get(url).json()
	token_df = pd.DataFrame.from_dict(d)
	token_df['expiry'] = pd.to_datetime(token_df['expiry']).apply(lambda x: x.date())
	token_df = token_df.astype({'strike': float})
	# token_df
	token_df1= token_df[(token_df['name'] == 'BANKNIFTY') & (token_df['instrumenttype'] == 'OPTIDX') & (token_df['expiry']==expiry) ]
	print("\n Token Generation df\n",token_df)

	print("\n Token Generation df1\n",token_df1)

	return token_df,token_df1

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

def get_token_and_exchange(name): # get_token_and_exchange('BANKNIFTY27OCT22FUT') # token, exchange = get_token_and_exchange('BANKNIFTY27OCT22FUT')
	symboltoken = instrument_df.loc[name]['token']
	exchange = instrument_df.loc[name]['exch_seg']
	return symboltoken, exchange


# defaults
countt = 0
apikey = 'DodjVpCE' # Sridharan knsridharan@winrich.in
kiteSetupKeyForTOTP = 'ZT4OKWGC3TXIRPRZJLDKX3IBCM'
#username = 'k31094'
#pwd = 'KnsAng@12#'
#pwd = '1985'
#kiteSetupKeyForTOTP = 'ZT4OKWGC3TXIRPRZJLDKX3IBCM'
expiry = date(2023, 6, 29) # For Future
#time_15_15 = datetime.time(15,15)


#customer all data
all_cust=customer_data()

all_cust=get_obj(customer_dict=all_cust)	#updated dictionary with objects

obj_list,obj_dict=obj_ls_di(cus_obj_dict=all_cust)


# Entry conditions read
#entry_con_df = pd.read_csv('Entry_conditions.csv', index_col=0)
entry_con_df=sql.fetch_tables(entry_conditions)
entry_con_df['Start Date']=pd.to_datetime(entry_con_df['Start Date'])


#token_df,token_df1=token_generation()

# token1 = getTokenInfo ('BANKNIFTY', 'NFO','FUTIDX','','',expiry_day = None).iloc[0] # For Future
#token1 = getTokenInfo (token_df,'BANKNIFTY', 'NSE','','','',expiry_day = None).iloc[0] # For Index
#symbol = token1['symbol']
#token = token1['token']
#lot = token1['lotsize']

print("check obj")
#pdb.set_trace()

trade_inf={}

choice=0
time_15_15 = dt.time(15,15)
print(time_15_15)

print(entry_con_df.iloc[-1]['Start Date'].date())
print(entry_con_df.iloc[-1]['Entry Above High'])
print(entry_con_df.iloc[-1]['Entry Below Low'])
#pdb.set_trace()
"""
print("Collecting LTP values....")
while True:
	today = date.today()
	obj=obj_list[1]
	#for obj in obj_list:
	if  entry_con_df.iloc[-1]['Start Date'].date()==today:
		#bnf_ltp = obj.ltpData("NSE", "BANKNIFTY", "26009")['data']['ltp']

		bnf_ltp=44706
		print(bnf_ltp)
		time.sleep(1)
		if bnf_ltp>entry_con_df.iloc[-1]['Entry Above High']:
			print("buying BANKNIFTY")
			print(entry_con_df.iloc[-1]['Entry Above High'])
			stop_loss_buy=entry_con_df.iloc[-1]['Stop Loss Above Entry']
			target_buy=entry_con_df.iloc[-1]['Target Profit Above Entry']
			choice='1'
			print("stop_loss_buy=",stop_loss_buy)
			print("target_buy=",target_buy)
			print("choice=",choice)
			break
		if bnf_ltp<entry_con_df.iloc[-1]['Entry Below Low']:
			print("selling BANKNIFTY")
			print(entry_con_df.iloc[-1]['Entry Below Low'])
			stop_loss_sell=entry_con_df.iloc[-1]['Stop Loss Below Entry']
			target_sell=entry_con_df.iloc[-1]['Target Profit Below Entry']
			choice='2'
			print("stop_loss_sell=",stop_loss_sell)
			print("target_sell=",target_sell)
			print("choice=",choice)
			break
		
	else:
		break

print(obj_dict)
"""
"""
dat=historic_data(object=obj)

new = pd.DataFrame.from_dict(dat['data'])
new.to_csv("new_ang.csv")
print(new)
"""
"""	
xval = make_straddle('BANKNIFTY', '29MAR23', 100)
print(xval)
instrument_df = get_instruments()
print(instrument_df)
"""
# pdb.set_trace()

print(obj_list)
for name in obj_list:
	print(type(name))
	#print(name.position())
	nobj = get_key(name)
	print(nobj)
	current_time=datetime.now()
	if str(type(name))!="<class 'str'>":

		try:

			Trade_net = name.position()['data'] # Angel Trade Net Positions
			Trade_df=pd.DataFrame(Trade_net)
			Angel_net_df = Trade_df[Trade_df['symbolname']=='BANKNIFTY']
			Angel_net_df.to_csv("Angel_net_positions_" +nobj+".csv")
			angel_up=Angel_net_df.copy()
			angel_up.insert(0,"customerusername",nobj)
			angel_up.insert(1,"status","Success")
			angel_up.insert(2,"object",name)
			angel_up.insert(3,"createdate",current_time)
			sql.upload_to_table(angel_up,order_log_table,"append")
			print("angel trade\n")
			print(angel_up)

		except Exception as e:

			print(obj_dict[name], " ---> Order net positions subset csv file creation failed for :  ", nobj)
			print("\n")
	else:
		Angel_net_df = pd.DataFrame(data={"createdate":current_time},index=[0])
		Angel_net_df.to_csv("Angel_net_positions_"+nobj+".csv")
		angel_up=Angel_net_df.copy()
		angel_up.insert(0,"customerusername",nobj)
		angel_up.insert(1,"status","Failed")
		angel_up.insert(2,"object",name)
		sql.upload_to_table(angel_up,order_log_table,"append")
		print("angel trade\n")
		print(angel_up)
		
"""
# pdb.set_trace()
def angel_place_order(transaction_type, tsymbol, ttoken): # Change Product type to MIS ----> INTRADAY (from ---> CARRYFORWARD )
	global orderparams
	
	orderparams = {"variety": "NORMAL", "tradingsymbol": tsymbol, "symboltoken": ttoken, "transactiontype": transaction_type, 
	"exchange": exch_seg, "ordertype": "MARKET", "producttype": "CARRYFORWARD", "duration": "DAY", "price": "0", "squareoff": "0", 
	"stoploss": "0", "quantity": fin_q }

			print(get_key(name))
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