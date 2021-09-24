import turtle as t
import math
from random import *


def feather(color, width): #менятет параметры пера: цвет и толщина
    t.pendown()
    t.color(color)
    t.width(width)
    
def ballistics():
    t.speed(3)
    sp = 10
    
    def shmak(sp):
        t.speed(0)
        feather('red', 1)
        for i in range(30):
            t.forward(sp * random())
            t.right(360 * random())
        t.speed(3)
        
    t.shape('turtle')
    t.right(90)
    Vx0, Vy0 = 20, 50
    Vx, Vy = Vx0, Vy0
    ay = -10
    dt = 0.03
    x0, y0 = -300, 0
    x, y = x0, y0
    t.penup()
    t.goto(x, y)
    t.pendown()
    k = 0.8
    for i in range(10000):
        x += Vx * dt
        y += Vy * dt
        Vy += ay * dt
        t.goto(x, y)
        if Vx0/Vx >= 10:
            break
        if y < y0:
            Vy *= -1 * k
            Vx *= k
            y = y0
            shmak(sp)
            sp *= k
            feather('black', 1)
            t.goto(x, y)

ballistics()
