'''
Задание:

1. Создайте новый проект или продолжите работу в текущем проекте.
2. Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
3. Примените os.path.join для формирования полного пути к файлам.
4. Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
5. Используйте os.path.getsize для получения размера файла.
6. Используйте os.path.dirname для получения родительской директории файла.

'''

import os
import time

directory = 'C:\\Users\\Ildar\\Desktop\\proba1\\pythonProject\\urban\\module_7'

# os.walk для обхода каталога, путь к которому указывает переменная directory
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file) # os.path.join для формирования полного пути к файлам.
        filetime = os.path.getmtime(filepath) # os.path.getmtime и модуль time для получения и
# отображения времени последнего изменения файла.
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath) # os.path.getsize для получения размера файла.
        parent_dir = os.path.dirname(filepath) # os.path.dirname для получения родительской директории файла.
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
        f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')










