# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def number(n, i=2):
    if n == 1 or n == 2:
        return True
    elif n % i == 0:
        return False
    elif i*i>n:
        return True
    return number(n, i+1)

print(number(5))
