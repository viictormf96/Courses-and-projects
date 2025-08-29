import mysql.connector
from .db_connection import get_connection
from models.users import Users 
from models.notes import Notes

class NoteDAO:

    #CREATE NEW NOTES
    def addNote(self, user:Users, name, desc):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            note = (user.getId(), name, desc)
            cursor.execute("INSERT INTO notes VALUES(null, %s, %s, %s)", note)
            conn.commit()
            conn.close()
            return f"\n✅ Perfect, You've saved the note: {name}"
        except mysql.connector.Error as e:
            raise mysql.connector.Error(f"\n❌ Error creating new note: {e}\n")
    
    #SHOW NOTES
    def showNotes(self, user:Users):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM notes WHERE user_id = %s ", (user.getId(),))
            rows = cursor.fetchall()
            notes = [Notes(row[0], row[1], row[2], row[3]) for row in rows]
            conn.close()
            return notes
        except mysql.connector.Error as e:
            raise mysql.connector.Error(f"\n❌ Error showing notes: {e}\n")
    
    #DELETE NOTES
    def deleteNote(self, title, user: Users):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM notes WHERE name = %s AND user_id = %s ", (title, user.getId()))
            conn.commit()
            conn.close()
            return f"\nWe've deleted the note: {title}"
        except mysql.connector.Error as e:
            raise mysql.connector.Error(f"\n❌ Error deleting note: {e}\n")


        