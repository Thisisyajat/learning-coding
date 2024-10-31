# This program integrates SQL and Python using the SQL module.
# (C) Yajat Gupta

import mysql.connector
db = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'test1')
print('SQL Database test1 online.')

# Output
'''
SQL Database test1 online.
'''