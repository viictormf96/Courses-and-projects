"""
5. Sistema de Gestión de Estudiantes (Nivel Avanzado)
🧩 Objetivo:
Usar varias clases

Aplicar composición (clases dentro de clases)

Gestionar listas de objetos

📋 Enunciado:
Crea una clase Estudiante con nombre, edad y notas.
Crea una clase Curso que contenga una lista de estudiantes.
Agrega métodos a Curso para:

Añadir estudiantes

Calcular la nota media del curso

Mostrar los nombres de todos los estudiantes

🧪 Extra:
Haz que no se puedan añadir dos estudiantes con el mismo nombre.

"""
from student import Student
from course import Course

#CREATE LISTS
students = list()
courses = list()

#SHOW LIST OF COURSES
def coursesList(courses):
    print("\n------ COURSES LIST------")
    for index, course in enumerate(courses):
        print(f"{index + 1}. {course.getName()}")
    
    return int(input("\nSelect a course: "))

#ADD STUDENT
def addStudent():
    try:
        print("\n------ NEW STUDENT ------")
        course = coursesList(courses)
        name = input("\nName: ")
        if name.isdigit():
            print("\nName must be a string")
        else:
            age_inp = input("Age: ")
            if not age_inp.isdigit():
                raise ValueError("\nAge must be a number")
            age = int(age_inp)
            grades_inp = input("Grades: ")
            
            try:
                grades = float(grades_inp)
            except ValueError:
                raise ValueError("\nGrades must be a number")
            
            if(grades < 0 or grades > 10):
                print("\nGrades must be between 0 and 10")
            else:
                courses[course - 1].addStudent(Student(name, age, grades))
    except ValueError as e:
        print(e)

#NEW COURSE
def addCourse():
    print("\n------ NEW COURSE ------")
    name = input("name: ")
    courses.append(Course(name))

#MAIN
option = 1
while option != 0:
    try:
        print("\n------ WHAT DO YOU WANT TO DO ------")
        print("1. Add new Course")
        print("2. Add new Student")
        print("3. Show average from one course")
        print("4. Show students from one course")
        print("0. Exit")
        
        option = int(input("\nSelect one option: "))
        
        if option == 0:
            
            print("GOODBYE!!")
        
        elif option == 1:
            
            addCourse()
        
        elif option == 2:
            
            if len(courses) == 0:
                print("\nYou need to add a course to add new students.")
            else:
                addStudent()
        
        elif option == 3:
            try:
                course = coursesList(courses)
                print(f"\n------ {courses[course -1].getName().upper()} GRADE AVERAGE ------")
                print(courses[course - 1].getAVG())
            except ValueError:
                print("fdsdfdsfsd")

        elif option == 4:
            
            course = coursesList(courses)
            print(courses[course - 1].getStudents())
        
        elif option > 4 or option < 0:
            
            print("\Insert a valid value")
    
    except ValueError:
        print("\nInsert a valid value")
