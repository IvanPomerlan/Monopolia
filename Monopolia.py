import random

pole1 = {

    'arenda': 5,
    'cell': 10,
    'name': "Маями",
    'vladelec': "Нету",
}
pole2 = {

    'arenda': 20,
    'cell': 40,
    'name': "Таити",
    'vladelec': "Нету",
}
pole3 = {

    'arenda': 40,
    'cell': 80,
    'name': "Caн-Лоренс",
    'vladelec': "Нету",
}
pole4 = {

    'arenda': 60,
    'cell': 120,
    'name': "Пфриж",
    'vladelec': "Нету",
}
pole5 = {

    'arenda': 80,
    'cell': 160,
    'name': "Mосква",
    'vladelec': "Нету",
}
pole6 = {

    'arenda': 100,
    'cell': 200,
    'name': "Львов",
    'vladelec': "Нету",
}
pole7 = {

    'arenda': 120,
    'cell': 240,
    'name': "Шепетовка",
    'vladelec': "Нету",
}
pole8 = {

    'arenda': 140,
    'cell': 280,
    'name': "Киев",
    'vladelec': "Нету",
}
pole9 = {

    'arenda': 160,
    'cell': 320,
    'name': "Сан-Франциско",
    'vladelec': "Нету",
}
pole10 = {

    'arenda': 180,
    'cell': 360,
    'name': "Нью-Йорк",
    'vladelec': "Нету",
}
pole11 = {

    'arenda': 200,
    'cell': 400,
    'name': "Токио",
    'vladelec': "Нету",
}
pole12 = {

    'arenda': 220,
    'cell': 440,
    'name': "Пекин",
    'vladelec': "Нету",
}

all_pole = []
all_pole.append(pole1)
all_pole.append(pole2)
all_pole.append(pole3)
all_pole.append(pole4)
all_pole.append(pole5)
all_pole.append(pole6)
all_pole.append(pole7)
all_pole.append(pole8)
all_pole.append(pole9)
all_pole.append(pole10)
all_pole.append(pole11)
all_pole.append(pole12)

Igroky = []
Run = True


class Igroki():
    """Класс для создания героя из нашей игры"""

    def __init__(self, name, figurka):
        """Иницинировать нашего героя"""
        self.name = name
        self.figurca = figurka
        self.money = 500
        self.hod_kunika = 0
        enemy = {}
        enemy['name'] = self.name
        enemy['fihurka'] = self.figurca
        enemy['money'] = self.money
        enemy['hod_kubika'] = int(self.hod_kunika)
        Igroky.append(enemy.copy())


haha1 = Igroki(input("Твое имя "), input("Твоя фигурка "))
haha2 = Igroki(input("Твое имя "), input("Твоя фигурка "))
haha3 = Igroki(input("Твое имя "), input("Твоя фигурка "))
haha4 = Igroki(input("Твое имя "), input("Твоя фигурка "))


def kubatorit(x):
    kubik = random.randint(1, 6)
    print("Твой ход " + x['name'])
    print("Твой капитал " + str(x['money']))
    print("Бросаю кубики..." + str(kubik))
    Igroky[0]['hod_kubika'] += kubik


while Run:
    for x in Igroky:
        print("=================== Playr " + str(x['name']) + " ====================")
        kubatorit(x)
        if (x['hod_kubika'] > 12):
            x['hod_kubika'] -= 12
            x['money'] += 200
        xx = int(x['hod_kubika'])
        print("Вы на клетке " + all_pole[xx]['name'] + "\nВладелец " + all_pole[xx]['vladelec'])
        if all_pole[xx]['vladelec'] == "Нету":
            print("Стоимость клетки " + str(all_pole[xx]['cell']) + "\nЦена аренды " + str(all_pole[xx]['arenda']))
        cel = input("Хотите купить? да или нет: ")
        if cel == "да":
            x['money'] -= all_pole[xx]['cell']
            all_pole[xx]['vladelec'] = x['name']
        elif cel == 'нет':
            print("Не проданно")
        elif all_pole[xx]['vladelec'] != "Нету":
            x['money'] -= all_pole[xx]['arenda']
            print("Аренда уплачена")
        for xxx in Igroky:
            if xxx['name'] == all_pole[xx]['vladelec']:
                xxx['money'] += all_pole[xx]['arenda']
        print("===================Playr2====================")

        if x['money'] == 0:
            Run = False

Igroky = []
