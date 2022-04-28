import math
import re



def generate_nc(text_input="", b_x=0, b_y=0, b_z=0, b_a=0):
    """
    :param text_input: текст управляющей прогрраммы
    :param b_x:Значение смещения по х, по умолчанию ноль
    :param b_y: Значение смещения по у, по умолчанию ноль
    :param b_z: Значение смещения по z, по умолчанию ноль
    :param b_a: Значение угла поворота уравляющей программы вокруг нуля, по умолчанию ноль
    :return: обьединеный текст с изменениями
    """
    text = text_input.split("\n")
    text_out = []
    old_coord = dict({"X": 0, "Y": 0, "Z": 0, "I": 0, "J": 0})  # старые кординаты предыдущих строк
    act_coord = dict({"X": 0, "Y": 0, "Z": 0, "I": 0, "J": 0})  # актуальные кординаты
    new_coord = dict({"X": 0, "Y": 0, "Z": 0, "I": 0, "J": 0})  # измененые кординаты
    g_code_on = dict({"group_1": "G00"})                        # включенные G-коды

    # При каждой итеррации проходит по каждой строке управляюще программы
    for number, str_text in enumerate(text):

        g_code_on = get_g_code_on(str_text, g_code_on)

        if str_text.count("G28") == 0 and str_text.count("G30") == 0:
            if b_x != 0:
                str_text = get_bias("X", b_x, str_text)
            if b_y != 0:
                str_text = get_bias("Y", b_y, str_text)
            if b_z != 0:
                str_text = get_bias("Z", b_z, str_text)

            # принимает координаты по каждой оси
            for name_axis in act_coord:
                act_coord[name_axis] = get_coord(name_axis, str_text, act_coord)

            if b_a != 0:
                str_text = get_turn_coord(b_a, act_coord, new_coord, old_coord, str_text, g_code_on)

            # принимает новые координаты по каждой оси
            for name_axis in new_coord:
                new_coord[name_axis] = get_coord(name_axis, str_text, act_coord)

        text_out.append(str_text.replace(" ", ""))

        # замена старых координат на актуальные
        for name_axis in old_coord:
            old_coord[name_axis] = act_coord[name_axis]

    return "\n".join(text_out)


def get_g_code_on(str_text, g_code_on):
    """
    Функция поиска G-кодов в строке управляющей программы.
    :param str_text: текст строки управляющей программы
    :param g_code_on: включенные G-коды
    :return: все включенные G-коды
    """
    regex_str = re.compile(r"(?:(?<=G0)|(?<=G))[0-3](?:(?=\D+))")
    tmp_g_code = regex_str.findall(str_text)

    if tmp_g_code:
        g_code_on["group_1"] = tmp_g_code

    return g_code_on


def get_bias(name_axis, bias, str_text):
    """
    Функция осуществляет поисх значения по оси, прибавляет значение смещения,
    заменят это значение в строке управляюще программы

    :param name_axis: ось, по которой осуществляется смещение
    :param bias: значение смещения
    :param str_text: текст строки управляюще программы
    :return: измененную строку управляющей программы со сещенными занчениями
    """
    regex_str = re.compile("({0})([+-?0-9]+)".format(name_axis))
    coord = regex_str.findall(str_text)
    if coord:
        bias_coord_digit = str(round((float(coord[0][1])+bias), 3))
        str_text = str_text.replace("{0}{1}".format(name_axis, coord[0][1]),
                                    "{0}{1}".format(name_axis, bias_coord_digit))
    return str_text


def get_coord(name_axis, str_text, d_coord):
    """
    Функция осуществляет поиск значения координат по оси.
    :param name_axis: ось, по которой осуществляется смещение
    :param str_text: текст строки управляющей программы
    :param d_coord: стырые координаты
    :return: значение координат оси
    """
    regex_str = re.compile("({0})([+-?0-9]+)".format(name_axis))
    coord = regex_str.findall(str_text)

    if (name_axis == "I" or name_axis == "J") and len(coord) == 0:
        return 0

    return coord[0][1] if coord else d_coord["{0}".format(name_axis)]


