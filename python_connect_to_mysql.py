import mysql.connector
db = mysql.connector.connect(host="localhost", username="criminaluser", password="criminaldb",database="saidatabase")
cursor = db.cursor()
db.commit()
db.close()
print("database connected")