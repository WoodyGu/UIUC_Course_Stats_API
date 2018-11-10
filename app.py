from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World! this is a test website'


@app.route('/api/testing', methods=['GET'])
def return_testing_message():
    return "200 OK!"


if __name__ == '__main__':
    app.run()
