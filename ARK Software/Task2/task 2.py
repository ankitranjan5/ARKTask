import cv2 as cv
import numpy as np
import math

def centre(detected):
    for (x, y, width, height) in detected:
        #print(x , y , width , height)
        #global x2
        #x2 = y + int(width/2)
        global y2
        y2 = w - (x + int(height/2))

# Resolution of game window
h = 700
w = 1364

# Ball radii
Rball = 100  # ideal is 100
Robstacle = 100 # ideal is 90

# initial parameters of 1st ball 
x1 = 350 
y1 = Rball + 1

# initial parameters of 2nd ball
x2 = h - Robstacle
y2 = w - Robstacle - 1

# Ball speed
vx1 = -5.0  # speed in verticle direction 
vy1 = 5.0  # speed in Horizontal direction
vi = v1 =   5.0 * math.sqrt(2)

# Collision condition
Rtotal = Rball + Robstacle

img = np.full((h,w,3),255,dtype= 'uint8') # Perfect Shape
# initail start
cv.circle(img, (y1,x1), Rball, (0,0,203))
#cv.circle(img, (y2,x2), Robstacle, (0,0,255),-1)

d = 0.0

#url = "https://10.204.140.58:8080" # Your url might be different, check the app
#vs = cv.VideoCapture(url+"/video")
vs = cv.VideoCapture(0)

while True:
    
    ret, frame = vs.read()
    if not ret:
        continue

    frame = cv.resize(frame,(w,h))
    # Convert image to grayscale
    image = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Create Cascade Classifiers
    face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
    profile_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_profileface.xml")
    
    # Detect faces using the classifiers
    detected_faces = face_cascade.detectMultiScale(image=image, scaleFactor=1.3, minNeighbors=4)
    detected_profiles = profile_cascade.detectMultiScale(image=image, scaleFactor=1.3, minNeighbors=4)

    # Filter out profiles
    profiles_not_faces = [x for x in detected_profiles if x not in detected_faces]

    # Draw circle around faces on the original, colored image
    centre(detected_faces)  

    img = np.full((700,1364,3),255,dtype= 'uint8') # Perfect Shape
    cv.circle(img, (y1,x1), Rball, (125,125,120),-1)
    cv.circle(img, (y2,x2),Robstacle, (0,0,255),-1)
    cv.imshow('test',img) 
    k = cv.waitKey(1)
    
    if k == ord('q'):
        break

    # check for boundries collisions for ball 1
    if x1 <= Rball :
       vx1 = -vx1 
       x1 = Rball
    if y1 <=  Rball:
       vy1 = -vy1
       y1 = Rball
    if x1 >= (h - Rball) :
       font = cv.FONT_HERSHEY_SIMPLEX
       cv.putText(img,' Game Over',(382,350), font, 3,(0,0,0),2,cv.LINE_AA)
       cv.imshow('test',img)
       break
    if y1 >=  (w - Rball):
       vy1 = -vy1
       y1 =  (w - Rball)

    # Checking for ball to ball collision
    elif math.sqrt((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2)) <= (Rtotal + 1):
       v1 = math.sqrt(vx1 * vx1 + vy1 * vy1)
       
       d = math.sqrt((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2))
       
       Theta = math.acos((((x2-x1)*vx1)+((y2-y1)*vy1))/(d*v1))
       alpha = math.acos((x2-x1)/d)

       vx1 = -((v1 * math.cos(Theta) * math.cos(alpha)) + (v1 * math.sin(Theta) * math.sin(alpha)))
       vy1 = ((v1 * math.sin(Theta) * math.cos(alpha)) - (v1 * math.cos(Theta) * math.sin(alpha)) )
       
       # optimization of value of velocities because of pixel problem
       if 0.3 <= vx1 < 1:
          vx1 = 1.0
       elif -0.3 <= vx1 < 0.3 :
          vx1 = 0.0
       elif -1 <= vx1 < -0.3:
          vx1 = -1.0
       
       if 0.3 <= vy1 < 1:
          vy1 = 1.0
       elif -0.3 <= vy1 < 0.3 :
          vy1 = 0.0
       elif -1 <= vy1 < -0.3:
          vy1 = -1.0
    
    if v1 > vi :
        v1 = vi


    # update position of ball 1
    x1 = x1 + int(vx1)
    y1 = y1 + int(vy1)
#    print(' x1 = ', x1,' y1 = ', y1,' vx1 = ',vx1, ' v1 = ' ,v1 ,' x2 = ',x2, ' y2 = ',y2, ' v2 = ',v2,' d =',d)
#    print(vi , math.sqrt((v1*v1) + (v2*v2)))
cv.destroyAllWindows()

