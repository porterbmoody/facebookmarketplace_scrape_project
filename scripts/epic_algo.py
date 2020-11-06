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





