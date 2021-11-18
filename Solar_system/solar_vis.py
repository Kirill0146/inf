# coding: utf-8
# license: GPLv3

from solar_main import *
from solar_graph import *
import tkinter

"""Модуль визуализации.
Нигде, кроме этого модуля, не используются экранные координаты объектов.
Функции, создающие географические объекты и перемещающие их на экране, принимают физические координаты
"""

header_font = "Arial-16"
"""Шрифт в заголовке"""

window_width = 800
"""Ширина окна"""

window_height = 600
"""Высота окна"""

scale_factor = None
"""Масштабирование экранных координат по отношению к физическим.
Тип: float
Мера: количество пикселей на один метр."""


def calculate_scale_factor(max_distance):
    """Вычисляет значение глобальной переменной **scale_factor** по данной характерной длине"""
    global scale_factor
    scale_factor = 0.4*min(window_height, window_width)/max_distance
    print('Scale factor:', scale_factor)


def scale_x(x):
    """Возвращает экранную **x** координату по **x** координате модели.
    Принимает вещественное число, возвращает целое число.
    В случае выхода **x** координаты за пределы экрана возвращает
    координату, лежащую за пределами холста.

    Параметры:

    **x** — x-координата модели.
    """

    return int(x*scale_factor) + window_width//2


def scale_y(y):
    """Возвращает экранную **y** координату по **y** координате модели.
    Принимает вещественное число, возвращает целое число.
    В случае выхода **y** координаты за пределы экрана возвращает
    координату, лежащую за пределами холста.
    Направление оси развёрнуто, чтобы у модели ось **y** смотрела вверх.

    Параметры:

    **y** — y-координата модели.
    """

    return int(y*scale_factor) + window_height // 2


def create_star_image(space, star):
    """Создаёт отображаемый объект звезды.

    Параметры:

    **space** — холст для рисования.
    **star** — объект звезды.
    """

    x = scale_x(star.x)
    y = scale_y(star.y)
    r = star.R
    star.image = space.create_oval([x - r, y - r], [x + r, y + r], fill=star.color)


def create_planet_image(space, planet):
    """Создаёт отображаемый объект планеты.

    Параметры:

    **space** — холст для рисования.
    **planet** — объект планеты.
    """
    
    x = scale_x(planet.x)
    y = scale_y(planet.y)
    r = planet.R
    planet.image = space.create_oval([x - r, y - r], [x + r, y + r], fill=planet.color)


def update_system_name(space, system_name):
    """Создаёт на холсте текст с названием системы небесных тел.
    Если текст уже был, обновляет его содержание.

    Параметры:

    **space** — холст для рисования.
    **system_name** — название системы тел.
    """
    space.create_text(30, 80, tag="header", text=system_name, font=header_font)


def update_object_position(space, body):
    """Перемещает отображаемый объект на холсте.

    Параметры:

    **space** — холст для рисования.
    **body** — тело, которое нужно переместить.
    """
    
    x = scale_x(body.x)
    y = scale_y(body.y)
    r = body.R
    if x + r < 0 or x - r > window_width or y + r < 0 or y - r > window_height:
        space.coords(body.image, window_width + r, window_height + r,
                     window_width + 2*r, window_height + 2*r)  # положить за пределы окна
    space.coords(body.image, x - r, y - r, x + r, y + r)


def draw_graph(graph_objects, space):
    """Отображает пульт управления, нужный для построения графиков.
    Пользователь вводит номер объекта, данные которого интересуют его

    Параметры:

    **graph_objects** - список объектов со всем необходимым для графиков (V(t), r(t))
    **space** - холст, через который будет создавать пульт управления (формально root)
    """

    window = tkinter.Toplevel(space)
    window.geometry('250x120')
    window.title('Пульт')

    label = tkinter.Label(window, text = "Enter object number:")
    label.pack(pady = 4)
    
    N = tkinter.DoubleVar()
    N.set(0)
    entry = tkinter.Entry(window, text = 'Введите номер объекта', textvariable = N)
    entry.pack(pady = 8)

    def do_graph():
        """Функция, вызывающая построение графиков для объекта с заданным номером"""
        
        n = N.get()
        for g in graph_objects:
            if g.N == n:
                G(g)
            

    but = tkinter.Button(window, text = 'OK', command = do_graph, height = 10, width = 12)
    but.pack(pady = 8)
    
    window.mainloop()

if __name__ == "__main__":
    print("This module is not for direct call!")
