from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random

Base = declarative_base()  #базовий клас. основний
faker = Faker()

courses_list = [
    "Python",
    "SQL",
    "API",
    "Git",
    "QA"
]

class Students(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name_stud = Column(String)


class  Courses(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    name_course = Column(String)

class St_courses(Base):
    __tablename__ = "student_courses"

    student_id = Column(Integer,ForeignKey("students.id"), primary_key=True)
    course_id = Column(Integer,ForeignKey("courses.id"),primary_key=True)

engine = create_engine("sqlite:///students.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

for _ in range(20):
    stud = Students(name_stud = faker.name())
    session.add(stud)
session.commit()

for name in courses_list:
    course = Courses(name_course = name)
    session.add(course)
session.commit()

students = session.query(Students).all()
courses = session.query(Courses).all()
for student in students:

    rand_courses = random.sample(
        courses,
        random.randint(1, 3)
    )

    for course in rand_courses:

        link = St_courses(
            student_id=student.id,
            course_id=course.id
        )

        session.add(link)

session.commit()

new_student = Students(
    name_stud="John Smith"
)

session.add(new_student)
session.commit()


python_course = session.query(Courses).filter_by(
    name_course="Python"
).first()


new_link = St_courses(
    student_id=new_student.id,
    course_id=python_course.id
)

session.add(new_link)
session.commit()

python_students = (
    session.query(Students)
    .join(
        St_courses,
        Students.id == St_courses.student_id
    )
    .join(
        Courses,
        Courses.id == St_courses.course_id
    )
    .filter(
        Courses.name_course == "Python"
    )
    .all()
)

print("\nStudents on Python course:")

for student in python_students:
    print(student.id, student.name_stud)
student_courses = (
    session.query(Courses)
    .join(
        St_courses,
        Courses.id == St_courses.course_id
    )
    .filter(
        St_courses.student_id == new_student.id
    )
    .all()
)

print("\nJohn Smith courses:")

for course in student_courses:
    print(course.id, course.name_course)

student_to_update = session.query(Students).filter_by(
    id=new_student.id
).first()

student_to_update.name_stud = "Alex Smith"

session.commit()

course_to_update = session.query(Courses).filter_by(
    name_course="QA"
).first()

course_to_update.name_course = "QA Automation"

session.commit()

student_to_delete = session.query(Students).filter_by(
    id=new_student.id
).first()

# сначала удаляем его связи с курсами

session.query(St_courses).filter_by(
    student_id=new_student.id
).delete()

# потом самого студента

session.delete(student_to_delete)

session.commit()




