import cv2 
import face_recognition
import os

def dect(loc):
    try:
        cam = cv2.VideoCapture(0) 
        cam.set(3, 1280)
        cam.set(4, 720)
        for i in range(30):
            temp = cam.read()  
        s, img = cam.read()
    except:
        return 2
    if s:   
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        MEDIA_ROOT = os.path.join(BASE_DIR, '') 
        loc = (str(MEDIA_ROOT)+str(loc))
        print(loc)
        
        face_1_image = face_recognition.load_image_file(loc)
        face_1_face_encoding = face_recognition.face_encodings(face_1_image)[0]
        
        small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        check=face_recognition.compare_faces(face_1_face_encoding, face_encodings)
        
        print(check)
        if check[0]:
            return 1
        else :
            return 0  