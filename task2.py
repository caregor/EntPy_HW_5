"""
    ---Task 2---
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. Функция возвращает
кортеж из трёх элементов: путь, имя файла, расширение файла.
"""

import os

def split_file_path(file_path):
    path, filename = os.path.split(file_path)
    name, extension = os.path.splitext(filename)
    return path, name, extension


file_path = '/path/to/file.txt'
path, name, extension = split_file_path(file_path)
print("Путь:", path)
print("Имя файла:", name)
print("Расширение файла:", extension)