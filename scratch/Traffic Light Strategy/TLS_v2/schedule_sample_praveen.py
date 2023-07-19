
import schedule
import time
import datetime
import os
import sys
import pdb

#pdb.set_trace()

def do_nothing2_0():
    print("******************************************************************************************")
    print("\n")
    print("Data frame 1 -->")
    #print("\n")
    print(datetime.datetime.now())
    print("\n")
    
    os.system('get_data.py')

def do_nothing3_0():
    print("******************************************************************************************")
    print("\n")
    print("data frame 2 -->")
    #print("\n")
    print(datetime.datetime.now())
    print("\n")
    
    os.system('get_data.py')

def bye2_0():
    print("exiting program at  -->")
    #print("\n")
    print(datetime.datetime.now())
    print("\n")
    
    sys.exit()


    

schedule.every().hour.at(":14").do(do_nothing2_0)
schedule.every().hour.at(":44").do(do_nothing3_0)
#schedule.every(60).minutes.at(":14").do(do_nothing2_0)
#schedule.every(60).minutes.at(":44").do(do_nothing2_0)

#sys.exit()
schedule.every().day.at("15:15").do(bye2_0)
# schedule.every().day.at("09:37").do(bye2_0)







while 1:
    schedule.run_pending()
    time.sleep(1)
    print("waiting--->")

    #
    
