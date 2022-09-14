# Вычислить число pi c заданной точностью d Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math


def find_numbers_of_pi(user_number: str):
    return len(user_number) - 2


print('Программа высчитывает число "pi" с заданной точностью')
number = input('Введите точность расчета в виде вещественного числа: ')
print(f'π = {round(math.pi, find_numbers_of_pi(number))}')

# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

def get_multipliers(user_number):
    result = []
    cur_number = user_number
    probe = 2
    while cur_number != 1:
        if cur_number % probe != 0:
            probe += 1
        else:
            cur_number /= probe
            result.append(probe)
    return result


number = int(input('Введите число для разложения на простые множители: '))
print(get_multipliers(number))

# Задайте последовательность чисел.
# Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

import random

def fill_list(min_number=0, max_number=9, length=0):
    new_list = []
    for i in range(length):
        new_list.append(random.randint(min_number, max_number))
    return new_list


user_length = int(input('Введите длину последовательности: '))
my_list = fill_list(length=user_length)
print(f'Начальная последовательность ---> {my_list}')
my_set = list(set(my_list))
print(f'Неповторяющиеся элементы последовательности ---> {my_set}')

# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и
# записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random


def fill_list(min_number=0, max_number=100, length=0):
    new_list = []
    for i in range(length):
        new_list.append(random.randint(min_number, max_number))
    return new_list


k = int(input('Введите степень: '))
string = ''
array = fill_list(length=k)
print(f'Список коэффициентов ---> {array}')
for i in range(k):
    if k - i <= 1:
        string += str(array[i]) + ' * x ' + ' = 0'
        break
    string += str(array[i]) + ' * x ^ ' + str(k - i) + ' + '
print(f'Полученный многочлен ---> {string} <---')
with open('task_4_homework.txt', 'w', encoding='utf-8') as file:
    file.writelines(string)

# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

file1 = []
file2 = []

with open('File1', 'r') as file:
    temp = file.read()
    file1 = temp.split()
    file1 = list(map(str, file1))

with open('File2', 'r') as file:
    temp = file.read()
    file2 = temp.split()
    file2 = list(map(str, file2))
sum_files = file1 + file2

print(file1)
print(file2)
print(sum_files)