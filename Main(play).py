import pygame
import sys
import random
import time
from ctypes import *


class Igroki():
    """Класс для создания героя из нашей игры"""

    def __init__(self, name):
        """Иницинировать нашего героя"""
        self.name = name
        self.money = 500
        self.hod_kubika = 0
        self.my_area = ""
        enemy = {}
        enemy['name'] = self.name
        enemy['money'] = self.money
        enemy['hod_kubika'] = int(self.hod_kubika)
        enemy['my_area'] = self.my_area
        Igroky.append(enemy.copy())


class Mesta:
    def __init__(self, name, name_little, arenda, cell, mx1, my1, mx2, my2):
        self.name = name
        self.name_little = name_little
        self.arenda = arenda
        self.cell = cell
        self.mx1 = int(mx1)
        self.my1 = int(my1)
        self.mx2 = int(mx2)
        self.my2 = int(my2)
        self.vlasnuk = 0

        enemy = {}
        enemy['name'] = self.name
        enemy['name_little'] = self.name_little
        enemy['arenda'] = self.arenda
        enemy['cell'] = self.cell
        enemy['valsnuk'] = self.vlasnuk
        enemy['mx1'] = int(self.mx1 * 3)
        enemy['my1'] = int(self.my1 * 3)
        enemy['mx2'] = int(self.mx2 * 3)
        enemy['my2'] = int(self.my2 * 3)

        All_pole.append(enemy.copy())


class Batton:
    # х это первая координата кнопки, хх вторая(по величене)
    # у и уу тоже самое только для оси у
    # ххх ууу первые углы фона(самые маленькие, если по координатам)
    def __init__(self, x, y, xx, yy, xxx, yyy, image, image_fon):
        self.x = x
        self.y = y
        self.xx = xx
        self.yy = yy
        self.xxx = xxx
        self.yyy = yyy
        self.image = image
        self.image_fon = image_fon

    # добавил if чтобы закрывать окно
    def battons(self, action=None):
        for ev in pygame.event.get():
            mouses = pygame.mouse.get_pos()
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if self.x <= mouses[0] <= self.xx and self.y <= mouses[1] <= self.yy:
                    # if action is not NONE: тут так было, но я изменил

                    screen.blit(self.image_fon, (self.xxx, self.yyy))
                    pygame.display.update()
                    action()

            if ev.type == pygame.MOUSEMOTION:
                if self.x <= mouses[0] <= self.xx and self.y <= mouses[1] <= self.yy:
                    screen.blit(self.image, (self.x, self.y))
                else:
                    screen.blit(self.image_fon, (self.xxx, self.yyy))

                pygame.display.update()


def mesta_obozna4enie():
    pole1 = Mesta("Старт", "Я ГЕЙ", 0, 0, 292, 31, 321, 31)
    pole2 = Mesta("Запоріжжя", "ЗП", 20, 40, 292, 79, 321, 79)
    pole3 = Mesta("Укр. Залізниця", "УЗ", 20, 60, 292, 127, 321, 127)
    pole4 = Mesta("Форс Мажор", "НЕ КОПАЙТЕСЬ В ГОЛОМ КОДЕ", 5, 6, 292, 178, 321, 178)
    pole5 = Mesta("Маріуполь", "МР", 30, 100, 292, 223, 321, 223)
    pole6 = Mesta("Арабаська стілка", "Ас", 40, 120, 292, 271, 321, 271)
    pole7 = Mesta("Армія", "Кобчена сосиска", 10, 11, 292, 319, 321, 319)
    pole8 = Mesta("Полтава", "ПЛ", 50, 110, 244, 319, 272, 319)
    pole9 = Mesta("Житомир", "ЖТ", 60, 120, 196, 319, 224, 319)
    pole10 = Mesta("Шанс", "Error 404", 0, 0, 148, 319, 176, 319)
    pole11 = Mesta("Поїхати в Польшу", "Мене в дитинстві", 0, 0, 100, 319, 128, 319)
    pole12 = Mesta("Херсон", "ХР", 70, 130, 52, 319, 80, 319)
    pole13 = Mesta("Дивна темка", "били...", 0, 0, 4, 319, 32, 319)
    pole14 = Mesta("Одеса", "Од", 90, 150, 4, 271, 32, 271)
    pole15 = Mesta("Укр. Залізниця", "УЗ", 20, 60, 4, 223, 32, 223)
    pole16 = Mesta("Форс Мажор", "", 0, 0, 4, 175, 32, 175)
    pole17 = Mesta("Шепетівка", "ШП", 120, 170, 4, 127, 32, 127)
    pole18 = Mesta("Харків", "ХК", 140, 190, 4, 79, 32, 79)
    pole19 = Mesta("Пійман на закладці", "", 0, 0, 4, 31, 32, 31)
    pole20 = Mesta("Дніпро", "ДН", 160, 210, 52, 31, 80, 31)
    pole21 = Mesta("Київ", "КЇ", 190, 240, 100, 31, 128, 31)
    pole22 = Mesta("Шанс", "", 0, 0, 148, 31, 176, 31)
    pole23 = Mesta("Укр. Залізниця", "УЗ", 20, 60, 196, 31, 224, 31)
    pole24 = Mesta("Львів", "ЛВ", 200, 260, 244, 31, 272, 31)


