# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


import easy


txt = ''
while txt != 'exit':
    print(f'Текущая папка {easy.current_dir()}\n')
    print('1. Перейти в папку\n'
                '2. Просмотреть содержимое текущей папки\n'
                '3. Удалить папку\n'
                '4. Создать папку\n')
    txt = input('Выберите действие: ')

    if txt == '1':
        _txt = input('Введите имя папки: ')
        easy.change_dir(_txt)

    elif txt == '2':
        result = easy.view_dir()
        if result:
            print(f'Содержимое текущей папки:\n{result}')
        else:
            print('Папка пуста')

    elif txt == '3':
        _txt = input('Введите имя папки из текущей директории для удаления: ')
        if easy.remove_dir(_txt):
            print(f'Папка {_txt} удалена\n')

    elif txt == '4':
        _txt = input('Введите имя папки для создания в текущей директории: ')
        if easy.create_dir(_txt):
            print(f'Папка {_txt} создана\n')