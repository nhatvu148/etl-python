# import modules
import mysql.connector
from mysql.connector import errorcode

try:
    conn = mysql.connector.connect(read_default_file='/Users/oscar/.my.cnf')
    cursor = conn.cursor()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Check Credentials')
    else:
        print(err)

query = "select year, title from `oscarval_sql_course`.`imdb_movies` limit 5"

cursor.execute(query)

for (year, title) in cursor:
    print(year, title)

# close your connection, very important
conn.close()

# write a query that brings down year, title and genre