# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    lst_tn = list(str(ticket_number))
    return sum(map(int, lst_tn[:3])) == sum(map(int, lst_tn[3:6]))


print(lucky_ticket(123006))
print(lucky_ticket(123321))
print(lucky_ticket(436751))
