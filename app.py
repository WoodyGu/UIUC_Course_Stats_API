from flask import Flask
import csv
from get_gpa_data import *
app = Flask(__name__)

fd = open("dataSource/uiuc-gpa-dataset.csv", 'r')
csvReader = csv.reader(fd, delimter='')


@app.route('/')
def hello_world():
    return 'Hello World! this is a test website'


@app.route('/api/course', methods=['GET'])
def get_course_gpa():
    return get_course_gpa.get_frist_row(csvReader)


@app.route('/api/testing', methods=['GET'])
def return_testing_message():
    return "200 OK!"


if __name__ == '__main__':
    app.run()
