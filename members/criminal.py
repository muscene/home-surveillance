import cv2
import numpy as np
import face_recognition as face_rec
import os
import pyttsx3 as textSpeech
from datetime import datetime
import pyttsx3
from geopy.geocoders import Nominatim
import requests
import socket
engine = textSpeech.init()
recognized_images_folder = 'recognized_images'
detected_images_folder = 'recognized_images'
if not os.path.exists(recognized_images_folder):
    os.mkdir(recognized_images_folder)
def resize(img, size):
    width = int(img.shape[1] * size)
    height = int(img.shape[0] * size)
    dimension = (width, height)
    return cv2.resize(img, dimension, interpolation=cv2.INTER_AREA)
def get_public_ip():
    try:
        # Use a web service to get the public IP address
        response = requests.get('https://ipinfo.io')      
        if response.status_code == 200:
            data = response.json()
            return data.get('ip')
    except Exception as e:
        print(f"An error occurred while getting the public IP: {e}")
    # If the request fails, fall back to getting the local IP
    return socket.gethostbyname(socket.gethostname())
def get_geolocation_info(ip_address):
    try:
        response = requests.get(f'https://ipinfo.io/{ip_address}/json')
        if response.status_code == 200:
            data = response.json()
            return data
    except Exception as e:
        print(f"An error occurred while getting geolocation information: {e}")
    return None

