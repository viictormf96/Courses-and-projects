from student import Student

class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    #GETTERS
    def getName(self):
        return self.name
    
    #SETTERS
    def setName(self, name):
        self.name = name

    #METHODS
    def addStudent(self, student):
        if any(s.getName() == student.getName() for s in self.students):
            raise ValueError(f"The name '{student.getName()}' is alrredy in the list")
        else:
            self.students.append(student)
        
    def getAVG(self):
        avg = 0
        for student in self.students:
            avg += student.getGrades()
        result = avg / len(self.students)
        return round(result, 2)

    def getStudents(self):
        txt = f"\n------ STUDENTS FROM {self.getName().upper()} COURSE ------"
        for student in self.students:
            txt +=f"\n- {student.getName()}"
        return txt
    