import cv2

filepath = "../img/picture.jpg"
img = cv2.imread(filepath)
cv2.namedWindow('Image')
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