def end_game():
    pygame.mixer.music.load("Arstotska.mp3")
    pygame.mixer.music.play(-1)
    if player == 1:
        a = 0
    else:
        a = 1
    b = 338
    b1 = 1008
    c = 495
    c1 = 1100
    d = 490
    d1 = 1200
    start = time.time()
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()

        ensd = time.time() - start
        if ensd >= 1:

            print("end")
            screen.blit(end_fon, (0, 0))
            screen.blit(end, (b, b1))
            f1 = pygame.font.Font(None, 40)
            text1 = f1.render(Igroky[player]['name'], 1, (0, 0, 0))
            screen.blit(text1, (c, c1))
            f2 = pygame.font.Font(None, 36)
            text2 = f2.render(str(Igroky[a]['name']), 1, (0, 0, 0))
            screen.blit(text2, (d, d1))
            pygame.display.update()
            b1 -= 50
            c1 -= 50
            d1 -= 50
            start = time.time()
            if b1 <= 200:
                while True:
                    for ev in pygame.event.get():
                        if ev.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                    ensd = time.time() - start
                    if ensd >= 84:
                        sys.exit()


def menus_play():
    button_menu_play = Batton(308, 435, 488, 482, 279, 334, menus_plays, menu)
    button_menu_play.battons(fff)


def end_hod():
    global aa

    screen.blit(renz, (333, 545))
    aa += 2


def kubik():
    button_kubik = Batton(475, 475, 533, 532, 475, 475, ggty, ggty12)
    button_kubik.battons(you_lox)


def bD():
    batton_buy_cell = Batton(347, 656, 509, 756, 347, 656, buy2, buy4)
    batton_buy_cell.battons(buy_area)


def bN():
    batton_buy_cell1 = Batton(516, 656, 678, 756, 516, 656, buy3, buy5)
    batton_buy_cell1.battons(no_bay_area)


def buy_cell():
    bD()
    bN()


def chans():  # !!!!!!!!!!!!!!!!
    batton_buy_cell1 = Batton(180, 411, 279, 591, 180, 411, Chans, Chans_fon)
    batton_buy_cell1.battons(shans_core)


def fors_major():
    batton_buy_cell1 = Batton(750, 411, 849, 591, 750, 411, fors, fors_fon)
    batton_buy_cell1.battons(fors_major_core)


def buy_area():
    render_area(player)
    screen.blit(renz, (333, 545))
    time.sleep(3)
    print(2)
    end_hod()


def no_bay_area():
    screen.blit(renz, (333, 545))
    print("не продано")
    end_hod()


def propustitb_XOD(z):
    global propusk
    # z либо 1 если пропустить первому игроку, либо 2 второму
    if z == 1:
        propusk[0] = 1
    else:
        propusk[1] = 1


