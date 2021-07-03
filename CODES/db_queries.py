import mysql.connector
from mysql.connector import errorcode

# MYSQL DATABASE CONFIGURATION
DB_configuration = {"host": "localhost", "user": "root", "password": "admin", "database": "inventory_system_tupc_uitc"}

equipments = []
brands = []
models = []

noSerialNum = []
yesSerialNum = []

class db_queries():

    def addremove_item_db(self):
        # GET ITEMS WITH NO SERIAL NUMBER IN MYSQL DB
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT * FROM items WHERE serial_number ='N/A'")
        for item in mycursor:
            noSerialNum.append(item)
        print("ITEMS WITH NO SERIAL NUMBER")
        print(noSerialNum)

        # GET ITEMS WITH SERIAL NUMBER IN MYSQL DB
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT * FROM items WHERE serial_number !='N/A'")
        for item in mycursor:
            yesSerialNum.append(item)
        print("ITEMS WITH SERIAL NUMBER")
        print(yesSerialNum)

        # GET EQUIPMENTS IN MYSQL DB
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT equipment FROM items")
        for equipment in mycursor:
            equipments.append(equipment)
        print("EQUIPMENTS")
        print(equipments)

        # GET BRANDS IN MYSQL DB
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT brand FROM items")
        for brand in mycursor:
            brands.append(brand)
        print("BRANDS")
        print(brands)

        # GET MODELS IN MYSQL DB
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT model FROM items")
        for model in mycursor:
            models.append(model)
        print("MODELS")
        print(models)