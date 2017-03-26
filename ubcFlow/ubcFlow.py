from flask import Flask, session, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI, SECRET_KEY

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.secret_key = SECRET_KEY

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(120), unique=True)
    firstName = db.Column(db.String(20))
    lastName = db.Column(db.String(20))
    password = db.Column(db.String(20))

class Course(db.Model):
    code = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(20))
    description = db.Column(db.String(300))
    year = db.Column(db.Integer)


class Review(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    rating = db.Column(db.Integer)
    message = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    course_code = db.Column(db.Integer, db.ForeignKey('course.code'))

db.create_all()

@app.route('/')
def main():
    courses = Course.query.all()
    return render_template('index.html', courses=courses)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        exists = User.query.filter_by(email=request.form['email']).first()
        if exists is None:
            session['logged_in'] = True
            new_user = User(email=request.form['email'], firstName=request.form['f_name'], lastName=request.form['l_name'], password=request.form['password'])
            db.session.add(new_user)
            db.session.commit()
            return render_template('index.html')
        else:
            error = 'There is already an account with that email'
    return render_template('signup.html', error=error)

if __name__ == '__main__':
    app.debug = True
    app.run()
