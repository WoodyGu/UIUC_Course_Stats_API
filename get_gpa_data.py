import csv
import pandas as pd
from flask import *


def get_frist_row(csvReader):
    retval = ""
    for row in csvReader:
        retval = row
        break
    return jsonify(retval)


# schema: {subject, number, course name, average gpa, [{instructor A: GPA}, {instructor B: GPA}....}]}
def get_course_info(subject, number, df):
    is_target = (df['Subject'] == subject) & (df['Number'] == number)
    all_offerings = df[is_target]
    average_gpa = round(all_offerings['Average Grade'].mean(), 2)
    grouped = all_offerings['Average Grade'].groupby(df['Primary Instructor'])
    instructor_course_gpa = grouped.mean().round(2)
    retval = {}
    retval['Subject'] = subject
    retval['Number'] = number
    retval['Course Title'] = all_offerings['Course Title'].values.tolist()[0]
    retval['Average GPA'] = average_gpa
    retval['Instructors'] = instructor_course_gpa.to_dict()
    return retval
