import turtle as t
import math
from random import *


def feather(color, width): #менятет параметры пера: цвет и толщина
    t.pendown()
    t.color(color)
    t.width(width)

def tp(x, y): #перемещает черепашку в координаты (x, y)
    t.penup()
    t.goto(x, y)

numbers = [''] * 10

def f_number(s, a): #функция, для рисования цифр
    t.left(90)
    c = 0
    for i in s:
        if i == '1':
            t.pendown()
        else:
            t.penup()
        dx, dy = 0, 0
        if c == 0 or c == 1:
            dy = a
        elif c == 2:
            dx = a
        elif c == 3 or c == 4:
            dy = -a
        elif c == 5 or c == 7:
            dx = -a
        elif c == 6 or c == 8:
            dx, dy = a, a
        x, y = t.pos()
        t.goto(x + dx, y + dy)
        t.penup()
        c += 1

def number(n, a): #рисует цифру n, размера a
    f_number(numbers[n], a)

def all_numbers(n): #рисует число n
    feather('blue', 2)
    s = []
    n = str(n)
    for i in n:
        s.append(int(i))
    for i in range(len(s)):
        tp(-300 + i * 60, 0)
        number(s[i], 40)

def file_numbers():
    file = open('3.3.txt', 'r')
    d = []
    for line in file:
        d.append(line.replace('\n', ''))
    for i in range(10):
        numbers[i] = d[i]
    print('Введите число:')
    s = input()
    all_numbers(s)

file_numbers()
