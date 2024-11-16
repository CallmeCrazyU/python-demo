# 图片人脸检测
使用到的技术是OpenCv

## 功能展示

## 技术思路
图片转成灰色  
图片上画矩形  
使用训练分类器查找人脸
## 代码实现
### 图片转成灰色
```commandline
import cv2

filepath = "img/fage.png"
img = cv2.imread(filepath)
# 转换灰色
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 显示图像
cv2.imshow("Image", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
### 图片上画矩形
```commandline
import cv2

filepath = "img/fage.png"
img = cv2.imread(filepath)
# 转换灰色
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
x = y = 50
w = 100
color = (0,0,255)
cv2.rectangle(img,(x,y),(x+w,y+w),color,1)
# 显示图像
# cv2.imshow("Image",gray)
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
### 使用训练分类器查找人脸
