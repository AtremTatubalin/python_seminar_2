'''Задача 12: Петя и Катя – брат и сестра. Петя – студент, 
а Катя – школьница. Петя помогает Кате по математике. Он задумывает два 
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и 
их произведение P. Помогите Кате отгадать задуманные Петей числа.'''

import math

Summ = input("Введите сумму двух чисел: ")
Multiplication = input("Введите произведение двух чисел: ")
Summ = int(Summ)
Multiplication = int(Multiplication)
y1 = 0
y2 = 0

Dis = Summ ** 2 - 4 * Multiplication
if (Dis < 0):
    print("Таких чисел нет.")
else:
    y1 = (- Summ - math.sqrt(Dis)) / -2
    y2 = (- Summ + math.sqrt(Dis)) / -2

if (y1 >= 0 and y2 >= 0):
    x1 = Summ - y1
    x2 = Summ - y2
    print(f"X = {x1}; Y = {y1}, либо X = {x2}; Y = {y2}")
elif (y1 >= 0 and y2 < 0):
    x = Summ - y1
    print(f"X = {x}; Y = {y1}")
elif (y1 < 0 and y2 >= 0):
    x = Summ - y2
    print(f"X = {x}; Y = {y2}")
