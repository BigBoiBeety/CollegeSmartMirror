import face_recognition as fr
import cv2 as cv

camera = cv.VideoCapture(0) # Get default video capture

def mainLoop(): # Start the main display loop
    while True:
        ret, frame = camera.read() # Get the current frame

        faceLocations = fr.face_locations(frame) # Find the location of all the faces in the frame

        for (top, right, bottom, left) in faceLocations: # For every face location
            cv.rectangle(frame, (left, top), (right, bottom), (0,0,255), 2) # Draw a red rectangle over the face

        cv.imshow('Video', frame) # Display the frame in a window

        if cv.waitKey(1) & 0xFF == ord('q'): # If q is pressed, end the loop
            break
    
    camera.release() # Unlink camera
    cv.destroyAllWindows() # Remove all windows