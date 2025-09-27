from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return {"message": "Day 3 – Learning POST requests!"}

# Route to accept data from user
@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form.get('name')
        return {"message": f"Hello {name}, welcome to Flask Day 3!"}
    return '''
        <form method="POST">
            <input type="text" name="name" placeholder="Enter your name" />
            <input type="submit" value="Greet Me" />
        </form>
    '''

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == "Arham" and password == "123":
            return {"message": f"Hello {username}, good to see you again!", "status": "Login successful"}
        else:
            return {"status":"Invalid username or password"  }
    return '''
        <form method="POST">
            <input type="text" name="username" placeholder="Enter your username" />
            <input type="password" name="password" placeholder="Enter your password" />
            <input type="submit" value="Login" />
        </form>
    '''

@app.route('/square', methods=['GET', 'POST'])
def square():
    if request.method == 'POST':
        try:
            square_number = int(request.form.get('squareNumber'))
            return {"input": square_number, "square": square_number * square_number}
        except (ValueError, TypeError):
            return {"error": "Please enter a valid number"}
    return '''
        <form method="POST">
            <input type="text" name="squareNumber" placeholder="Enter a number" />
            <input type="submit" value="Square" />
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
