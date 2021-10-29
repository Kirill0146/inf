import math
from random import choice
from random import randint

import pygame


FPS = 30
TIME = 0
SCORE = 0
N_TARGETS = 5

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

balls = []
bombs = []
targets = []

class Ball:
    def __init__(self, screen: pygame.Surface, ball_type = 1, x = 40, y = 450, g = 1, r = 10, live = 100):
        """ Конструктор класса ball

        Args:
        ball_type - тип снарядов
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        g - ускорение шарика по оси игрек
        r - радиус шарика
        live - число жизней шарика
        """
        
        self.screen = screen
        self.x = x
        self.y = y
        self.g = g
        self.r = r
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = live
        self.dead = 0

    def new_ball(self, ball_type):
        """Изменение нового шарика в зависимости от его типа"""
        
        self.type = ball_type

        if self.type == 1:
            pass
        elif self.type == 2:
            self.r *= 2
            self.vx /= 2
            self.vy /= 2
        elif self.type == 3:
            self.vx *= 2
            self.vy *= 2
            self.r /= 2
        
    
    def board(self):
        """
        Проверка и обработка выхода за пределы стен
        """
        
        if self.x > WIDTH:
            self.x = WIDTH
            self.vx *= -1
            
        if self.x < 0:
            self.x = 0
            self.vx *= -1
            
        if self.y > HEIGHT:
            self.y = HEIGHT
            self.vy *= -0.7
            
        if self.y < 0 :
            self.y = 0
            self.vy *= -1
      
    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        
        self.x += self.vx
        self.y += self.vy
        self.vy += self.g
        self.live -= 1
        
        self.board()
        

    def draw(self):
        """
        Рисует шарик
        """
        
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        
        if obj.type == 1:
            if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.r + obj.r) ** 2:
                return True
            return False
        elif obj.type == 2:
            if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.r + obj.r) ** 2:
                return True
            return False


class Gun:
    def __init__(self, screen):
        """Конструктор класса Gun"""
        
        self.screen = screen #Экран
        self.f2_power = 10 #Начальная скорость шариков
        self.f2_on = 0 #Начата ли стрельба. 1, если да.
        self.an = 0 #Начальный угол
        self.color = GREY #Цвет пушки
        self.b = 7 #Ширина пушки
        self.L = 20 #Длина пушки
        self.L_min = 20 #Начальная длина пушки (минимальная)
        self.L_max = 90 #Максимальная длина пушки
        self.max_power = 100 #Максимальная скорость шарика
        self.type = 1 #Выбранный тип снарядов
        self.v = 2 #Скорость танка
        self.right = 0 #Елит ли танк направо
        self.left = 0 #Едит ли танк налево 
        self.up = 0 #Едит ли танк вверх
        self.down = 0 #Едит ли танк вниз
        self.x = 40 #Координата левого нижнего угла танка
        self.y = 450 #Координата левого нижнего угла танка
        self.mouse_x = 40 #Координаты мыши
        self.mouse_y = 450 #Координаты мыши
        
    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        
        global balls
        
        n_ball = Ball(screen, x = self.x, y = self.y)
        n_ball.vx = self.f2_power * math.cos(self.an)
        n_ball.vy =  self.f2_power * math.sin(self.an)
        
        if self.mouse_x < self.x:
            n_ball.vx *= -1
            n_ball.vy *= -1
            
        balls.append(n_ball)
        self.f2_on = 0
        self.f2_power = 10
        self.L = self.L_min

        n_ball.new_ball(self.type)

    def power_up(self):
        """
        Отвечает за рост скорости при выстреле
        """
        
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = YELLOW
            self.L = self.L_min + (self.L_max - self.L_min) * (self.f2_power - self.f2_on) / (self.max_power - self.f2_on)
            
        else:
            self.color = BLACK

    def draw(self):
        """
        Рисует пушку
        """
        
        x0, y0 = self.x, self.y #Координаты нижнего левого угла
        L, b = self.L, self.b #Длина и ширина пушки
        an = -self.an #угол в радианах

        if x0 <= self.mouse_x:
            pass
        else:
            L *= -1
            b *= -1
            
        pygame.draw.polygon(self.screen, self.color, [(x0, y0),
            (x0 + L * math.cos(an), y0 - L * math.sin(an)),
            (x0 + L * math.cos(an) - b * math.sin(an), y0 - L * math.sin(an) - b * math.cos(an)),
            (x0 - b * math.sin(an), y0 - b * math.cos(an)),
            (x0, y0)])

            
        
    def targetting(self):
        """Прицеливание. Зависит от положения мыши."""

        if event:
            x0, y0 = event.pos[0], event.pos[1]
            self.mouse_x, self.mouse_y = x0, y0
            
            if x0 > self.x:
                self.an = math.atan((y0-self.y) / (x0-self.x))
            elif x0 == self.x:
                self.an = math.pi / 2
            elif x0 < self.x:
                self.an = math.atan((y0-self.y) / (x0-self.x))
            
        if self.f2_on:
            self.color = YELLOW
        else:
            self.color = BLACK

    def move(self):
        """Движение танка"""

        if self.right == 1:
            self.x += self.v
        if self.left == 1:
            self.x -= self.v
        if self.up == 1:
            self.y -= self.v
        if self.down == 1:
            self.y += self.v

