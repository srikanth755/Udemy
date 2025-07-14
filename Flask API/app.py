from flask import Flask
'''This WSGI instance is our Web Server Gateway Interface app'''

WSGI_app = Flask(__name__)

@WSGI_app.route("/")
def welcome():
    return "Hi How r u? What r u dng?"

@WSGI_app.route("/index")
def index():
    return "This is index page"

if __name__ == "__main__":
    WSGI_app.run(debug = True)