import math
import Graphics as gr

SIZE_X = 400  # размер окна по x
SIZE_Y = 900  # размер окна по y
center_x = 200  # центр подвешивания нити по x
center_y = 0  # центр подвешивания нити по y
window = gr.GraphWin("Model", SIZE_X, SIZE_Y)  # создание рабочего окна
len_line = 0.2  # длина веревки
angle = 45  # начальный угол
g = 9.8  # ускорение свабодного падения


A = math.pi * len_line * (angle/180)  # Амплитуда (длина дуги)
T = 2 * math.pi * math.sqrt(len_line/g)  # Одно колебание туда и обратно
w = 2 * math.pi/(2 * math.pi * math.sqrt(len_line/g))  #частота колебания

t = 0  # момент времени

coord_x = A * math.cos(w * t + math.radians(angle))  # координата по х в момент твремени t
coord_y = math.sqrt(len_line ** 2 - coord_x ** 2)  # координата по у в момент твремени t
coord_x = center_x - coord_x * 1000
coord_y = coord_y * 1000

coord_ball = gr.Point(coord_x, coord_y)  # начальные координаты шарика

ball = gr.Circle(gr.Point(coord_ball.x, coord_ball.y), 10)  #  прорисовка шарика
ball.setFill("red")
ball.draw(window)


def move_ball(t):
    """
    Движение шарика в зависимости изменения времени t.
    :param t: момент времени.
    :return:
    """
    while True:
        old_x = coord_ball.x  # запоминание предыдущего положения шарика по x
        old_y = coord_ball.y  # запоминание предыдущего положения шарика по y
        t += 0.01

        # изменение координат шарика в данный момент времени t
        coord_ball.x = A * math.cos(w * t + math.radians(angle))
        coord_ball.y = math.sqrt(len_line**2 - coord_ball.x**2)
        coord_ball.x = center_x - (coord_ball.x * 1000)
        coord_ball.y = coord_ball.y * 1000

        velocity = gr.Point(coord_ball.x - old_x, coord_ball.y - old_y)  # скорость шарика в данный момент времени t

        ball.move(velocity.x, velocity.y)  # движение шарика
        line = gr.Line(gr.Point(center_x, center_y), gr.Point(coord_ball.x, coord_ball.y))  # прорисовка нити шарика
        line.draw(window)

        gr.time.sleep(0.05)  #  задержка кадров для замедления процесса
        line.undraw()  # удаление старой прорисовки нити шарика


move_ball(t)
