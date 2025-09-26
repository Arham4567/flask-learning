from flask import Flask#,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Its home page"  #render_template('index.html')

@app.route('/products')
def products(): 
    return "This is products page"


@app.route('/view')
def view(): 
    return "This is view page"

@app.route('/user/<username>')

def user_profile(username):
    return {"username": username, "message": f"Welcome {username}!"}

if __name__ == '__main__':
    app.run(debug=True,port=8000)
