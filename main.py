class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}



    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашнее задание:{self.average_student_rate()} \nКурсы в процессе изучения: {self.courses_in_progress} \nЗавершенные курсы:{self.finished_courses}'


    def __lt__(self, other):
        if self.average_student_rate() < other.average_student_rate():
            return True
        return False




    def average_student_rate(self):
        self.average_rate_stud = 0
        for val in self.grades.values():
            for val_new in val:
                self.average_rate_stud += val_new
        summ = int(self.average_rate_stud/len(str(val_new)))

        return summ



    def rate_lc(self, lector, course, grade):
        # if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
        if course in lector.grades_new:
            lector.grades_new[course] += [grade]
        else:
            lector.grades_new[course] = [grade]
        # else:
        #     return 'Ошибка'










class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []





class Lecturer(Mentor):
    # def __init__(self, name, surname):
    #     super().__init__(name, surname)

    grades_new = {}


    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_value()}'

    def __lt__(self, other):
        if self.average_value() < other.average_value():
            return True
        else:
            return False


    def average_value(self):
        return self.__average_value()

    def __average_value(self):
        for aver in self.grades_new.values():
            average = int(sum(aver)/ len(aver))



        return average




class Reviewer(Mentor):

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'


    def rate_hw(self, student, course, grade):
        # if course in self.courses_attached and course in student.courses_in_progress:
        if course in student.grades:
            student.grades[course] += [grade]
        else:
            student.grades[course] = [grade]
        # else:
        #     return 'Ошибка'
        #








best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']



lec_1 = Lecturer("Dmitriy", "Medvedev")
lec_2 = Lecturer("Vladimir", "Putin")

stud_1 = Student("Roman", "Romanov", "male")
stud_2 = Student("Sergey", "Sergeev", "male")
stud_1.courses_in_progress += ["Python"]
stud_2.courses_in_progress += ["Git"]
stud_1.finished_courses += ["Operator of compare"]
stud_2.finished_courses += ["Python"]

mentor = Mentor("Glavniy", "Boss")
rew_1 = Reviewer("Genadiy", "Surkov")
rew_2 = Reviewer("Oleg", "Petrov")

stud_2.rate_lc(lec_1, "PYTHON", 14)
stud_1.rate_lc(lec_1, "PYTHON", 2)
stud_1.rate_lc(lec_2, "Git", 2)
stud_2.rate_lc(lec_2, "Git", 2)

mentor.courses_attached += ["Python", "Git", "Operator of compare"]
rew_1.rate_hw(stud_2, "PYTHON", 6)
rew_2.rate_hw(stud_2, "Git", 10)
rew_1.rate_hw(stud_1, "PYTHON", 3)
rew_2.rate_hw(stud_1, "Git", 4)



# print(stud_2.average_student_rate())
#  print(stud_1.average_student_rate())
# print(stud_2 < stud_1)
# print(lec_1 < lec_2)
# print(lec_2.average_value())



stud_list = [stud_1.grades, stud_2.grades]

#  Проблема с реализацией функции, в течении нескольких дней не смог найти правильное решение
# def average_grade_stud_of_courses():
#     all_grade = []
#     for person_t in stud_list:
#         for courses, grade in person_t.items():
#             all_grade.extend(average_student_rate.get("Python", []))
#
#     return round(sum(all_grade) / len(all_grade), 2)
#
#
#
#
# print(average_grade_stud_of_courses())






