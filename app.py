from flask import Flask, render_template, request,flash

app = Flask(__name__)
app.secret_key = 'Programmer Saiyam'

@app.route('/')
def main_page():
    flash("What is your name?")
    return render_template('index.html')

@app.route('/greet', methods=['POST', 'GET'])
def greet():
     flash("Hello " + str(request.form['name']) + "!")
     return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)