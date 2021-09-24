import turtle as t
import math
from random import *

def feather(color, width): #менятет параметры пера: цвет и толщина
    t.pendown()
    t.color(color)
    t.width(width)

def brown(): #броуновское движение частицы
    feather('red', 1)
    for i in range(1000):
        t.forward(30 * random())
        t.right(360 * random())

brown()
