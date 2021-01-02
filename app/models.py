from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

class Ogrenci(UserMixin, db.Model):
    """ Ogrenci tablosu """
    __tablename__ = 'ogrenciler'

    ogr_no = db.Column(db.Integer, primary_key=True)
    ogr_firstname = db.Column(db.String(200), nullable= False)
    ogr_lastname = db.Column(db.String(200), nullable= False)
    ogr_age = db.Column(db.Integer, nullable= False)
    ogr_relative = db.Column(db.String(200), nullable= True)
    ogr_address = db.Column(db.String(200), nullable= False)

class Lecture(UserMixin, db.Model):
    __tablename__ = 'lectures'

    lecture_teacher = db.Column(db.String(200), nullable= False)
    lecture_credit = db.Column(db.Integer, nullable= False)
    lecture_name = db.Column(db.String(200), primary_key= True)

class Teacher(UserMixin, db.Model):
    __tablename__ = 'teacher'

    teacher_no = db.Column(db.Integer, primary_key =True)
    teacher_firstname = db.Column(db.String(200), nullable= False)
    teacher_lastname = db.Column(db.String(200), nullable= False)
    teacher_age = db.Integer(db.String(200), nullable= False)
    teacher_profession = db.Column(db.String(200), nullable= False)
    teacher_telno = db.Integer(db.String(200), nullable= False)
    teacher_relative = db.Column(db.String(200), nullable= False)
    teacher_address = db.Column(db.String(200), nullable= False)

class Homework(UserMixin, db.Model):
    __tablename__ = 'hw'
    
    hw_lecture = db.Column(db.String(200), primary_key= True)
    hw_deadline = db.Column(db.String(200), nullable= False)
    hw_type = db.Column(db.String(200), nullable= False)
    hw_belonging = db.Column(db.String(200), nullable= False)
    hw_point = db.Column(db.Integer, nullable= False)
