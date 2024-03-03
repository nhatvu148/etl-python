import pandas as pd
import mysql.connector

conn = mysql.connector.connect(read_default_file='/Users/oscar/.my.cnf')

query = """select year
, title
, duration
, genre
, avg_vote
, case 
    when avg_vote < 3 then 'bad'
    when avg_vote < 6 then 'okay'
    when avg_vote >= 6 then 'good'
  end as movie_rating
from `oscarval_sql_course`.`imdb_movies`
where true
and language = 'English'
and year = 2005
"""

df = pd.read_sql_query(query, conn)
print(df.head())

# create a filter for movies > 100 mins in duration