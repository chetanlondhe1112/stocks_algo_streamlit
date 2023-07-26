# https://www.youtube.com/watch?v=n04dtnMl_BU&list=PLifIWB1V-ILMpnExpxly40KhZ_gVVwHVm&index=12
# https://www.youtube.com/watch?v=B1jjo0zcE6g&list=PLifIWB1V-ILMpnExpxly40KhZ_gVVwHVm&index=13
# https://www.youtube.com/watch?v=wHLrMyzdgJw
import pdb
from kiteconnect import KiteConnect
from kiteconnect import KiteTicker
from sqlalchemy import create_engine,text
from datetime import datetime,date
import pandas as pd
from functions.db_conn import sqlalchemy_connect


def get_login(api_k, api_s,access_token):
	print("logging into zerodha")
	global kws, kite
	kite = KiteConnect(api_key=api_k)

	# print("[*] Generate Request Token : ", kite.login_url())
	# request_tkn = input("[*] Enter Your Request Token Here : ")
	# data = kite.generate_session(request_tkn, api_secret=api_s)
	# kite.set_access_token(data["access_token"])
	# kws = KiteTicker(api_k, data["access_token"])
	# print(data['access_token'])

	kite.set_access_token(access_token)
	kws = KiteTicker(api_k, access_token)

	return kite

def zrd_login(connection_object):
    access_token_l=[]
    sql=connection_object
    print("Collecting Access Token")
    access_tk_df=sql.fetch_access_tokens()

    today=str(date.today())
    print("todays date: "+str(today))
    last_date=str(access_tk_df["createdate"][0]).split(" ")[0]
    print("Last token updated date: "+str(last_date))
    print("Last Token: "+str(access_tk_df.iloc[0]["access_token"]))

    if today!=last_date:
        #access_token=str(access_tk_df.iloc[0]["access_token"])
        print("token is not available for today")
        return 0
    elif today==last_date:
        
        access_token=str(access_tk_df.iloc[0]["access_token"])
        api_k=str(access_tk_df.iloc[0]["api_key"])
        api_s=str(access_tk_df.iloc[0]["api_secret"])
        print(access_token)
            
        #access_token='hk7etpah6kA7R9Bq7TDS3U8kzkJlkOsZ'
        # pdb.set_trace()

        kite = get_login(api_k,api_s,access_token)
        margins = kite.margins()

        print(margins)


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
        return kite

