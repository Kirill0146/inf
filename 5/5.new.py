import pygame
from pygame.draw import *

pygame.init()

FPS = 3 #Частота
#Цвета:
BLACK = (0, 0, 0)
ORANGE = (252, 153, 45)
PURPLE = (44, 7, 33)
REDD = (173, 65, 49)

W, H = 700, 625 #Ширина и высота

screen = pygame.display.set_mode((W, H)) #Вся картинка разбита на 4 полосы

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


def from_file(file_name, surface):
    file = open(file_name, 'r') #Считываю файл, в котором указаны пары координат для рисования сложных фигур в виде polygon
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
    return surface


def bird(x0, y0, w, h):
    #Рисует птицу w*h с координатой левого верхнего угла (x0, y0)
    
    w0, h0 = 45, 21 #Размеры птицы
    surface = pygame.Surface([w0, h0], pygame.SRCALPHA) #Создает картинку w*h, полностью прозрачную
    from_file('bird.txt', surface) #Рисует птицу на surface
    options(x0, y0, w, h, 0, False, surface, screen)

def fluct(s, y0):
    #Берет исходный список пар точек и немного меняет его по некому правилу
    #Правило: d = d1 + d2,
    #        d1 = eps * A * random(-0.5; 0.5)
    #        d2 = eps * (y[i - 1] - y[i] + y[i + 1] - y[i]) * random(0; 1)
    
    import random
    eps = 0.02 #Процент от амплитуды
    k = 2 #Коэффициент поправки
    for i in range(len(s)):
        #Учитываем поправку d, связанную с соседями (чтобы не были сильно острыми горы)
        
        d = 0
        if i > 0:
            d += (s[i - 1][1] - s[i][1]) * random.random()
        if i < len(s) - 2:
            d += (s[i + 1][1] - s[i][1]) * random.random()
        t = (s[i][1] - y0) * (random.random() - 0.5) #Случайная поправка t 
        s[i][1] += eps * (t + d)

    return s

def get_mountains():
    #Возвращает список mountains, который состоит из трех словарей,
    #внутри которых содержится color, x0, y0, coords, lx (ширина основания), ly (высота основания), dx (смещение картинки по икс), dy (смещение картинки по игрек)

    file = open('gor.txt', 'r')
    mountains = []
    number = 0
    
    for a in file: #Построчно считываю файл
        k = a.replace('\n', '') #Так как строчка оканчивается на '\n', то его удаляем
        if len(k.split()) == 1:
            mountains.append({'color':'', 'x0':0, 'y0':0, 'lx':0, 'ly':0, 'dx':0, 'dy':0, 'coords':[]}) #Добавляю новую гору
            if len(mountains[number]['coords']) != 0: #Если новый цвет, значит новая гора
                number += 1
            mountains[number]['color'] = eval(k)
        elif len(k.split()) == 6: #Параметры горы
            x0, y0, lx, ly, dx, dy = map(float, k.split())
            mountains[number]['x0'], mountains[number]['y0'], mountains[number]['lx'], mountains[number]['ly'], mountains[number]['dx'], mountains[number]['dy'] = x0 + dx, y0 + dy, lx, ly, dx, dy
        elif len(k.split()) == 2: #Координаты одной из точки горы
            x, y = map(float, k.split())
            x, y = x + mountains[number]['dx'], y + mountains[number]['dy']
            mountains[number]['coords'].append([x, y])

    return mountains


def iter_mountains(mountains):
    #Рисует горы. Очередная итерация

    for number in range(len(mountains)):
        mountains[number]['coords'] = fluct(mountains[number]['coords'], mountains[number]['y0']) #Немного флуктуируем координаты
        s = mountains[number]['coords'] #Записываем координаты в список s
        s.append([mountains[number]['x0'] + mountains[number]['lx'], mountains[number]['y0']  + mountains[number]['ly']]) #Добавляем в список левую нижнюю вершину
        s.append([mountains[number]['x0'], mountains[number]['y0']]) #и правую нижнюю
        polygon(screen, mountains[number]['color'], s) #Рисуем гору
        s.pop(len(s) - 1) #Убираем две добавленные вершины
        s.pop(len(s) - 1)
        
    return mountains

def draw_background():
    #Рисует задний фон и Солнце
    
    rect(screen, (255, 204, 153), (0,0,700,140)) #1я полоса
    rect(screen, (255, 204, 204), (0,140,700,140)) #2я полоса
    circle(screen,(255,255,0),(375,140),50) #звезда по имени Солнце
    rect(screen, (255, 204, 153), (0,280,700,140)) #3я полоса
    rect(screen, (159, 100, 159), (0,420,700,280)) #4я полоса


def draw_birds():    
    #Птицы
    
    bird(300,220,40,40)
    bird(370,228,40,40)
    bird(370,265,40,40)
    bird(270,295,40,40)
    bird(450,430,40,40)
    bird(480,470,28,28)
    bird(540,510,80,60)
    bird(570,460,28,28)


def draw_all(mountains):
    #Рисует все!
    
    draw_background()
    mountains = iter_mountains(mountains)
    draw_birds()
    return mountains

mountains = get_mountains()

pygame.display.update()
clock = pygame.time.Clock()
finished = False


while not finished:
    clock.tick(FPS)
    
    mountains = draw_all(mountains)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            
    pygame.display.update()

pygame.quit()
