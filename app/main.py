from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from models import *


@app.route('/')
def Index():
    all_data_students = Student.query.all()
    all_data_teachers = Teacher.query.all()
    all_data_lectures = Lecture.query.all()
    all_data_homeworks = Homework.query.all()
    return render_template('index.html', students=all_data_students, teachers=all_data_teachers, lectures=all_data_lectures, homeworks=all_data_homeworks)

@app.route('/giris')
def giris():
    login = request.form.get('login')
    if login == 'admin':
        return redirect(url_for('Index'))
    return render_template('giris.html')

@app.route('/student')
def redirect():
    return render_template('student.html')

@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        cls = request.form.get('cls')
        if cls == 'Student':
            no = request.form.get('no') 
            fname = request.form.get('fname')
            lname = request.form.get('lname')
            age = request.form.get('age') 
            relative = request.form.get('relative') 
            address = request.form.get('address')
            data = Student(no=no,firstname=fname, lastname=lname, age=age, relative=relative, address=address) 
            db.session.add(data)
            db.session.commit()
            flash("Ogrenci basariyla eklendi.")   
            return redirect(url_for('Index'))
        elif cls == 'Teacher':
            no = request.form.get('no') 
            fname = request.form.get('fname')
            lname = request.form.get('lname')
            age = request.form.get('age') 
            relative = request.form.get('relative') 
            address = request.form.get('address')
            profession = request.form.get('profession')
            telno = request.form.get('telno')
            data = Teacher(no=no,firstname=fname, lastname=lname, age=age, profession=profession, telno=telno, relative=relative, address=address) 
            db.session.add(data)
            db.session.commit()
            flash("Ogretmen basariyla eklendi.")   
            return redirect(url_for('Index'))
        elif cls == 'Lecture':
            no = request.form.get('no') 
            credit = request.form.get('credit')
            name = request.form.get('name')
            teacher = request.form.get('teacher')
            homeworks = request.form.get('homeworks')
            data = Lecture(no=no,name=name, credit=credit)
            db.session.add(data)
            db.session.commit()
            flash("Ders basariyla eklendi.")   
            return redirect(url_for('Index'))
        else:
            no = request.form.get('no') 
            name = request.form.get('name')
            deadline = request.form.get('deadline')
            point = request.form.get('point')
            data = Homework(no=no,name=name, deadline=deadline, point=point)
            db.session.add(data)
            db.session.commit()
            flash("Odev basariyla eklendi.")   
            return redirect(url_for('Index'))

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        cls = request.form['cls']
        if cls == 'Student':
            data = Student.query.get(request.form.get('no'))
            data.firstname = request.form.get('fname')
            data.lastname = request.form.get('lname')
            data.no = request.form.get('no')
            data.age = request.form.get('age')
            data.relative = request.form.get('relative')
            data.address = request.form.get('address')
        elif cls == 'Teacher':
            data = Teacher.query.get(request.form.get('no'))
            data.profession = request.form.get('profession')
            data.telno = request.form.get('telno')
            #data.lecture = request.form.get('lecture')
            data.firstname = request.form.get('fname')
            data.lastname = request.form.get('lname')
            data.no = request.form.get('no')
            data.age = request.form.get('age')
            data.relative = request.form.get('relative')
            data.address = request.form.get('address')
        elif cls == 'Lecture':
            data = Lecture.query.get(request.form.get('no'))
            data.name = request.form.get('name')
            data.credit = request.form.get('credit')
            data.no = request.form.get('no')
        else:
            data = Homework.query.get(request.form.get('no'))
            data.name = request.form.get('name')
            data.deadline = request.form.get('deadline')
            data.point = request.form.get('point')
        
        db.session.commit()
        flash("Basarıyla ogretmen eklendi")
        return redirect(url_for('Index'))
@app.route('/delete/<cls>/<no>/', methods=['GET','POST'])
def delete(no, cls):
    if cls == 'Student':
        data = Student.query.get(no)
        db.session.delete(data)
        db.session.commit()
        flash('Ogrenci basariyla silindi.')
        return(redirect(url_for('Index')))
    elif cls == 'Teacher':
        data = Teacher.query.get(no)
        db.session.delete(data)
        db.session.commit()
        flash('Ogretmen basariyla silindi.')
        return(redirect(url_for('Index')))
    elif cls == 'Lecture':
        data = Lecture.query.get(no)
        db.session.delete(data)
        db.session.commit()
        flash('Ders basariyla silindi.')
        return(redirect(url_for('Index')))
    else:
        data = Homework.query.get(no)
        db.session.delete(data)
        db.session.commit()
        flash('Odev basariyla silindi.')
        return(redirect(url_for('Index')))

if __name__ == "__main__":
    app.run(debug=True)    