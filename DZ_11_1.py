import requests
import pandas
import numpy
import matplotlib.pyplot
import pillow
# Инструкции:
# 1. Выберите одну или несколько сторонних библиотек Python, например, requests, pandas, numpy, matplotlib, pillow и другие.
# 2. Изучите документацию выбранных библиотек, ознакомьтесь с их основными возможностями и функциями.
# 3. Напишите простые задачи, в которых нужно использовать выбранные библиотеки, и выполните их.
# Приведите примеры использования библиотек в различных сценариях:
#   - Запросить данные с помощью библиотеки requests из API и вывести их в консоль.
p = requests.get('https://yandex.ru/pogoda/almetyevsk?lat=54.901172&lon=52.297229')
class_ = 'temp__value temp__value_with-unit'
print(p)
print(p.content)
#   - Считать данные из файла с помощью библиотеки pandas, выполнить простой анализ данных и вывести результаты.
d = pandas.read_csv('Internet Speed 2022.csv')
print(d)
print(d.describe())
#   - Создать массив чисел с помощью библиотеки numpy, выполнить математические операции с массивом
#   и вывести результаты.
a = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = numpy.random.randint(0,10, size=(3,3))
print(a)
print(b)
print(a * b)
print(b / a)
print(a + b)
#   - Визуализировать данные с помощью библиотеки matplotlib.
vals = [24, 17, 53, 21, 35]
labels = ["Ford", "Toyota", "BMW", "Audi", "Jaguar"]
matplotlib.pyplot.pie(vals, labels=labels)
matplotlib.pyplot.title("Распределение марок автомобилей на дороге")
matplotlib.pyplot.show()

#   - Обработать изображение с помощью библиотеки pillow, например, изменить его размер,
#   применить эффекты и сохранить в другой формат.
image = pillow.Image.open("abc.jpg")
new_size = (100, 100)

# Изменение размера изображения
resized_image = image.resize(new_size)
resized_image.save("abc.jpg")
print(resized_image)

# Преобразование изображения в черно-белое
grayscale_image = pillow.ImageOps.grayscale(image)
grayscale_image.save("abc.jpg")
print(grayscale_image)




