from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

NEXT_ID = 0
TODOS = {}

@app.route('/create/<name>')
def create(name):
    global NEXT_ID
    TODOS[NEXT_ID] = {'name': name, 'done': False}
    NEXT_ID += 1
    return TODOS

print("Nick was here 2021")
print(" Dan was here 2021")
