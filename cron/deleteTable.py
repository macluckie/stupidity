import mysql.connector
import os   

ipmysql = os.environ['IPDB']
database = os.environ['DB']

user = os.environ['USER']
password = os.environ['PASSWORD']

# print("http://"+ipmysql)

try:    
    mydb = mysql.connector.connect(
    host=ipmysql,
    user=user,
    password=password,
    database=database
)

    mycursor = mydb.cursor()
    sql = "DELETE FROM stupidity"
except:
    print("error connexion databases")
    
mycursor.execute(sql)
mydb.commit()