# Registration Mode
#def register_faces():
    path = 'member_profiles/'
    if not os.path.exists(path):
        os.mkdir(path)

    studentName = input("Enter student name: ")
    
    if studentName:
        capture = cv2.VideoCapture(0)
        while True:
            ret, frame = capture.read()
            frame_small = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            faces = face_rec.face_locations(frame_small)

            if len(faces) == 1:  # Capture only when one face is detected
                encodeFace = face_rec.face_encodings(frame_small, faces)[0]
                cv2.imwrite(f'{path}/{studentName}.jpg', frame)
                print(f"Face sample for {studentName} captured.")
                break

            cv2.imshow('Capture Face', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        capture.release()
        cv2.destroyAllWindows()
    else:
        print("Invalid  name. Registration canceled.")
# def register_faces():
    path = 'student_images/'
    if not os.path.exists(path):
        os.mkdir(path)

    studentName = input("Enter  name: ")

    if studentName:
        capture = cv2.VideoCapture(0)
        image_count = 0  # Counter for captured images

        while image_count < 5:  # Capture 5 images for registration
            ret, frame = capture.read()
            frame_small = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            faces = face_rec.face_locations(frame_small)

            if len(faces) == 1:  # Capture only when one face is detected
                encodeFace = face_rec.face_encodings(frame_small, faces)[0]
                cv2.imwrite(f'{path}/{studentName}_{image_count}.jpg', frame)
                print(f"Image {image_count + 1} captured for {studentName}.")
                image_count += 1

            cv2.imshow('Capture Face', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        capture.release()
        cv2.destroyAllWindows()
    else:
        print("Invalid  name. Registration canceled.")
# def register_faces():
    path = 'member_profiless/'
    if not os.path.exists(path):
        os.mkdir(path)

    studentName = input("Enter student name: ")

    if studentName:
        capture = cv2.VideoCapture(0)
        while True:
            ret, frame = capture.read()
            frame_small = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            faces = face_rec.face_locations(frame_small)

            if len(faces) == 1:  # Capture only when one face is detected
                encodeFace = face_rec.face_encodings(frame_small, faces)[0]
                image_filename = f'{path}/{studentName}_{datetime.now().strftime("%Y%m%d%H%M%S")}.jpg'
                cv2.imwrite(image_filename, frame)
                print(f"Face sample for {studentName} captured as {image_filename}.")
            cv2.imshow('Capture Face', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        capture.release()
        cv2.destroyAllWindows()
    else:
        print("Invalid  name. Registration canceled.")
# def register_faces():
    path = 'unrecognized_faces'
    if not os.path.exists(path):
        os.mkdir(path)

    studentName = input("Enter  name: ")
    if studentName:
        capture = cv2.VideoCapture(0)
        sample_count = 0  # Counter for captured samples
        while sample_count < 8:  # Capture up to 8 samples
            ret, frame = capture.read()
            frame_small = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            faces = face_rec.face_locations(frame_small)
            if len(faces) == 1:  # Capture only when one face is detected
                encodeFace = face_rec.face_encodings(frame_small, faces)[0]
                image_filename = f'{path}/{studentName}_{sample_count + 1}.jpg'
                cv2.imwrite(image_filename, frame)
                print(f"Sample {sample_count + 1} for {studentName} captured as {image_filename}.")
                sample_count += 1
            cv2.imshow('Capture Face', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        capture.release()
        cv2.destroyAllWindows()
    else:
        print("Invalid  name. Registration canceled.")
        
         
def register_faces():
    path = 'member_profiless'
    if not os.path.exists(path):
        os.mkdir(path)
    studentName = input("Enter  name: ")
    if studentName:
        if not os.path.exists(os.path.join(path, studentName)):
            os.mkdir(os.path.join(path, studentName))
        capture = cv2.VideoCapture(0)
        sample_count = 0  # Counter for captured samples
        while sample_count < 8:  # Capture up to 8 samples
            ret, frame = capture.read()
            frame_small = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            faces = face_rec.face_locations(frame_small)
            if len(faces) == 1:  # Capture only when one face is detected
                encodeFace = face_rec.face_encodings(frame_small, faces)[0]
                image_filename = os.path.join(path, studentName, f'{studentName}_{sample_count + 1}.jpg')
                cv2.imwrite(image_filename, frame)
                print(f"Sample {sample_count + 1} for {studentName} captured as {image_filename}.")
                sample_count += 1

            cv2.imshow('Capture Face', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        capture.release()
        cv2.destroyAllWindows()
    else:
        print("Invalid  name. Registration canceled.")
        
        
def findEncoding(images):
    imgEncodings = []
    for img in images:
        try:
            img = resize(img, 0.50)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encodeimg = face_rec.face_encodings(img)[0]
            imgEncodings.append(encodeimg)
        except Exception as e:
            print(f"Error processing image: {e}")
    return imgEncodings
# Recognition Mode
def recognize_faces():
    path = '../member_profiles'
    studentName = []
    for cl in os.listdir(path):
        studentName.append(os.path.splitext(cl)[0])
    if not studentName:
        print("No registered . Please register  first.")
        return
    EncodeList = findEncoding([cv2.imread(os.path.join(path, name + ".jpg")) for name in studentName])
    vid = cv2.VideoCapture(0)
    while True:
        success, frame = vid.read()
        Smaller_frames = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
        facesInFrame = face_rec.face_locations(Smaller_frames)
        encodeFacesInFrame = face_rec.face_encodings(Smaller_frames, facesInFrame)
        for encodeFace, faceloc in zip(encodeFacesInFrame, facesInFrame):
            facedis = face_rec.face_distance(EncodeList, encodeFace)
            matchIndex = np.argmin(facedis)
            if facedis[matchIndex] < 0.5:
                name = studentName[matchIndex]
                y1, x2, y2, x1 = faceloc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                # Recognized Face
                recognized_face = frame[y1:y2, x1:x2]
                # Sample Image
                sample_image = cv2.imread(os.path.join(path, f'{name}.jpg'))
                # Save the recognized face
                cv2.imwrite(f'Recognized_Faces/{name}_recognized.jpg', recognized_face)
                print(f"Recognized {name}'s face and saved the image.")
                # Save the sample image
                cv2.imwrite(f'Criminal/{name}_sample.jpg', sample_image)
                print(f"Saved the sample image for {name}.")
                MarkAttendance(name)
        cv2.imshow('video', frame)
        cv2.waitKey(1)
# def recognize_faces():
#     path = '../media/member_profiles'
#     studentName = []
#     for cl in os.listdir(path):
#         studentName.append(os.path.splitext(cl)[0])
#     if not studentName:
#         print("No registered . Please register  first.")
#         return
#     EncodeList = findEncoding([cv2.imread(os.path.join(path, name + ".jpg")) for name in studentName])
#     vid = cv2.VideoCapture(0)
#     while True:
#         success, frame = vid.read()
#         Smaller_frames = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
#         facesInFrame = face_rec.face_locations(Smaller_frames)
#         encodeFacesInFrame = face_rec.face_encodings(Smaller_frames, facesInFrame)
#         for encodeFace, faceloc in zip(encodeFacesInFrame, facesInFrame):
#             facedis = face_rec.face_distance(EncodeList, encodeFace)
#             matchIndex = np.argmin(facedis)
#             if facedis[matchIndex] < 0.5:
                
#                 name = studentName[matchIndex]
#                 y1, x2, y2, x1 = faceloc
#                 y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4

#                         # Recognized Face
#                 recognized_face = frame[y1:y2, x1:x2]

#                         # Save the recognized face to the recognized_images_folder
#                 name = studentName[matchIndex]

#                 # Save the entire frame when a face is detected
#                 detected_image_path = os.path.join(detected_images_folder, f'{name}_{datetime.now().strftime("%Y%m%d%H%M%S")}_detected.jpg')
#                 cv2.imwrite(detected_image_path, frame)
#                 print(f"Detected {name}'s face and saved the entire frame as {detected_image_path}.")

#                 # Save the sample image
#                 sample_image = cv2.imread(os.path.join(detected_images_folder, f'{name}.jpg'))

#                 print(f"Recognized {name}'s face and saved the image as {detected_images_folder}.")

#                         # Save the sample image
#                 sample_image = cv2.imread(os.path.join(detected_images_folder, f'{name}.jpg'))

#                 # Save the recognized face
#                 cv2.imwrite(f'Recognized_Faces/{name}_recognized.jpg', recognized_face)
#                 print(f"Recognized {name}'s face and saved the image.")
#                 # Save the samp2le image
#                 # cv2.imwrite(f'Criminal/{name}_sample.jpg', sample_image)
#                 print(f"Saved the sample image for {name}.")
#                 # Call MarkAttendance with a placeholder for image_path
#                 MarkAttendance(name, image_path=None)  # You can set image_path to None or an empty string
#         cv2.imshow('video', frame)
#         cv2.waitKey(1)

# def MarkAttendance(name):
#     # Get the public IP address
#     public_ip = get_public_ip()

#     if public_ip:
#         geolocation_info = get_geolocation_info(public_ip)
#     else:
#         geolocation_info = None

#     # Open the CSV file for reading and appending
#     with open('../Attendance.csv', 'r+') as f:
#         myDataList = f.readlines()
#         nameList = []

#         # Extract existing names from the CSV
#         for line in myDataList:
#             entry = line.strip().split(',')
#             nameList.append(entry[0])

#         # Check if the name is already in the list
#         if name not in nameList:
#             now = datetime.now()
#             timestr = now.strftime('%H:%M')
#             address = "Kicukiro_sonatube"

#             # Write attendance information to the CSV
#             if geolocation_info and isinstance(geolocation_info, dict):
#                 geolocation_data = f'"{geolocation_info.get("city", "")}", {geolocation_info.get("region", "")}, "{geolocation_info.get("country", "")}", "{geolocation_info.get("loc", "")}"'
#             else:
#                 geolocation_data = '""'  # Use empty values if geolocation data is not available

#             f.write(f'{name}, {timestr}, "{address}", {geolocation_data}\n')

#             # Notify that the person's attendance has been marked
#             statement = f'Welcome marked for {name}'
#             engine = pyttsx3.init()
#             engine.say(statement)
#             engine.runAndWait()
import os  # Import the os module to work with file paths

def MarkAttendance(name, image_path):
    # Get the public IP address
    public_ip = get_public_ip()

    if public_ip:
        geolocation_info = get_geolocation_info(public_ip)
    else:
        geolocation_info = None

    # Determine the path to the CSV file (you may need to adjust the path)
    csv_file_path = 'Attendance.csv'

    # Check if the CSV file exists, and create it if it doesn't
    if not os.path.exists(csv_file_path):
        with open(csv_file_path, 'w') as f:
            f.write('Name, Image Path, Time, Address, Geolocation\n')

    # Open the CSV file for appending
    with open(csv_file_path, 'a') as f:
        now = datetime.now()
        timestr = now.strftime('%H:%M')
        address = "Kicukiro_sonatube"

        # Write attendance information to the CSV
        if geolocation_info and isinstance(geolocation_info, dict):
            geolocation_data = f'"{geolocation_info.get("city", "")}", {geolocation_info.get("region", "")}, "{geolocation_info.get("country", "")}", "{geolocation_info.get("loc", "")}"'
        else:
            geolocation_data = '""'  # Use empty values if geolocation data is not available

        # Add the name and image path to the CSV line
        f.write(f'{name}, "{image_path}", {timestr}, "{address}", {geolocation_data}\n')

        # Notify that the person's attendance has been marked
        statement = f'Criminal  {name} is Detected at '
        engine = pyttsx3.init()
        engine.say(statement)
        engine.runAndWait()

def main_menu():
    while True:
        print("Main Menu:")
        print("1. Registration Mode")
        print("2. Recognition Mode")
        print("3. Exit")
        # choice = input("Choose an option (1/2/3): ")
        # if choice == "1":
        #     print("Registration mode is active. You can register faces.")
        #     register_faces()
        # elif choice == "2":
        #     print("Recognition mode is active. Recognizing faces.")
        recognize_faces()
        # elif choice == "3":
        #     break
        # else:
        #     print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()
