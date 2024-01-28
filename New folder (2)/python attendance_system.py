import cv2
import face_recognition
import numpy as np
import time

# Load a sample image with known faces (you should replace these images with your own)
known_image_paths = ["path/to/known_person1.jpg", "path/to/known_person2.jpg"]
known_face_names = ["Person 1", "Person 2"]

# Create arrays to store face encodings and names
known_face_encodings = []
for image_path in known_image_paths:
    image = face_recognition.load_image_file(image_path)
    encoding = face_recognition.face_encodings(image)[0]
    known_face_encodings.append(encoding)

# Initialize variables for attendance
present_names = set()
attendance_interval = 10  # Attendance will be marked every 10 seconds

# Open the camera
video_capture = cv2.VideoCapture(0)

while True:
    # Capture each frame from the camera
    ret, frame = video_capture.read()

    # Find all face locations and face encodings in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Loop through each face found in the frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Check if the face matches any known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"

        # If a match is found, use the name of the known face
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            present_names.add(name)

        # Draw a rectangle and display the name on the frame
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Check if the attendance interval has passed
    if int(time.time()) % attendance_interval == 0:
        print("Attendance:", present_names)
        present_names = set()

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
video_capture.release()
cv2.destroyAllWindows()
