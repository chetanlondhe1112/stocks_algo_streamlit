import warnings
from SmartApi.smartConnect import SmartConnect
import pdb
import requests
import os
import pandas as pd
import datetime
import time
import mibian
import pyotp
import sys

countt = 0

data1 = pd.read_csv('Entry_conditions.csv', index_col=0)
#next_candle = data1.iloc[-1]["End Date"]
#next_candle_time=pd.to_datetime(next_candle).time()
#time_now = dt.datetime.now()
#time_now = datetime.datetime.now().replace(microsecond=0)
#pdb.set_trace()
#(pd.to_datetime(next_candle.name).time()<pd.to_datetime(['15:00:00']).time)

# while True:
# 	data1 = pd.read_csv('Entry_conditions.csv', index_col=0)
# 	end_date = data1.iloc[-1]["End Date"]
# 	#end_date= Timestamp('2023-06-20 12:00:00+0530', tz='UTC+05:30')
# 	now_utc = dt.now(pytz.timezone('UTC'))+ pd.Timedelta(minutes=330)
# 	end_date= pd.to_datetime(end_date)
# 	five_minutes = pd.Timedelta(minutes=5)
# 	zero_minutes = pd.Timedelta(minutes=0)
# 	#5_30_minutes = pd.Timedelta(minutes=330)
# 	expired_entries = end_date - now_utc
# 	#close_entries = (now_utc - end_date) <= five_minutes
# 	#close_entries1 = (now_utc - end_date) <= five_minutes
# 	condition1= zero_minutes>expired_entries<five_minutes
# 	time_12 = datetime.time(12,00)
# 	time_now = datetime.datetime.now().time().replace(microsecond=0)
# 	condition_exit=time_now>time_12
# 	if condition1:
# 		break
# 	elif condition_exit:
# 		sys.exit()
# 	else:
# 		os.system('TLS17.py')

# pdb.set_trace()


# from datetime import datetime,date
from datetime import date
expiry = date(2023, 6, 29) # For Future
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

#pdb.set_trace()

def angelbrok_login():
	try:
		global feed_token, client_code, obj, obj3, obj4, obj5, obj6, obj7, obj8, obj9, obj10, obj11, obj12, obj13, obj14, obj16, obj17, obj20, obj21, obj22, obj23, password, refreshToken, accessToken, data
		


		countt = 0
		countt = countt+1
		apikey = 'DodjVpCE' # Sridharan knsridharan@winrich.in
		username = 'k31094'
		pwd = 'KnsAng@12#'
		pwd = '1985'
		kiteSetupKeyForTOTP = 'ZT4OKWGC3TXIRPRZJLDKX3IBCM'
		totp = pyotp.TOTP(kiteSetupKeyForTOTP)
		totp = totp.now()
		obj=SmartConnect(api_key=apikey) # Sridharan
		# pdb.set_trace()
		data = obj.generateSession(username,pwd,totp)
		time.sleep(0.5)
		# pdb.set_trace()
		print("\n")
		print("Sridharan")
		print(data)
		refreshToken= data['data']['refreshToken']
		#fetch the feedtoken
		feedToken=obj.getfeedToken()
		#fetch User Profile
		userProfile= obj.getProfile(refreshToken)

		# apikey = 'vdcFOWoL' # Nidhi Angel API ----> Check login vdcFOWoL
		# username = 'N70467'
		# pwd = 'M@yur_1234'
		# pwd = '1605'
		# kiteSetupKeyForTOTP = 'RY4QTCBKAVRNO6VNH2SCUAYJL4' #G22OADUF4WVAXPTAHK7YRYUBRI
		# totp = pyotp.TOTP(kiteSetupKeyForTOTP)
		# totp = totp.now()
		# obj=SmartConnect(api_key=apikey) # Nidhi
		# data = obj.generateSession(username,pwd,totp)
		# time.sleep(0.5)
		# print("\n")
		# print("Nidhi")
		# print(data)
		# #refreshToken= data['data']['refreshToken']
		# #fetch the feedtoken
		# #feedToken
		
		
		
	except Exception as e:
		print("Error in login", e)


angelbrok_login()
#


obj_list =[obj] 
obj_dict ={obj:"Sridharan"}
# obj_dict ={obj:"Nidhi"}



print("check obj")
time_15_15 = datetime.time(15,10)
#pdb.set_trace()
data1['Start Date']=pd.to_datetime(data1['Start Date'])
from datetime import datetime as dt
while True:
	today = date.today()
	current_time = time.strftime("%H:%M")
	datetime_object = dt.strptime(current_time,'%H:%M').time()
	if  data1.iloc[-1]['Start Date'].date()==today:
		bnf_ltp = obj.ltpData("NSE", "BANKNIFTY", "26009")['data']['ltp']
		# bnf_ltp=44240
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
		if datetime.time(11,14)==datetime_object:
			os.system('TLS17.py')
			#run tls17
		if datetime.time(11,44)==datetime_object:
			os.system('TLS17.py')
			#run tls17
		if datetime.time(12,15)==datetime_object:
			sys.exit()

	else:
		break

def roundup(x):
	return x if x % 100 == 0 else x + 100 - x % 100

bnf_ltp = obj.ltpData("NSE", "BANKNIFTY", "26009")['data']['ltp']

