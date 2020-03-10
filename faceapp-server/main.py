from flask import Flask

app=Flask(__name__)

@app.route(rule='/')
def index():
    return "Hello Universe"

@app.route(rule='/getuser')
def getuser():
    a={}
    a.name='abcd'
    a.roll=10

    return a
