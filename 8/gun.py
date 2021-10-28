import math
from random import choice
from random import randint

import pygame


FPS = 30

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

bullet = 0
balls = []

class Ball:
    def __init__(self, screen: pygame.Surface, x = 40, y = 450, g = 1, r = 10, live = 100):
        """ Конструктор класса ball

        Args:
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
        
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.r + obj.r) ** 2:
            return True
        return False


class Gun:
    def __init__(self, screen):
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
        
    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy =  self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10
        self.L = self.L_min

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
        x0, y0 = 40, 450 #Координаты нижнего левого угла
        L, b = self.L, self.b #Длина и ширина пушки
        an = -self.an #угол в радианах
        pygame.draw.polygon(self.screen, self.color, [(x0, y0),
                                                 (x0 + L * math.cos(an), y0 - L * math.sin(an)),
                                                 (x0 + L * math.cos(an) - b * math.sin(an), y0 - L * math.sin(an) - b * math.cos(an)),
                                                 (x0 - b * math.sin(an), y0 - b * math.cos(an)),
                                                 (x0, y0)])
        
    def targetting(self):
        """Прицеливание. Зависит от положения мыши."""

        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = YELLOW
        else:
            self.color = BLACK



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


class Target:

    def new_target(self):
        """ Инициализация новой цели. """
        
        x = self.x = randint(600, 780)
        y = self.y = randint(300, 550)
        r = self.r = randint(5, 50)
        color = self.color = RED
        self.live = 1

    def __init__(self):
        """Параметры объекта, как целое"""
        
        self.points = 0
        self.new_target()
    
    def hit(self, ball, points = 1):
        """
        Попадание шарика в цель.
        ball: попавший шарик
        poins: очки за попадание в данную цель
        """
        
        self.points += points
        ball.dead = 1

    def draw(self):
        """
        Рисование цели
        """
        
        pygame.draw.circle(
            screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def score_draw(self):
        """
        Рисут счет
        """

        score = self.points
        draw_text('Score: '+ str(score), 10, 10)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
gun = Gun(screen)
target = Target()
finished = False

while not finished:
    
    screen.fill(WHITE)
    gun.draw()
    target.draw()
    target.score_draw()
    
    for b in balls:
        b.draw()
    pygame.display.update()


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
            
    i = 0
    while i < len(balls):
        b = balls[i]
        b.move()
        if b.hittest(target) and target.live:
            target.live -= 1
            target.hit(b)
            target.new_target()
        if b.live == 0 or b.dead == 1:
            balls.pop(i)
        else:
            i += 1
    gun.power_up()
    
pygame.quit()
