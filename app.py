from flask import Flask, request,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html',name="Arham")

@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html',username=username)


# Route to accept data from user
@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form.get('name')
        return {"message": f"Hello {name}"}
    return render_template('greet.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == "Arham" and password == "123":
            return {"message": f"Hello {username}, good to see you again!", "status": "Login successful"}
        else:
            return {"status":"Invalid username or password"  }
    return render_template('login.html')

@app.route('/square', methods=['GET', 'POST'])
def square():
    if request.method == 'POST':
        try:
            square_number = int(request.form.get('squareNumber'))
            return {"input": square_number, "square": square_number * square_number}
        except (ValueError, TypeError):
            return {"error": "Please enter a valid number"}
    return render_template("square.html")

@app.route('/cube/<int:number>')
def cube(number):
    org=number
    number = number*number*number
    return render_template("cube.html", number=number,org=org)

@app.route('/age/<int:age>')
def age(age):
    return render_template('age.html', age=age,name="Arham")

@app.route('/friends')
def friends():
    return render_template('friends.html',friends=['Arham','Asad','Ibrahim'])

@app.route('/number')
def number():
    return render_template('numbers.html',numbers=[1,2,3,4,5,6,7,8,9])
if __name__ == '__main__':
    app.run(debug=True)
