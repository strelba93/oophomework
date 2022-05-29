class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def mid_grade(self):
        list = []
        for el in self.courses_in_progress:
            for key, value in self.grades.items():
                if key == el:
                    list.extend(value)
                else:
                   None
        res = sum(list) / len(list)
        return res

                
    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.mid_grade():.1f}\nКурсы в процессе обучения: {', '.join(self.courses_in_progress)} \nЗавершенные курсы: {', '.join(self.finished_courses)}\n"
        return res

    def compare(self, other):
        if self.mid_grade() > other.mid_grade():
            res = f'У студента {self.name} {self.surname} средний балл выше.\nСредний бал {self.mid_grade():.1f}'
            return res
        elif self.mid_grade() < other.mid_grade():
            res = f'У студента {other.name} {other.surname} средний балл выше.\nСредний бал {other.mid_grade():.1f}'
            return res
        else:
            res = f'У студентов одиннаковый средний балл.\nСредний бал {self.mid_grade():.1f}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print ('Not a Student')
            return
        return self.mid_grade() > other.mid_grade()

class Lecturer:   
        
    def mid_lec(self):
        list = []
        for el in self.lecture_attached:
            for key, value in self.lec_grade.items():
                if key == el:
                    list.extend(value)
                else:
                   None
        res = sum(list) / len(list)
        return res


    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Mentor) and course in self.lecture_attached:
            if course in lecturer.lec_grade:
                lecturer.lec_grade[course] += [grade]
            else:
                lecturer.lec_grade[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print ('Not a Lecturer')
            return
        return self.mid_lec() > other.mid_lec()

  

    
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.mid_lec():.1f}\n'
        return res
 
        

class Reviewer:
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res
  
class Mentor(Lecturer, Reviewer):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.st_grade = []
        self.lecture_attached = []
        self.lec_grade = {}

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

bad_student = Student('Alexandr', 'Kokorin', 'male')
bad_student.courses_in_progress += ['HTML']
bad_student.courses_in_progress += ['Python']
bad_student.finished_courses += ['Введение в программирование']

 
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Git']

good_mentor = Mentor('Peter', 'Mann')
good_mentor.courses_attached += ['HTML']

cool_lector = Mentor('Nik', 'Walker')
cool_lector.lecture_attached += ['Python']
cool_lector.lecture_attached += ['Git']

good_lector = Mentor('Alisher', 'Olograv')
good_lector.lecture_attached += ['Python']
good_lector.lecture_attached += ['HTML']


 
cool_mentor.rate_hw(best_student, 'Python', 8)
cool_mentor.rate_hw(best_student, 'Python', 9)
cool_mentor.rate_hw(best_student, 'Python', 6)
cool_mentor.rate_hw(best_student, 'Git', 6)
cool_mentor.rate_hw(best_student, 'Git', 9)
cool_mentor.rate_hw(best_student, 'Git', 3)

good_mentor.rate_hw(bad_student, 'HTML', 4)
good_mentor.rate_hw(bad_student, 'HTML', 7)
good_mentor.rate_hw(bad_student, 'HTML', 9)
cool_mentor.rate_hw(bad_student, 'Python', 8)
cool_mentor.rate_hw(bad_student, 'Python', 7)
cool_mentor.rate_hw(bad_student, 'Python', 4)

cool_lector.rate_lec(cool_lector, 'Python', 1)
cool_lector.rate_lec(cool_lector, 'Python', 7)
cool_lector.rate_lec(cool_lector, 'Python', 8)
cool_lector.rate_lec(cool_lector, 'Git', 8)
cool_lector.rate_lec(cool_lector, 'Git', 9)
cool_lector.rate_lec(cool_lector, 'Git', 6)

good_lector.rate_lec(good_lector, 'Python', 8)
good_lector.rate_lec(good_lector, 'Python', 9)
good_lector.rate_lec(good_lector, 'Python', 4)
good_lector.rate_lec(good_lector, 'HTML', 9)
good_lector.rate_lec(good_lector, 'HTML', 8)
good_lector.rate_lec(good_lector, 'HTML', 10)
 
print(best_student.grades)
print(cool_lector.lec_grade)

print(best_student)
print(cool_lector)
print(bad_student)

print(cool_mentor.courses_attached)
print(best_student.courses_in_progress)


print(best_student.compare(bad_student))

print(best_student.grades)

print(best_student < bad_student)

print(cool_lector > good_lector)




list_py = []

def mid_py(self, course):
    a = self.grades[course]
    list_py.extend(a)


mid_py(best_student, 'Python')
mid_py(bad_student, 'Python')

def res_py():
    b = sum(list_py)/len(list_py)
    return b

print (f'На курсе Python средний балл студентов = {res_py():.1f}')

list_lec_py = []

def mid_lec_py(self, course):
    a = self.lec_grade[course]
    list_py.extend(a)


mid_lec_py(cool_lector, 'Python')
mid_lec_py(good_lector, 'Python')

def res_lec_py():
    b = sum(list_lec_py)/len(list_lec_py)
    return b

print (f'На курсе Python средний балл лекторов = {res_py():.1f}')