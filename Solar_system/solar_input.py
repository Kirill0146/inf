# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet, Graph


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":  
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects

def read_graphs_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла для построения графиков

    Параметры:

    **input_filename** — имя входного файла
    """

    def float_list(s):
        """Переводит список из строк в список вещественных чисел"""
        for i in range(len(s)):
            s[i] = float(s[i])

        return s

    graph_objects = []
    with open(input_filename) as input_file:
        count = 0
        lines = []
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            else:
                if count == 0:
                    lines.append(line.split())
                else:
                    line = line.split()
                    for i in range(len(line)):
                        line[i] = float(line[i])
                    lines.append(line)
                count += 1
            if count == 4:
                count = 0
                graph = Graph()
                graph.V_t = float_list(lines[1])
                graph.r_t = float_list(lines[2])
                graph.t_t = float_list(lines[3])
                graph.type = lines[0][0]
                graph.N = int(lines[0][1])
                graph_objects.append(graph)
                lines = []
    return graph_objects

def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """

    line = list(line.split())
    star.R = float(line[1])
    star.color = line[2]
    star.m = float(line[3])
    star.x = float(line[4])
    star.y = float(line[5])
    star.Vx = float(line[6])
    star.Vy = float(line[7])
    star.type_for_write = 'Star'

def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    
    line = list(line.split())
    planet.R = float(line[1])
    planet.color = line[2]
    planet.m = float(line[3])
    planet.x = float(line[4])
    planet.y = float(line[5])
    planet.Vx = float(line[6])
    planet.Vy = float(line[7])
    planet.type_for_write = 'Planet'

def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        text = ""
        for obj in space_objects:
            line = obj.type_for_write + " " + str(obj.R) + " " + obj.color + " " + str(obj.m) + " " + str(obj.x) + " " + str(obj.y) + " " + str(obj.Vx) + " " + str(obj.Vy) 
            text += line + '\n'
        out_file.write(text)
            

def write_graphs_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах для графиков в файл.
    Строки должны иметь следующий формат:
        <type> <Номер объекта>
        Далее идет 3 списка:
            V_t (список скоростей)
            r_t (список радиусов)
            t_t (список времен)
    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """

    def list_in_str(s):
        """Переводит список в строку"""
        text = ""
        for a in s:
            text += str(a) + " "
        return text
    
    with open(output_filename, 'w') as out_file:
        text = ""
        i = 0
        for obj in space_objects:
            i += 1
            text += obj.type + ' ' + str(i) + '\n'
            text += list_in_str(obj.V_t) + '\n'
            text += list_in_str(obj.r_t) + '\n'
            text += list_in_str(obj.t_t) + '\n'
        out_file.write(text)


if __name__ == "__main__":
    print("This module is not for direct call!")
