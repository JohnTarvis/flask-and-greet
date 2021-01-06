# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/<operation>')
def math(operation):
    a = request.args['a']
    b = request.args['b']
    if operation == 'add':
        return a + b
    elif operation == 'sub':
        return a - b
    elif operation == 'mult':
        return a * b
    elif operation == 'div':
        return a / b