class Student:
    def __init__(self, name, surname, age, midle_score):
        self.name=name
        self.surname=surname
        self.age=age
        self.midle_score=midle_score

    def changin_mid_score(self, group):
        if self in group.students:
            self.midle_score += 50
        return self.midle_score

    # def get_best_student(self):
    #     temp = 0
    #     if self.midle_score > temp:
    #         temp = self.show_student_info()
    #     return "The best Student ---> "+ temp

    def show_student_info(self):
        return f"Student name -> {self.name}\nStudent surname -> {self.surname}\nStudent age -> {self.age}\nStudent score -> {self.midle_score}\n{"-"*100}"


class Group():
    def __init__(self,group_name):
        self.group_name = group_name
        self.students = []
    def add_students(self, student):
        self.students.append(student)
    def show_all_students(self):
        for i in self.students:
            print(f" he/she visiting extra lesson:\n{i.show_student_info()}\n{"="*100}")
    def find_student(self, name, surname):
        for stud in self.students:
            if stud.name == name and stud.surname == surname:
                print(f">>>THIS STUDENT {name} {surname} IN LEARNING IN EXTRA LESSON GROUP<<<")
                return
        print(f">>>This student {name} {surname} not in extra lesson group<<<")
    def get_best_student(self):
        res = self.students[0]
        for i in self.students:
            if i.midle_score > res.midle_score:
                res= i
        return res





# Створюємо студентів
student_1 = Student(name="Stepan", surname= "Bandera",age=117, midle_score= 99)
student_2 = Student(name="Taras", surname= "Shevchenko",age= 47, midle_score=95)
student_3 = Student(name="Lesia",surname= "Ukrainka",age= 42,midle_score= 79)
student_4 = Student(name="Yevhen",surname= "Poliezhaiev",age= 35,midle_score=99)
student_5 = Student(name="Bogdan",surname= "Hmelnicky",age= 250,midle_score= 60)
list_students = [student_1,student_2,student_3,student_4,student_5]
# друкуємо інф. про студента
print(student_2.show_student_info())


# створюємо групи
python_group = Group("Python")
java_group = Group("Java")

# додаємо студентів до конкретних груп
python_group.add_students(student_2)
python_group.add_students(student_4)
java_group.add_students(student_3)
java_group.add_students(student_5)
java_group.add_students(student_1)

#змінюємо оцінки за присутність на Lessons
list_students = [student_1,student_2,student_3,student_4,student_5]
for i in list_students:
    i.changin_mid_score(python_group)
    i.changin_mid_score(java_group)

#перевіряємо чи змінились оцінки
for i in list_students:
    print(i.show_student_info())


# показуємо які студенти в групах
python_group.show_all_students()
java_group.show_all_students()

#шукаємо студентів в групах
python_group.find_student(name="Stepan", surname="Bandera")
python_group.find_student(name="Yevhen",surname= "Poliezhaiev")
java_group.find_student(name="Yevhen",surname= "Poliezhaiev")
java_group.find_student(name="Bogdan",surname= "Hmelnicky")

#показуємо кращого студента по группам
best_from_python = python_group.get_best_student()
best_from_java = java_group.get_best_student()
print(best_from_python.show_student_info())
print(best_from_java.show_student_info())

