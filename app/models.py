from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os
from sqlalchemy.orm import relationship

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "ubys.db"))

app = Flask(__name__)
app.secret_key = "secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = database_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Many-To-Many icin yardimci tablo
student_teacher = db.Table('StudentTeacher',
        db.Column('student_no', db.Integer, db.ForeignKey('student.no')),
        db.Column('teacher_no', db.Integer, db.ForeignKey('teacher.no')) )

student_lecture = db.Table('StudentLecture',
        db.Column('student_no', db.Integer, db.ForeignKey('student.no')),
        db.Column('lecture_no', db.Integer, db.ForeignKey('lecture.no')) )


class Student(db.Model):

    no = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(200), nullable= False)
    lastname = db.Column(db.String(200), nullable= False)
    age = db.Column(db.Integer)
    relative = db.Column(db.String(200))
    address = db.Column(db.String(200))
    teachers = db.relationship('Teacher', secondary=student_teacher, lazy='dynamic', backref=db.backref('students', lazy='dynamic'))
    lectures = db.relationship('Lecture', secondary=student_lecture, lazy='dynamic', backref=db.backref('students', lazy='dynamic'))
    def __repr__(self):
        return self.firstname
class Teacher(db.Model):

    no = db.Column(db.Integer, primary_key =True)
    firstname = db.Column(db.String(200), nullable= False)
    lastname = db.Column(db.String(200), nullable= False)
    age = db.Column(db.Integer)
    profession = db.Column(db.String(200), nullable= False)
    telno = db.Column(db.Integer)
    relative = db.Column(db.String(200))
    address = db.Column(db.String(200))
    lecture_name = db.Column(db.String(200), db.ForeignKey('lecture.name'))
    lecture = db.relationship('Lecture', 
                            back_populates='teacher', uselist=False)
    def __repr__(self):
        return self.firstname


class Lecture(db.Model):
    no = db.Column(db.Integer, primary_key=True)
    credit = db.Column(db.Integer, nullable= False)
    name = db.Column(db.String(200), nullable=False)
    homeworks = relationship("Homework",backref="lecturen", lazy=True)
    teacher = db.relationship('Teacher', back_populates = 'lecture', uselist=False)
    def __repr__(self):
        return self.name


class Homework(db.Model):
    name = db.Column(db.String(200), nullable=False)
    no = db.Column(db.Integer, primary_key =True)
    deadline = db.Column(db.String(200))
    point = db.Column(db.Integer, nullable= False)
    lecture = db.Column(db.Integer, db.ForeignKey('lecture.name'))
    teacher_name = db.Column(db.Integer, db.ForeignKey('teacher.firstname'))
    teacher = relationship("Teacher",backref="homeworks", lazy=True)
    def __repr__(self):
        return self.name


db.create_all()

