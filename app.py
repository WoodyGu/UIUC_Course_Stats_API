from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World! this is a test website'


if __name__ == '__main__':
    app.run()
