from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Member, UploadedImage
from django.http import FileResponse
from PIL import Image
import os
import csv
from .models import UnrecognizedFaceRecord
import numpy as np
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# unrecognized_faces_folder = 'unrecognized_faces'
unrecognized_faces_directory = "media/unrecognized_faces"

# Initialize known_faces and known_names
known_faces = []
known_names = []

def members(request):
    mymembers = Member.objects.all()
    template = loader.get_template('index.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))


def image_view(request):
    image_path = settings.MEDIA_ROOT / 'employee_profile_images' / 'myimage.jpg'
    return FileResponse(open(image_path, 'rb'), content_type='image/jpeg')
  
  
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
def read_csv(request):
    data = []  # To store CSV data

    with open('members/Attendance.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)

        for row in csvreader:
            data.append(row)
    context = {
        'csv_data': data,
    }

    return render(request, 'detected.html', context)


def read_images_from_directory(directory):
    image_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                image_path = os.path.join(root, file)
                image = Image.open(image_path)
                image_list.append((image_path, image))
    return image_list
def member_images(request):
    # Specify the directory where you want to search for images
    directory_to_search = '../unrecognized_faces'

    # Call the function to read images
    image_list = read_images_from_directory(directory_to_search)

    # Pass the image list to the template
    context = {'image_list': image_list}

    # Render a template with the image list
    return render(request, 'index.html', context)



def load_known_faces():
    known_faces = []  # List to store face encodings
    known_names = []  # List to store corresponding names
    # Define the path to the directory containing known faces
    known_faces_directory = 'member_profiles'  # Update this path
    # List files in the directory
    for filename in os.listdir(known_faces_directory):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            # Load the image using face_recognition
            image_path = os.path.join(known_faces_directory, filename)
            image = face_recognition.load_image_file(image_path)

            # Encode the face in the image
            encoding = face_recognition.face_encodings(image)

            if len(encoding) > 0:
                # Assume there's only one face in each image
                known_faces.append(encoding[0])
                # Remove the file extension to get the name
                name = os.path.splitext(filename)[0]
                known_names.append(name)

    return known_faces, known_names

import cv2
from django.http import StreamingHttpResponse
import time
import os

# Define the directory where you want to save the images
image_save_directory = '../member_profiles'

# def generate_frames():
#     camera = cv2.VideoCapture(0)
#     while True:
#         success, frame = camera.read()
#         if not success:
#             break
#         else:
#             ret, buffer = cv2.imencode('.jpg', frame)
#             if ret:
#                 # Save the image to the specified directory
#                 image_filename = f'{image_save_directory}/image_{int(time.time())}.jpg'
#                 cv2.imwrite(image_filename, frame)
                
#                 yield (b'--frame\r\n'
#                        b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')
#         time.sleep(1)

# def camera_feed(request):
#     return StreamingHttpResponse(generate_frames(), content_type='multipart/x-mixed-replace; boundary=frame')

import face_recognition
# Define the directory where known faces are stored
known_faces_directory = "media/member_profiles"
def load_known_faces():
    known_faces = []
    known_names = []

    for filename in os.listdir(known_faces_directory):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            # Load the image using face_recognition
            image_path = os.path.join(known_faces_directory, filename)
            image = face_recognition.load_image_file(image_path)
            # Encode the face in the image
            encoding = face_recognition.face_encodings(image)

            if len(encoding) > 0:
                # Assume there's only one face in each image
                known_faces.append(encoding[0])
                # Remove the file extension to get the name
                name = os.path.splitext(filename)[0]
                known_names.append(name)

    return known_faces, known_names
# Load known faces and names
known_faces, known_names = load_known_faces()
# known_faces, known_names = load_known_faces()
# ...

# def generate_frames():
    # camera = cv2.VideoCapture(0)
    
    # recognized_names = []  # To store names of recognized faces

    # while True:
    #     success, frame = camera.read()
    #     if not success:
    #         break
    #     else:
    #         # Perform face detection
    #         face_locations = face_recognition.face_locations(frame)
    #         face_encodings = face_recognition.face_encodings(frame, face_locations)

    #         for name in recognized_names:
    #             cv2.putText(frame, name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    #         # Recognize faces and draw rectangles
    #         for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    #             matches = face_recognition.compare_faces(known_faces, face_encoding)
    #             name = "Unknown"

    #             if True in matches:
    #                 first_match_index = matches.index(True)
    #                 name = known_names[first_match_index]

    #                 # Add the recognized name to the list
    #                 recognized_names.append(name)

    #             # Draw a rectangle on the frame
    #             cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
    #             cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    #         ret, buffer = cv2.imencode('.jpg', frame)
    #         if ret:
    #             yield (b'--frame\r\n'
    #                    b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')


save_folder = "media"  # Change this to your desired folder path

def generate_frames():
    camera = cv2.VideoCapture(0)
    # camera = cv2.VideoCapture("http://192.168.1.88:8000/video")
    recognized_names = set()  # To store names of recognized faces

    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            # Perform face detection
            face_locations = face_recognition.face_locations(frame)
            face_encodings = face_recognition.face_encodings(frame, face_locations)

            for name in recognized_names:
                cv2.putText(frame, name, (45, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                matches = face_recognition.compare_faces(known_faces, face_encoding)
                name = "Unknown"

                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_names[first_match_index]

                    # Add the recognized name to the set
                    recognized_names.add(name)
                else:
                    # Face is unrecognized, save it to the folder
                    save_unrecognized_face(frame)

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

            ret, buffer = cv2.imencode('.jpg', frame)
            if ret:
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

def save_unrecognized_face(frame):
    # Generate a unique filename for the unrecognized face (e.g., using timestamps)
    timestamp = str(time.time())
    unrecognized_face_filename = os.path.join(unrecognized_faces_folder, f'unrecognized_face_{timestamp}.jpg')

    # Save the unrecognized face to the folder
    cv2.imwrite(unrecognized_face_filename, frame)
def camera_feed(request):
    return StreamingHttpResponse(generate_frames(), content_type='multipart/x-mixed-replace; boundary=frame')
def unrecognized_faces(request):
    unrecognized_records = UnrecognizedFaceRecord.objects.all()
    return render(request, 'unrecognized_faces.html', {'unrecognized_records': unrecognized_records})

@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and 'image' in request.FILES:
        image = request.FILES['image']
        
        # Save the image to a directory on the server
        with open('uploads/' + image.name, 'wb') as destination:
            for chunk in image.chunks():
                destination.write(chunk)

        return JsonResponse({'message': 'Image uploaded successfully'})
    else:
        return JsonResponse({'message': 'Invalid request'}, status=400)
    # urlpatterns = [
    #     path('upload_image/', views.upload_image, name='upload_image'),
    # ]
def save_unrecognized_face(frame):
    # Create the save folder if it doesn't exist
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    # Generate a unique filename for the unrecognized face
    filename = os.path.join(save_folder, f"unrecognized_face_{len(os.listdir(save_folder)) + 1}.jpg")
    # Save the unrecognized face to the folder
    cv2.imwrite(filename, frame)
    print(f"Saved unrecognized face as {filename}")
    
def view_unrecognized_faces(request):
    unrecognized_faces = []

    # List all files in the unrecognized_faces_directory
    for filename in os.listdir(unrecognized_faces_directory):
        if filename.endswith(".jpg"):
            unrecognized_faces.append(os.path.join(unrecognized_faces_directory, filename))

    return render(request, 'unrecognized_faces.html', {'unrecognized_faces': unrecognized_faces})

import os
import glob
def get_image_files(directory):
    image_files = []

    image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.gif', '*.bmp', '*.tiff', '*.ico', '*.svg', '*.webp']

    for ext in image_extensions:
        pattern = os.path.join(directory, ext)
        image_files.extend(glob.glob(pattern))

    return image_files

def image_list(request):
    directory_path = 'media/'  # Replace with the actual directory path
    image_files = get_image_files(directory_path)
    return render(request, 'image_list.html', {'image_files': image_files})
def display_unrecognized_image():
    # Load the unrecognized image
    unrecognized_image = cv2.imread('unrecognized_faces/unrecognized_face.jpg')

    if unrecognized_image is not None:
        # Display the unrecognized image
        cv2.imshow('Unrecognized Face', unrecognized_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Unrecognized image not found.")
def image_list(request):
    images = member_images.objects.all()
    return render(request, 'unrecognized_faces.html', {'images': images})

from .models import UploadedImage
@require_POST
@csrf_exempt  # This decorator is used to disable CSRF protection for this view. Use it with caution and consider adding security measures.
def upload_image(request):
    if 'image' in request.FILES:
        uploaded_image = UploadedImage(image=request.FILES['image'])
        uploaded_image.save()
        # generate_frames().uploaded_image
        return JsonResponse({'message': 'Image uploaded successfully'})
    else:
        return JsonResponse({'message': 'No image file found'}, status=400)
    
# import sys
# from .models import UploadedImage
# # from .utils import classify_face

# @require_POST
# @csrf_exempt
# def upload_image(request):
#     if 'image' in request.FILES:
#         image_file = request.FILES['image']

#         # Classify the face in the uploaded image
#         is_recognized_face = classify_face(image_file)

#         if is_recognized_face:
#             # This is a recognized face, save it as such
#             uploaded_image = UploadedImage(image=image_file)
#             uploaded_image.is_recognized = True
#             uploaded_image.save()
#             return JsonResponse({'message': 'Recognized face uploaded successfully'})
#         else:
#             # This is an unrecognized face, save it as such
#             uploaded_image = UploadedImage(image=image_file)
#             uploaded_image.is_recognized = False
#             uploaded_image.save()
#             return JsonResponse({'message': 'Unrecognized face uploaded successfully'})
#     else:
#         return JsonResponse({'message': 'No image file found'}, status=400)

# import cv2
# from django.http import JsonResponse
# from .models import UploadedImage

# import cv2
# from django.shortcuts import render
# from .models import DetectedFace
# from django.core.files.base import ContentFile

# def upload_image(request):
#     if request.method == 'POST' and request.FILES['image']:
#         # Load the pre-trained cascade classifier
#         face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default(1).xml')

#         # Get the uploaded image
#         image = request.FILES['image'].read()

#         # Convert the image data to a numpy array
#         image_np = np.frombuffer(image, np.uint8)

#         # Read the image using OpenCV
#         img = cv2.imdecode(image_np, cv2.IMREAD_COLOR)

#         # Convert the image to grayscale for face detection
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#         # Detect faces in the image
#         faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

#         # Draw rectangles around the detected faces
#         for (x, y, w, h) in faces:
#             cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

#         # Save the image with detected faces
#         with BytesIO() as buffer:
#             cv2.imwrite(buffer, img, format="JPEG")
#             image_data = buffer.getvalue()
#             detected_face = DetectedFace()
#             detected_face.image.save('detected_face.jpg', ContentFile(image_data))
#             detected_face.save()

#         return render(request, 'detected_face.html', {'image': detected_face.image.url})

#     return render(request, 'detect_face.html')
