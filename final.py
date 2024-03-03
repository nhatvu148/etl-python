# needed modules
import os
import mysql.connector
import pandas as pd
from google.cloud import bigquery

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
conn = mysql.connector.connect(read_default_file='/Users/oscar/.my.cnf')
client = bigquery.Client(project=proj)

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

# load data
job_config = bigquery.LoadJobConfig(
    skip_leading_rows=1,
    source_format=bigquery.SourceFormat.CSV,
    autodetect=True,
    write_disposition='WRITE_TRUNCATE'
)

# open file for loading
with open(load_file, 'rb') as file:
    load_job = client.load_table_from_file(
        file,
        table_id,
        job_config=job_config
    )

load_job.result()

destination_table = client.get_table(table_id)
print("You have {} rows in your table.".format(destination_table.num_rows))