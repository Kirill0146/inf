import pygame
import math
from pygame.draw import *
from random import randint
from random import random

pygame.init()

N_BALLS = 5 #Максимальное число шариков
N_SQRS = 5 #Максимальное число квадратов
FPS = 30
dt = 1
FLAG = True #Флаг на то, окончилась ли игра
W, H = 800, 600 #Ширина и высота окна
TIME = 5 #Время игры

screen = pygame.display.set_mode((W, H))

SCORE = 0 #Текущий счет игрока
#Цвета:
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN] #Список цветов

all_balls = [] #Список шаров
all_sqrs = [] #Список квадратов


def draw_score_and_time():
    """
    Отображаем счет SCORE и время TIME
    """

    f = pygame.font.Font(None, 36)
    text = f.render('Счет: ' + str(SCORE), False, RED)
    screen.blit(text, (10, 10))

    f = pygame.font.Font(None, 36)
    text = f.render('Время: ' + str(round(TIME, 1)), False, RED)
    screen.blit(text, (10, 30))
    

def draw_ball(ball):
    """
    Рисует шарик в координатах (ball.x, ball.y)
    """

    circle(screen, ball['color'], (ball['x'], ball['y']), ball['r'])


def draw_sqr(sqr):
    """
    Рисует квадрат в координатах (sqr.x, sqr.y)
    """
    
    a, x, y, color = sqr['a'], sqr['x'], sqr['y'], sqr['color']
    rect(screen, color, (x - a / 2, y - a / 2, a, a))


def new_sqr():
    """
    Создает объект sqr и отображает его
    x, y: координаты центра квадрата
    Vx, Vy: проекции скоростей на ось икс и игрек
    a: сторона квадрата
    color: цвет квадрата
    score: счет
    ay: ускорение квадрата по игрек
    """
    
    sqr = {'x':0, 'y':0, 'Vx':0, 'Vy':0, 'a':0, 'color':'', 'score': 2, 'ay':0}
    sqr['x'] = randint(100, W - 100)
    sqr['y'] = randint(100, H - 100)
    sqr['Vx'] = randint(-20, 20) / 3
    sqr['Vy'] = randint(-10, 10) / 3
    sqr['a'] = randint(20, 40)
    sqr['ay'] = random() * 2 / 3
    color = COLORS[randint(0, 5)]
    sqr['color'] = color
    draw_sqr(sqr)
    all_sqrs.append(sqr)

    
def new_ball():
    """
    Создает объект ball и отображает его
    x, y: координаты центра шарика
    Vx, Vy: проекции скоростей на ось икс и игрек
    r: радиус шарика
    color: цвет шарика
    score: счет 
    """
    
    ball = {'x':0, 'y':0, 'Vx':0, 'Vy':0, 'r':0, 'color':'', 'score': 1}
    ball['x'] = randint(100, W - 100)
    ball['y'] = randint(100, H - 100)
    ball['Vx'] = randint(-10, 10) / 3
    ball['Vy'] = randint(-10, 10) / 3
    ball['r'] = randint(30, 50)
    color = COLORS[randint(0, 5)]
    ball['color'] = color
    draw_ball(ball)
    all_balls.append(ball)


