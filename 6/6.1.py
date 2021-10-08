import pygame
from pygame.draw import *
from random import randint
from random import random

pygame.init()

N_BALLS = 5 #Максимальное число шариков
N_RECTS = 5 #Максимальное число квадратов
FPS = 10
dt = 1
W, H = 800, 600
screen = pygame.display.set_mode((W, H))

SCORE = 0
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

all_balls = []
all_rects = []

def draw_score():
    """
    Отображаем счет SCORE
    """

    f = pygame.font.Font(None, 36)
    text = f.render('Счет: ' + str(SCORE), False, RED)
    screen.blit(text, (10, 10))


def draw_ball(ball):
    """
    Рисует шарик в координатах (ball.x, ball.y)
    """

    circle(screen, ball['color'], (ball['x'], ball['y']), ball['r'])


def draw_rect(rec):
    """
    Рисует квадрат в координатах (rect.x, rect.y)
    """
    
    a, x, y, color = rec['a'], rec['x'], rec['y'], rec['color']
    circle(screen, color, (x, y), a)


def new_rect():
    """
    Создает объект rect и отображает его
    x, y: координаты центра квадрата
    Vx, Vy: проекции скоростей на ось икс и игрек
    a: сторона квадрата
    color: цвет квадрата
    """
    
    rect = {'x':0, 'y':0, 'Vx':0, 'Vy':0, 'a':0, 'color':''}
    rect['x'] = randint(100, W - 100)
    rect['y'] = randint(100, H - 100)
    rect['Vx'] = randint(-10, 10)
    rect['Vy'] = randint(-10, 10)
    rect['a'] = randint(10, 100)
    color = COLORS[randint(0, 5)]
    rect['color'] = color
    draw_rect(rect)
    all_rects.append(rect)
    
def new_ball():
    """
    Создает объект ball и отображает его
    x, y: координаты центра шарика
    Vx, Vy: проекции скоростей на ось икс и игрек
    r: радиус шарика
    color: цвет шарика
    """
    
    ball = {'x':0, 'y':0, 'Vx':0, 'Vy':0, 'r':0, 'color':''}
    ball['x'] = randint(100, W - 100)
    ball['y'] = randint(100, H - 100)
    ball['Vx'] = randint(-10, 10)
    ball['Vy'] = randint(-10, 10)
    ball['r'] = randint(10, 100)
    color = COLORS[randint(0, 5)]
    ball['color'] = color
    draw_ball(ball)
    all_balls.append(ball)


def border(ball):
    """
    Обновляет скорость в случае выхода за границу
    """
    
    k1 = 2 #Коэффициент препендикулярной сост. скорости
    k2 = 0.25 #Коэффициент для нормальной сост. скорости
    
    if ball['x'] > W or ball['x'] < 0:
        ball['Vx'] *= -1 * (1 - (random() + 0.5) * k2)
        ball['Vy'] *= random() * k1
        
        if ball['x'] > W:
            ball['x'] = W
        if ball['x'] < 0:
            ball['x'] = 0
            
    elif ball['y'] < 0 or ball['y'] > H:
        ball['Vy'] *= -1 * (1 - random() * k2)
        ball['Vx'] *= random() * k1
        
        if ball['y'] > H:
            ball['y'] = H
        if ball['y'] < 0:
            ball['y'] = 0
            
def move():
    """
    Проверяет для каждого шарика выход за границы
    Затем перемещает каждый шарик
    """

    for ball in all_balls:
        border(ball)
        ball['x'] += ball['Vx'] * dt
        ball['y'] += ball['Vy'] * dt
    dead()
    
def dead():
    """
    Заново все перерисовывает
    """

    screen.fill(BLACK)
    draw_score()
    for ball in all_balls:
        draw_ball(ball)


def delete(index):
    """
    Удаляет щарик из списка all_balls с индексом index
    index: индекс шарика
    """

    del all_balls[index]
    dead()


def dist(x1, y1, x2, y2):
    """
    Находит квадрат расстояния между двумя точками
    (x1, y1): координаты первой точки
    (x2, y2): координаты второй точки
    """

    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def update_score(ball):
    """
    Обновляет счет
    """

    global SCORE
    
    SCORE += 1


def click(event):
    """
    Если попали по шарику, то он удаляется и счет обновляется
    event: событие мыши (от 1 до 5)
    """
    
    global SCORE 
    x0, y0 = event.pos
    i = 0
    
    while i < len(all_balls):
        ball = all_balls[i]
        x, y, r = ball['x'], ball['y'], ball['r']
        
        if dist(x0, y0, x, y) <= r ** 2:
            update_score(ball)
            delete(i)
        else: 
            i += 1


pygame.display.update()
clock = pygame.time.Clock()
finished = False

draw_score()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
    if len(all_rects) < N_RECTS:
        new_rect()
    move()
    pygame.display.update()

pygame.quit()
