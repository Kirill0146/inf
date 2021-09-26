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


def options(x0, y0, w, h, alpha, flag_y, surface, flag):
    #Поворачивает surface на alpha, переводит размеры в w*h, отражает относительно игрек,
    #если стоит флаг, ставит в (x0, y0) screen, если стоит флаг
    
    surface = pygame.transform.rotate(surface, alpha)
    surface = pygame.transform.scale(surface, (w, h))
    surface = pygame.transform.flip(surface, flag_y, False)
    if (flag):
        screen.blit(surface, (x0, y0))
    return surface

def brench_1(x0, y0, kx, ky, flag_y, flag):
    #Первая веточка
    #Координаты (x0, y0), коэффициент увеличение, флаг на отражение относительно оси игрек, рисует на screen, если стоит флаг
    w = 400
    h = 600
    surface = pygame.Surface([w, h], pygame.SRCALPHA)
    arc(surface, GREEN, (0, 0, 400, 200), PI * 0.2, PI * 1 , 15)
    surface = pygame.transform.rotate(surface, -45 + 12)
    ellipse(surface, GREEN, (300, 60, 6.0 * 5, 34 * 5))
    ellipse(surface, GREEN, (360, 65, 6.0 * 5, 34 * 5))
    ellipse(surface, GREEN, (420, 75, 6.0 * 5, 34 * 5))
    surface = options(x0 - 100, y0 - 40, int(round(w * kx)), int(round(h * ky)), -12, flag_y, surface, flag)
    return surface, x0 - 100, y0 - 40

def brench_2(x0, y0, kx, ky, flag_y, flag):
    #Вторая веточка
    #Координаты (x0, y0), коэффициент увеличение, флаг на отражение относительно оси игрек, рисует на screen, если стоит флаг
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
    
    surface = options(x0 - 100, y0 - 50, int(round(w * kx)), int(round(h * ky)), -12, flag_y, surface, flag)
    return surface, x0 - 100, y0 - 50

def trunk(x0, y0, kx, ky, flag):
    #Ствол
    #Координаты (x0, y0), коэффициент масштабирования, рисует на screen, если стоит флаг
    w, h = 750, 500
    surface = pygame.Surface([w, h], pygame.SRCALPHA)
    rect(surface, GREEN, (254, 221, 8.6, 64))
    rect(surface, GREEN, (254, 293, 8.6, 57))
    polygon(surface, GREEN, [(259, 173), (265, 176),(259, 213), (254, 210)])
    polygon(surface, GREEN, [(258, 165), (261, 167),(269, 115), (266, 112)])

    surface = options(x0 - 254, y0 - 115, int(round(w * kx)), int(round(h * ky)), 0, False, surface, flag)
    return surface, x0 - 254, y0 - 115

def bambuk(x, y, kx, ky):
    #Рисует бамбук
    surface = pygame.Surface([750, 500], pygame.SRCALPHA)
    
    surface0, x0, y0 = brench_1(220, 220, 0.4, 0.4, False, False)
    surface.blit(surface0, (x0, y0))
    
    surface0, x0, y0 = trunk(254, 115, 1, 1, False)
    surface.blit(surface0, (x0, y0))
    
    surface0, x0, y0 = brench_2(198, 137, 0.41, 0.41, False, False)
    surface.blit(surface0, (x0, y0))
    
    surface0, x0, y0 = brench_1(345, 175, 0.4, 0.4, True, False)
    surface.blit(surface0, (x0, y0))
    
    surface0, x0, y0 =brench_2(360, 100, 0.41, 0.41, True, False)
    surface.blit(surface0, (x0, y0))

    options(x, y, int(round(750 * kx)), int(round(500 * ky)), 0, False, surface, True)

    
bambuk(0, 0, 1, 1)
bambuk(-100, -120, 2, 1.3)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
