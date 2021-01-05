'''

from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from models import *
#db.create_all()
global ogr

Student.query.delete()
Teacher.query.delete()
Lecture.query.delete()
Homework.query.delete()

student1 = Student(no=34534345345,firstname='Akif', lastname='Selbi', age=21, relative='hasan asd', address='asdkjghas asdkljashld')
student2 = Student(no=167867867783,firstname='Cihan', lastname='Kavuk', age=21, relative='hasan asasdasd', address='asdkjghasdaas asdkljashld')
teacher1 = Teacher(no= 123687345602,firstname='İsmail', lastname='Kahraman',age=46, profession= 'Veri Tabanı', telno=123123123, relative='asda asdas', address= 'asdfjgsd sdodfsıds sdf')
teacher2 = Teacher(no=5673569897, firstname='Utku', lastname='Bayram', profession= 'Elektrik', telno=12311231233123, relative='asda aasdsdas', address= 'asdfjgsd sdodfsıdsasfd sdf', age=34)
lecture1 = Lecture(no=67867967897,credit=2322323, name='Veri tabani')
lecture2 = Lecture(no=7897897878, credit=3232, name='Elektrik')
homework1 = Homework(no=45645646456, deadline='12 ocak', name='Veri tabanı proje', point='20')
homework2 = Homework(no=2342342423432, deadline='11 ocak', name='Elektrik ders tekrarı', point='20')

db.session.add_all([student1, student2, teacher1, teacher2, lecture1, lecture2, homework1, homework2])
db.session.commit()

student1.teachers.append(teacher1)
student1.teachers.append(teacher2)
student2.teachers.append(teacher1)


@app.route('/', methods=['GET', 'POST'])
def show_all():
   if request.form:
        student = Student(no=request.form.get("no"), firstname=request.form.get("firstname"), lastname=request.form.get("lastname"), age=request.form.get("age"), relative=request.form.get("relative"), address=request.form.get("address"),)
        db.session.add(student)
        db.session.commit() 
   return render_template('index.html')

@app.route('/kayitlar',methods=["POST","GET"])
def records():
   students = Student.query.all() 
   return render_template('records.html', students=students) 

@app.route("/delete", methods=["POST"])
def delete():
   book = Ogrenci.query.filter_by(no=ogrno).first()
   print("book: ", book)
   db.session.delete(book)
   db.session.commit()
   return redirect("/")

@app.route("/giris", methods=["POST","GET"])
def giris():
   if request.form:
      sifre = request.form.get('sifre')
      ogr = Student.query.filter_by(no=sifre).all()
      ogrinfo = ogr[0]
      session["logged_in"] = True
      session["ogr_id"] = ogrinfo.id
      return redirect(url_for("kayitlar"))
   return render_template('index copy.html')
if __name__ == '__main__':
    app.run(debug=True)

@app.route("/renderogr")
def renderogr(ogr):
   return render_template('renderogr.html', students=ogr) 
   '''