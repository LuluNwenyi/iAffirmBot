from os import environ
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "This is the iAfirm Bot"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=environ.get('PORT'))
