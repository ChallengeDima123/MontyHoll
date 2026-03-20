import random

ch = 0
notch = 0
count = 100000
m = 0

while m <= count:
    m += 1
    mas = [[0, 0, False], [1, 0, False], [2, 0, False]]  # инициализация главного массива
    l = random.randint(0, 2)  # в какой двери у нас будет приз
    mas[l][1] = 1  # ставим приз

    mas[random.randint(0, 2)][2] = True  # первый выбор
    mas1 = [[mas[0][0], mas[0][1], mas[0][2]], [mas[1][0], mas[1][1], mas[1][2]], [mas[2][0], mas[2][1], mas[2][2]]] #затычка для вывода в консоль

    badmas = []
    for i in range(0, 3):
        if i != l and not mas[i][2]:
            badmas.append(i)  # ищем двери, которые подходят под снос

    k = 0
    if len(badmas) == 1:
        k = badmas[0]
        mas.remove(mas[k])  # удаляем дверь, если она одна

    else:
        k = badmas[random.randint(0, 1)]
        mas.remove(mas[k])  # удаляем дверь, если их 2

    isch = random.randint(0, 1)  # меняем ли выбор


    second_choise = [x for x in range(0, 2) if mas[x][2] == False]  # выбираем дверь, которая не выбрана (гарантируется что такая дверь только одна)
    if mas[second_choise[0]][1] == 1:  # победили ли мы, если изменили выбор?
        ch += 1
    second_choise = []
    second_choise = [x for x in range(0, 2) if mas[x][2] == True]  # выбираем дверь, которая уже выбрана (затычка)
    if mas[second_choise[0]][1] == 1:  # победили ли мы, если не изменили выбор?
        notch += 1

print(f'Кол-во запусков: {count}')
print('====================')
print(f'Кол-во побед, когда мы изменили выбор - {ch}')
print(f'Кол-во побед, когда мы не изменили выбор - {notch}')
print()
print(f'Кол-во побед, когда мы изменили выбор (отношение) - {ch/count}')
print(f'Кол-во побед, когда мы не изменили выбор (отношение) - {notch/count}')
print('====================')