def render_area_use(ae):
    if len(Igroky[ae]['my_area']) < 12:
        screen.blit(player_menu, (338, 154))
        f1 = pygame.font.Font(None, 36)
        text1 = f1.render(Igroky[ae]['name'], 1, (0, 0, 0))
        screen.blit(text1, (495, 169))
        f2 = pygame.font.Font(None, 36)
        text2 = f2.render(str(Igroky[ae]['money']), 1, (0, 0, 0))
        screen.blit(text2, (510, 195))
        f1 = pygame.font.Font(None, 36)
        text1 = f1.render(str(Igroky[ae]['my_area']), 1, (0, 0, 0))
        screen.blit(text1, (526, 232))
        pygame.display.update()

    else:
        screen.blit(player_menu, (338, 154))
        f1 = pygame.font.Font(None, 36)
        text1 = f1.render(Igroky[ae]['name'], 1, (0, 0, 0))
        screen.blit(text1, (495, 169))
        f2 = pygame.font.Font(None, 36)
        text2 = f2.render(str(Igroky[ae]['money']), 1, (0, 0, 0))
        screen.blit(text2, (510, 195))
        s1 = str(Igroky[ae]['my_area'])
        result1 = s1[12:]
        f1 = pygame.font.Font(None, 36)
        text2 = f1.render(str(result1), 1, (0, 0, 0))
        screen.blit(text2, (360, 260))
        result2 = s1[:12]
        f1 = pygame.font.Font(None, 36)
        text3 = f1.render(str(result2), 1, (0, 0, 0))
        screen.blit(text3, (526, 232))
        pygame.display.update()


def render_area(ea):
    screen.blit(player_menu, (338, 154))
    house = int(Igroky[ea]['hod_kubika'])
    Igroky[ea]['my_area'] += str(All_pole[house]['name_little'] + ", ")
    All_pole[house]['valsnuk'] = int(player) + 1
    if len(Igroky[ea]['my_area']) < 12:
        Igroky[ea]['money'] -= All_pole[house]['cell']
        print(len(Igroky[ea]['my_area']))
        pygame.display.update()

        f1 = pygame.font.Font(None, 36)
        text1 = f1.render(Igroky[ea]['name'], 1, (0, 0, 0))
        screen.blit(text1, (495, 169))
        f2 = pygame.font.Font(None, 36)
        text2 = f2.render(str(Igroky[ea]['money']), 1, (0, 0, 0))
        screen.blit(text2, (510, 195))

        f1 = pygame.font.Font(None, 36)
        text1 = f1.render(str(Igroky[ea]['my_area']), 1, (0, 0, 0))
        screen.blit(text1, (526, 232))
        print("render area_if")
        pygame.display.update()


    else:
        Igroky[ea]['money'] -= All_pole[house]['cell']
        print("render area else  " + Igroky[ea]['my_area'])
        screen.blit(player_menu, (338, 154))
        pygame.display.update()
        f1 = pygame.font.Font(None, 36)
        text1 = f1.render(Igroky[ea]['name'], 1, (0, 0, 0))
        screen.blit(text1, (495, 169))
        f2 = pygame.font.Font(None, 36)
        text2 = f2.render(str(Igroky[ea]['money']), 1, (0, 0, 0))
        screen.blit(text2, (510, 195))

        s1 = str(Igroky[ea]['my_area'])
        result1 = s1[12:]
        f1 = pygame.font.Font(None, 36)
        text2 = f1.render(str(result1), 1, (0, 0, 0))
        screen.blit(text2, (360, 260))
        result2 = s1[:12]
        f1 = pygame.font.Font(None, 36)
        text3 = f1.render(str(result2), 1, (0, 0, 0))
        screen.blit(text3, (526, 232))
        pygame.display.update()


