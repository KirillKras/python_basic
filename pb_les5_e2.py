# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os

def view_dir():
    for r, d, f in os.walk(os.getcwd()):
        for folder in d:
            print(folder)

view_dir()