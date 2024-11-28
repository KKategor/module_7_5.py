# Task "Файлы в операционной системе"

import os
from os.path import join, getmtime, getsize, dirname
import time

def dir_info(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = join(root, file)
            filetime = getmtime(filepath)
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            filesize = getsize(filepath)
            parent_dir = dirname(filepath)

        print(f'Обнаружен файл: {file}, Путь: {filepath},\n Размер: {filesize} , Время изменения: {formatted_time},\n'
              f'Родительская директория: {parent_dir}')


if __name__ == '__main__':
    dir_info('.')