import streamlit as st
from sqlalchemy import create_engine,text
import pandas as pd
import time
import numpy as np


def reconnection(connection_object=object):  
    #try: 
        # Creating Connection       
        return connection_object.engine()
    #except:
        st.info("Reconnecting.............")
        time.sleep(1)
        #st.experimental_rerun()
        st.stop() 
    #st.experimental_rerun()
   