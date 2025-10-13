from flask import Flask, render_template,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key="Arham"
#Home page
@app.route('/')
def index():
    return render_template('home.html')

#Thank You page
@app.route("/thank_you/<username>")
def thank_you(username):
    return render_template('thank_you.html',username=username)

#Showing Feedback Page
@app.route('/show_feedback')
def show_feedback():
    feedbacks = Feedback.query.all()
    return render_template('show_feedback.html', feedbacks=feedbacks)

#Edit record from database

class EditDatabase(FlaskForm):
    id=StringField('id', validators=[DataRequired()])
    name=StringField('name', validators=[DataRequired()])
    email=StringField('email', validators=[DataRequired()])
    message=TextAreaField('message', validators=[DataRequired()])
    submit=SubmitField('Update')


@app.route("/edit_feedback", methods=['GET', 'POST'])
def edit_feedback():
    form = EditDatabase()
    if form.validate_on_submit():
        fedback = Feedback.query.get(form.id.data)
        if fedback :
            fedback.username = form.name.data
            fedback.email = form.email.data
            fedback.message = form.message.data
            db.session.commit()
            feedbacks = Feedback.query.all()
            return redirect(url_for('show_feedback', feedbacks=feedbacks))
        else :
             return "Feedback record not found",404
    return render_template('edit_database.html',form=form)

# Deleting record
class DeleteRecord(FlaskForm):
    id=StringField('id', validators=[DataRequired()])
    submit=SubmitField('Delete')

@app.route("/delete_feedback", methods=['GET', 'POST'])
def delete_feedback():
    form = DeleteRecord()
    if form.validate_on_submit():
        delete= Feedback.query.get(form.id.data)
        if delete:
            db.session.delete(delete)
            db.session.commit()
            feedbacks = Feedback.query.all()
            return redirect(url_for('show_feedback', feedbacks=feedbacks))
        else:
            return "Feedback record not found",404
    return render_template('delete_record.html',form=form)


# ________________________Adding database___________________________

# step1 : database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
db = SQLAlchemy(app)

# step2 : create database model i.e. defining what rows should be included in the SQL table
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

# Making a WTForm  including validators . it will only define fields with their labels
class FeedbackForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit')


# It will actually take input from user and store them in the database
@app.route('/feedback',methods=("GET","POST"))
def feedback():
    form = FeedbackForm()
    if form.validate_on_submit():
        new_feedback = Feedback(
            username=form.username.data,
            email=form.email.data,
            message=form.message.data
        )
        db.session.add(new_feedback)
        db.session.commit()
        return redirect(url_for('thank_you', username=form.username.data))
    return render_template('feedback.html',form=form)




if __name__ == '__main__':
    app.run(debug=True ,port=3001)
