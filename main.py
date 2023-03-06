class Student:
    class_instances = []
    class_instance_grades = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.class_instances.append(self.name +' '+ self.surname)
        self.class_instance_grades.append(self.grades)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Error'

    def average_grade_homework_of_courses(course):
            result = {}
            for dict in Student.class_instance_grades:
                for list in dict:
                    if list in result:
                        result[list] += (dict[list])
                    else:
                        result[list] = dict[list]
            for key, value in result.items():
                if key == course:
                    return f'Calculation of the average grade for homework ' \
                           f'for all students within the course of {key}: ' \
                           f'{round(sum(value) / len(value), 1)}'

    def average_grade(self):
        return round(sum([sum(grade) for grade in self.grades.values()]) / sum([len(val) for val in self.grades.values()]), 1)

    def __ge__(self, other):
        if not isinstance(other, Student):
            print("It's someone else!!!")
            return
        return self.average_grade() < other.average_grade()

    def __str__(self):
        self.courses_in_progress = ', '.join(self.courses_in_progress)
        self.finished_courses = ', '.join(self.finished_courses)
        return f'Name: {self.name}\nLast name: {self.surname}\n' \
               f'Average homework grade: {self.average_grade()}' \
               f'\nCourses in progress: {self.courses_in_progress}' \
               f'\nCompleted Courses: {self.finished_courses} '

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    class_instances = []
    class_instance_grades = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.class_instance_grades.append(self.grades)
        self.class_instances.append(self.name + ' ' + self.surname)

    def average_grade_homework_of_courses(course):
        result = {}
        for dict in Lecturer.class_instance_grades:
            for list in dict:
                if list in result:
                    result[list] += (dict[list])
                else:
                    result[list] = dict[list]
        for key, value in result.items():
            if key == course:
                return f'Calculation of the average grade for the lectures ' \
                       f'of all lecturers within the course of {key}: ' \
                       f'{round(sum(value) / len(value), 1)}'

    def average_grade(self):
       return round(sum([sum(grade) for grade in self.grades.values()]) / sum([len(val) for val in self.grades.values()]), 1)

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            print("It's someone else!!!")
            return
        return self.average_grade() < other.average_grade()

    def __str__(self):
        return f'Name: {self.name}\nLast name: {self.surname}\n' \
               f'Average lecture grade: {self.average_grade()}'

class Reviewer(Mentor):
    class_instances = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.class_instances.append(self.name +' '+ self.surname)


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Error'

    def __str__(self):
        return f'Name: {self.name}\nLast name: {self.surname}'

"""Ревьюеры"""
best_reviewer_1 = Reviewer('Jimmy', 'Page')
best_reviewer_1.courses_attached += ['Guitar', 'Solo guitar']
best_reviewer_2 = Reviewer('Janis', 'Joplin')
best_reviewer_2.courses_attached += ['Vocal', 'Backing vocal']
best_reviewer_3 = Reviewer('John', 'Bonham')
best_reviewer_3.courses_attached += ['Drums', 'Hang']
"""Лекторы"""
best_lecturer_1 = Lecturer('John', 'Lennon')
best_lecturer_1.courses_attached += ['Guitar', 'Piano']
best_lecturer_2 = Lecturer('Paul', 'McCartney')
best_lecturer_2.courses_attached += ['Vocal', 'Guitar', 'Bass guitar']
best_lecturer_3 = Lecturer('Ringo', 'Starr')
best_lecturer_3.courses_attached += ['Drums', 'Percussion']
"""Студенты"""
best_student_1 = Student('Matthew', 'Bellamy', 'male')
best_student_1.courses_in_progress += ['Guitar', 'Solo guitar', 'Drums', 'Piano']
best_student_1.finished_courses += ['Organ', 'Musical notation']
best_student_2 = Student('Сhad', 'Smith', 'male')
best_student_2.courses_in_progress += ['Drums', 'Hang', 'Percussion']
best_student_2.finished_courses += ['Tuba']
best_student_3 = Student('Chester', 'Bennington', 'male')
best_student_3.courses_in_progress += ['Vocal', 'Backing vocal', 'Guitar', 'Bass guitar']
best_student_3.finished_courses += ['Violin', 'Keyboard']

"""Оценки за д/з студентам от ревьюеров"""
best_reviewer_1.rate_hw(best_student_1, 'Guitar', 10)
best_reviewer_1.rate_hw(best_student_1, 'Guitar', 2)
best_reviewer_1.rate_hw(best_student_1, 'Solo guitar', 7)
best_reviewer_3.rate_hw(best_student_1, 'Drums', 9)
best_reviewer_2.rate_hw(best_student_3, 'Vocal', 8)
best_reviewer_2.rate_hw(best_student_3, 'Backing vocal', 10)
best_reviewer_3.rate_hw(best_student_2, 'Drums', 9)
best_reviewer_3.rate_hw(best_student_2, 'Drums', 5)
best_reviewer_3.rate_hw(best_student_2, 'Hang', 6)

"""Студенты выставляют оценки лекторам"""
best_student_1.rate_lecture(best_lecturer_1, 'Guitar', 9)
best_student_1.rate_lecture(best_lecturer_1, 'Piano', 7)
best_student_2.rate_lecture(best_lecturer_3, 'Drums', 10)
best_student_2.rate_lecture(best_lecturer_3, 'Percussion', 2)
best_student_3.rate_lecture(best_lecturer_2, 'Vocal', 10)
best_student_3.rate_lecture(best_lecturer_2, 'Bass guitar', 7)
best_student_3.rate_lecture(best_lecturer_2, 'Guitar', 5)

"""Наши студенты"""
print('Our students:', ', '.join(Student.class_instances))
print('=' * 15)
"""Наши лекторы"""
print('Our lecturers:', ', '.join(Lecturer.class_instances))
print('=' * 15)
"""Наши ревьюеры"""
print('Our reviewers:', ', '.join(Reviewer.class_instances))
print()

"""Магический метод __str__ у всех классов"""
print(best_student_1)
print('=' * 15)
print(best_student_2)
print('=' * 15)
print(best_student_3)
print()
print(best_lecturer_1)
print('=' * 15)
print(best_lecturer_2)
print('=' * 15)
print(best_lecturer_3)
print()
print(best_reviewer_1)
print('=' * 15)
print(best_reviewer_2)
print('=' * 15)
print(best_reviewer_3)
print()

"""сравниваем студентов по средней оценке за домашние задания"""
print(best_student_1.__ge__(best_student_2))
print(best_student_1.__ge__(best_student_3))
print(best_student_2.__ge__(best_student_3))
print()
"""сравниваем между собой лекторов по средней оценке за лекции"""
print(best_lecturer_1.__ge__(best_lecturer_2))
print(best_lecturer_1.__ge__(best_lecturer_3))
print(best_lecturer_2.__ge__(best_lecturer_3))
print()
"""Подсчет средней оценки за домашние задания по всем студентам в рамках конкретного курса"""
print(Student.average_grade_homework_of_courses('Drums'))
print('=' * 15)
"""Подсчет средней оценки за лекции всех лекторов в рамках курса"""
print(Lecturer.average_grade_homework_of_courses('Guitar'))
print('=' * 15)