def render_icons():
    screen.blit(render1, (861, 0))
    screen.blit(render2, (147, 861))
    screen.blit(render3, (0, 0))
    screen.blit(render4, (147, 0))

    ren1 = pygame.Rect(861, 0, 147, 1008)
    ren2 = pygame.Rect(147, 861, 714, 147)
    ren3 = pygame.Rect(0, 0, 147, 1008)
    ren4 = pygame.Rect(147, 0, 714, 1447)
    pygame.display.update(ren1)
    pygame.display.update(ren2)
    pygame.display.update(ren3)
    pygame.display.update(ren4)

    r = int(Igroky[0]['hod_kubika'])
    r1 = int(Igroky[1]['hod_kubika'])
    e1 = int(All_pole[r]['mx1'])
    e11 = int(All_pole[r]['my1'])
    e2 = int(All_pole[r1]['mx2'])
    e22 = int(All_pole[r1]['my2'])

    screen.blit(player1, (e1, e11))
    screen.blit(player2, (e2, e22))
    icon1 = pygame.Rect(e1, e11, 30, 30)
    icon2 = pygame.Rect(e2, e22, 30, 30)
    pygame.display.update(icon1)
    pygame.display.update(icon2)


def fff():
    pygame.mixer.music.stop()
    print(len(Igroky[0]['my_area']))
    global aa
    screen.blit(myimagge, (0, 0))
    pygame.display.update()

    render_icons()

    # playmenu = pygame.Rect(350, 150, 350, 276)
    pygame.display.update()
    print(Igroky)
    print(All_pole)
    pygame.mixer.music.load("Song_fon.mp3")
    pygame.mixer.music.play(-1)
    while 2 == 2:
        for x in Igroky:
            while x['money'] < 0:
                if x['money'] <= 0:
                    if len(x['my_area']) == 0:
                        print("end_game")
                        screen.blit(end_fon, (0, 0))
                        pygame.display.update()
                        start = float(time.time())
                        pygame.mixer.music.stop()
                        while True:
                            for ev in pygame.event.get():
                                if ev.type == pygame.QUIT:
                                    pygame.quit()
                                    quit()
                            ends = float(time.time()) - float(start)
                            if ends >= 7.0:
                                end_game()
                    else:
                        for y in All_pole:
                            print("не то")
                            p = str(x['my_area'])
                            j = str(y['name_little'] + ", ")
                            i = p[:4]
                            if j == i:
                                print("то")
                                x['my_area'] = p.replace(i, "")
                                y['valsnuk'] = 0
                                x['money'] += int(y['cell'] * 0.9)

            global propusk

            p, p1 = propusk[0], propusk[1]
            print(propusk[0])
            print(propusk[1])
            if p == 1:
                if x['name'] == 'Перший':
                    propusk[0] = 0
                    continue

                else:
                    pass
            if p1 == 1:
                if x['name'] == 'Другий':
                    propusk[1] = 0
                    break
                else:
                    pass
            print("propusk off")

            global player
            if x['name'] == 'Перший':
                player = 0
            elif x['name'] == 'Другий':
                player = 1
            print("kuku")
            screen.blit(renz, (333, 545))

            aa = 0
            screen.blit(player_menu, (338, 154))
            f1 = pygame.font.Font(None, 36)
            text1 = f1.render(x['name'], 1, (0, 0, 0))
            screen.blit(text1, (495, 169))
            f2 = pygame.font.Font(None, 36)
            text2 = f2.render(str(x['money']), 1, (0, 0, 0))
            screen.blit(text2, (510, 195))
            render_area_use(player)
            x['hod_kubika'] += random.randint(1, 5)  # КУБИК ТУТ

            pygame.display.update()

            while aa < 2:
                kubik()


# тоже самое но для второго(если игроков будет больше просто добавь elif


