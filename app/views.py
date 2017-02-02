from flask import render_template, flash, redirect, request
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('index.html')

@app.route('/website')
def website():
    return render_template('website.html')

@app.route('/send', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        website = request.form['website']

        return render_template('index.html', webpage=website)

    return render_template('website.html')

if __name__ == "__main__":
    app.run()

