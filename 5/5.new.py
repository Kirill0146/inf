import pygame
from pygame.draw import *

pygame.init()

FPS = 30
BLACK = (0, 0, 0)
ORANGE = (255, 128, 0)
PURPLE = (92, 28, 92)

screen = pygame.display.set_mode((700, 625)) #Вся картинка разбита на 4 полосы


rect(screen, (255, 204, 153), (0,0,700,140)) #1я полоса
rect(screen, (255, 204, 204), (0,140,700,140)) #2я полоса
circle(screen,(255,255,0),(375,140),50) #звезда по имени Солнце
rect(screen, (255, 204, 153), (0,280,700,140)) #3я полоса
rect(screen, (159, 100, 159), (0,420,700,280)) #4я полоса


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
    w0, h0 = 45, 21
    surface = pygame.Surface([w0, h0], pygame.SRCALPHA) #Создает картинку w*h, полностью прозрачную
    from_file('bird.txt', surface)
    options(x0, y0, w, h, 0, False, surface, screen)
   
    
#Птицы
bird(300,220,40,40)
bird(370,228,40,40)
bird(370,265,40,40)
bird(270,295,40,40)
bird(450,430,40,40)
bird(480,470,28,28)
bird(540,510,80,60)
bird(570,460,28,28)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
