import csv
from flask import *


def get_frist_row(csvReader):
    retval = ""
    for row in csvReader:
        retval = row
        break
    return jsonify(retval)
