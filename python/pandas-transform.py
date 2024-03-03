# modules
import mysql.connector
import pandas as pd
import os
import numpy as np

conn = mysql.connector.connect(read_default_file='/Users/oscar/.my.cnf')
cur_path = os.getcwd()
file = '../data_files/city_house_prices.csv'
out_file = os.path.join(cur_path, file)

sql = "select * " \
      "from `oscarval_sql_course`.`city_house_prices`"

# read in the table
df = pd.read_sql(sql, conn)
# df = df.replace(r'^\s*$', np.nan, regex=True)

# data transform
df.set_index('Date', inplace=True)
df = df.stack().reset_index()

# create new columns
df.columns = ['date', 'city', 'price']

# export to .csv
df.to_csv(out_file, index=False)


# Exercise - split out State Abbrev & City for city field
df[['state', 'city']] = df['city'].str.split("-", expand=True)