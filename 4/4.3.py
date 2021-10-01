#Краткая документация:
#Данная программа рисует статичную картину: 4 бамбука и 2 панды
#Рисование бамбука оформлено в виде отдельной функции, что позволяет нарисовать сколько угодно бамбука
#Рисование панд НЕ оформлено в виде отдельной функций, в силу того,
#что у панд сильно отличаются лапы


import pygame 
from pygame.draw import *
import math

pygame.init()

#Цвета, заданные с помощью RGB:
GREEN = (0, 104, 52)  
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

FPS = 30 #FPS, в данной программе рисунок статичен
PI = math.pi #Пи
W, H = 750, 500 #Ширина и высота главного окна

screen = pygame.display.set_mode((W, H)) #Окно screen
rect(screen, (255, 177, 129), (0, 0, 750, 500)) #Задний фон


def options(x0, y0, w, h, alpha, flag_y, surface, screen_0):
    #Поворачивает surface на alpha, переводит размеры в w*h, отражает
    #относительно игрек, если стоит флаг, ставит в (x0, y0)
    #(левый верхний угол, везде и далее левый верхний угол, если не оговорено
    #обратное) screen_0 и его возвращает
    #(Вставляет в screen_0 surface)
    
    surface = pygame.transform.rotate(surface, alpha) #Поворот на угол alpha
    surface = pygame.transform.scale(surface, (w, h)) #Переводит исходные размеры в w*h
    surface = pygame.transform.flip(surface, flag_y, False) #Отражение картинки относительно игрек, если стоит флаг
    screen_0.blit(surface, (x0, y0)) #Размещает surface на screen_0 в (x0, y0)
    return screen_0 #Возвращает картинку screen_0, на которой теперь уже наложен surface


def brench_1(x0, y0, kx, ky, flag_y, screen_0):
    #Первая веточка
    #Координаты (x0, y0), коэффициент увеличение по икс и по игрек, флаг на отражение относительно оси игрек (отражает, если True), рисует на screen_0
    
    w, h = 400, 600 #ширина и высота
    surface = pygame.Surface([w, h], pygame.SRCALPHA) #Создает картинку w*h, полностью прозрачную
    arc(surface, GREEN, (0, 0, 400, 200), PI * 0.2, PI * 1 , 15) #Рисование дуги-веточки
    surface = pygame.transform.rotate(surface, -45 + 12) #Поворот на -45+12 градусов дуги
    ellipse(surface, GREEN, (300, 60, 6.0 * 5, 34 * 5)) #Листок 1
    ellipse(surface, GREEN, (360, 65, 6.0 * 5, 34 * 5)) #Листок 2
    ellipse(surface, GREEN, (420, 75, 6.0 * 5, 34 * 5)) #Листок 3
    surface = options(x0 - 100, y0 - 40, int(round(w * kx)), int(round(h * ky)), -12, flag_y, surface, screen_0) #Обновляю surface и ставляю в screen_0
    #(поворачиваю на 12, растягиваю, отражаю по игрек (если True), ставлю в соответствующие координаты)


def brench_2(x0, y0, kx, ky, flag_y, screen_0):
    #Вторая веточка
    #Координаты (x0, y0), коэффициент увеличение по икс и по игрек, флаг на отражение относительно оси игрек, рисует на screen_0
    
    w, h = 400, 600 #ширина и высота
    surface = pygame.Surface([w, h], pygame.SRCALPHA) #Создает картинку w*h, полностью прозрачную
    arc(surface, GREEN, (0, 0, 500 * 1.5, 220 * 1.5), PI * 0.1, PI * 0.9 , 15)#Рисование дуги-веточки
    surface = pygame.transform.rotate(surface, -45 + 12) #Поворот на -45+12 градусов дуги
    ellipse(surface, GREEN, (300, 95, 6.0 * 5, 34 * 5)) #Листок 1
    ellipse(surface, GREEN, (340, 92, 6.0 * 5, 34 * 5)) #Листок 2
    ellipse(surface, GREEN, (390, 110, 6.0 * 5, 34 * 5)) #Листок 3
    ellipse(surface, GREEN, (440, 130, 6.0 * 5, 34 * 5)) #Листок 4
    ellipse(surface, GREEN, (510, 145, 6.0 * 5, 34 * 5)) #Листок 5
    
    surface = options(x0 - 100, y0 - 50, int(round(w * kx)), int(round(h * ky)), -12, flag_y, surface, screen_0)#Обновляю surface и ставляю в screen_0
    #(поворачиваю на 12, растягиваю, отражаю по игрек (если True), ставлю в соответствующие координаты)


