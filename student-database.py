import mysql.connector
table_name = "customers"
def login():
      while True:
        try:
            user_name = input("User Name : ")
            if user_name == "exit":
                return ["exit","exit"]
            password = input("Password : ")

            mydb = mysql.connector.connect(
                host="localhost",
                user= user_name,
                passwd= password
            )
            connection = [user_name,password]
            print("Connection Successful...")
            return connection

        except:
            print("Check Your Data And Try Again")

def main_menu():
        print('''
__________________________________
STUDENT DATA - MAIN MENU

1). Add Data
2). Edit Data
3). View Data
4). Remove Data
5). Create Data HTML
6.) Settings

99.) Exit Program''')
        menu = input(":")
        return menu

def add_data():
        stu_count = 0
        loop_name = False
        phone = ""
        language = ""
        try:
            stu_count = stu_count + 1
            while True:
                name = ""
                if name == "":
                    name = input(f" Enter student name \t\t: ")
                    loop_name = True
                    break
                elif name == "exit":
                    loop_name = False
                    return False
                    break
            if loop_name == True:
                while True:
                        phone = input(f" Enter phone number \t\t: ")
                        if phone != "":
                            break
                        
                while True:
                        language = input(f" Enter Programming Language \t: ")
                        if language != "":
                            break           
                mycursor = mydb.cursor()
                sql = "INSERT INTO customers (name, phone, language) VALUES (%s, %s, %s)"
                val = (name, phone, language) #name	phone	language	
                mycursor.execute(sql, val)
                mydb.commit()
                print(mycursor.rowcount, "record inserted.\n")

        except Exception as error:
            print("ERROR : ", error)

def settings():
        try:
            while True:
                print('''
__________________________________
1. View Database
2. View Tables
3. Create Table
4. Remove Table
        ''')
                select_ithem = input(": ")
                if select_ithem == "1":
                    mycursor = mydb.cursor()
                    mycursor.execute("SHOW DATABASES")
                    for databases in mycursor:
                        print(str(databases))

                elif select_ithem == "2":
                    mycursor = mydb.cursor()
                    mycursor.execute("SHOW TABLES")
                    for data_tables in mycursor:
                        print(data_tables)
                elif select_ithem == "3":
                    try:
                        mycursor = mydb.cursor()
                        mycursor.execute("CREATE TABLE " + table_name + " (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), phone VARCHAR(225), language VARCHAR(225))")
                    except Exception as error:
                        print("ERROR : ", error)
                elif select_ithem == "4":
                    mycursor = mydb.cursor()
                    sql = f"DROP TABLE {table_name}"
                    mycursor.execute(sql)
                else:
                    break
        except Exception as error:
             print("ERROR :", error)

def view_data():
    try:
        mycursor = mydb.cursor()
        sql = f"SELECT * FROM {table_name} ORDER BY id"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        print("___________________________________________________")
        print("|id\t| name\t\t| phone\t\t| language")
        print("___________________________________________________")
        for all_data in myresult:
            print(f"| {all_data[0]} \t| {all_data[1]} \t| {all_data[2]} \t| {all_data[3]}")
        print("___________________________________________________")
    except Exception as error:
         print("ERROR : ", error)

