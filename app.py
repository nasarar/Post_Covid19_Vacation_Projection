#Import Dependencies 
from flask import Flask

#Create a new flask app
app= Flask(__name__)

#Create Flask Routes
@app.route('/')
def hello_world():
    return 'Hello world'
