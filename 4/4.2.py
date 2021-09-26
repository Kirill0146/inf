import pygame
from pygame.draw import *

pygame.init()

GREEN = (0, 104, 52)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 30
screen = pygame.display.set_mode((750, 500))


rect(screen, (255, 177, 129), (0, 0, 750, 500))


def options(x0, y0, w, h, alpha, surface):
    #Поворачивает surface на alpha, переводит размеры в w*h, ставит в (x0, y0) screen
    
    surface = pygame.transform.rotate(surface, alpha)
    surface = pygame.transform.scale(surface, (w, h))
    screen.blit(surface, (x0, y0))

def bamb_1(x0, y0, k):
    #Первый бамбук (проверка options)
    w = 85
    h = 120
    surface = pygame.Surface([w, h], pygame.SRCALPHA)

    pygame.draw.ellipse(surface, GREEN, (7, 0, 85, 9))

    options(x0, y0, w * k, h * k, 45, surface)

bamb_1(100, 100, 2)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
