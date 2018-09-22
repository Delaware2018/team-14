import mysql.connector
from mysql.connector import errorcode

try:
  # attempt to connect to database
  # enter credentials  
  db = mysql.connector.connect(user='team14', password='', 
  host='35.173.239.182',
  database='bpos')

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  print('connected')
  cursor =  db.cursor()
  
  cursor.execute("CREATE TABLE users (" 
  + "firstname varchar(255),"
  + "lastname varchar(255),"
  + "email varchar(255),"    
  + "city varchar(255),"
  + "state varchar(255),"
  + "zipcode int,"
  + "school varchar(255),"
  + "year int," 
  + "phone varchar(255),"
  + "organization varchar(255),"
  + "gender varchar(255),"
  + "streetnum varchar(255),"
  + "streetname varchar(255),"
  + "amount int,"
  + "businessOrNot varchar(255),"
  + "businessdescription varchar(255)"
  + ");")

db.close()