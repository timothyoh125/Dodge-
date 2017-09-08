import os
from flask import Flask, url_for, render_template, request

app = Flask(__name__)


@app.route('/')
def whack():
    return render_template('pro.html')

if __name__ == "__main__":
    app.run(debug=False, port=5000) 
