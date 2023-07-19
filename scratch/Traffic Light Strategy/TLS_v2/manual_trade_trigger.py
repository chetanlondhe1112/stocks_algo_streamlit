import warnings
from SmartApi.smartConnect import SmartConnect
import pdb
import requests
import pandas as pd
import datetime
import time
import mibian
import pyotp
import sys

countt = 0

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

# pdb.set_trace()

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

		# apikey17 = 'dSttihPV' # Sujithra Angel API --->  
		# username17 = 'S1728035'
		# pwd17 = '5538'
		# kiteSetupKeyForTOTP17 = 'YVJ4DSODQE6E7PSYNHRXMX3A6M' 
		# totp17 = pyotp.TOTP(kiteSetupKeyForTOTP17)
		# totp17 = totp17.now()
		# obj17=SmartConnect(api_key=apikey17) #Sujithra
		# data17 = obj17.generateSession(username17,pwd17,totp17)
		# time.sleep(0.5)
		# print("\n")
		# print("Sujithra")
		# print(data17)
		
		
		
	except Exception as e:
		print("Error in login", e)


angelbrok_login()
#


obj_list =[obj] 
obj_dict ={obj:"Sridharan"}



print("check obj")
bnf_ltp = obj.ltpData("NSE", "BANKNIFTY", "26009")['data']['ltp']

# ONE_MINUTE
# "fromdate": "2023-01-23 09:00", 
#     "todate": "2023-01-24 15:29"
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

	except Exception as e:
		print(obj_dict[name], " ---> Order net positions subset csv file creation failed for :  ", nobj)
		print("\n")


# pdb.set_trace()

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

pdb.set_trace()
while True:	
	print("\n")
	# pdb.set_trace()
	print(CE_Symbol, " , ",  PE_Symbol)
	val = input("Enter your trade action value (1)Buy Call , (2)Buy Put,  (3)Sell Call , (4)Sell Put , (5) EXIT loop : ----> ")
	
	print("You have chosen ---> ", val)
	print("\n")
	# pdb.set_trace()

	if val == "1":	
		# transaction_type = "BUY"
		print('Buying CALL ----> ')
		# pdb.set_trace()
		angel_place_order("BUY", CE_Symbol, CE_Token)
	elif val == "2":	
		# transaction_type = "BUY"
		print('Buying PUT ----> ')
		angel_place_order("BUY", PE_Symbol, PE_Token)
	elif val == "3":	
		# transaction_type = "SELL"
		print('Selling CALL ----> ')
		angel_place_order("SELL", CE_Symbol, CE_Token)
	elif val == "4":	
		# transaction_type = "SELL"
		print('Selling PUT ----> ')
		angel_place_order("SELL", PE_Symbol, PE_Token)
	elif val == "5":
		print("\n")
		print("exiting Loop")
		sys.exit()		
	else:
		print("\n")
		print("Wrong Entry  ---> Please retry ")
		# sys.exit()
		# pdb.set_trace()



