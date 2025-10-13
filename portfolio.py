from flask import Flask,request,render_template

app = Flask(__name__)
@app.route('/')
def portfolio():
    return render_template('portfolio.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True,port=7000)