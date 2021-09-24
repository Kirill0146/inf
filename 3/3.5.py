import turtle as t
import math
from random import *

def feather(color, width): #менятет параметры пера: цвет и толщина
    t.pendown()
    t.color(color)
    t.width(width)

def final():
    global pool, numbers_of_turtles, dt, k #список черепах, их количество, dt, коэффициент гравитационного вз-ия
    global x_border, y_border, alpha #границы, коэффициент потерь
    x_border = 300
    y_border = 300
    alpha = 1
    pool = []
    number_of_turtles = 20
    dt = 5
    k = 1

    def dist(unit1, unit2): #расстояние между 2 черепашками
        x1, y1 = unit1['x'], unit1['y']
        x2, y2 = unit2['x'], unit2['y']
        s = (x1 - x2) ** 2 + (y1 - y2) ** 2
        return s ** 0.5
    
    def check(unit1, unit2): #проверяет, столкнулись ли черепахи
        r1 = unit1['r']
        r2 = unit2['r']
        if dist(unit1, unit2) <= (r1 + r2):
            return 1
        return 0
    
    def create(m, x, y, vx, vy, ax, ay, size, speed): #создает черепашку
        d = {'m':m, 'vx':vx, 'vy':vy, 'x':x, 'y':y, 'ax':ax, 'ay':ay, 'r':size * 10, 't':t.Turtle(shape = 'circle')}
        d['t'].shapesize(size)
        d['t'].penup()
        d['t'].speed(0)
        d['t'].goto(x, y)
        d['t'].speed(speed)
        pool.append(d)
        
    def check_border(unit): #проверяет выход черепашки за границы карты
        if unit['x'] >= x_border or unit['x'] <= -x_border:
            unit['vx'] *= -1 
        if unit['y'] >= y_border or unit['y'] <= - y_border:
            unit['vy'] *= -1 
            
    def move(): #сдвигает все черепашки
        for unit in pool:
            unit['x'] += unit['vx'] * dt
            unit['y'] += unit['vy'] * dt
            unit['vx'] += unit['ax']* dt
            unit['vy'] += unit['ay'] * dt
            unit['t'].goto(unit['x'], unit['y'])
            check_border(unit)
            
    def F(unit1, unit2): #считает силу взаимодействия между 2 черепашками
        s = dist(unit1, unit2)
        return -k * unit1['m'] * unit2['m'] / s ** 2


    def a(): #пересчитывает все ускорения
        for unit in pool:
            unit['ax'] = 0
            unit['ay'] = 0
            
        for unit1 in pool:
            for unit2 in pool:
                if unit1 != unit2:
                    f = F(unit1, unit2)
                    unit1['ax'] += f * (unit2['x'] - unit1['x']) / dist(unit1, unit2) / unit1['m']
                    unit1['ay'] += f * (unit2['y'] - unit1['y']) / dist(unit1, unit2) / unit1['m']
                    unit2['ax'] += f * (unit1['x'] - unit2['x']) / dist(unit2, unit1) / unit2['m']
                    unit2['ay'] += f * (unit1['y'] - unit2['y']) / dist(unit2, unit1) / unit2['m']
                    if check(unit1, unit2) == 1:
                        unit1['vx'] *= alpha
                        unit2['vy'] *= alpha


            
             
    def iter_(): #одна итерация
        move()
        a()
    
    t.tracer(False)
    for i in range(number_of_turtles):
        mas = randint(1, 1)
        create(mas, randint(-300, 300), randint(-300, 300), random() - 0.5, random() - 0.5, 0, 0, 1 + mas / 10, 0)
    t.tracer(True)
    for i in range(10000):
        iter_()


final()
