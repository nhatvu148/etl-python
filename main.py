import os
import mysql.connector
import pandas as pd
import configparser

config = configparser.ConfigParser()
config.read('.my.cnf')

mysql_config = {
    'user': config['client']['user'],
    'password': config['client']['password'],
    'host': config['client']['host'],
    'database': config['client']['database'],
}


# variables
cur_path = os.getcwd()
data_dir = os.path.join(cur_path, 'data_files')
load_file = 'mysql_export.csv'
load_file = os.path.join(data_dir, load_file)

proj = 'osk-demo-277900'
dataset = 'osk'
table = 'annual_movie_summary'
table_id = f'{proj}.{dataset}.{table}'

# data connections
conn = mysql.connector.connect(**mysql_config)

# extract is transformed via query (i.e. aggregation)
query = "select year " \
        ", count(distinct imdb_title_id) as movie_count " \
        ", avg(avg_vote) as avg_rating " \
        "from `oscarval_sql_course`.`imdb_movies` " \
        "where true " \
        "and year between 1940 and 2018 " \
        "group by 1"

# extract data
df = pd.read_sql(query, conn)

# transform data


def year_rating(x):
    if x <= 5.65:
        return 'bad movie year'
    elif x <= 5.9:
        return 'okay movie year'
    elif x <= 7:
        return 'great movie year'
    else:
        return 'not rated'


# transformation by derivation
df['year_rating'] = df['avg_rating'].apply(year_rating)
df.to_csv(load_file, index=False)
