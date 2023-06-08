#from flask import Flask
#app = Flask(__name__)

#@app.route("/")

#def home():
#    return "Hello, Flask!"

from website import app
if __name__ == '__main__':
    app.run(debug=True)
