import streamlit as strem
import pandas as pd
import mysql.connector
from mysql import connector
import warnings
warnings.filterwarnings('ignore')

mydbconn = connector.connect( host=" 127.0.0.1", 
								user="root", 
                                password="", 
                                database="redbus")
query = "SELECT * FROM bus_routes"
strem.write(query)

df = pd.read_sql(query, con = mydbconn)
strem.dataframe(df)
