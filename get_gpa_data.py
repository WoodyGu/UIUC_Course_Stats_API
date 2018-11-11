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
    if not all_offerings.empty:
        average_gpa = round(all_offerings['Average Grade'].mean(), 2)
        grouped = all_offerings['Average Grade'].groupby(all_offerings['Primary Instructor'])
        instructor_course_gpa = grouped.mean().round(2)
        retval = {}
        retval['Status'] = '200 OK'
        retval['Subject'] = subject
        retval['Number'] = number
        retval['Course Title'] = all_offerings['Course Title'].values.tolist()[0]
        retval['Average GPA'] = average_gpa
        instructor_course_gpa_dict = instructor_course_gpa.to_dict()
        instructor_course_gpa_list = []
        for elem in instructor_course_gpa_dict.items():
            instructor_course_gpa_list.append({'name': elem[0], 'Average Grade': elem[1]})
        retval['Instructors'] = instructor_course_gpa_list
        return retval
    else:
        return None


# schema: {name, average_GPA, course_taught: []}
def get_instructor_info(name, df):
    is_target = df['Primary Instructor'] == name
    all_taught = df[is_target]
    if not all_taught.empty:
        average_gpa = round(all_taught['Average Grade'].mean(), 2)
        grouped = all_taught.groupby(['Subject', 'Number'], as_index=False)
        instructor_course_gpa = grouped['Average Grade'].mean().round(2)
        retval = {}
        retval['Status'] = '200 OK'
        retval['Name'] = name
        retval['Average GPA'] = average_gpa
        instructor_course_gpa_dict = instructor_course_gpa.to_dict('records')
        retval['Course Taught'] = instructor_course_gpa_dict
        return retval
    else:
        return None
