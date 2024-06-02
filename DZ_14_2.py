'''
Задание:
Разработайте функцию для извлечения информации из HTML-текста (строки Python) о ссылках на изображения
(URL-адресах картинок). Функция должна находить все ссылки на изображения в форматах JPEG, JPG,
PNG или GIF и возвращать их список.

1. Создайте функцию extract_image_links(html_text), которая принимает HTML-текст и извлекает ссылки на изображения.
2. Используйте регулярные выражения для поиска URL-адресов картинок с расширениями .jpg, .jpeg, .png или .gif.
3. Верните список всех найденных ссылок на изображения.

Вывод на консоль:
https://example.com/image1.jpg
http://example.com/image2.png
https://example.com/image3.gif

Примечания:
Вам могут понадобится следующие спец. символы: / ? [] | +
Учтите что 'http' это подстрока строки 'https'.
'''

import re

sample_html = ("<img src='https://example.com/image1.jpg'> <img src='http://example.com/image2.png'> "
                "<img src='https://example.com/image3.gif'>")

def extract_image_links(html_text):
    picture_str = ''
    r = re.split('<img src=|> <img src=|>', html_text)
    for _ in r:
        _ = _.replace("'", '')
        if _[-4:] == '.jpg':
            picture_str+= _ + '\n'
        elif _[-5:] == '.jpeg':
            picture_str+= _ + '\n'
        elif _[-4:] == '.png':
            picture_str+= _ + '\n'
        elif _[-4:] == '.gif':
            picture_str+= _ + '\n'
    if len(picture_str) != 0:
        return picture_str
    else:
        return ("Нет ссылок с картинками в HTML тексте.")


image_links = extract_image_links(html_text=sample_html)
print(image_links)
