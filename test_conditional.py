from flask import Flask
from flask.ext.conditional import conditional

app = Flask(__name__)

@conditional(app.route('/'), True)
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(port=2000, debug=True)
