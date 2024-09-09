class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, cource, grade):
        if isinstance(lecturer, Lecturer) and \
            cource in self.courses_in_progress and \
                cource in lecturer.courses_attached:
            if cource in lecturer.grades:
                lecturer.grades[cource] += [grade]
            else:
                lecturer.grades[cource] = [grade]
        else:
            return 'Ошибка'
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self) :
        return "Имя: " + self.name  + "\nФамилия: " + self.surname + "\nСредняя оценка за лекции: " 

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self) :
        return "Имя: " + self.name  + "\nФамилия: " + self.surname

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_reviwer = Reviewer('Some', 'Buddy_reviewer')
cool_reviwer.courses_attached += ['Python']

cool_lecturer = Lecturer('Some', 'Buddy_lecturer')
cool_lecturer.courses_attached += ['Python']


cool_reviwer.rate_hw(best_student, 'Python', 10)
cool_reviwer.rate_hw(best_student, 'Python', 10)
cool_reviwer.rate_hw(best_student, 'Python', 10)

print(best_student.grades)

best_student.rate_hw(cool_lecturer, 'Python', 8)
best_student.rate_hw(cool_lecturer, 'Python', 9)
best_student.rate_hw(cool_lecturer, 'Python', 10)

print(cool_lecturer.grades)
pass
