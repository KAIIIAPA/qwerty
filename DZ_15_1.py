import cv2
import numpy

picture = numpy.zeros((450, 450, 3), dtype='uint8')

cv2.circle(picture, (picture.shape[1] // 2, picture.shape[0] // 2), 180, (250, 250, 250), 4)

cv2.ellipse(picture, (picture.shape[1] // 2, picture.shape[0] // 2), angle=270.0, startAngle=90, endAngle=270,
            color=(0, 255, 84), axes=(50, 50), thickness=4)

cv2.ellipse(picture, (picture.shape[1] // 2, picture.shape[0] // 2), angle=270.0, startAngle=90, endAngle=270,
            color=(0, 255, 84), axes=(25, 25), thickness=4)

cv2.line(picture, (450 // 2 - 50, picture.shape[1] // 2), (450 // 2 - 50, 170), (228, 10, 0),thickness=4)

cv2.line(picture, (450 // 2 + 50, picture.shape[1] // 2), (450 // 2 + 50, 170), (228, 10, 0),thickness=4)

cv2.line(picture, (450 // 2 - 25, picture.shape[1] // 2), (450 // 2 - 25, 170), (228, 10, 0),thickness=4)

cv2.line(picture, (450 // 2 + 25, picture.shape[1] // 2), (450 // 2 + 25, 170), (228, 10, 0), thickness=4)

cv2.line(picture, (450 // 2 - 50, 170), (450 // 2 - 25, 170), (0, 0, 255), thickness=4)

cv2.line(picture, (450 // 2 + 50, 170), (450 // 2 + 25, 170), (0, 0, 255), thickness=4)

cv2.imshow('DZ', picture)
cv2.waitKey(0)
