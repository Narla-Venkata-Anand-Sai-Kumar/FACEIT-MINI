import csv
from datetime import datetime

def time_diff_in_minutes(start_time, end_time):
    format_str = "%H:%M:%S"
    start = datetime.strptime(start_time, format_str)
    end = datetime.strptime(end_time, format_str)
    diff_seconds = (end - start).total_seconds()
    diff_minutes = diff_seconds / 60
    return int(diff_minutes)

def read_student_data(file_path):
    student_data = []
    with open(file_path, 'r', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Remove the BOM character if present in column names
            corrected_row = {key.replace('\ufeff', ''): value for key, value in row.items()}
            student_data.append(corrected_row)
    print(student_data)
    return student_data

def write_to_csv(attendance_data, student_data, output_file):
    student_dict = {student['rollno']: student for student in student_data}

    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['Name','Roll No', 'InTime', 'OutTime', 'Email', 'TimeDifference']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for roll_no, times in attendance_data.items():
            name = student_dict[roll_no]['name']
            email = student_dict[roll_no]['email']
            intime = times[0]
            outtime = times[0]
            difference = None
            if intime and outtime:
                difference = time_diff_in_minutes(intime, outtime)

            writer.writerow({
                'Name': roll_no,
                'Roll No': name,
                'InTime': intime,
                'OutTime': outtime,
                'Email': email,
                'TimeDifference': difference if difference is not None else 'Not Available'
            })

