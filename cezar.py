o_ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
O_ru = "АБВГДЕЁЖЗИЁКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def cezar(t_str, n):
    result = ""
    for i in range(len(t_str)):
        if t_str[i] in o_ru:
            result += o_ru[(o_ru.index(t_str[i]) + n) % 33]
        elif t_str[i] in O_ru:
            result += O_ru[(O_ru.index(t_str[i]) + n) % 33]
        else:
            result += t_str[i]
    return result


def pleyfer(text):
    result = ""

    if len(text) % 2 == 1:
        text += "я"

    mass = []

    for i in range(0, len(text), 2):
        mass.append(text[i] + text[i + 1])

    data = [
        ["а", "б", "в", "г", "д", "е"],
        ["ё", "ж", "з", "и", "й", "к"],
        ["л", "м", "н", "п", "р", "с"],
        ["т", "у", "ф", "х", "ц", "ч"],
        ["ш", "щ", "ь", "ы", "ь", "э"],
        ["ю", "я", "о", ".", ",", "?"],
    ]

    for i in mass:

        x1 = -1
        y1 =-1

        for g in range(6):
            for t in range(6):
                if data[g][t] == i[0].lower():
                    x1 = g
                    y1 = t

        x2 = -1
        y2 = -1

        for g in range(6):
            for t in range(6):
                if data[g][t] == i[1].lower():
                    x2 = g
                    y2 = t

        if x1 == -1 or x2 == -1:
            result += i
            continue

        if x1 != x2 and y1 != y2:
            result += data[x1][y2] + data[x2][y1]

        elif x1 == x2 and y1 != y2:
            result += data[x1][(y1 + 1) % 6] + data[x2][(y2 + 1) % 6]

        elif x1 != x2 and y1 == y2:
            result += data[(x1 + 1) % 6][y1] + data[(x2 + 1) % 6][y2]

        elif x1 == x2 and y1 == y2:
            result += data[x1][y1] + 'э' + data[x2][y2]

    return result


pleyfer("В начале 1806 года Николай Ростов вернулся в отпуск. Денисов ехал тоже домой в Воронеж, и Ростов уговорил "
        "его ехать с собой до Москвы и остановиться у них в доме. На предпоследней станции, встретив товарища, "
        "Денисов выпил с ним три бутылки вина и подъезжая к Москве, несмотря на ухабы дороги, не просыпался, лежа"
        " на дне перекладных саней, подле Ростова, который, по мере приближения к Москве, приходил все более и"
        " более в нетерпение. «Скоро ли? Скоро ли? О, эти несносные улицы")


