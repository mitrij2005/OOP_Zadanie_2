from statistics import mean
    



class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grades = {}
        self.average_ball = None

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

        # считаем средний бал сразу после добавлении очередной оценки лектора
        lecturer.average_grades = {name:mean(balls) for name, balls in lecturer.grades.items()}
        lecturer.average_ball = mean(lecturer.average_grades.values())

    def __str__(self) :
       return "Имя: " + self.name  + "\nФамилия: " + self.surname + "\nСредняя оценка за домашние задания: " + str(self.average_ball) + "\nКурсы в процессе изучения: " + ",".join(self.courses_in_progress) + "\nЗавершенные курсы: " + ",".join(self.finished_courses)

    def __eq__(self, value: object) -> bool:
        if self.average_ball is None or value.average_ball is None:
            return("Ошибка")
        else:
            return self.average_ball == value.average_ball
        pass

    def __lt__(self, value: object) -> bool:
        if self.average_ball is None or value.average_ball is None:
            return("Ошибка")
        else:
            return self.average_ball < value.average_ball
        pass
 
    def __gt__(self, value: object) -> bool:
        if self.average_ball is None or value.average_ball is None:
            return("Ошибка")
        else:
            return self.average_ball > value.average_ball
        pass
       
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_grades = {}
        self.average_ball = None

    def __str__(self) :
       return "Имя: " + self.name  + "\nФамилия: " + self.surname + "\nСредняя оценка за лекции: " + str(self.average_ball)

    def __eq__(self, value: object) -> bool:
        if self.average_ball is None or value.average_ball is None:
            return("Ошибка")
        else:
            return self.average_ball == value.average_ball
        pass

    def __lt__(self, value: object) -> bool:
        if self.average_ball is None or value.average_ball is None:
            return("Ошибка")
        else:
            return self.average_ball < value.average_ball
        pass
 
    def __gt__(self, value: object) -> bool:
        if self.average_ball is None or value.average_ball is None:
            return("Ошибка")
        else:
            return self.average_ball > value.average_ball
        pass



class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
        # считаем средний бал сразу после добавлении очередной оценки за курс
        student.average_grades = {name:mean(balls) for name, balls in student.grades.items()}
        student.average_ball = mean(student.average_grades.values())

    def __str__(self) :
        return "Имя: " + self.name  + "\nФамилия: " + self.surname

class Staistika(Student, Lecturer):
    def __init__(self, name):
        self.name = name
        self.cource_name = None
        self.obj = None
        self.average_ball = None
        self.tmp_average_ball_list = []

    def set_cource_rang (self, cource_name:str, obj:list):
        self.tmp_average_ball_list = []
        self.cource_name = cource_name
        for i in obj:
        #   print (type(i))
        #   print (str(i.average_ball) + " " + i.name + i.surname)
            if cource_name in i.grades:
                self.tmp_average_ball_list += i.grades[cource_name]
        self.average_ball = mean(self.tmp_average_ball_list)
        pass

    def __str__(self):
        return f"Название статистики: {self.name} \nКурс: {self.cource_name} \nРейтинг: {self.average_ball}"


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

best_best_student = Student('Vasya', 'Pupkin' , 'superman')
best_best_student.courses_in_progress += ['Programming Basics']

cool_reviwer = Reviewer('Some', 'Buddy_reviewer')
cool_reviwer.courses_attached += ['Python']
cool_reviwer.courses_attached += ['Programming Basics']

cool_lecturer = Lecturer('Some', 'Buddy_lecturer')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Programming Basics']

cool_cool_lecturer = Lecturer('Emos', 'Yddub_lecturer')
cool_cool_lecturer.courses_attached += ['Python']
cool_cool_lecturer.courses_attached += ['Programming Basics']


cool_reviwer.rate_hw(best_student, 'Python', 10)
cool_reviwer.rate_hw(best_student, 'Python', 10)
cool_reviwer.rate_hw(best_student, 'Python', 10)

print(best_student.grades)

cool_reviwer.rate_hw(best_best_student, 'Programming Basics', 8)
cool_reviwer.rate_hw(best_best_student, 'Programming Basics', 10)

print(best_best_student.grades)


best_student.rate_hw(cool_lecturer, 'Python', 8)
best_student.rate_hw(cool_lecturer, 'Python', 9)
best_student.rate_hw(cool_lecturer, 'Python', 10)


best_best_student.rate_hw(cool_cool_lecturer, 'Python', 8)
best_best_student.rate_hw(cool_cool_lecturer, 'Programming Basics', 9)

print(cool_lecturer.grades)
print(cool_cool_lecturer.grades)

print("\nВывод результатов Задания 3 Темы \"ООП\"\n")
print(best_best_student)
print(best_student)


print(cool_cool_lecturer)
print(cool_lecturer)

print (cool_lecturer == cool_cool_lecturer)
print (best_best_student.__gt__(best_student))
print (best_best_student  < best_student)


pass

print("\nВывод результатов Задания 4 Темы \"ООП\"\n")
statistika1 = Staistika("Успеваемость студентов")
Students = [best_student, best_best_student]
statistika1.set_cource_rang ("Python", Students)
print(statistika1)
Lecturers = [cool_lecturer, cool_cool_lecturer]
statistika2 = Staistika("Рейтинг преподавателей")
statistika2.set_cource_rang ("Python", Lecturers)
print(statistika2)

pass