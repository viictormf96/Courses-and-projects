class Notes():

    #CONSTRUCTOR
    def __init__(self, id, user_id, noteTitle, noteContent):
        self.id = id
        self.user_id = user_id
        self.noteTitle = noteTitle
        self.noteContent = noteContent
    
    #GETTERS
    def getId(self):
        return self.id
    
    def getUser_id(self):
        return self.user_id
    
    def getNoteTitle(self):
        return self.noteTitle
    
    def getNoteContent(self):
        return self.noteContent

    #SETTERS
    def setId(self, id):
        self.id = id

    def setUser_id(self, user_id):
        self.User_id = user_id

    def setNoteTitle(self, noteTitle):
        self.noteTitle = noteTitle
    
    def setNoteContent(self, noteContent):
        self.noteContent = noteContent
