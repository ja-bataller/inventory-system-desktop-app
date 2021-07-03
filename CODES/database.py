import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'root',
    'password': 'admin',
    'host': 'localhost'
}

db = mysql.connector.connect(**config)
cursor = db.cursor()

DB_NAME = 'inventory_system_tupc_uitc'

TABLES = {}

# ACCOUNTS SCHEMA
TABLES['accounts'] = (
    "CREATE TABLE `accounts` ("
    " `id` int(10) NOT NULL AUTO_INCREMENT,"
    " `first_name` varchar(250) NOT NULL,"
    " `last_name` varchar(250) NOT NULL,"
    " `username` varchar(250) NOT NULL,"
    " `password` varchar(250) NOT NULL,"
    " `account_type` varchar(250) NOT NULL,"
    " PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB"
)

# ITEMS SCHEMA
TABLES['items'] = (
    "CREATE TABLE `items` ("
    " `id` int(10) NOT NULL AUTO_INCREMENT,"
    " `equipment` varchar(250) NOT NULL,"
     " `quantity` int(10)  NOT NULL,"
    " PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB"
)

# BORROWERS SCHEMA
TABLES['borrowers'] = (
    "CREATE TABLE `borrowers` ("
    " `id` int(10) NOT NULL AUTO_INCREMENT,"
    " `name` varchar(250) NOT NULL,"
    " `borrowers_num` varchar(250) NOT NULL,"
    " `item` varchar(250) NOT NULL,"
    " `date_out` varchar(250) NOT NULL,"
    " `date_in` varchar(250),"
    " PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB"
)

def create_database():
    cursor.execute(
        "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    print("Database {} created successfully.".format(DB_NAME))


def create_tables():
    cursor.execute("USE {}".format(DB_NAME))

    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            cursor.execute(table_description)
            print("Table ({}) created successfully".format(table_name), end="")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Table Exists")
            else:
                print(err.msg)


create_database()
create_tables()