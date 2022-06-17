import cv2 as cv

def Color_Bottle(n):

    if n == 0:
        name  ="Pepsi"
        hsv_lower = (95 , 100 , 100)
        hsv_upper = (115 , 255 , 255)
        return (name , hsv_lower , hsv_upper)
    if n == 1:
        name = "Coca"
        hsv_lower = (0 , 100 , 100)
        hsv_upper = (10 , 255 , 255)
        return (name , hsv_lower , hsv_upper)

frame = cv.imread('image.jpg')

hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
rects = {}

for i in range(2):
    name , hsv_lower , hsv_upper = Color_Bottle(i)
    mask = cv.inRange(hsv , hsv_lower , hsv_upper)
    conts, herirarchy = cv.findContours(mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    biggest = sorted(conts,key=cv.contourArea,reverse=True)[0]
    rect = cv.boundingRect(biggest)
    x,y,w,h = rect
    cv.rectangle(frame,(x,y),(x+w ,y+h) , (0 , 255 , 255) , 3)
    cv.putText(frame, name, (x, y), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)


cv.imshow('image' , frame)
#cv.imshow('HSV', mask)
cv.waitKey(0)
cv.destroyAllWindow()




