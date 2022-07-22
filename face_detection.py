import face_recognition as fr
import cv2 as cv
from numpy import mat

my_face = fr.load_image_file("faces/lewis.jpg")
my_face_encoding = fr.face_encodings(my_face)[0]

knownFaceEncodings = [
    my_face_encoding
]

knownFaceNames = [
    "Lewis"
]

camera = cv.VideoCapture(0) # Get default video capture

def mainLoop(): # Start the main display loop
    while True:
        ret, frame = camera.read() # Get the current frame

        rgbFrame = frame[:, :, ::-1] # This converts the frame from BGR colour to RGB colour

        faceLocations = fr.face_locations(rgbFrame) # Find the location of all the faces in the frame
        faceEncodings = fr.face_encodings(rgbFrame, faceLocations) # Find all the face encodings

        faceNames = [] # Will hold all the names of the faces found

        for faceEncoding in faceEncodings:
            matches = fr.compare_faces(knownFaceEncodings, faceEncoding) # See if the current face encoding is in the known list
            name = "?" # will change if a matching name is found

            if True in matches: # If a match is found
                name = knownFaceNames[matches.index(True)] # Set name as the index of 
            
            faceNames.append(name)

        print(faceNames)

        if cv.waitKey(1) & 0xFF == ord('q'): # If q is pressed, end the loop
            break
    
    camera.release() # Unlink camera
    cv.destroyAllWindows() # Remove all windows