def get_replace_str(str_text, act_coord, new_coord):
    """
    Функция с помощью замены меняет координаты(act_coordd) на новые координаты(new_coord)
    и если в строке управляющией программы нет одной из кординат,то вставляет отсутсвующую
    рядом с имеющейся.
    :param str_text: текст строки управляющей программы
    :param act_coord: актульные кординаты, которые нужно поменять
    :param new_coord: новые кординаты на которые нужно поменять
    :return:возращает измененую строку
    """
    if act_coord != new_coord:

        for name_axis_1, name_axis_2 in [["X", "Y"], ["I", "J"]]:

            str_text = str_text.replace("{0}{1}".format(name_axis_1, act_coord[name_axis_1]),
                                        "{0}{1}".format(name_axis_1, new_coord[name_axis_1]))

            str_text = str_text.replace("{0}{1}".format(name_axis_2, act_coord[name_axis_2]),
                                        "{0}{1}".format(name_axis_2, new_coord[name_axis_2]))

            regex_str_ix = re.compile("({0})([+-?0-9]+)".format(name_axis_1))
            num_ix_coord = regex_str_ix.search(str_text)

            regex_str_jy = re.compile("({0})([+-?0-9]+)".format(name_axis_2))
            num_jy_coord = regex_str_jy.search(str_text)

            if num_jy_coord is None and num_ix_coord:
                str_text = str_text[:num_ix_coord.end()] + "{0}{1}".format(name_axis_2, new_coord[name_axis_2])\
                            + str_text[num_ix_coord.end():]
            if num_ix_coord is None and num_jy_coord:
                str_text = str_text[:num_jy_coord.start()] + "{0}{1}".format(name_axis_1, new_coord[name_axis_1])\
                            + str_text[num_jy_coord.start():]

    return str_text


def get_turn_coord(b_a, act_coord, new_coord, old_coord, str_text, g_code_on):
    """
    Функция поворота координат вокруг нуля программ, вычисляется по
    формуле X2 = X1*cos(a) + Y1*sin(a) и Y2 = Y1*cos(a) - X1*cos(a),
    если включен G2 или G3 и I или J не равно нулю: вычисляется центр окружности с помощью векторов I и J
    затем по формуле находятся координаты при вовороте на угол b_a,
    и находятся вектора.
    :param b_a: значение угла для поворота
    :param act_coord: актуальные кординаты
    :param new_coord: измененые координаты предыдущей строки
    :param old_coord: кординаты предыдущей строки
    :param str_text: текст строки управляюще программы
    :param g_code_on: включеные G-коды
    :return: возвращает изменную строку с новыми кординаты поворота
    """
    b_a = b_a / 360 * math.pi * 2

    tmp_x = new_coord["X"]
    tmp_y = new_coord["Y"]

    new_coord["X"] = round(float(act_coord["X"])*math.cos(b_a) + float(act_coord["Y"])*math.sin(b_a), 3)
    new_coord["Y"] = round(float(act_coord["Y"])*math.cos(b_a) - float(act_coord["X"])*math.sin(b_a), 3)

    if (g_code_on["group_1"][0] == "2" or g_code_on["group_1"][0] == "3") and (act_coord["I"] != 0
                                                                               or act_coord["J"] != 0):

        cc_x = round(float(old_coord["X"]) + float(act_coord["I"]), 3)
        cc_y = round(float(old_coord["Y"]) + float(act_coord["J"]), 3)

        cc_x_new = round(cc_x * math.cos(b_a) + cc_y * math.sin(b_a), 3)
        cc_y_new = round(cc_y * math.cos(b_a) - cc_x * math.sin(b_a), 3)

        new_coord["I"] = round(cc_x_new - float(tmp_x), 3)
        new_coord["J"] = round(cc_y_new - float(tmp_y), 3)

    str_text = get_replace_str(str_text, act_coord, new_coord)

    return str_text
