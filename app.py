from flask import *
import csv
import pandas as pd
import get_gpa_data


app = Flask(__name__)

# fd = open("dataSource/uiuc-gpa-dataset-withGPA.csv", 'r')
# csvReader = csv.reader(fd, delimiter=',')
# headers = next(csvReader, None)
df = pd.read_csv("dataSource/uiuc-gpa-dataset-withGPA.csv")
df['Term'] = df['Term'].astype('str')
df['YearTerm'] = df['YearTerm'].astype('str')
df['Subject'] = df['Subject'].astype('str')
df['Course Title'] = df['Course Title'].astype('str')


@app.route('/')
def hello_world():
    return 'Hello World! this is a test website'


# api/course/:subject/:number
@app.route('/api/course/<string:Subject>/<int:Number>', methods=['GET'])
def get_course_gpa(Subject, Number):
    return jsonify(get_gpa_data.get_course_info(Subject.upper(), Number, df))


@app.route('/api/testing', methods=['GET'])
def return_testing_message():
    return jsonify("200 OK")


@app.route('/api/instructor/<string:name>', methods=['GET'])
def get_instructor_gpa(name):
    return "200 OK!"


if __name__ == '__main__':
    app.run()
