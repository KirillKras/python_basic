# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import os
from shutil import copyfile

def copy_current_file():
    print(os.path.basename(__file__))
    copyfile(os.path.basename(__file__), 'copy__' + os.path.basename(__file__))

copy_current_file()