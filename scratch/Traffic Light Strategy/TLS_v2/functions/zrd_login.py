import pdb
from kiteconnect import KiteConnect
from kiteconnect import KiteTicker


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
