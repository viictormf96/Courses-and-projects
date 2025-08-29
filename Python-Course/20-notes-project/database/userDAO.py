import mysql.connector
from .db_connection import get_connection
from models.users import Users 

class UserDAO:

    #ADD USER
    def addUser(self, user:Users):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users VALUES(%s, %s, %s, %s, %s)", user.to_tuple())
            conn.commit()
            conn.close()
            return f"\n✅ Perfect {user.getName()}, You've been registred with the email {user.getEmail()}"
        except mysql.connector.Error as e:
            raise mysql.connector.Error(f"\n❌ Error registering new user: {e}\n")
    
    #CHECK LOGIN
    def checkLogin(self, email, password):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            user = (email, password)
            cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", user)
            row = cursor.fetchone() 
            conn.close()
            if row != None:
                user = Users(row[0], row[1], row[2], row[3], row[4])
                return user
            else:
                return row
        except mysql.connector.Error as e:
            raise mysql.connector.Error(f"\n❌ Error login user: {e}\n")




    