
from flask import Flask

#Make the actual Application
app = Flask(__name__)

#Make the route
@app.route("/")

#Define a function
def hello():
    return "Hello beautiful world!"

