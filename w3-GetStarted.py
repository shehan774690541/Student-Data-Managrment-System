import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=""
)

# print(mydb)

mycursor = mydb.cursor()

def create_database():
    mycursor.execute("CREATE DATABASE mydatabase")



def show_databases():
    mycursor.execute("SHOW DATABASES")
 
    for x in mycursor:
        print(x)

def create_table():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mydatabase"
    )

    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE customers2 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(225))")
    # mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

def show_tabels():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mydatabase"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SHOW TABLES")

    for x in mycursor:
        print(x)

def insert_data():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mydatabase"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = ("shehan1", "kegalla")
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

def insert_multi_data():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mydatabase"
    )

    mycursor = mydb.cursor()
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = [
            ('Peter', 'Lowstreet 4'),
            ('Amy', 'Apple st 652'),
            ('Hannah', 'Mountain 21'),
            ('Michael', 'Valley 345'),
            ('Sandy', 'Ocean blvd 2'),
            ('Betty', 'Green Grass 1'),
            ('Richard', 'Sky st 331'),
            ('Susan', 'One way 98'),
            ('Vicky', 'Yellow Garden 2'),
            ('Ben', 'Park Lane 38'),
            ('William', 'Central st 954'),
            ('Chuck', 'Main Road 989'),
            ('Viola', 'Sideway 1633')
    ]
    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "was inserted!")

def Insert_one_row_and_return_the_ID():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mydatabase"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = ("Michelle", "Blue Village")
    mycursor.execute(sql, val)

    mydb.commit()

    print("1 record inserted, ID:", mycursor.lastrowid)

def Select_From_a_Table():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mydatabase"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM customers")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)


def fetchone_Method():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mydatabase"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM customers")
    myresult = mycursor.fetchone()

    print(myresult)

def Select_With_a_Filter():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mydatabase"
    )
    mycursor = mydb.cursor()
    sql = "SELECT * FROM customers WHERE address = 'Park Lane 38'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def Wildcard_Characters():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mydatabase"
    )

    mycursor = mydb.cursor()

    sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def Prevent_SQL_Injection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mydatabase"
    )

    mycursor = mydb.cursor()

    sql = "SELECT * FROM customers WHERE address = %s"
    adr = ("Yellow Garden 2", )

    mycursor.execute(sql, adr)

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def Sort_the_name():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mydatabase"
    )

    mycursor = mydb.cursor()

    sql = "SELECT * FROM customers ORDER BY name"

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def Sort_the_DESC():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mydatabase"
    )

    mycursor = mydb.cursor()

    sql = "SELECT * FROM customers ORDER BY name DESC"

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def Delete_Record():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mydatabase"
    )

    mycursor = mydb.cursor()

    sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted")

def Delete_Record2():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mydatabase"
    )

    mycursor = mydb.cursor()

    sql = "DELETE FROM customers WHERE address = %s"
    adr = ("Yellow Garden 2", )

    mycursor.execute(sql, adr)

    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted")

def Delete_a_Table():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mydatabase"
    )

    mycursor = mydb.cursor()
    sql = "DROP TABLE customers2"
    mycursor.execute(sql)

def Delete_a_Table2():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mydatabase"
    )

    mycursor = mydb.cursor()

    sql = "DROP TABLE IF EXISTS customers2"

    mycursor.execute(sql)

def Update_Table():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mydatabase"
    )

    mycursor = mydb.cursor()

    sql = "UPDATE customers SET address = 'Valley 345' WHERE address = 'Apple st 652'"

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record(s) affected")


def Update_Table():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mydatabase"
    )

    mycursor = mydb.cursor()

    sql = "UPDATE customers SET name = %s WHERE id = %s"
    val = ("chappie", "2")

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record(s) affected")

Update_Table()