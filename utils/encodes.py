import cv2
import face_recognition
import json
import numpy as np
import os

def find_encodings(images):
    encode_list = []
    for img in images:
        encode = face_recognition.face_encodings(img, model="large")[0]
        encode_list.append(encode)
    return encode_list

def save_encodings(encodings, filename):
    encodings_serializable = [enc.tolist() for enc in encodings]
    with open(filename, 'w') as file:
        json.dump(encodings_serializable, file)
        print("Encoding complete!")


def load_encodings(filename):
    with open(filename, 'r') as file:
        encodings_serializable = json.load(file)
        encodings = [np.array(enc) for enc in encodings_serializable]
    return encodings


def dry_run():
    path = "MCW-LABELLED-PICTURES"
    images = []
    classNames = []
    myList = os.listdir(path)
    for cl in myList:
        cur_img = cv2.imread(f'{path}/{cl}')
        images.append(cur_img)
        classNames.append(os.path.splitext(cl)[0])
    encodings_file = 'face_encodings.json'
    if not os.path.exists(encodings_file):
        known_face_encodings = find_encodings(images)
        save_encodings(known_face_encodings, encodings_file)
    else:
        known_face_encodings = load_encodings(encodings_file)

    known_face_names = classNames
    
    return known_face_encodings, known_face_names