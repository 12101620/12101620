import mysql.connector
db_connection = mysql.connector.connect(
host = "bpkhpgtz4yfyyyiu3vii-mysql.services.clever-cloud.com",
user = "uf6y8xpdp9antzdl",
passwd = "GtN9ivhMDHzMgxnhSmpG",
database = "bpkhpgtz4yfyyyiu3vii"
)
dbCursor=db_connection.cursor()


dbCursor.execute("""
    UPDATE Students
    SET Address ='Bang Na' WHERE id IN (1, 2, 3, 4, 5, 6)
""")
db_connection.commit()
dbCursor.execute("SELECT id,name,age,attend,hobby,address FROM Students")
data = dbCursor.fetchall()
for db in data:
    print(db)