def get_symbol():
	max_level=bnf_ltp
	min_level=bnf_ltp
	print(max_level)
	print(int(roundup(max_level)))
	strikec = (int(roundup(max_level)))
	strike_call = strikec - 300 
	print(strike_call)
	print("\n")
	print(min_level)
	print(int(roundup(min_level)))
	strikep = (int(roundup(min_level)))
	strike_put= strikep + 300 
	print(strike_put)

	#expiry_day = datetime.date(2023,5,25) #<------------------------Change every Week ----------------------->
	expiry_day = datetime.date(2023,7,13) #praveen- change expiry every week before friday start# need to work with dashbboard  
	ATMStrike1 = strike_call
	ATMStrike2 = strike_put
	# expiry_day = expiry
	symbol = 'BANKNIFTY'

	ce_strike_symbolatm = getTokenInfo(symbol,'NFO','OPTIDX',ATMStrike1,'CE',expiry_day).iloc[0]
	pe_strike_symbolatm = getTokenInfo(symbol,'NFO','OPTIDX',ATMStrike2,'PE',expiry_day).iloc[0]
	ltpatmce=obj.ltpData('NFO',ce_strike_symbolatm['symbol'],ce_strike_symbolatm['token']) # obj made to obj1
	ltpatmpe=obj.ltpData('NFO',pe_strike_symbolatm['symbol'],pe_strike_symbolatm['token'])

	CE_Symbol = ce_strike_symbolatm['symbol']
	CE_Token = ce_strike_symbolatm['token']
	print(CE_Symbol, ",", CE_Token, " LTP = ", ltpatmce )

	PE_Symbol = pe_strike_symbolatm['symbol']
	PE_Token = pe_strike_symbolatm['token']
	print(PE_Symbol, ",", PE_Token, " LTP = ", ltpatmpe)

	df_log = pd.read_csv('angel_trade_log_list.csv', index_col=0)
	
	symbol_log_dict = df_log.to_dict('records')[0]
	# {'CE_Symbol': 'BANKNIFTY27APR2339800CE', 'CE_Token': 53304, 'PE_Symbol': 'BANKNIFTY27APR2338700PE', 'PE_Token': 53277, 'fin_q': 25}
	symbol_log_dict.update({"CE_Symbol":CE_Symbol, "CE_Token":CE_Token, "PE_Symbol":PE_Symbol, "PE_Token":PE_Token, "bnf_ltp":bnf_ltp})
	print(symbol_log_dict)
	trade_list1=[]
	trade_list1.append(symbol_log_dict)
	df_tl = pd.DataFrame(trade_list1)
	df_tl.to_csv("angel_trade_log_list.csv")
	return strike_put,strike_call, CE_Symbol, CE_Token, PE_Symbol, PE_Token

get_symbol()

# pdb.set_trace()


for name in obj_list:
	try:
		Trade_net = name.position()['data'] # Angel Trade Net Positions
		nobj = obj_dict[name]
		Trade_df=pd.DataFrame(Trade_net)
		Angel_net_df = Trade_df[Trade_df['symbolname']=='BANKNIFTY']
		Angel_net_df.to_csv("Angel_net_positions_" + obj_dict[name]+".csv")

	except Exception as e:
		print(obj_dict[name], " ---> Order net positions subset csv file creation failed for :  ", nobj)
		print("\n")


# pdb.set_trace()
def order_status():
	try:
		Trade_net = name.position()['data'] # Angel Trade Net Positions
		nobj = obj_dict[name]
		Trade_df=pd.DataFrame(Trade_net)
		Angel_net_df = Trade_df[Trade_df['symbolname']=='BANKNIFTY']
		Angel_net_df.to_csv("Angel_net_positions_" + obj_dict[name]+".csv")
		
	except Exception as e:
		print(obj_dict[name], " ---> Order net positions subset csv file creation failed for :  ", nobj)
		print("\n")


#pdb.set_trace()
def angel_place_order(transaction_type, tsymbol, ttoken): # Change Product type to MIS ----> INTRADAY (from ---> CARRYFORWARD )
	global orderparams
	
	orderparams = {"variety": "NORMAL", "tradingsymbol": tsymbol, "symboltoken": ttoken, "transactiontype": transaction_type, 
	"exchange": exch_seg, "ordertype": "MARKET", "producttype": "INTRADAY", "duration": "DAY", "price": "0", "squareoff": "0", 
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
fin_quantity = 25 #praveen - check lot size
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
		angel_place_order("BUY", CE_Symbol, CE_Token)
		time.sleep(3)
		order_status()
		break
	elif val == "2":	
		# transaction_type = "BUY"
		print('Buying PUT ----> ')
		angel_place_order("BUY", PE_Symbol, PE_Token)
		time.sleep(3)
		order_status()
		break
	elif val == "3":	
		# transaction_type = "SELL"
		print('Selling CALL ----> ')
		angel_place_order("SELL", CE_Symbol, CE_Token)
		time.sleep(3)
		order_status()
		break
	elif val == "4":	
		# transaction_type = "SELL"
		print('Selling PUT ----> ')
		angel_place_order("SELL", PE_Symbol, PE_Token)
		time.sleep(3)
		order_status()
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
	# bnf_ltp=44240
	print(bnf_ltp)
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
			angel_place_order("SELL", CE_Symbol, CE_Token)
			break
		if current_stop:
			print("Stop Loss Reached")
			print('Selling CALL ----> ')
			angel_place_order("SELL", CE_Symbol, CE_Token)
			break
		if EOD:
			print("EOD Reached")
			angel_place_order("SELL", CE_Symbol, CE_Token)
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
			angel_place_order("SELL", PE_Symbol, PE_Token)
			break
		if current_stop:
			print("Stop Loss Reached")
			print('Selling PUT ----> ')
			angel_place_order("SELL", PE_Symbol, PE_Token)
			break
		if EOD:
			print("EOD Reached")
			angel_place_order("SELL", PE_Symbol, PE_Token)
			break
sys.exit()




