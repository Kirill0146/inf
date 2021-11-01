import math
from random import choice
from random import randint
from random import random
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
bombs = pygame.sprite.Group()
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
        
def update(image, w, h, angle):
    """
    Меняет исходные размеры картинки, а затем поворачивает ее
    w, h: новые размеры картинки
    angle: угол поворота картинки
    """

    image = pygame.transform.scale(image, (w, h))
    image = pygame.transform.rotate(image, angle)

    return image

class Tank:
    def __init__(self, screen):
        """Конструктор класса Tank"""
        
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen #Экран
        self.f2_power = 10 #Начальная скорость шариков
        self.f2_on = 0 #Начата ли стрельба. 1, если да.
        self.angle = 0 #Начальный угол
        self.color = GREY #Цвет пушки
        self.k = 1 #Коэффициент пропорциональности длины танка
        self.max_power = 100 #Максимальная скорость шарика
        self.type = 1 #Выбранный тип снарядов
        self.v = 3 #Скорость танка
        self.right = 0 #Елит ли танк направо
        self.left = 0 #Едит ли танк налево 
        self.up = 0 #Едит ли танк вверх
        self.down = 0 #Едит ли танк вниз
        self.x = 40 #Координата левого нижнего угла танка
        self.y = 450 #Координата левого нижнего угла танка
        self.mouse_x = 40 #Координаты мыши
        self.mouse_y = 450 #Координаты мыши
        self.w = 50 #Ширина танка
        self.h = 50 #Высота танка
        self.image = pygame.image.load('images/tank.png').convert_alpha() #Картинка танка
        self.image_start = self.image #Сохраняем исходную экземпляр
        self.hp = 3 #Жизни танка
        
    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        
        global balls
        
        n_ball = Ball(screen, x = self.x, y = self.y)
        n_ball.vx = self.f2_power * math.cos(self.angle)
        n_ball.vy =  self.f2_power * math.sin(self.angle)
        
        if self.mouse_x < self.x:
            n_ball.vx *= -1
            n_ball.vy *= -1
            
        balls.append(n_ball)
        self.f2_on = 0
        self.f2_power = 10
        self.k = 1

        n_ball.new_ball(self.type)

    def power_up(self):
        """
        Отвечает за рост скорости при выстреле
        """
        
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = YELLOW
            self.k =  (self.f2_power - self.f2_on) / (self.max_power - self.f2_on) + 1
            
        else:
            self.color = BLACK

    def draw(self):
        """
        Рисует пушку
        """
        
        x0, y0 = self.x , self.y #Координаты нижнего левого угла
        angle = -self.angle / math.pi * 180
        
        if x0 > self.mouse_x:
            angle += 180

        
        self.image = update(self.image_start, int(50 * self.k), 50, angle)

        screen.blit(self.image, (x0 - self.image.get_size()[0] / 2, y0 - self.image.get_size()[1] / 2))
        
    def targetting(self):
        """Прицеливание. Зависит от положения мыши."""

        if event:
            x0, y0 = event.pos[0], event.pos[1]
            self.mouse_x, self.mouse_y = x0, y0
            
            if x0 > self.x:
                self.angle = math.atan((y0-self.y) / (x0-self.x))
            elif x0 == self.x:
                self.angle = math.pi / 2
            elif x0 < self.x:
                self.angle = math.atan((y0-self.y) / (x0-self.x))
            
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


class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y, vx = 0, vy = 0, ay = 0.25, color = BLACK, r = 20):
        """Конструктор класса Bomb"""
        
        pygame.sprite.Sprite.__init__(self)
        self.vy = vy #Скорость бомбы по игрек
        self.r = r #Радиус бомбы
        self.ay = ay #Ускорение бомбы 
        self.x = x #Координата икс бомбы
        self.y = y #Координата игрек бомбы
        self.image = pygame.image.load('images/bomb_2.png').convert_alpha() #Картинка бомбы
        self.image_start = self.image #Сохраняем исходную экземпляр
        self.flag = True
        self.add(bombs)
        self.time0 = -999
        self.time = self.time0
        
    def move(self):
        """Движение бомбы"""
        
        self.y += self.vy
        self.vy += self.ay

    def draw(self):
        """Рисует бомбу"""
        
        self.image = update(self.image_start, 2 * self.r, 2 * self.r, 0)
        screen.blit(self.image, (self.x, self.y))

    def meet(self, obj):
        """Проверка на то, встретились ли бомба и объект obj"""
        
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
        obj.mask = pygame.mask.from_surface(obj.image)
        obj.rect = obj.image.get_rect()
        obj.rect.x = obj.x - obj.image.get_size()[0] / 2
        obj.rect.y = obj.y - obj.image.get_size()[1] / 2
        
        if pygame.sprite.collide_mask(self, obj):
            return True
        return False

    def bum(self, obj):
        """Взрыв из-за бомбы"""

        if self.meet(obj) and self.flag:
            self.image_start = pygame.image.load('images/buum.png').convert_alpha() #Картинка взрыва
            obj.hp -= 1
            self.flag = False
            self.time = 0.3

        if (self.time <= 0 and self.time > self.time0) or self.y > HEIGHT:
            self.kill()
        
        
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
        self.time = 2 #Время, через которое произойдет выпуск бомбы
        self.time0 = self.time
        
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
        self.time = 10 #Время, через которое произойдет выпуск бомбы
        self.time0 = self.time
        
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
    draw_text('HP: '+ str(tank.hp), 10, 30)
    

def draw_all():
    """Рисует все объекты заново"""
    
    screen.fill(WHITE)
    tank.draw()
    score_draw()
    target.draw()

    for b in bombs:
        b.draw()
    
    for t in targets:
        t.draw()
    
    for b in balls:
        b.draw()

        
    pygame.display.update()

bombs = pygame.sprite.Group()
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
tank = Tank(screen)


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
            tank.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            tank.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            tank.targetting()
            tank.draw()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                tank.type = 1 #Обычные снаряды
            elif event.key == pygame.K_2:
                tank.type = 2 #Большие и тяжелые снаряды
            elif event.key == pygame.K_3:
                tank.type = 3 #Маленькие и легкие снаряды

            #Обработка движения танка:
            if event.key == pygame.K_RIGHT:
                tank.right = 1 
            if event.key == pygame.K_LEFT:
                tank.left = 1
            if event.key == pygame.K_UP:
                tank.up = 1
            if event.key == pygame.K_DOWN:
                tank.down = 1  
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                tank.right = 0 
            if event.key == pygame.K_LEFT:
                tank.left = 0
            if event.key == pygame.K_UP:
                tank.up = 0
            if event.key == pygame.K_DOWN:
                tank.down = 0
            

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
        target = targets[j]
        target.move()
        target.time -= 1/FPS
        if target.time <= 0:
            b = Bomb(target.x, target.y)
            b.add(bombs)
            target.time = target.time0 * 2 * (random() - j / len(targets) ** 2)

    for b in bombs:
        b.move()
        b.bum(tank)
        b.time -= 1/FPS
    
    tank.power_up() #Обновляет скорость, если идет прицеливание
    tank.move()
    
    TIME -= 1/FPS
    
pygame.quit()
