# %%
import pandas as pd
import re
import epic_cars
import mysql.connector
import numpy as np
import connect_to_mysql
import sys
# insert at 1, 0 is the script path (or '' in REPL)
# sys.path.insert(0, 'C:/Users/porte/Downloads/yoyo/send_stuff/send_sms')
import send_sms
from sqlalchemy import create_engine
import pymysql
# %%
pd.set_option("display.max_rows", 120)
pd.set_option('display.max_colwidth', -1)

#%%
epic_cars.main()


# dat3 = pd.read_csv("data/cars.csv")

# dat_queried = (dat3.query('year >= 2008')
#         .query('miles <= 150000')
#         .query('price <= 4500')
#         # .query('price >= 500')
#         .reset_index(drop = True)
# )

# %%


# dat.dropna(['title'], axis = 'rows')

# dat = dat.assign(
#     title = lambda x: x['title'].replace(r'^\s*$', np.nan, regex=True)
#     )

# %%

# Count number of epic rows, execute the query and assign it to a pandas dataframe, detect if new epic rows were added
connect_to_mysql.main()


# %%
# dat = dat_queried
# recipients = ["+17193385009", "+17192002926"]



    # send_sms.send_sms_epic_to()
#%%


# %%




