from os import system
from random import randint

wait = 500  # Определяет задержку перед переключением
chance_of_star = 7  # Значение между 0 и 9 (включительно) - указывает на шанс появления звезды

lastLog = ''
frame = 0


def tree():
    global wait, chance_of_star, lastLog, frame
    console = ''
    colors = ['\033[31m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m']

    new_year_tree = [
        '\033[32m                   ',
        '\033[31m         *         ',
        '\033[31m        ***        ',
        '\033[32m        /_\\        ',
        '\033[32m       /_\\_\\       ',
        '\033[32m      /_/_\\_\\      ',
        '\033[32m       /_/_\\       ',
        '\033[32m      /_/_\\_\\      ',
        '\033[32m     /_\\_/_/_\\     ',
        '\033[32m    /_\\_\\_/_\\_\\    ',
        '\033[32m      /_/_\\_\\      ',
        '\033[32m     /_\\_/_/_\\     ',
        '\033[32m    /_\\_\\_/_\\_\\    ',
        '\033[32m   /_/_\\_/_\\_/_\\   ',
        '\033[32m  /_/_\\_\\_/_\\_/_\\ ',
        '\033[32m  /_\\_/_\\_/_/_\\_/_\\ ',
        '\033[33m       [---]       '
    ]

    if frame >= wait:
        frame = 0
    if frame == 0:
        for i in new_year_tree:
            for j in i:
                if j == '_':
                    n = randint(0, 10)
                    if n > chance_of_star:
                        console += '\033[1m' + '{}'.format(colors[randint(0, len(colors) - 1)]) + '*' + '\033[0m' + '\033[32m'
                    else:
                        console += '_'
                else:
                    console += j
        lastLog = console
        print(console)
    else:
        print(lastLog)
    frame += 1


system("mode con cols=19 lines=17")

while True:
    tree()
