from database.db_connection import createDB
import functions

try:
    #CREATE DATABASE
    createDB()
    num = 5
    while num != 0:
        print("\nSelect an action:")
        print(" 1. Register")
        print(" 2. Login")
        print(" 0. Exit")
        #GET OPTION
        num = functions.get_int_input("\n¿What do you want to do?: ", 0, 2)
        if num == 1:
            functions.register_user()
        elif num == 2:
            functions.login_user()
except Exception as e:
    print(e)
    #print("\n❌Can't connect to MySQL server.\n")
