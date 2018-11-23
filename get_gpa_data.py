import csv
import pandas as pd
from flask import *


def get_first_row(csvReader):
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
        average_gpa = round(all_offerings['Average_Grade'].mean(), 2)
        grouped = all_offerings['Average_Grade'].groupby(all_offerings['Primary_Instructor'])
        instructor_course_gpa = grouped.mean().round(2)
        retval = {}
        retval['Status'] = '200 OK'
        retval['Subject'] = subject
        retval['Number'] = number
        retval['Course_Title'] = all_offerings['Course_Title'].values.tolist()[0]
        retval['Average_GPA'] = average_gpa
        instructor_course_gpa_dict = instructor_course_gpa.to_dict()
        instructor_course_gpa_list = []
        for elem in instructor_course_gpa_dict.items():
            instructor_course_gpa_list.append({'name': elem[0], 'Average_Grade': elem[1]})
        retval['Instructors'] = instructor_course_gpa_list
        return retval
    else:
        return None


def generate_grade_distbution_dict(all_offerings):
    total_Apls = all_offerings['A+'].sum().astype('str')
    total_A = all_offerings['A'].sum().astype('str')
    total_Amin = all_offerings['A-'].sum().astype('str')
    total_Bpls = all_offerings['B+'].sum().astype('str')
    total_B = all_offerings['B'].sum().astype('str')
    total_Bmin = all_offerings['B-'].sum().astype('str')
    total_Cpls = all_offerings['C+'].sum().astype('str')
    total_C = all_offerings['C'].sum().astype('str')
    total_Cmin = all_offerings['C-'].sum().astype('str')
    total_Dpls = all_offerings['D+'].sum().astype('str')
    total_D = all_offerings['D'].sum().astype('str')
    total_Dmin = all_offerings['D-'].sum().astype('str')
    total_F = all_offerings['F'].sum().astype('str')
    distribution = {}
    distribution['A+'] = int(total_Apls)
    distribution['A'] = int(total_A)
    distribution['A-'] = int(total_Amin)
    distribution['B+'] = int(total_Bpls)
    distribution['B'] = int(total_B)
    distribution['B-'] = int(total_Bmin)
    distribution['C+'] = int(total_Cpls)
    distribution['C'] = int(total_C)
    distribution['C-'] = int(total_Cmin)
    distribution['D+'] = int(total_Dpls)
    distribution['D'] = int(total_D)
    distribution['D-'] = int(total_Dmin)
    distribution['F'] = int(total_F)
    return distribution


def get_course_gpa_detail(subject, number, instructor, df):
    is_target = (df['Subject'] == subject) & (df['Number'] == number) & (df['Primary_Instructor'] == instructor)
    all_offerings = df[is_target]
    if not all_offerings.empty:
        average_gpa = round(all_offerings['Average_Grade'].mean(), 2)
        retval = {}
        retval['Status'] = '200 OK'
        retval['Subject'] = subject
        retval['Number'] = number
        retval['Course_Title'] = all_offerings['Course_Title'].values.tolist()[0]
        retval['Average_GPA'] = average_gpa
        retval['Instructors'] = instructor
        retval['Grade_Distribution'] = generate_grade_distbution_dict(all_offerings)
        retval['Offered_Semesters'] = all_offerings['YearTerm'].drop_duplicates().values.tolist()
        print(retval)
        return retval
    else:
        return None


# schema: {name, average_GPA, course_taught: []}
def get_instructor_info(name, df):
    is_target = df['Primary_Instructor'] == name
    all_taught = df[is_target]
    if not all_taught.empty:
        average_gpa = round(all_taught['Average_Grade'].mean(), 2)
        grouped = all_taught.groupby(['Subject', 'Number'], as_index=False)
        instructor_course_gpa = grouped['Average_Grade'].mean().round(2)
        retval = {}
        retval['Status'] = '200 OK'
        retval['Name'] = name
        retval['Average_GPA'] = average_gpa
        instructor_course_gpa_dict = instructor_course_gpa.to_dict('records')
        retval['Course_Taught'] = instructor_course_gpa_dict
        return retval
    else:
        return None

def generate_depart_list(df):
    department_list = df['Subject']
    retval = department_list.drop_duplicates().tolist()
    return retval