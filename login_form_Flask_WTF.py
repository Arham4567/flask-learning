from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key="mysecretkey"
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password',validators=[DataRequired()])
    submit = SubmitField('Login')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return f"Hello {form.username.data}, you are logged in !"
    return render_template('login.html', form=form)

@app.route("/")
def home():
    return render_template('button.html')
if __name__ == "__main__":
    app.run(debug=True ,port=3000)