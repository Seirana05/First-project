# Приветствие
def greet():
    print("------------------")
    print("   Начало игры ")
    print("в крестики-нолики")
    print("------------------")
    print("Ввод: строка, затем столбец")

#  Создание поля
field = [[" "]*3,
         [" "]*3,
         [" "]*3]

# Показать поле
def show():
    print(f' 0  1  2')
    for i in range(3):
        print(f'{i} {field[i][0]} {field[i][1]} {field[i][2]}')


# Координаты хода

def ask():
    while True:
        cords = input("Ваш ход:").split()
        if len(cords) != 2:
            print('Введите 2 координаты')
        x, y = cords

        if not(x.isdigit()) or not (y.isdigit()):
            print('Введите числа:')
        x, y = int(x), int(y)

        if 0 <= x <= 2 and 0 <= y <= 2:
            if field[x][y] == " ":
                return x, y
            else:
                print("Здесь занято!")
        else:
            print("Координаты вне диапазона")


# Выигрышные комбинации

def win():
    win_cord = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
    for cord in win_cord:
        a = cord[0]
        b = cord[1]
        c = cord[2]
        if field[a[0]][a[1]] == field[b[0]][b[1]] == field[c[0]][c[1]] != ' ':
                print(f'Выиграл {field[a[0]][a[1]]}')
                return True
    return False

# Игровой цикл
greet()

num = 0
while True:
    num += 1
    show()
    if num % 2 == 1:
        print('Ходит крестик')
    else:
        print('Ходит нолик')

    x, y = ask()

    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if win():
        break

    if num == 9:
        print('Ничья!')
        break
