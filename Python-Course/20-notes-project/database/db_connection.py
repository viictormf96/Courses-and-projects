import mysql.connector
import config

#CONNECTION TO DB
def get_connection():
    try:
        return mysql.connector.connect(
            host = config.DB_HOST,
            user = config.DB_USER,
            passwd = config.DB_PASSWORD,
            database = config.DB_NAME
        )
    except mysql.connector.Error:
        raise mysql.connector.Error("\n❌Can't connect to MySQL server.\n")

#CREATE DB AND TABLES
def createDB():
    try:
        conn = mysql.connector.connect(
            host = config.DB_HOST,
            user = config.DB_USER,
            passwd = config.DB_PASSWORD,
        )
        cursor = conn.cursor()

        #CREATE DB
        cursor.execute("CREATE DATABASE IF NOT EXISTS notesDB;")
        cursor.execute("USE notesDB;")
        conn.commit()

        #CREATE TABLE USERS
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INT(10) AUTO_INCREMENT NOT NULL,
            name VARCHAR(50) NOT NULL,
            surname VARCHAR(50) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL,
            CONSTRAINT pk_user PRIMARY KEY(id)
        );
        """
        )

        #CREATE TABLE NOTES
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes(
            id INT(10) AUTO_INCREMENT NOT NULL,
            user_id INT(10) NOT NULL,
            name VARCHAR(50) NOT NULL,
            description VARCHAR(500),
            CONSTRAINT pk_note PRIMARY KEY(id),
            CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id)
        );
        """
        )
        conn.commit()

        #CLOSE CONNECTION
        conn.close()
    except mysql.connector.Error:
        raise mysql.connector.Error("\n❌Can't connect to MySQL server.\n")