def border_ball(ball):
    """
    Обновляет скорость шарика в случае выхода за границу
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

            
def border_sqr(sqr):
    """
    Обновляет скорость квадрата в случае выхода за границу
    """
    
    k1 = 2 #Коэффициент препендикулярной сост. скорости
    k2 = 0.25 #Коэффициент для нормальной сост. скорости
    
    if sqr['x'] > W or sqr['x'] < 0:
        sqr['Vx'] *= -1 
        
        if sqr['x'] > W:
            sqr['x'] = W
        if sqr['x'] < 0:
            sqr['x'] = 0
            
    elif sqr['y'] < 0 or sqr['y'] > H:
        sqr['Vy'] *= -1 
        
        if sqr['y'] > H:
            sqr['y'] = H
        if sqr['y'] < 0:
            sqr['y'] = 0

            
def move():
    """
    Проверяет для каждого шарика выход за границы
    Затем перемещает каждый шарик
    Аналогично для квадрата
    """

    for ball in all_balls:
        border_ball(ball)
        ball['x'] += ball['Vx'] * dt
        ball['y'] += ball['Vy'] * dt

    for sqr in all_sqrs:
        border_sqr(sqr)
        sqr['x'] += sqr['Vx'] * dt
        sqr['y'] += sqr['Vy'] * dt
        sqr['Vy'] += sqr['ay'] * dt
    dead()

    
def dead():
    """
    Заново все перерисовывает
    """

    screen.fill(BLACK)
    draw_score_and_time()
    
    for ball in all_balls:
        draw_ball(ball)
        
    for sqr in all_sqrs:
        draw_sqr(sqr)


def delete_ball(index):
    """
    Удаляет шарик из списка all_balls с индексом index
    index: индекс шарика
    """

    del all_balls[index]
    dead()


def delete_sqr(index):
    """
    Удаляет квадрат из списка all_sqrs с индексом index
    index: индекс шарика
    """

    del all_sqrs[index]
    dead()


def dist(x1, y1, x2, y2):
    """
    Находит квадрат расстояния между двумя точками
    (x1, y1): координаты первой точки
    (x2, y2): координаты второй точки
    """

    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def update_score(score):
    """
    Обновляет счет по закону: сумма очков за данный клик, помноженный на количество объектов
    score: список очков за каждый объект, в который попали данным щелком
    """

    global SCORE
    
    SCORE += sum(score) * len(score)


def check_sqr(x0, y0, x, y, a):
    """
    Проверяет, находится ли точка (x0, y0) в квадрате
    с центром в (x, y) и шириной a. Возвращает True/False
    x0, y0: координаты точки
    x, y: координаты центра квадрата
    a: сторона квадрата
    """
    
    if x0 >= x - a / 2 and x0 <= x + a / 2 and y0 >= y - a / 2 and y0 <= y + a / 2:
        return True
    return False


def click(event):
    """
    Если попали по шарику, то он удаляется и счет обновляется
    event: событие мыши (от 1 до 5)
    """
    
    x0, y0 = event.pos
    i = 0
    score = []
    
    while i < len(all_balls):
        ball = all_balls[i]
        x, y, r = ball['x'], ball['y'], ball['r']
        if dist(x0, y0, x, y) <= r ** 2:
            score.append(ball['score'])
            delete_ball(i)
        else: 
            i += 1

    i = 0
    while i < len(all_sqrs):
        sqr = all_sqrs[i]
        if check_sqr(x0, y0, sqr['x'], sqr['y'], sqr['a']):
            score.append(sqr['score'])
            delete_sqr(i)
        else: 
            i += 1

    update_score(score)


def update_results():
    """
    Обновляет результат данного игрока в файле.
    Пересортировывает игрока по рейтингу.
    Выводит результат игрока, его лучший результат,
    положение в рейтинге, сам рейтинг
    """

    flag = True

    print('Игра окончена!')
    print('Введите Ваше Имя:')
    name_new, score_new = input(), SCORE
    
    file = open('best_players.txt', 'r')    
    players_and_scores = []

    for line in file:
        line = line.replace('\n', '')
        line = line.replace(':', '')
        number, name, score = line.split()
        if name == name_new:
            flag = False
            score = max(int(score), score_new)
            score_new = max(int(score), score_new)
            
        players_and_scores.append([int(score), name])
        
    if flag:
        players_and_scores.append([score_new, name_new])
    players_and_scores.sort()
    players_and_scores.reverse()
    
    new_text = ''
    for i in range(len(players_and_scores)):
        name, score = players_and_scores[i][1], str(players_and_scores[i][0])
        new_text += str(i + 1) + '. ' + name + ': ' + score + '\n'
    
    file.close()
    file = open('best_players.txt', 'w')
    file.write(new_text)

    k = 0
    for i in range(len(players_and_scores)):
        if score_new >= players_and_scores[i][0]:
            break
        else:
            k += 1
    
    print('Ваш результат успешно записан!')
    print('Ваш счет:', SCORE)
    print('Ваш лучший счет:', score_new)
    print('Ваше место в рейтинге:', k + 1)
    print('Рейтинг:')
    print(new_text)


def game_over():
    """
    Конец игры
    """

    pygame.quit()
    update_results()
    

def create():
    """
    Создает объекты: шары и квадраты, если их стало меньше положенного
    """

    if len(all_sqrs) < N_SQRS:
        new_sqr()
    if len(all_balls) < N_BALLS:
        new_ball()


def check_TIME():
    """
    Обновляет таймер. Если время вышло, то вызываем функцию game_over (конец игры)
    Иначе обновляем время, запускаем следующую итерацию движения
    """

    global TIME, FLAG
    
    if TIME <= 0:
        TIME = 0
        if (FLAG):
            game_over()
            FLAG = False
    else:
        TIME -= 1/FPS
        move()

    
pygame.display.update()
clock = pygame.time.Clock()

draw_score_and_time()

while FLAG:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
                
    create()
    check_TIME()

    if FLAG:
        pygame.display.update()

pygame.quit()
