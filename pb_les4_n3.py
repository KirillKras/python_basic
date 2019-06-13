# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

import random
import re

n = [str(random.randint(0,9)) for _ in range(2500)]
n = ''.join(n)

with open('number.txt', 'w') as f:
    f.write(n)

with open('number.txt', 'r') as f:
    n = f.read()

result = []
for r in [r'0+', r'1+', r'2+', r'3+', r'4+', r'5+', r'6+', r'7+', r'8+', r'9+']:
    math = re.findall(r, n)
    result.extend(math)

max_len = 0
pos = None
for s in result:
    if len(s) > max_len:
        max_len = len(s)
        pos = s

print(pos)