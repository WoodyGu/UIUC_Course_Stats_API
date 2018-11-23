from flask import *
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
df['Course_Title'] = df['Course_Title'].astype('str')
df['Primary_Instructor'] = df['Primary_Instructor'].astype('str')


@app.route('/')
def hello_world():
    return 'Hello World! this is a test website'


# api/course/:subject/:number
@app.route('/api/course/<string:Subject>/<int:Number>', methods=['GET'])
def get_course_gpa(Subject, Number):
    retval = get_gpa_data.get_course_info(Subject.upper(), Number, df)
    if retval is None:
        abort(404)
        abort(Response("Cannot Find Course Info for " + Subject + " " + str(Number)))
    else:
        return jsonify(retval)


@app.route('/api/course/detail/<string:Subject>/<int:Number>/<string:Instructor>', methods=['GET'])
def get_course_detail(Subject, Number, Instructor):
    retval = get_gpa_data.get_course_gpa_detail(Subject.upper(), Number, Instructor, df)
    if retval is None:
        abort(404)
        abort(Response("Cannot Find Course Info for " + Subject + " " + str(Number)))
    else:
        return jsonify(retval)


@app.route('/api/testing', methods=['GET'])
def return_testing_message():
    return jsonify("200 OK")


@app.route('/api/instructor/<string:name>', methods=['GET'])
def get_instructor_gpa_accurate(name):
    retval = get_gpa_data.get_instructor_info(name, df)
    if retval is None:
        abort(404)
        abort(Response("Cannot Find Instructor Info for " + name))
    else:
        return jsonify(retval)

@app.route('/api/subjects', methods=['GET'])
def get_department_list():
    retval = get_gpa_data.generate_depart_list(df)
    if retval is None:
        abort(404)
        abort(Response("Cannot Find Instructor Info for " + name))
    else:
        return jsonify(retval)


if __name__ == '__main__':
    app.run()
