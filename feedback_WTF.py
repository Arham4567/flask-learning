from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key="Arham"

class FeedbackForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/feedback',methods=("GET","POST"))
def feedback():
    form = FeedbackForm()
    if form.validate_on_submit():
        return f"welcome {form.username.data}!,thank you for your feedback message {form.message.data}"
    return render_template('feedback.html', form=form)

if __name__ == '__main__':
    app.run(debug=True ,port=3001)
