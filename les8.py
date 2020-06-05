# == Лото ==
#
# Правила игры в лото.
#
# Игра ведется с помощью спе циальных карточек, на которых отмечены числа,
# и фишек (бочонков) с цифрами.
#
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
#
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
#
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86
# --------------------------
#
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
# случайная карточка.
#
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
#
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
#     Если цифра есть на карточке - она зачеркивается и игра продолжается.
#     Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
#     Если цифра есть на карточке - игрок проигрывает и игра завершается.
#     Если цифры на карточке нет - игра продолжается.
#
# Побеждает тот, кто первый закроет все числа на своей карточке.
#
# Пример одного хода:
#
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
#  6  7          49    57 58
#    14 26     -    78    85
# 23 33    38    48    71
# --------------------------
# -- Карточка компьютера ---
#  7 87     - 14    11
#       16 49    55 88    77
#    15 20     -       76  -
# --------------------------
# Зачеркнуть цифру? (y/n)
#
# Подсказка: каждый следующий случайный бочонок из мешка удобно получать
# с помощью функции-генератора.
#
# Подсказка: для работы с псевдослучайными числами удобно использовать
# модуль random: http://docs.python.org/3/library/random.html

import random

my_list = []
my_matrix2= []

matrix_size = ["3", "9"]
print(matrix_size)

def matrix_generation(size):
    my_temp_list = []
    for el in range(int(size[0])):
        temp_list = []
        for el in range(int(size[1])):
            temp_list.append(random.randint(1, 25))
        my_temp_list.append(temp_list)
    return my_temp_list

my_list = matrix_generation(matrix_size)
my_matrix2 = matrix_generation(matrix_size)

def generate_barrel(start, end, quantity):
    temp_list = []
    for el in range(quantity):
        temp = random.randint(start, end)
        while True:
            try:
                pos = temp_list.index(temp)
                temp = random.randint(start, end)
            except ValueError:
                temp_list.append(temp)
                break
    return temp_list

class LottoCard():
    def __init__(self):
        self._numbers = []

        self.card_size = ["3","9"]
        self.card = [ [], [], [] ]
        self.list_temp = []
        self._numbers = generate_barrel(1, 90, 15)
        self.lotto_card_generation()
        pass

    def __str__(self):
        super.__str__(self)
        temp_list = []
        max_lengt = 0
        for el in range(len(self.list_temp)):
            for el2 in self.list_temp[el]:
                if max_lengt <= len(str(el2)): max_lengt = len(str(el2))
        for el in range(len(self.list_temp)):
            temp =""
            str_space = ""
            for el2 in self.list_temp[el]:
                if len(str(el2)) < max_lengt: str_space = " "
                else: str_space = ""
                temp+=str_space+str(el2) + " "
            temp += " \n"
            temp_list.append(''.join(temp))
        return ''.join(temp_list)

    def lotto_card_generation(self):
        self.list_temp = []
        self._numbers.sort()
        temp_sorted = []
        for el in range(9):
            self.list_temp.append([])
            for el2 in range(len(self._numbers)):
                if (self._numbers[el2]<10*(el+1)) and (self._numbers[el2]>=10*el):
                    self.list_temp[el].append(str(self._numbers[el2]))
        return self.list_temp

    def check_number(self, number):
        line = 0
        try:
            temp = self._numbers.index(number)
            return True
        except ValueError:
            return False

    def check_out(self, number):
        line = 0
        try:
            temp = self._numbers.index(number)
            self._numbers.pop(temp)
            self.lotto_card_generation()
            return True
        except ValueError:
            return False

    def card_empty(self):
        if len(self._numbers) == 0: return True
        else: return False


user_card = LottoCard()
comp_card = LottoCard()

barrel = generate_barrel(1,90, 90)
moves_number = 0

while moves_number<90:

    number_on_move = barrel[0]
    barrel.remove(number_on_move)
    print(f"Новый бочонок: {number_on_move} (осталось {90-moves_number-1}) номер хода - {moves_number+1}")
    moves_number += 1
    print("------ Ваша карточка ------")
    print(user_card)
    print("--- Карточка компьютера ---")
    print(comp_card)
    user_answer = input('Зачеркнуть цифру? (y/n)').upper()
    if comp_card.check_number(number_on_move) == True: comp_card.check_out(number_on_move)
    if (user_answer == "Y"):
        if user_card.check_number(number_on_move) == False:
            print("Вы проиграли!")
            moves_number = 91
        else:
            user_card.check_out(number_on_move)
    else:
        if user_card.check_number(number_on_move) == True:
            print("Вы проиграли!")
            moves_number = 91

    if comp_card.card_empty():
        print("Игра закончена, победил Компьютер!")
        moves_number = 91
    if user_card.card_empty():
        print("Игра закончена, победил Человек!")
        moves_number = 91





