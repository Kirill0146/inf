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

def bamb_1(x0, y0, k):
    #Первая веточка
    w = 400
    h = 600
    surface = pygame.Surface([w, h], pygame.SRCALPHA)
    arc(surface, GREEN, (0, 0, 400, 200), PI * 0.2, PI * 1 , 15)
    surface = pygame.transform.rotate(surface, -45 + 12)
    ellipse(surface, GREEN, (300, 60, 5.0 * 5, 34 * 5))
    ellipse(surface, GREEN, (360, 65, 5.0 * 5, 34 * 5))
    ellipse(surface, GREEN, (420, 75, 5.0 * 5, 34 * 5))
    options(x0, y0, int(round(w * k)), int(round(h * k)), -12, surface)

bamb_1(100, 100, 0.5)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()