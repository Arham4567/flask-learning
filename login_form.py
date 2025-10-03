from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('form.html')


@app.route('/login', methods=['POST'])
def submit():
    username = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    if not username or not email or not message:
        return "❌ All fields are required!"

    return render_template('response.html', username=username, email=email, message=message)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True,port=8000)