def trunk(x0, y0, kx, ky, screen_0):
    #Ствол
    #Координаты (x0, y0), коэффициент масштабирования, рисует на screen_0
    
    w, h = 750, 500 #Ширина и высота
    surface = pygame.Surface([w, h], pygame.SRCALPHA) #Создает картинку w*h, полностью прозрачную
    rect(surface, GREEN, (254, 221, 8.6, 64)) #Прямоугольник 1
    rect(surface, GREEN, (254, 293, 8.6, 57)) #Прямоугольник 2
    polygon(surface, GREEN, [(259, 173), (265, 176),(259, 213), (254, 210)])#Прямоугольник 3
    polygon(surface, GREEN, [(258, 165), (261, 167),(269, 115), (266, 112)]) #Прямоугольник 4

    surface = options(x0 - 254, y0 - 115, int(round(w * kx)), int(round(h * ky)), 0, False, surface, screen_0)


def bambuk(x, y, kx, ky):
    #Рисует бамбук
    #Координаты (x, y), коэффициент масштабирования
    
    surface = pygame.Surface([750, 500], pygame.SRCALPHA) #Создает картинку w*h, полностью прозрачную
    brench_1(220, 220, 0.4, 0.4, False, surface) #Первая ветка
    
    trunk(254, 115, 1, 1, surface) #Ствол
    brench_2(198, 137, 0.41, 0.41, False, surface) #Вторая ветка
    brench_1(345, 175, 0.4, 0.4, True, surface) #Первая ветка, сим. отраженная по игрек
    brench_2(360, 100, 0.41, 0.41, True, surface) #Вторая векта, сим. отраженная по игрек

    options(x - 175, y - 130, int(round(750 * kx)), int(round(500 * ky)), 0, False, surface, screen)


def panda():
    #Рисует обе панды: Панда1 -- правая большая панда, Панда2 -- маленькая панда, слева
    
    w, h = 750, 500 #Ширина и высота
    surface = pygame.Surface([750, 500], pygame.SRCALPHA) #Создает картинку w*h, полностью прозрачную
    ellipse(surface, WHITE, (418.5, 219, 203, 118.2)) #Панда1. Тело (овал)
    ellipse(surface, WHITE, (331.1, 373.4, 39.6 * 2, 23 * 2)) #Панда2. Тело (овал)
    
    file = open('4.3.txt', 'r') #Считываю файл, в котором указаны пары координат для рисования сложных фигур в виде polygon
    #Файл имеет следующую структуру: сперва цвет большими буквами, затем пары координат polygon
    list_coords = [] #Список координат для рисования polygon
    color = "BLACK" #Цвет по умолчанию (начальный цвет)

    for a in file: #Построчно считываю файл
        k = a.replace('\n', '') #Так как строчка оканчивается на '\n', то его удаляем

        if len(k.split()) <= 1: #Если встретили строчку с одним словом, то это новый цвет и пора нарисовать polygon

            if len(list_coords) != 0: #Если список координат не пуст, то рисуем polygon
                polygon(surface, color, list_coords) #polygon

            list_coords = [] #Обнуляем список координат
            color = k #Обновляем цвет

        else:
            a, b = k.split() #Считываем пару координат (x,y)
            list_coords.append([float(a), float(b)]) #Добавляем пару координат в список list_coords
            
    polygon(surface, color, list_coords) #Рисуем последний Полигон     
    file.close() #Закрываю файл

    #Остатки панды1
    circle(surface, BLACK, (476.6, 288.9), 18.9) #Правый глаз панды1
    ellipse(surface, BLACK, (417.1, 260.2, 25.7, 37.3)) #Левый глаз панды1
    ellipse(surface, BLACK, (423.8, 312.3, 28.7, 17.2)) #Нос панды1

    #Остатки панды2
    circle(surface, BLACK, (346.5, 400.7), 7.4) #Правый глаз панды2
    ellipse(surface, BLACK, (322.6, 389.3, 10.6, 14.6)) #Левый глаз панды2
    ellipse(surface, BLACK, (325.7, 410, 15, 9)) #Нос панды2
    
    options(0, 0, 750, 500, 0, False, surface, screen)



bambuk(0, 160, 1, 1) #Первый бамбук
bambuk(150, 106, 1.0, 1.2) #Второй бамбук
bambuk(50, -20, 2, 1.5) #Третий бамбук
bambuk(570, 0, 1.0, 1.3) #Четвертый бамбук

panda() #Панды


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
