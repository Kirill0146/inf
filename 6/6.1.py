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
FLAG = 1
"""Флаг на то, где сейчас игра:
            0: Игра окончена
            1: Меню
            2: Рейтинг
            3: Готовность перейти в Игру
            4: Игра
            5: Просмотр игроком результата
"""

W, H = 800, 600 #Ширина и высота окна
TIME = 10 #Время игры

screen = pygame.display.set_mode((W, H))

SCORE, K, SCORE_BEST = 0, -1, 0 #Текущий счет игрока, место игрока в рейтинге, лучший счет игрока
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
all_buts = [] #Список кнопок


def draw_text(text, x, y, color_text, font_text):
    """
    Рисует текст на экране
    text: Текст
    x, y: координаты веррнего левого угла текста
    color_text: цвет текста
    font_text: шрифт текста
    """
    
    f = pygame.font.Font(None, font_text)
    text = f.render(text, False, color_text)
    screen.blit(text, (x, y))


def dead():
    """
    Уничтожает все объекты и закрашивает экран
    """

    global all_balls, all_sqrt, all_buts
    
    screen.fill(BLACK)
    all_balls = []
    all_sqrt = []
    all_buts = []


def return_menu():
    """
    Команда, которая вызывается при нажатие на кнопку "Назад" (в меню)
    Меняет FLAG, возвращение в меню
    """

    dead()
    global FLAG
    FLAG = 1
 

def new_game():
    """
    Команда, которая вызывается при нажатие на кнопку "Новая игра"
    Меняет FLAG, запускается игра
    """

    global FLAG
    FLAG = 3


def exit_game():
    """
    Команда, которая вызывается при нажатие на кнопку "Выход"
    Выход из игры
    """
    
    global FLAG
    FLAG = 0


def rating():
    """
    Команда, которая вызывается при нажатие на кнопку  "Рейтинг"
    Показывает рейтинг
    """
    
    global FLAG
    FLAG = 2


def draw_but(but):
    """
    Рисует кнопку
    """
    
    rect(screen, but['color_but'], (but['x'], but['y'], but['w'], but['h']))
    draw_text(but['text'], but['x'] + but['x_text'], but['y'] + but['y_text'],
              but['color_text'], but['font_text'])


def create_but(x, y, w, h, color_but, color_text,
               text, x_text, y_text, font_text, name, command):
    """
        Создает объект кнопка
    x, y: координата нижнего левого угла кнопки
    w, h: ширина и высота кнопки
    color_but: Цвет кнопки
    color_text: Цвет текста
    text: Текст
    x_text, y_text: Координаты левого верхнего угла текста
        относительно левого верхнего угла прямоугольника
    font_text: Размер шрифта 
    name: Имя кнопки
    command: Функция, которая выполняется после нажатия кнопки
    """
    
    but = {'x':x, 'y':y, 'w':w, 'h':h, 'color_but':color_but,
           'color_text':color_text, 'text':text, 'name':name,
           'x_text':x_text, 'y_text':y_text,
           'font_text':font_text, 'command':command}
    rect(screen, color_but, (x, y, w, h))
    draw_but(but)
    all_buts.append(but)


def print_rating():
    """
    Выводит рейтинг игроков
    """

    dead()
    file = open('best_players.txt', 'r')

    i = 0
    draw_text('Рейтинг:', 20, 10, 'red', 36)
    
    for line in file:
        if i <= 20:
            draw_text(line.replace('\n', ''), 20, 35 + i * 25, 'red', 36)
        i += 1

    create_but(x = 650,
               y = 30,
               w = 120,
               h = 50,
               color_but = 'red',
               color_text = 'black',
               text = 'Назад',
               x_text = 5,
               y_text = 7,
               font_text = 50,
               name =  'Назад',
               command = return_menu
        )
    
    
    file.close()
    

