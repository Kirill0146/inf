import pygame
from pygame.draw import *
import math

pygame.init()

GREEN = (0, 104, 52)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 30
PI = math.pi
screen = pygame.display.set_mode((750, 500))


rect(screen, (255, 177, 129), (0, 0, 750, 500))


def options(x0, y0, w, h, alpha, flag_y, surface, screen_0):
    #Поворачивает surface на alpha, переводит размеры в w*h, отражает относительно игрек,
    #если стоит флаг, ставит в (x0, y0) screen_0 и его возвращает
    #(Вставляет в screen_0 surface)
    
    surface = pygame.transform.rotate(surface, alpha)
    surface = pygame.transform.scale(surface, (w, h))
    surface = pygame.transform.flip(surface, flag_y, False)
    screen_0.blit(surface, (x0, y0))
    return screen_0

def brench_1(x0, y0, kx, ky, flag_y, screen_0):
    #Первая веточка
    #Координаты (x0, y0), коэффициент увеличение, флаг на отражение относительно оси игрек, рисует на screen_0
    w = 400
    h = 600
    surface = pygame.Surface([w, h], pygame.SRCALPHA)
    arc(surface, GREEN, (0, 0, 400, 200), PI * 0.2, PI * 1 , 15)
    surface = pygame.transform.rotate(surface, -45 + 12)
    ellipse(surface, GREEN, (300, 60, 6.0 * 5, 34 * 5))
    ellipse(surface, GREEN, (360, 65, 6.0 * 5, 34 * 5))
    ellipse(surface, GREEN, (420, 75, 6.0 * 5, 34 * 5))
    surface = options(x0 - 100, y0 - 40, int(round(w * kx)), int(round(h * ky)), -12, flag_y, surface, screen_0)

def brench_2(x0, y0, kx, ky, flag_y, screen_0):
    #Вторая веточка
    #Координаты (x0, y0), коэффициент увеличение, флаг на отражение относительно оси игрек, рисует на screen_0
    w = 400
    h = 600
    surface = pygame.Surface([w, h], pygame.SRCALPHA)
    arc(surface, GREEN, (0, 0, 500 * 1.5, 220 * 1.5), PI * 0.1, PI * 0.9 , 15)
    surface = pygame.transform.rotate(surface, -45 + 12)
    ellipse(surface, GREEN, (300, 95, 6.0 * 5, 34 * 5))
    ellipse(surface, GREEN, (340, 92, 6.0 * 5, 34 * 5))
    ellipse(surface, GREEN, (390, 110, 6.0 * 5, 34 * 5))
    ellipse(surface, GREEN, (440, 130, 6.0 * 5, 34 * 5))
    ellipse(surface, GREEN, (510, 145, 6.0 * 5, 34 * 5))
    
    surface = options(x0 - 100, y0 - 50, int(round(w * kx)), int(round(h * ky)), -12, flag_y, surface, screen_0)

def trunk(x0, y0, kx, ky, screen_0):
    #Ствол
    #Координаты (x0, y0), коэффициент масштабирования, рисует на screen_0
    w, h = 750, 500
    surface = pygame.Surface([w, h], pygame.SRCALPHA)
    rect(surface, GREEN, (254, 221, 8.6, 64))
    rect(surface, GREEN, (254, 293, 8.6, 57))
    polygon(surface, GREEN, [(259, 173), (265, 176),(259, 213), (254, 210)])
    polygon(surface, GREEN, [(258, 165), (261, 167),(269, 115), (266, 112)])

    surface = options(x0 - 254, y0 - 115, int(round(w * kx)), int(round(h * ky)), 0, False, surface, screen_0)

def bambuk(x, y, kx, ky):
    #Рисует бамбук
    #Координаты (x, y), коэффициент масштабирования
    surface = pygame.Surface([750, 500], pygame.SRCALPHA)
    brench_1(220, 220, 0.4, 0.4, False, surface)
    
    trunk(254, 115, 1, 1, surface)
    brench_2(198, 137, 0.41, 0.41, False, surface)
    brench_1(345, 175, 0.4, 0.4, True, surface)
    brench_2(360, 100, 0.41, 0.41, True, surface)

    options(x - 175, y - 130, int(round(750 * kx)), int(round(500 * ky)), 0, False, surface, screen)

def panda():
    surface = pygame.Surface([750, 500], pygame.SRCALPHA)
    ellipse(surface, WHITE, (418.5, 219, 203, 118.2)) #Панда1. Тело
    ellipse(surface, WHITE, (331.1, 373.4, 39.6 * 2, 23 * 2)) #Панда2. Тело
    
    file = open('панда2.txt', 'r')
    s = []
    color = "BLACK"
    for a in file:
        k = a.replace('\n', '')
        if len(k.split()) <= 1:
            if len(s) != 0:
                polygon(surface, color, s)
            s = []
            color = k
        else:
            a, b = k.split()
            s.append([float(a), float(b)])
    polygon(surface, color, s)       
    file.close()

    #Остатки панды1
    circle(surface, BLACK, (476.6, 288.9), 18.9)
    ellipse(surface, BLACK, (417.1, 260.2, 25.7, 37.3))
    ellipse(surface, BLACK, (423.8, 312.3, 28.7, 17.2))

    #Остатки панды2
    circle(surface, BLACK, (346.5, 400.7), 7.4)
    ellipse(surface, BLACK, (322.6, 389.3, 10.6, 14.6))
    ellipse(surface, BLACK, (325.7, 410, 15, 9))
    
    options(0, 0, 750, 500, 0, False, surface, screen)



bambuk(0, 160, 1, 1) #Первый бамбук
bambuk(150, 106, 1.0, 1.2) #Второй бамбук
bambuk(50, -20, 2, 1.5) #Третий бамбук
bambuk(570, 0, 1.0, 1.3) #Четвертый бамбук

panda() #Панда

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
