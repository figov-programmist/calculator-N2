import math 
import os 
import time 
while True:
    print("Введи 1, чтобы очистить консоль ")
    print("Введи 2, чтобы связатся с разработчиком") 
    print("Выбери действие (+,-,/,*,)")
    znak = input()
    if znak == "+":
        a = int(input("Введи первое число "))
        b = int(input("Введи второе число "))
        c = a + b 
        print("Ответ: ", int(c))
    if znak == "-":
        a = int(input("Введи первое число "))
        b = int(input("Введи второе число "))
        c = a + b 
        if a < b: 
            print("Ошибка... ")
            print("Переменная 'a' (", int(a), "), меньше переменной 'b' (", int(b), ") "
            continue
            break
        print("Ответ: ", int(c))
    if znak == "*":
        a = int(input("Введи первое число "))
        b = int(input("Введи второе число "))
        c = a + b 
        print("Ответ: ", int(c))
    if znak == "/":
        a = int(input("Введи первое число "))
        b = int(input("Введи второе число "))
        c = a + b 
        print("Ответ: ", int(c))
    if znak == "1":
        os.system('clear')
        print("Вы очистили консоль. ")
        time.sleep(3)
        os.system('clear')
    if znak == "2":
        print("(Discord) lampochka#4376")