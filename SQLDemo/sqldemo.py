#!/usr/bin/python

import mysql.connector

# Open database connection
db = mysql.connector.connect(user='root', password='password',host='127.0.0.1',database='test')

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT * FROM emp"
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      print(row[0]+" "+row[1])
except:
   print("Error: unable to fecth data")

# disconnect from server
db.close()