def edit_data():
    try:
        view_data()
        print("")
        edit_for_row = int(input("Enter edit column ID : ")) 
        mycursor = mydb.cursor()
        sql = f"SELECT * FROM customers WHERE id ='{edit_for_row}'"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for all_data in myresult:
            print(f"| {all_data[0]} \t| {all_data[1]} \t| {all_data[2]} \t| {all_data[3]}")

        stu_ID = str(all_data[0])
        while True:
                name = ""
                name = input(f"{all_data[1]} edit to student name \t\t: ")
                if name != "":
                    sql = "UPDATE "+ table_name +" SET name = %s WHERE id = %s"
                    val = (name, stu_ID)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    break
                elif name == "":
                    name = all_data[1]
                    break
                elif name == "exit -y":
                    break

        while True:
                phone= ""
                phone = input(f"{all_data[2]} edit to phone number \t\t: ")
                if phone == "":
                    phone = all_data[2]
                    break
                else:
                    sql = f"UPDATE "+ table_name +" SET phone = %s WHERE id = %s"
                    val = (phone, stu_ID)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    break
            
        while True:
                language = ""
                language = input(f"{all_data[3]} edit to Programming Language \t: ")
                if language == "":
                    language = all_data[3]
                    break
                else:
                    sql = f"UPDATE "+ table_name +" SET language = %s WHERE id = %s"
                    val = (language, stu_ID)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    break 
    except Exception as error:
         print("ERROR : ", error)

def remove_data():
    view_data()

    try:
        removeForRow = int(input("Enter remove column ID : "))
        mycursor = mydb.cursor()
        sql = f"DELETE FROM customers WHERE id = '{removeForRow}'"
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")
    except Exception as error:
         print ("ERROR : ", error)

def export():
    try:
        html_code = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Alpha Ceph Data Exporter</title>
        <style>
            .container{
                display: flex;
                justify-content: center;
                width: 100%;
            }
            .table{
                width: 1000px;
            }
            table {
            border-collapse: collapse;
            width: 100%;
            font-size: large;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            th, td {
            padding: 8px;
            text-align: left;
            border-bottom: 1px solid #ddd;
            }
            tr:hover {background-color:#f5f5f5;}
            @media (max-width: 700px){
                .container{
                    display: flex;
                    justify-content: center;
                    width: 700px;
                }
            }
            </style>
    </head>
    <body>
        <div class="container">
            <div class="table">
                <table>
                    <tr>
                    <th>ID</th>
                    <th>Full Name</th>
                    <th>Phone Number</th>
                    <th>Programming Language</th>
                    </tr>
                    '''
        html_end='''
                </table>
            </div>
        </div>
    </body>
    </html>    
        '''
        mycursor = mydb.cursor()
        sql = f"SELECT * FROM {table_name} ORDER BY id"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        the_html_rows = ""
        for all_data in myresult:
            id = str(all_data[0])
            name = str(all_data[1])
            phone = str(all_data[2])
            language = str(all_data[3])
            HTML_row = "<tr><td>" + id + "</td><td>" + name + "</td><td>" + phone + "</td><td>" + language + "</td></tr>\n"             
            the_html_rows = the_html_rows + HTML_row 
        export_for_file = html_code + the_html_rows + html_end
        f = open("index.html", "w")
        f.write(export_for_file)
        print("exporting successful")
        f.close()

    except Exception as error:
        print(error)

connection = login()

if connection[0] == "exit" and connection [1] == "exit":
    program = False
    print("program finished!")
    exit()

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user=connection[0],
        passwd=connection[1],
        database="mydatabase"
    )
except:
    mydb = mysql.connector.connect(
        host="localhost",
        user=connection[0],
        passwd=connection[1],)
    
    try:
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE mydatabase")
    except Exception as error:
         print("ERROR : ", error)

while True:
        menu = main_menu()
        if menu == "1":
            print("__________________________________\nDATA INSERT MENU :")
            add_data_menu = add_data()
        elif menu == "2":
            edit_data()
        elif menu == "3":
            view_data()
        elif menu == "4":
            remove_data()
        elif menu == "5":
            export()
            try:
                import webbrowser
                webbrowser.open("index.html")
            except:
                print("web opening error!")
        elif menu == "6":
            settings()

        elif menu == "exit -y":
               print("Program is ended !")
               exit()
        else:
                ask_to_exit = input("Confirt To Ecit (y/n) : ")
                if ask_to_exit == "y" or ask_to_exit == "yes":
                    print("Prgram is ended !")
                    exit()
                else:
                    print("continue This Program!\n\n")   

     

