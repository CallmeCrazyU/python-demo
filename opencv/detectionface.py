import cv2

filepath = "../img/fage.png"
# 读取图片
img = cv2.imread(filepath)
# 转换灰色
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# OpenCV人脸识别分类器
classifier = cv2.CascadeClassifier("../file/haarcascade_frontalface_default.xml")
# 定义绘制颜色
color = (0,255,0)
# 调用识别人脸
faceRects = classifier.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=3,minSize=(32,32))
# 大于0则检测到人脸
if len(faceRects):
    for faceRect in faceRects:
        x,y,w,h = faceRect
        # 框出人脸
        cv2.rectangle(img,(x,y),(x+w,y+w),color,2)
        # 左眼
        cv2.circle(img,(x+w//4,y+h//4+30),min(w//8,h//8),color)
        # 右眼
        cv2.circle(img,(x + 3 * w // 4, y + h // 4 + 30), min(w // 8, h // 8),color)
        # 嘴巴
        cv2.rectangle(img, (x + 3 * w // 8, y + 3 * h // 4),(x + 5 * w // 8, y + 7 * h // 8), color)
# 显示图像
cv2.imshow("Image",img)
cv2.waitKey(10)

cv2.waitKey(0)
cv2.destroyAllWindows()