def you_lox():
    global aa
    a = player
    print('ход кубика' + str(Igroky[a]['hod_kubika']))
    if Igroky[a]['hod_kubika'] >= 24:
        Igroky[a]['hod_kubika'] -= 24
        Igroky[a]['money'] += 200
    print('you lox')
    render_icons()
    rul = int(Igroky[a]['hod_kubika'])
    lur = [1, 2, 4, 5, 7, 8, 11, 13, 14, 16, 17, 19, 20, 22, 23]
    result_armia = rul in [6]
    result_fors = rul in [3, 15]
    result_chans = rul in [9, 21]
    result_klad = rul in [18]
    result_poland = rul in [10]
    result_temka = rul in [12]
    print(rul)
    print(All_pole[rul])
    result = rul in lur
    print("VLASNUK " + str(All_pole[rul]['valsnuk']))
    print("c xtv chfdybdftv " + str(a + 1))
    ab = int(All_pole[rul]['valsnuk'])
    ba = int(a + 1)
    if ab == ba:
        # тут можна добавлять покупку домов, тут проходит определение ты владелец или нет.
        time.sleep(3)
        aa = 2
    elif result == True:

        if Igroky[a]['money'] < All_pole[rul]['cell']:
            print("Грошей маловато")
            end_hod()

        if All_pole[rul]['valsnuk'] == 0:
            print(All_pole[rul]['valsnuk'])
            screen.blit(buy1, (338, 550))
            f1 = pygame.font.Font(None, 36)
            text1 = f1.render("Ціна: " + str(All_pole[rul]['cell']), 1, (0, 0, 0))
            screen.blit(text1, (480, 610))
            f2 = pygame.font.Font(None, 36)
            text2 = f2.render("Аренда: " + str(All_pole[rul]['arenda']), 1, (0, 0, 0))
            screen.blit(text2, (465, 778))
            while aa < 2:
                buy_cell()

        else:
            # это аренда
            s = 0
            if player == 0:
                s = 1
            else:
                s = 0
            print("поле чьето")
            Igroky[player]['money'] -= All_pole[rul]['arenda']
            Igroky[s]['money'] += All_pole[rul]['arenda']
            screen.blit(orenda, (338, 550))
            f1 = pygame.font.Font(None, 50)
            text1 = f1.render(str(All_pole[rul]['name']), 1, (0, 0, 0))
            screen.blit(text1, (360, 600))
            f2 = pygame.font.Font(None, 100)
            text2 = f2.render("-" + str(All_pole[rul]['arenda']), 1, (0, 0, 0))
            screen.blit(text2, (470, 720))
            pygame.display.update()
            render_area_use(player)
            time.sleep(3)
            end_hod()

    elif result_fors == True:
        while aa < 2:
            fors_major()

    elif result_armia == True:
        while aa < 2:
            print("armia")

            screen.blit(fors_major_1, (338, 550))
            Igroky[a]['money'] -= 50
            Igroky[a]['hod_kubika'] = 6
            render_icons()
            render_area_use(a)
            propustitb_XOD(player + 1)
            time.sleep(3)
            end_hod()

    elif result_chans == True:
        while aa < 2:
            chans()



    elif result_klad == True:
        print("KlAD")
        screen.blit(klad, (338, 550))
        render_icons()
        render_area_use(a)
        propustitb_XOD(player + 1)
        time.sleep(3)
        end_hod()

    elif result_poland == True:
        print("Poland")
        screen.blit(poland, (338, 550))
        render_icons()
        Igroky[a]['money'] += 300
        render_area_use(a)
        time.sleep(3)
        end_hod()

    elif result_temka == True:
        print("Temkka")
        t = random.randint(1, 2)
        if t == 1:
            screen.blit(temka_minus, (338, 550))
            render_icons()
            Igroky[a]['money'] -= 100
            render_area_use(a)
            time.sleep(3)
            end_hod()
        else:
            screen.blit(temka_plus, (338, 550))
            render_icons()
            Igroky[a]['money'] += 100
            render_area_use(a)
            time.sleep(3)
            end_hod()


    else:
        print("поле не являеться area")
        end_hod()


# def kubik(x):
# Igroky[x]['hod_kubika'] += random.randint(1, 3)
#  if Igroky[x]['hod_kubika'] > 24:
#    Igroky[x]['hod_kubika'] -= 24
#     Igroky[x]['money'] += 200
# return Igroky[x]['hod_kubika']

