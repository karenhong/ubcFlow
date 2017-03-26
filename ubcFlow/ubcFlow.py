from flask import Flask, abort, flash, session, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI, SECRET_KEY

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.secret_key = SECRET_KEY

db = SQLAlchemy(app)

class User(db.Model):
    email = db.Column(db.String(120), primary_key = True)
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
    title = db.Column(db.String(100))
    message = db.Column(db.String(300))
    user = db.Column(db.Integer, db.ForeignKey('user.email'))
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
            new_user = User(email=request.form['email'], firstName=request.form['f_name'], lastName=request.form['l_name'], password=request.form['password'])
            db.session.add(new_user)
            db.session.commit()
            session['email'] =  new_user.email
            return redirect(url_for('main'))
        else:
            error = 'There is already an account with that email'
    return render_template('signup.html', error=error)

@app.route('/logout')
def logout():
    session.pop('email', None)
    flash('You were logged out')
    return redirect(url_for('main'))

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if user is None or user.password != request.form['password']:
            flash('Please check your email and password and try again.', 'error')
        else:
            session['email'] = user.email
            flash('You were successfully logged in', 'success')
        return redirect(url_for('main'))

@app.route('/<code>')
def view_course(code):
    course = Course.query.filter_by(code=code).first()
    reviews = Review.query.filter_by(course_code=code).all()
    user = User.query.filter_by(email=session.get('email')).first()
    return render_template('course.html', course=course, reviews=reviews, user=user)

@app.route('/add<code>', methods=['POST'])
def add_review(code):
    if not session.get('email'):
        flash('Please login to add a comment', 'error')
    else:
        flash('New review was successfully posted', 'success')
        review = Review(message=request.form['message'], title=request.form['title'], user=session['email'], rating=request.form['rating'], course_code=code)
        db.session.add(review)
        db.session.commit()
    return redirect(url_for('view_course', code=code))

@app.route('/search', methods=['POST'])
def search_course():
    if request.method == 'POST':
        course = Course.query.filter_by(code=request.form['code']).first()
        if course is None:
            flash('No courses with that code found', 'error')
            return render_template('index.html')
        else:
            return render_template('index.html', courses=[course])

@app.route('/edit<review_id>', methods=['POST'])
def edit_review(review_id):
    review = Review.query.filter_by(id=review_id).first()
    if request.method == 'POST':
        review.title = request.form['edit_title']
        review.message = request.form['edit_message']
        review.rating = request.form['edit_rating']
        db.session.commit()
    return redirect(url_for('view_course', code=review.course_code))

@app.route('/delete<review_id>')
def delete_review(review_id):
    review = Review.query.filter_by(id=review_id).first()
    db.session.delete(review)
    db.session.commit()
    return redirect(url_for('view_course', code=review.course_code))

if __name__ == '__main__':
    app.debug = True
    app.run()
