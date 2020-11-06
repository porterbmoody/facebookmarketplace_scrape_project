# %%
import pandas as pd
import re
import epic_cars
import mysql.connector
from termcolor import colored
import numpy as np
import connect_to_mysql
import sys
import send_sms
# from sqlalchemy import create_engine
# import pymysql
import time
import random
# %%
pd.set_option("display.max_rows", 120)
pd.set_option('display.max_colwidth', -1)

# %%
while True:
    epic_cars.main()
    # Count number of epic rows, execute the query and assign it to a pandas dataframe, detect if new epic rows were added
    connect_to_mysql.main()
    time.sleep(random.randint(2000*60,3000*60)/99)

# dat3 = pd.read_csv("data/cars.csv")

# dat_queried = (dat3.query('year >= 2008')
#         .query('miles <= 150000')
#         .query('price <= 4500')
#         # .query('price >= 500')
#         .reset_index(drop = True)
# )

# %%
# C:/Users/porte/AppData/Local/Programs/Python/Python38-32/python.exe "d:/BYUI/fall 2020/Side Projects/facebookmarketplace_scrape_project/scripts/epic_algo.py"

# %%
# dat = dat_queried
# recipients = ["+17193385009", "+17192002926"]

    # send_sms.send_sms_epic_to()
#%%





