import mysql.connector

connection1 = mysql.connector.connect(

  host='localhost',
  user="root",
  passwd="newrootpassword",
  database = "home_products_management"

)
cursor = connection1.cursor()

###creating home products database###

#cursor.execute("CREATE DATABASE home_products_management")
#cursor.execute("CREATE TABLE departments(Id_Department int(11) NOT NULL AUTO_INCREMENT,Department_Name VARCHAR(255) NOT NULL, PRIMARY KEY (Id_Department))")
#cursor.execute("CREATE TABLE products(Id_Product int(11) NOT NULL AUTO_INCREMENT,Product_Name VARCHAR(255) NOT NULL,Id_Department int(11) NOT NULL,Product_amount int(11) NOT NULL,Product_Notes VARCHAR(255) NOT NULL,Date_Buy DATE NOT NULL, PRIMARY KEY (Id_Product ))")
#cursor.execute("CREATE TABLE Users(Id_User int(11) NOT NULL AUTO_INCREMENT,User_Name VARCHAR(255) NOT NULL,Password VARCHAR(255) NOT NULL ,PRIMARY KEY (Id_User))")

### Inserting Data ###

#users_query = "INSERT INTO Users(Id_User,User_Name,Password) VALUES (%s,%s,%s)"
#users_values = [('1','Dan','dany'),
 #           ]
#cursor.executemany(users_query,users_values)

#departments_query = "INSERT INTO Departments(Id_Department,Department_Name) VALUES (%s,%s)"
#department_values = [('1','Dairy'),
#              ('2','Meat'),
#               ('3', 'Bakery')
 #               ]


#cursor.executemany(departments_query,department_values)
#mysql_query="UPDATE Products SET Date_Buy=DATE_FORMAT(Date_Buy,'%e/%c/%Y')"
#connection1.commit()

#products_values = [('1','milk','1','2','buy two tara','2020-1-10'),
 #             ('3','hamburger','2','1','package of four','2020-2-10'),
 #               ('4','pita','3','10','1 package of 10','2020-2-10')
 #              ]

#product_query = "INSERT INTO Products (Id_Product, Product_Name, Id_Department,Product_amount,Product_Notes,Date_Buy) VALUES (%s,%s,%s,%s,%s,%s)"
#cursor.executemany(product_query,products_values)

#connection1.commit()