def draw_text(text, x, y, color_text = 'black', font_text = 36):
    """
    Рисует текст на экране
    text: Текст
    x, y: координаты верхнего левого угла текста
    color_text: цвет текста
    font_text: шрифт текста
    """
    
    f = pygame.font.Font(None, font_text)
    text = f.render(text, False, color_text)
    screen.blit(text, (x, y))


class Bobm:
    def __init__(self, x, y, vx = 0, vy = 0, ay = 1, color = BLACK, r = 5):
        """Конструктор класса Bomb"""
        
        self.vx = vx
        self.vy = vy
        self.color = color
        self.r = r
        self.ay = ay
        self.x = x
        self.y = y
        
    def move(self):
        """Движение бомбы"""
        
        self.x += self.vx
        self.y += self.vy
        self.vy += self.ay

    def draw(self):
        """Рисует бомбу"""
        
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )
    

class Target:

    def new_target1(self):
        """ Инициализация новой мишени вида 1. """
        
        r = self.r = randint(10, 50)
        color = self.color = RED
        self.live = 1 #Число жизней цели
        self.points = 1
        self.type = 1 #Тип мишени
        self.vx = randint(-10, 10)
        self.vy = randint(-10, 10)
        
    def new_target2(self):
        """ Инициализация новой мишени вида 2. """
        
        r = self.r = randint(25, 50) 
        color = self.color = MAGENTA
        self.live = 2 #Число жизней цели
        self.points = 2
        self.type = 2 #Тип мишени
        self.vx0 = randint(-10, 10) #Начальная скорость по оси икс
        self.vy0 = randint(-10, 10) #Начальная скорость по оси игрек
        self.vx, self.vy = self.vx0, self.vy0
        self.ax0 = 1 #Начальное ускорение по оси икс
        self.ay0 = 1 #Начальное ускорение по оси игрек
        self.ax, self.ay = self.ax0, self.ay0

        
    def new_target(self):
        """Создает новую мишень вида 1 или 2"""

        x = self.x = randint(600, 750) 
        y = self.y = randint(300, 550)
        
        if randint(1, 2) == 1:
            self.new_target1()
        else:
            self.new_target2()
            
    def __init__(self):
        """ Параметры объекта, как целое"""
        
        self.score = 0 #Счет
        self.new_target()
    
    def hit(self, ball, points = 1):
        """
        Попадание шарика в цель.
        ball: попавший шарик
        points: очки за попадание в данную цель
        """

        global SCORE
        
        SCORE += points
        ball.dead = 1
        
        if self.type == 1:
            pass
        elif self.type == 2:
            if self.live == 1:
                self.color = RED
                self.vx *= 2
                self.vy *= 2

    def draw1(self):
        """Рисование цели 1"""
        
        pygame.draw.circle(
            screen,
            self.color,
            (self.x, self.y),
            self.r
        )
        
    def draw2(self):
        """Рисование цели 2"""
        
        pygame.draw.rect(
            screen,
            self.color,
            (self.x, self.y, self.r, self.r)
        )

    def draw(self):
        """Рисование цели"""

        if self.type == 1:
            self.draw1()
        elif self.type == 2:
            self.draw2()


    def board(self):
        """
        Проверка и обработка выхода за пределы стен
        """
        
        if self.x > WIDTH:
            self.x = WIDTH
            self.vx *= -1
            
        if self.x < WIDTH / 3:
            self.x = WIDTH / 3
            self.vx *= -1
            
        if self.y > HEIGHT:
            self.y = HEIGHT
            self.vy *= -0.7
            
        if self.y < 0 :
            self.y = 0
            self.vy *= -1
            
    def move1(self):
        """Перемещает цель типа 1 по прошествии единицы времени"""

        self.x += self.vx
        self.y += self.vy

        self.board()

    def move2(self):
        """Перемещает цель типа 2 по прошествии единицы времени"""

        k, r = 0.1, 10 #Параметры траектории движения целей
        
        self.x += self.vx
        self.y += self.vy
        self.vx += self.ax
        self.vy += self.ay
        self.ax = self.ax0 * math.cos(k * TIME)
        self.ay = self.ay0 * math.sin(k * TIME)
        self.board()
     
    def move(self):
        """Перемещает цель по прошествии единицы времени"""
        
        if self.type == 1:
            self.move1()
        elif self.type == 2:
            self.move2()


    def new_bomb(self):
        """Мишень скидывает бомбу"""

        bomb = Bomb(self.x, self.y)
        bobms.append(bomb)

