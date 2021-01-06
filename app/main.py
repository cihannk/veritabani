from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy, inspect
from models import *
num = None
def readjs():
    js = open(r'C:\Users\Cihan\Documents\GitHub\VTRepo\app\templates\main.js', 'r').readlines()
    print(js)

@app.route('/admin')
def Admin():
    all_data_students = Student.query.all()
    all_data_teachers = Teacher.query.all()
    all_data_lectures = Lecture.query.all()
    all_data_homeworks = Homework.query.all()
    return render_template('index.html', students=all_data_students, teachers=all_data_teachers, lectures=all_data_lectures, homeworks=all_data_homeworks)

@app.route('/', methods=['GET', 'POST'])
def giris():
    if request.method == 'POST':
        if request.form['login'] != 'adminis123':
            global num
            num = request.form['login']
            print('num',num)
            return redirect(url_for('student'))
        else:
            return redirect(url_for('Admin'))
    return render_template('giris.html')
@app.route('/hata')
def hata():
    return render_template()

@app.route('/student')
def student():
    data = Student.query.filter_by(no=num).all()
    all_data_students = Student.query.all()
    return render_template('student.html', student=data)

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
            for teacher in Teacher.query.all():
                if request.form.getlist(teacher.firstname):
                    data.teachers.append(teacher)
            for lecture in Lecture.query.all():
                 if request.form.getlist(lecture.name):
                    data.lectures.append(lecture)
            db.session.add(data)
            db.session.commit()
            flash("Ogrenci basariyla eklendi.")   
            return redirect(url_for('Admin'))
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
            for lecture in Lecture.query.all():
                if request.form.getlist(lecture.name):
                    print('heyyo')
                    data.lecture.append(lecture)
            db.session.add(data)
            db.session.commit()
            flash("Ogretmen basariyla eklendi.")   
            return redirect(url_for('Admin'))
        elif cls == 'Lecture':
            no = request.form.get('no') 
            credit = request.form.get('credit')
            name = request.form.get('name')
            teacher = request.form.get('teacher')
            data = Lecture(no=no,name=name, credit=credit)
            for hw in Homework.query.all():
                if request.form.getlist(hw.name):
                    print('heyyo')
                    data.homeworks.append(hw)
            db.session.add(data)
            db.session.commit()
            flash("Ders basariyla eklendi.")   
            return redirect(url_for('Admin'))
        else:
            no = request.form.get('no') 
            name = request.form.get('name')
            deadline = request.form.get('deadline')
            point = request.form.get('point')
            data = Homework(no=no,name=name, deadline=deadline, point=point)
            db.session.add(data)
            db.session.commit()
            flash("Odev basariyla eklendi.")   
            return redirect(url_for('Admin'))

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
        return redirect(url_for('Admin'))
@app.route('/delete/<cls>/<no>/', methods=['GET','POST'])
def delete(no, cls):
    if cls == 'Student':
        data = Student.query.get(no)
        db.session.delete(data)
        db.session.commit()
        flash('Ogrenci basariyla silindi.')
        return(redirect(url_for('Admin')))
    elif cls == 'Teacher':
        data = Teacher.query.get(no)
        db.session.delete(data)
        db.session.commit()
        flash('Ogretmen basariyla silindi.')
        return(redirect(url_for('Admin')))
    elif cls == 'Lecture':
        data = Lecture.query.get(no)
        db.session.delete(data)
        db.session.commit()
        flash('Ders basariyla silindi.')
        return(redirect(url_for('Admin')))
    else:
        data = Homework.query.get(no)
        db.session.delete(data)
        db.session.commit()
        flash('Odev basariyla silindi.')
        return(redirect(url_for('Admin')))

if __name__ == "__main__":
    app.run(debug=True)    