def fors_major_core():
    global player
    global aa
    x = int(player)
    print()
    a = random.randint(1, 5)

    if a == 1:
        print("armia")
        screen.blit(fors_major_1, (338, 550))
        Igroky[x]['money'] -= 50
        Igroky[x]['hod_kubika'] = 6
        render_area_use(x)
        render_icons()
        propustitb_XOD(x + 1)
        time.sleep(3)
        end_hod()

    elif a == 2:
        print("KlAD")
        screen.blit(klad, (338, 550))
        Igroky[x]['hod_kubika'] = 18
        render_icons()
        propustitb_XOD(player + 1)
        time.sleep(3)
        end_hod()

    elif a == 3:
        print("Krasa")
        screen.blit(fors_major_2, (338, 550))
        render_icons()
        Igroky[x]['money'] -= 100
        render_area_use(x)
        time.sleep(3)
        end_hod()

    elif a == 4:
        print("Temkka")
        t = random.randint(1, 2)
        if t == 1:
            screen.blit(temka_minus, (338, 550))
            render_icons()
            Igroky[x]['money'] -= 100
            render_area_use(x)
            time.sleep(3)
            end_hod()
        else:
            screen.blit(temka_plus, (338, 550))
            render_icons()
            Igroky[x]['money'] += 100
            render_area_use(x)
            time.sleep(3)
            end_hod()
    elif a == 5:
        print("9MA")
        screen.blit(fors_major_3, (338, 550))
        render_icons()
        Igroky[x]['money'] -= 50
        render_area_use(x)
        time.sleep(3)
        end_hod()


def shans_core():
    global player
    global aa
    x = int(player)
    print()
    a = random.randint(1, 5)

    if a == 1:
        print("matrazt")
        screen.blit(matrazt, (338, 550))
        render_icons()
        Igroky[x]['money'] += 200
        render_area_use(x)
        time.sleep(4)
        end_hod()

    elif a == 2:
        print("poland")
        screen.blit(poland, (338, 550))
        render_icons()
        Igroky[x]['money'] += 300
        render_area_use(x)
        render_icons()
        time.sleep(3)
        end_hod()

    elif a == 3:
        print("Temkka")
        t = random.randint(1, 2)
        if t == 1:
            screen.blit(temka_minus, (338, 550))
            render_icons()
            Igroky[x]['money'] -= 100
            render_area_use(x)
            time.sleep(3)
            end_hod()
        else:
            screen.blit(temka_plus, (338, 550))
            render_icons()
            Igroky[x]['money'] += 100
            render_area_use(x)
            time.sleep(3)
            end_hod()
    elif a == 4:
        print("50grn")
        screen.blit(chans2, (338, 550))
        render_icons()
        Igroky[x]['money'] += 50
        render_area_use(x)
        time.sleep(4)
        end_hod()

    elif a == 5:
        print("50grn")
        screen.blit(chans3, (338, 550))
        Igroky[x]['hod_kubika'] = 0
        Igroky[x]['money'] += 200
        render_area_use(x)
        render_icons()
        time.sleep(4)
        end_hod()


def Run_game():
    pygame.mixer.music.load("Nachalo.mp3")
    pygame.mixer.music.play(1)

    haha1 = Igroki("Перший")
    haha2 = Igroki("Другий")
    mesta_obozna4enie()
    screen.fill(bd_color)
    while eu5:
        menus_play()
        pygame.display.flip()

    #   for x in Igroky:
    #       xt = x
    #      kubik(xt)
    #     xx = x['hod_kubika']
    #       if All_pole[xx]['vlasnuk'] == 0:
    #        Igroky[x]['money'] -= All_pole[xx]['cell']
    #       All_pole[xx]['vlasnuk'] += 1
    #  elif All_pole[xx]['vlasnuk'] == 1:
    #       Igroky[x]['money'] -= All_pole[xx]['arenda']


#

# -----------------------------MAIN-----------------------------------
MAX_X = 1008
MAX_Y = 1008
xxx = 0
yyy = 0
bd_color = (0, 0, 0)
aa = 0
player = 0
propusk = [0, 0]

eu5 = True
pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y))
pygame.display.set_caption("MONOPOLIA")

