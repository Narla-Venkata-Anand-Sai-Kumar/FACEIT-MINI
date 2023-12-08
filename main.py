from utils.encodes import find_encodings
from Algostructured_new import *
from utils.encodes import *

known_face_encodings, known_face_names = dry_run()

a=Find_attend(known_face_encodings,known_face_names)


def execute_functions():
    current_time = datetime.now().time()
    current_minute = current_time.minute
    final_list = {}
    if current_minute < 30:
        first_half = Find_attend(known_face_encodings, known_face_names)
    elif current_minute >= 31 & current_minute <= 50:
        second_half = Find_attend(known_face_encodings, known_face_names)
    
    for i in second_half:
        if second_half[i] not in first_half:
            pass
        else:
            first_half[i].append(second_half[i])
    return first_half