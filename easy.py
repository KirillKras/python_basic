import os

def current_dir():
    return os.getcwd()

def change_dir(dir_name):
    try:
        os.chdir(dir_name)
    except OSError:
        print('Не удалось перейти в папку!\n'.upper())

def create_dir(dir_name):
    try:
        os.mkdir(dir_name)
        return True
    except OSError:
        print('Не удалось создать папку!\n'.upper())

def remove_dir(dir_name):
    try:
        os.removedirs(dir_name)
        return True
    except OSError:
        print('Не удалось удалить папку!\n'.upper())

def view_dir():
    folders = []
    for r, d, f in os.walk(os.getcwd()):
        for folder in d:
            folders.append(folder)
    return ''.join([f'{folder}\n' for folder in folders])