import cv2
# 人脸识别


def discren(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cap = cv2.CascadeClassifier("../file/haarcascade_frontalface_default.xml")
    faceRects = cap.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=3,minSize=(50,50))
    if len(faceRects):
        for faceRect in faceRects:
            x,y,w,h = faceRect
            cv2.rectangle(img, (x, y), (x + h, y + w), (0, 255, 0), 2)  # 框出人脸
    cv2.imshow("Image",img)

cap = cv2.VideoCapture(0)
while(1):
    ret,img = cap.read()
    discren(img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()