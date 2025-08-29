from database.noteDAO import NoteDAO
from models.notes import Notes
from models.users import Users

class NoteService:
    def __init__(self, dao: NoteDAO):
        self.dao = NoteDAO()

    def addNote(self, user: Users, name, desc):
        return self.dao.addNote(user, name, desc)
    
    def showNotes(self, user: Users):
        return self.dao.showNotes(user)
    
    def deleteNote(self, title, user:Users):
        return self.dao.deleteNote(title, user)