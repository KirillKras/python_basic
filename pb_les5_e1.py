# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

def create_dirs():
    for path_name in [f'dir_{i}' for i in range(1, 9+1)]:
        os.mkdir(path_name)

def remove_dirs():
    for path_name in [f'dir_{i}' for i in range(1, 9+1)]:
        os.removedirs(path_name)

create_dirs()
#remove_dirs()