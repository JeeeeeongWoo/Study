from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login_check',methods = ['post'])
def login_confirm():
    id_ = request.form['id_']
    pw_ = request.form['pw_']
    if id_ == '123' and pw_ == '123':
        return redirect(url_for('portfolio'))
    else:
        return redirect(url_for('fail'))



if __name__=='__main__':
    app.run(debug=True)

