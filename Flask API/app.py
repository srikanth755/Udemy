from flask import Flask, render_template
'''This WSGI instance is our Web Server Gateway Interface app'''

WSGI_app = Flask(__name__)

@WSGI_app.route("/")
def welcome():
    return "Hi How r u? What r u dng?"

# Rendering the html page 
@WSGI_app.route("/index")
def index():
    return render_template('index.html')

@WSGI_app.route("/about")
def about():
    return render_template('index.html')

if __name__ == "__main__":
    WSGI_app.run(debug = True)