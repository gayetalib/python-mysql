import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "passer"
)

if con.is_connected():
    print("Connection successful... !")
else:
    print("Connexion error to Database")

cur = con.cursor()

# cur.execute("create database class12")
cur.execute("use class12")
# prenom = input("Entrez votre prenom : ")
# nom = input("Entrez votre nom : ")
# cur.execute("Insert into student1 values({}, '{}', '{}')".format(0, prenom, nom))
# con.commit()
# print("Row inserted sucessfully...!")

# cur.execute("use class12")
cur.execute("select * from student1")
# cur.execute("update student1 set prenom = 'Omar' where prenom ='diop'") #update
# cur.execute("delete from student1 where id = 12")
data = cur.fetchall()
for i in data:
    print(i)
print("Query executed sucessfully...!")