def score_draw():
    """Рисут счет"""

    draw_text('Score: '+ str(SCORE), 10, 10)

def draw_all():
    """Рисует все объекты заново"""
    
    screen.fill(WHITE)
    gun.draw()
    score_draw()
    target.draw()
    
    for t in targets:
        t.draw()
    
    for b in balls:
        b.draw()
    pygame.display.update()

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
gun = Gun(screen)


for i in range(N_TARGETS):
    target = Target()
    targets.append(target)

finished = False

while not finished:
    
    draw_all() #Перерисовывает все объекты

    #Обработка событий:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting()
            gun.draw()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                gun.type = 1 #Обычные снаряды
            elif event.key == pygame.K_2:
                gun.type = 2 #Большие и тяжелые снаряды
            elif event.key == pygame.K_3:
                gun.type = 3 #Маленькие и легкие снаряды

            #Обработка движения танка:
            if event.key == pygame.K_RIGHT:
                gun.right = 1 
            if event.key == pygame.K_LEFT:
                gun.left = 1
            if event.key == pygame.K_UP:
                gun.up = 1
            if event.key == pygame.K_DOWN:
                gun.down = 1  
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                gun.right = 0 
            if event.key == pygame.K_LEFT:
                gun.left = 0
            if event.key == pygame.K_UP:
                gun.up = 0
            if event.key == pygame.K_DOWN:
                gun.down = 0
            

    #Обработка без событий:        
    i = 0
    while i < len(balls):
        b = balls[i]
        b.move()
        for j in range(len(targets)):
            target = targets[j]
            
            if b.hittest(target) and target.live:
                target.live -= 1
                target.hit(b, target.points)
                if target.live == 0:
                    target.new_target()
    
        if b.live == 0 or b.dead == 1:
            balls.pop(i)
        else:
            i += 1
            
    for j in range(len(targets)):
        targets[j].move()

    
    gun.power_up() #Обновляет скорость, если идет прицеливание
    gun.move()
    
    TIME -= 1/FPS
    
pygame.quit()