def menu():
    """
    Отображает кнопки:
    -Новая игра
    -Рейтинг
    -Выход
    """

    create_but(x = 300,
               y = 100,
               w = 200,
               h = 50,
               color_but = 'red',
               color_text = 'black',
               text = 'Новая игра',
               x_text = 5,
               y_text = 7,
               font_text = 50,
               name =  'Новая игра',
               command = new_game)
    
    create_but(x = 300,
               y = 170,
               w = 200,
               h = 50,
               color_but = 'red',
               color_text = 'black',
               text = 'Рейтинг',
               x_text = 35,
               y_text = 7,
               font_text = 50,
               name =  'Рейтинг',
               command = rating
        )
    
    create_but(x = 300,
               y = 240,
               w = 200,
               h = 50,
               color_but = 'red',
               color_text = 'black',
               text = 'Выход',
               x_text = 40,
               y_text = 7,
               font_text = 50,
               name =  'Выход',
               command = exit_game
        )
    
def click_buts(event):
    """
    Обработка нажатий на кнопки меню
    """
    
    x0, y0 = event.pos
    
    for but in all_buts:
        if x0 >= but['x'] and x0 <= but['x'] + but['w'] and y0 >= but['y'] and y0 <= but['y'] + but['h']:
            but['command']()

    
def draw_score_and_time():
    """
    Отображаем счет SCORE и время TIME
    """

    draw_text('Счет: ' + str(SCORE), 10, 10, 'red', 36)
    draw_text('Время: ' + str(round(TIME, 1)), 10, 30, 'red', 36)


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
    born()

    
def born():
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
    born()


def delete_sqr(index):
    """
    Удаляет квадрат из списка all_sqrs с индексом index
    index: индекс шарика
    """

    del all_sqrs[index]
    born()


def dist(x1, y1, x2, y2):
    """
    Находит квадрат расстояния между двумя точками
    (x1, y1): координаты первой точки
    (x2, y2): координаты второй точки
    """

    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def update_score(score):
    """
    Обновляет счет по закону: сумма очков за данный клик,
        помноженный на количество объектов
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


def click_game(event):
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


def results(k, score_new):
    """
    Окно, которое появляется после конца игры.
    На на отображен результат игрока
    k: место игрока в рейтинге
    score_new: лучший результат игрока
    """

    dead()
    print_rating()


    list_text = ['Ваш счет: ' + str(SCORE), 'Ваш лучший счет: ' + str(score_new),
                 'Ваше место в рейтинге: ' + str(k)]
    
    i = 0
    for text0 in list_text:
        f = pygame.font.Font(None, 36)
        text = f.render(text0, False, 'red')
        screen.blit(text, (200, 10 + i * 25))
        i += 1
        

def update_results():
    """
    Обновляет результат данного игрока в файле.
    Пересортировывает игрока по рейтингу.
    Выводит результат игрока, его лучший результат,
    положение в рейтинге, сам рейтинг
    """

    global FLAG, SCORE_BEST, K
    
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
    
    K, SCORE_BEST = k + 1, score_new
    FLAG = 5
    

def game_over():
    """
    Конец игры
    """

    #pygame.quit()
    update_results()
    dead()
    

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
    else:
        TIME -= 1/FPS
        move()

    
pygame.display.update()
clock = pygame.time.Clock()

k, score_new = 0, 0 #Место игрока в рейтинге и его лучший счет

while FLAG:
    clock.tick(FPS)


    #Обработка в зависимости от FLAG, вне зависимости от события:
    if FLAG == 1:
        menu()
    elif FLAG == 2:
        print_rating()
    elif FLAG == 3:
        draw_score_and_time()
        FLAG = 4
    elif FLAG == 4:
        create()
        check_TIME()
    elif FLAG == 5:
        results(K, SCORE_BEST)
        
    #Обработка в зависимости от FLAG, в зависимости от события:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            FLAG = 0

        if FLAG == 1 or FLAG == 2 or FLAG == 5:
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_buts(event)
        elif FLAG == 4:
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_game(event)
                
    pygame.display.update()
    
pygame.quit()
