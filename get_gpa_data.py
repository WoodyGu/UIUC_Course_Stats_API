import csv


def get_frist_row(csvReader):
    retval = ""
    for row in csvReader:
        retval = row
        break
    return retval