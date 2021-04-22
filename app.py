from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!\nNick was here 2021'

print("Nick was here 2021")
