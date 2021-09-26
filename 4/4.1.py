import pygame
from pygame.draw import *

pygame.init()



FPS = 30
screen = pygame.display.set_mode((400, 400))


rect(screen, (255, 255, 255), (0, 0, 400, 400))
circle(screen, (255, 255, 0), (200, 200), 100)
circle(screen, (0, 0, 0), (200, 200), 100, 1)
circle(screen, (255, 0, 0), (146, 183), 21)
circle(screen, (0, 0, 0), (146, 183), 9)
circle(screen, (255, 0, 0), (249, 181), 16)
circle(screen, (0, 0, 0), (249, 181), 8)
polygon(screen, (0, 0, 0), [(100, 117), (95, 126), (176, 177), (181, 167)])
polygon(screen, (0, 0, 0), [(218, 167), (222, 177), (302, 145), (297, 137)])
polygon(screen, (0, 0, 0), [(148, 251), (148, 271), (249, 271), (249, 253)])

#rect(screen, (10, 10, 10), (150, 250, 100, 25))



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
