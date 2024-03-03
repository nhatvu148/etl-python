import pandas as pd
import mysql.connector
from google.cloud import bigquery

client = bigquery.Client(project='osk-demo-277900')
table_id = 'osk-demo-277900.osk.movies'

conn = mysql.connector.connect(read_default_file='/Users/oscar/.my.cnf')

sql = "select year, " \
      "title, " \
      "duration, " \
      "country " \
      "from `oscarval_sql_course`.`imdb_movies` " \
      "where year = 2011"

df = pd.read_sql(sql, conn)

job_config = bigquery.LoadJobConfig(
    autodetect=True,
    write_disposition='WRITE_APPEND'
)


load_job = client.load_table_from_dataframe(
    df,
    table_id,
    job_config=job_config
)
load_job.result()

destination_table = client.get_table(table_id)  # Make an API request.
print("You have {} rows in your table.".format(destination_table.num_rows))

# Exercise: append the next year's data to your table (i.e. an incremental load)
