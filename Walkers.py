import cv2


# Create our body classifier
body_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Initiate video capture for video file
cap = cv2.VideoCapture('walking.avi')

# Loop once video is successfully loaded
while True:
    
    # Read first frame
    ret, frame = cap.read()

    #Convert Each Frame into Grayscale
    gray = cv2.cvtColor(body, cv2.COLOR_BGR2GRAY)

    # Pass frame to our body classifier
    body = body_classifier.detectMultiScale(gray, 1.1, 5)
    
    # Extract bounding boxes for any bodies identified
    for (x,y,w,h) in body:
       cv2.rectangle(body,(x,y),(x+w,y+h),(255,0,0),2)

    if cv2.waitKey(1) == 32: #32 is the Space Key
        break

cv2.imshow('body',body)
cap.release()
cv2.destroyAllWindows()