myimagge = pygame.image.load("ggtf.png").convert()
myimagge = pygame.transform.scale(myimagge, (1008, 1008))
ggty = pygame.image.load("x65.png").convert()
ggty = pygame.transform.scale(ggty, (57, 57))
menu = pygame.image.load("menu.png")
menu = pygame.transform.scale(menu, (450, 320))
menus_plays = pygame.image.load("menu_play.png")
menus_plays = pygame.transform.scale(menus_plays, (180, 46))
varios = pygame.image.load("playernamber.png")
varios = pygame.transform.scale(varios, (100, 100))
player1 = pygame.image.load("player1.png")
player1 = pygame.transform.scale(player1, (30, 30))
player2 = pygame.image.load("player2.png")
player2 = pygame.transform.scale(player2, (30, 30))
ggty12 = pygame.image.load("x655.png").convert()
ggty12 = pygame.transform.scale(ggty12, (57, 57))
player_menu = pygame.image.load("menu_players.png")
player_menu = pygame.transform.scale(player_menu, (350, 276))
mymaga = pygame.image.load("ggtf.png")
render1 = pygame.image.load("render1.png").convert()
render1 = pygame.transform.scale(render1, (147, 1008))
render2 = pygame.image.load("render2.png").convert()
render2 = pygame.transform.scale(render2, (714, 147))
render3 = pygame.image.load("render3.png").convert()
render3 = pygame.transform.scale(render3, (147, 1008))
render4 = pygame.image.load("render4.png").convert()
render4 = pygame.transform.scale(render4, (714, 147))
buy1 = pygame.image.load("Kupuelllb_4u_9k.png").convert()
buy1 = pygame.transform.scale(buy1, (350, 276))
buy2 = pygame.image.load("kup_da.png").convert()
buy2 = pygame.transform.scale(buy2, (164, 100))
buy3 = pygame.image.load("kup_NO.png").convert()
buy3 = pygame.transform.scale(buy3, (164, 100))
buy4 = pygame.image.load("kup_da_fon.png").convert()
buy4 = pygame.transform.scale(buy4, (164, 100))
buy5 = pygame.image.load("kup_NO_fon.png").convert()
buy5 = pygame.transform.scale(buy5, (164, 100))
renz = pygame.image.load("renz.png").convert()
renz = pygame.transform.scale(renz, (360, 286))
fors = pygame.image.load("Fors.png")
fors = pygame.transform.scale(fors, (102, 183))
fors_fon = pygame.image.load("Fors_fon.png")
fors_fon = pygame.transform.scale(fors_fon, (102, 183))
fors_major_1 = pygame.image.load("fors_major_1.png")
fors_major_1 = pygame.transform.scale(fors_major_1, (350, 276))
Chans = pygame.image.load("Chans.png")
Chans = pygame.transform.scale(Chans, (102, 183))
Chans_fon = pygame.image.load("Chans_fon.png")
Chans_fon = pygame.transform.scale(Chans_fon, (102, 183))
orenda = pygame.image.load("Orenda.png")
orenda = pygame.transform.scale(orenda, (350, 276))
end = pygame.image.load("END.png")
end = pygame.transform.scale(end, (324, 426))
end_fon = pygame.image.load("End_fon.png")
end_fon = pygame.transform.scale(end_fon, (1008, 1008))
klad = pygame.image.load("Klad.png")
klad = pygame.transform.scale(klad, (350, 276))
poland = pygame.image.load("Poland.png")
poland = pygame.transform.scale(poland, (350, 276))
matrazt = pygame.image.load("Shans1.png")
matrazt = pygame.transform.scale(matrazt, (350, 276))
fors_major_2 = pygame.image.load("fors_major_2.png")
fors_major_2 = pygame.transform.scale(fors_major_2, (350, 276))
temka_plus = pygame.image.load("Temka.png")
temka_plus = pygame.transform.scale(temka_plus, (350, 276))
temka_minus = pygame.image.load("Temka2.png")
temka_minus = pygame.transform.scale(temka_minus, (350, 276))
fors_major_3 = pygame.image.load("fors_major_3.png")
fors_major_3 = pygame.transform.scale(fors_major_3, (350, 276))
chans2 = pygame.image.load("Shans2.png")
chans2 = pygame.transform.scale(chans2, (350, 276))
chans3 = pygame.image.load("Shans3.png")
chans3 = pygame.transform.scale(chans3, (350, 276))

pygame.display.set_icon(mymaga)
Igroky = []
All_pole = []

Run_game()
