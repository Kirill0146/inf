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


def options(x0, y0, w, h, alpha, surface):
    #Поворачивает surface на alpha, переводит размеры в w*h, ставит в (x0, y0) screen
    
    surface = pygame.transform.rotate(surface, alpha)
    surface = pygame.transform.scale(surface, (w, h))
    screen.blit(surface, (x0, y0))

def brench_1(x0, y0, k):
    #Первая веточка
    w = 400
    h = 600
    surface = pygame.Surface([w, h], pygame.SRCALPHA)
    arc(surface, GREEN, (0, 0, 400, 200), PI * 0.2, PI * 1 , 15)
    surface = pygame.transform.rotate(surface, -45 + 12)
    ellipse(surface, GREEN, (300, 60, 6.0 * 5, 34 * 5))
    ellipse(surface, GREEN, (360, 65, 6.0 * 5, 34 * 5))
    ellipse(surface, GREEN, (420, 75, 6.0 * 5, 34 * 5))
    options(x0 - 100, y0 - 40, int(round(w * k)), int(round(h * k)), -12, surface)

def brench_2(x0, y0, k):
    #Вторая веточка
    w = 400
    h = 600
    surface = pygame.Surface([w, h], pygame.SRCALPHA)
    arc(surface, GREEN, (0, 0, 400 * 1.5, 190 * 1.5), PI * 0.2, PI * 0.9 , 15)
    surface = pygame.transform.rotate(surface, -45 + 12)
    ellipse(surface, GREEN, (300, 95, 6.0 * 5, 34 * 5))
    ellipse(surface, GREEN, (340, 92, 6.0 * 5, 34 * 5))
    ellipse(surface, GREEN, (390, 110, 6.0 * 5, 34 * 5))
    ellipse(surface, GREEN, (440, 130, 6.0 * 5, 34 * 5))
    ellipse(surface, GREEN, (510, 145, 6.0 * 5, 34 * 5))
    
    options(x0 - 100, y0 - 50, int(round(w * k)), int(round(h * k)), -12, surface)


def trunk_1():
    #Первый ствол
    rect(screen, GREEN, (254, 221, 8.6, 64))
    rect(screen, GREEN, (254, 293, 8.6, 57))
    polygon(screen, GREEN, [(259, 173), (265, 176),(259, 213), (254, 210)])
    polygon(screen, GREEN, [(258, 165), (261, 167),(269, 115), (266, 112)])

brench_1(220, 220, 0.4)
trunk_1()
brench_2(198, 137, 0.41)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
