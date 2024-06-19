import cv2
import numpy

img = cv2.imread('DZ.jpg')

new_png = numpy.zeros(img.shape, dtype='uint8') # создаем новое полотно по размерам img.png

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # делаем картинку ЧБ
img = cv2.GaussianBlur(img, (9, 9), 0)  # размытие картинки

img = cv2.Canny(img, 20, 20)  # точность для отображения контуров

kernel = numpy.ones((5, 5), numpy.uint8)
img = cv2.dilate(img, kernel, iterations=1) # увеличиваем толщину контура

img = cv2.erode(img, kernel, iterations=1) # размывание (эрозия)

con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)  # находим контуры изображений

print(con)
print(len(con))

cv2.drawContours(new_png, con[141:], -1, (40, 250, 40), 1)  # перекрашиваем изображение
cv2.drawContours(new_png, con[61:141], -1, (0, 0, 255), 1)  # перекрашиваем изображение
cv2.drawContours(new_png, con[:61], -1, (250, 40, 155), 1)  # перекрашиваем изображение

cv2.imshow('Resul_1', new_png)
cv2.waitKey(0)
