import pandas as pd
import mysql.connector
import os

conn = mysql.connector.connect(read_default_file='/Users/oscar/.my.cnf')

cur_path = os.getcwd()
file = 'data-export.csv'
export_file = os.path.join(cur_path, file)

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
df.to_csv(export_file)

# exercise: using the year made, determine if the movie is old, recent or new
# old 2005 - 2010
# recent 2010 - 2015
# new 2015 forward

