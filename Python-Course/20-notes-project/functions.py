from services.user_service import UserService
from services.note_service import NoteService
from database.userDAO import UserDAO
from database.noteDAO import NoteDAO
from models.users import Users
from models.notes import Notes
import datetime as dt

#DECLARE CLASSES
#USERS
user_dao = UserDAO()
user_service = UserService(user_dao)

#NOTES
note_dao = NoteDAO()
note_service = NoteService(note_dao)

#GET INTEGER INPUT FUNCTION
def get_int_input(prompt: str, min_val: int, max_val: int) -> int:
    try:
        num = int(input(prompt))
        if num < min_val or num > max_val:
            print(f"\n⚠️ Select a number between {min_val} and {max_val}.")
        else:
            return num
    except ValueError:
        print("\n⚠️ Value must be a number.")

#REGISTER NEW USER
def register_user():
    print("\n✅ We are going to register you in the system...")
    name = input("¿What's your name?: ")
    surname = input("¿What's your surname?: ")
    email = input("¿What's your email?: ")
    password = input("¿What's your password?: ")
    
    print(user_service.addUser(name, surname, email, password))

#LOGIN USER
def login_user():
    print("\nOkay!! Identify yourself in the system...")
    email = input("Introduce your email: ")
    password = input("Introduce your password: ")
    user = user_service.checkLogin(email, password)
    if user:
        logged_user(user)
    else:
        print(f"\n❌ Sorry {email} is not registred")

#USER LOGGED        
def logged_user(user:Users):
    print(f"\n✅ Welcome {user.getName()} 👤, You've identified yourself in the system on {dt.date.today()}")
    while True:
        print("\n   Available actions:")
        print("     1. Create note")
        print("     2. Show your notes")
        print("     3. Delete note")
        print("     0. Exit")
        #GET OPTION
        num = get_int_input("\n¿What do you want to do?: ", 0, 3)
        if num == 0:
            break
        elif num == 1:
            create_note(user)
        elif num == 2:
            show_notes(user)
        elif num == 3:
            delete_note(user)

#CREATE NEW NOTES
def create_note(user: Users):
    print(f"\nOk {user.getName()} 👤!! We're going to create a new note...")
    name = input("Enter the title of the note: ")
    desc = input("Enter the content of the note: ")
    print(note_service.addNote(user, name, desc))

def show_notes(user: Users):
    notes = note_service.showNotes(user)
    if notes:
        print(f"\nOk {user.getName()} 👤!! Here are your notes:")
        for note in notes:
            print("\n****************************************")
            print(note.getNoteTitle())
            print(note.getNoteContent())
            print("****************************************")
    else:
        print(f"\n{user.getName()} 👤, you don't have notes yet!")
    
def delete_note(user: Users):
    notes = note_service.showNotes(user)
    if notes:
        print(f"\nOk {user.getName()} 👤!! We are going to delete your note:")
        title = input("Enter the title of the note to be deleted: ")

        if any(title == note.getNoteTitle() for note in notes):
            print(note_service.deleteNote(title, user))
        else:
            print(f"\n⚠️ {user.getName()} 👤, You don't have notes with this title")
    else:
        print(f"\n{user.getName()} 👤, You don't have notes to be deleted!")
