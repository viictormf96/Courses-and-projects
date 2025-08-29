from database.userDAO import UserDAO
from models.users import Users

class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = UserDAO()
    
    def addUser(self,name, surname, email, password):
        user = Users(None,name, surname, email, password)
        return self.dao.addUser(user)
    
    def checkLogin(self, email, password):
        return self.dao.checkLogin(email, password)
    
        