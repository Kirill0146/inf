# coding: utf-8
# license: GPLv3


class Star:
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """

    type = "star"
    """Признак объекта звезды"""

    m = 0
    """Масса звезды"""

    x = 0
    """Координата по оси **x**"""

    y = 0
    """Координата по оси **y**"""

    Vx = 0
    """Скорость по оси **x**"""

    Vy = 0
    """Скорость по оси **y**"""

    Fx = 0
    """Сила по оси **x**"""

    Fy = 0
    """Сила по оси **y**"""

    R = 5
    """Радиус звезды"""

    color = "red"
    """Цвет звезды"""

    image = None
    """Изображение звезды"""

    def __init__(self):
        """Конструктор (для графиков)"""
        self.V_t = []
        """Зависимость V(t)"""

        self.r_t = []
        """Зависимость r(t)"""

        self.t_t = []
        """Зависимость t(t)"""

class Planet:
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """

    type = "planet"
    """Признак объекта планеты"""

    m = 0
    """Масса планеты"""

    x = 0
    """Координата по оси **x**"""

    y = 0
    """Координата по оси **y**"""

    Vx = 0
    """Скорость по оси **x**"""

    Vy = 0
    """Скорость по оси **y**"""

    Fx = 0
    """Сила по оси **x**"""

    Fy = 0
    """Сила по оси **y**"""

    R = 5
    """Радиус планеты"""

    color = "green"
    """Цвет планеты"""

    image = None
    """Изображение планеты"""

    def __init__(self):
        """Конструктор (для графиков)"""
        self.V_t = []
        """Зависимость V(t)"""

        self.r_t = []
        """Зависимость r(t)"""

        self.t_t = []
        """Зависимость t(t)"""

class Graph():
    """Данный тип используется для хранения информации,
    необходимой для построения графиков
    """

    type = "graph"
    """Признак объекта"""

    def __init__(self):
        """Конструктор (для графиков)"""
        self.V_t = []
        """Зависимость V(t)"""

        self.r_t = []
        """Зависимость r(t)"""

        self.t_t = []
        """Зависимость t(t)"""

        self.type = ''
        "Тип объекта, график которого в дальнейшем будем строить"

        self.N = 0
        "Номер объекта"
