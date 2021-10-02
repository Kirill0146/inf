import pygame
from pygame.draw import *

pygame.init()

FPS = 30
BLACK = (0, 0, 0)
ORANGE = (255, 128, 0)
PURPLE = (92, 28, 92)

screen = pygame.display.set_mode((700, 625)) #вся картинка разбита на 4 полосы
rect(screen, (255, 204, 153), (0,0,700,140)) #1я полоса
rect(screen, (255, 204, 204), (0,140,700,140)) #2я полоса


def brline(x1,y1,x2,y2,x3,y3,l): #делает заливку для трех точек и линии, ограничивающей их снизу. Или две прямоугольные трапеции, залитые цветом
    polygon(screen,ORANGE ,[(x1,y1),(x2,y2),(x1,l)])
    polygon(screen,ORANGE ,[(x3,y3),(x2,y2),(x3,l)])
    polygon(screen,ORANGE ,[(x1,l),(x2,y2),(x3,l)])

brline(5,280,8,250,160,130,280)
brline(160,130,175,135,190,155,280)
brline(190,155,300,240,350,230,280)
brline(350,230,375,243,425,210,280)
brline(425,210,455,220,465,210,280)
brline(465,210,565,120,585,120,280)
brline(585,120,615,150,635,145,280)
brline(635,145,665,170,680,155,280)
brline(665,170,680,155,700,175,280) #подобранные точки гор

polygon(screen,(255, 204, 204),[(210,280),(700,175),(700,280)]) #треугольник того же цвета, что и фон, чтобы "скосить" картинку
circle(screen,(255,128,0),(572,121),12.99) #скругленная вершина правой горы
circle(screen,(255, 204, 204),(10,100),150) #закругленный склон левой горы
circle(screen,(255, 204, 204),(490,130),70) #закругленный склон правой горы
rect(screen, (255, 204, 153), (0,0,160,140)) #убирает часть круга, закруглящего склон левой горы
rect(screen, (255, 204, 153), (420,0,140,140)) #аналогично для круга от правой горы
polygon(screen,(255,128,0),[(159,130),(160,140),(154,140)]) #треугольник для продолжения горы на новый слой
circle(screen,(255,255,0),(375,140),50) #звезда по имени Солнце

rect(screen, (255, 204, 153), (0,280,700,140)) #3я полоса

polygon(screen,(255,128,0),[(210,280),(3,320),(5,280)])
polygon(screen,(153,0,0),[(50,420),(0,320),(0,420)])
ellipse(screen, (153,0,0),(12,270,124,270))
polygon(screen,(153,0,0),[(50,420),(0,320),(0,420)])
rect(screen, (153,0,0), (0,400,700,20))
polygon(screen,(153,0,0),[(136,400),(156,330),(196,350)])
polygon(screen,(153,0,0),[(196,350),(216,290),(256,300)])
polygon(screen,(153,0,0),[(256,300),(296,340),(136,400)])
polygon(screen,(153,0,0),[(296,340),(356,320),(296,420)])
circle(screen,(153,0,0),(450,300),40)
polygon(screen,(153,0,0),[(356,320),(414,281),(390,420)])
polygon(screen,(153,0,0),[(50,420),(296,340),(296,420)])
polygon(screen,(153,0,0),[(296,420),(356,320),(390,420)])
polygon(screen,(153,0,0),[(484,280),(490,420),(550,330)]) #6
polygon(screen,(153,0,0),[(550,420),(490,420),(550,330)])
polygon(screen,(153,0,0),[(550,330),(590,290),(550,420)]) #5
polygon(screen,(153,0,0),[(590,290),(590,420),(550,420)])
polygon(screen,(153,0,0),[(590,290),(590,420),(620,300)]) #4
polygon(screen,(153,0,0),[(620,420),(590,420),(620,300)])
polygon(screen,(153,0,0),[(620,300),(620,420),(650,285)]) #3
polygon(screen,(153,0,0),[(650,420),(620,420),(650,285)])
polygon(screen,(153,0,0),[(650,285),(650,420),(670,290)]) #2
polygon(screen,(153,0,0),[(670,420),(650,420),(670,290)])
polygon(screen,(153,0,0),[(670,290),(700,210),(670,420)]) #1
polygon(screen,(153,0,0),[(700,420),(700,210),(670,420)])
rect(screen, (153,0,0), (386,305,120,100))
#трындец

rect(screen, (159, 100, 159), (0,420,700,280)) #4я полоса

def brline1(x1,y1,x2,y2,x3,y3,l): #полностью такая же функция, просто цвет поменял
    polygon(screen, PURPLE,[(x1,y1),(x2,y2),(x1,l)])
    polygon(screen, PURPLE,[(x3,y3),(x2,y2),(x3,l)])
    polygon(screen, PURPLE,[(x1,l),(x2,y2),(x3,l)])

brline1(0,320,100,350,250,575,625)
brline1(250,575,375,600,490,540,625)
brline1(490,540,555,560,650,420,625)
circle(screen,(159, 100, 159),(322,545),76) #закругляет слева
polygon(screen,(92,28,92),[(555,560),(535,555),(580,515)]) #убирает неровности в горе, чтобы круг лучше влез
circle(screen,(159, 100, 159),(540,515),40) #закругляет гору справа
circle(screen,(92,28,92),(676,425),25) #вершина горы справа
rect(screen,(92,28,92),(651,425,50,200)) # заливает оставшуюся часть горы
polygon(screen,(92,28,92),[(676,400),(700,398),(700,425)]) #убирает все оставшиеся пробелы


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
