# import modules
import mysql.connector
from mysql.connector import errorcode

try:
    conn = mysql.connector.connect(read_default_file='/Users/oscar/.my.cnf')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Check Credentials')
    else:
        print(err)

# close your connection (very important)
conn.close()
