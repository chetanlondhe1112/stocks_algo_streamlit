# Zerodha Login for tradding account

# Import libraries
import pdb
#from zrd_login import get_login 
#import logging
#logging.basicConfig(level=logging.DEBUG)
import pdb
from kiteconnect import KiteConnect
from kiteconnect import KiteTicker

def zerodha_cred():

	# create function to collect these values from db
	api_k = "m8lqe0lp92mndpzw"
	api_s = "lhg6sx4g3etshuleybete974h3voo8gz"
	#access_token = open('access_token1.txt').read()
	access_token='hk7etpah6kA7R9Bq7TDS3U8kzkJlkOsZ'
	return api_k,api_s,access_token

# Kite Login
def get_login(api_k, api_s):
	"""
		Kite Login
	"""
	print("logging into zerodha")

	global kws, kite

	kite = KiteConnect(api_key=api_k)

	kite.set_access_token(access_token)
	
	kws = KiteTicker(api_k, access_token)

	return kite

# API Keys
#api_k = "m8lqe0lp92mndpzw"
#api_s = "lhg6sx4g3etshuleybete974h3voo8gz"
 
# Access Token
#access_token = open('access_token1.txt').read()
#access_token='hk7etpah6kA7R9Bq7TDS3U8kzkJlkOsZ'

api_k,api_s,access_token=zerodha_cred()

kite = get_login(api_k, api_s)
margins = kite.margins()

print(margins)

# Quotes
v=kite.quote('NSE:INDIA VIX')
bk=kite.quote('NSE:NIFTY BANK')
nk=kite.quote('NSE:NIFTY 50')

#bf=kite.quote('NFO:BANKNIFTY20DECFUT')
#nf=kite.quote('NFO:NIFTY20DECFUT')


print("\n")
print("(1.0) ", "VIX LTP -->", v['NSE:INDIA VIX']['last_price'], " & ", "VIX open for today -->", v['NSE:INDIA VIX']['ohlc']['open'], " & ", "VIX net change from yesterday -->", v['NSE:INDIA VIX']['net_change'])
print("\n")
print("(2.0) ", "BANK Nifty Index LTP  -->", bk['NSE:NIFTY BANK']['last_price'], " & ", "BANK Nifty Index open for today -->", bk['NSE:NIFTY BANK']['ohlc']['open'], " & ", "Bank Nifty Index net change from yesterday -->", bk['NSE:NIFTY BANK']['net_change'])
#print("(2.1) ", "BANKNifty FUTURES LTP -->", bf['NFO:BANKNIFTY20DECFUT']['last_price'])
print("\n")
print("(3.0) ", "NIFTY 50 Index LTP -->", nk['NSE:NIFTY 50']['last_price'], " & ", "NIFTY 50 Index open for today -->", nk['NSE:NIFTY 50']['ohlc']['open'], " & ", "NIFTY 50 Index net change from yesterday -->", nk['NSE:NIFTY 50']['net_change'])
#print("(3.1) ", "Nifty FUTURES LTP  -->", nf['NFO:NIFTY20DECFUT']['last_price'])
print("\n")


nifty_50 = ["CIPLA","DRREDDY","SUNPHARMA","BPCL","ZEEL","IOC","TCS","ASIANPAINT","HINDALCO","INDUSINDBK","ONGC","MARUTI","TATASTEEL","BHARTIARTL","INFRATEL","NESTLEIND","HDFCBANK","TECHM","COALINDIA","ADANIPORTS","WIPRO","TATAMOTORS","EICHERMOT","RELIANCE","HEROMOTOCO","KOTAKBANK","BRITANNIA","BAJFINANCE","BAJAJFINSV","LT","ITC","M&M","HDFC","POWERGRID","NTPC","GRASIM","ULTRACEMCO","AXISBANK","HDFCLIFE","SBIN","GAIL","ICICIBANK","TITAN","SHREECEM","BAJAJ-AUTO","UPL","INFY","HCLTECH","HINDUNILVR","JSWSTEEL", "YESBANK"]
nifty_fno = ["CIPLA","LUPIN","DRREDDY","ADANIENT","FEDERALBNK","ASHOKLEY","SUNPHARMA","BPCL","VEDL","HINDPETRO","ZEEL","BHEL","IOC","TCS","PIDILITIND","ASIANPAINT","UBL","HINDALCO","PVR","TVSMOTOR","INDUSINDBK","ONGC","MARUTI","TATASTEEL","BHARTIARTL","SUNTV","MOTHERSUMI","INFRATEL","M&MFIN","NESTLEIND","PFC","MANAPPURAM","HDFCBANK","TECHM","COALINDIA","ADANIPORTS","AMARAJABAT","WIPRO","DLF","SRF","TATAMOTORS","RBLBANK","COLPAL","EICHERMOT","RELIANCE","BOSCHLTD","AMBUJACEM","SAIL","BALKRISIND","HEROMOTOCO","VOLTAS","KOTAKBANK","IBULHSGFIN","AUROPHARMA","BATAINDIA","DIVISLAB","CHOLAFIN","BRITANNIA","NMDC","BAJFINANCE","MARICO","BAJAJFINSV","BANKBARODA","LT","MUTHOOTFIN","ITC","TATAPOWER","RAMCOCEM","M&M","TATACONSUM","MINDTREE","BHARATFORG","HDFC","TATACHEM","TORNTPHARM","GLENMARK","POWERGRID","MGL","L&TFH","RECLTD","IGL","NTPC","GRASIM","BEL","CANBK","ESCORTS","EXIDEIND","ULTRACEMCO","LICHSGFIN","AXISBANK","HDFCLIFE","MCDOWELL-N","CADILAHC","IDFCFIRSTB","PNB","INDIGO","SBIN","GAIL","ICICIBANK","DABUR","HAVELLS","SRTRANSFIN","MFSL","BANDHANBNK","APOLLOTYRE","TITAN","PEL","SIEMENS","ICICIPRULI","SHREECEM","BAJAJ-AUTO","BIOCON","MRF","TORNTPOWER","ACC","SBILIFE","GODREJCP","UPL","PETRONET","PAGEIND","CONCOR","NAUKRI","APOLLOHOSP","GODREJPROP","HCLTECH","INFY","JUBLFOOD","NATIONALUM","JINDALSTEL","HINDUNILVR","COFORGE","GMRINFRA","IDEA","JSWSTEEL","CUMMINSIND","BERGEPAINT"]
watchlist = ["SBIN"]
