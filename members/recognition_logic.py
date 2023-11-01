# members/recognition_logic.py

import cv2
import face_recognition

def recognize_faces(input_frame, known_faces, known_names):
    # Implement the face recognition logic here

    # Example recognition logic
    processed_frame = input_frame.copy()
    face_locations = face_recognition.face_locations(processed_frame)
    for (top, right, bottom, left) in face_locations:
        # Draw a rectangle around the recognized face
        cv2.rectangle(processed_frame, (left, top), (right, bottom), (0, 255, 0), 2)
        
        # Recognize the face and add the name if recognized
        face_encodings = face_recognition.face_encodings(processed_frame, [(top, right, bottom, left)])
        for face_encoding, known_name in zip(face_encodings, known_names):
            matches = face_recognition.compare_faces(known_faces, face_encoding)
            if any(matches):
                cv2.putText(processed_frame, known_name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    
    return processed_frame
