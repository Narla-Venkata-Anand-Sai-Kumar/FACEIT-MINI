from utils.encodes import find_encodings
from Algostructured_new import *
from utils.encodes import *
from utils.attendace_write import *
from utils.sheduler import *

known_face_encodings, known_face_names = dry_run()

# a=Find_attend(known_face_encodings,known_face_names)
# 

attendance_data = execute_functions(known_face_encodings,known_face_names)


student_data_file = 'attendance/input.csv'
output_file = 'attendance/output.csv'
student_data = read_student_data(student_data_file)

write_to_csv(attendance_data, student_data, output_file)