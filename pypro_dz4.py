'''1. Напишите функцию для транспонирования матрицы'''


NUMBER_OF_ROWS = 3
NUMBER_OF_COLUMNS = 5
MIN_NUMBER = -10
MAX_NUMBER = 10

from random import randint


def create_matrix() -> list[list[int]]:
     my_list = [[randint(MIN_NUMBER, MAX_NUMBER + 1) for _ in range(NUMBER_OF_COLUMNS)] for _ in range(NUMBER_OF_ROWS)]
     return my_list


def print_matrix(my_list: list[list[int]]):
    nor = len(my_list)
    noc = len(my_list[0])
    for i in range(nor):
        for j in range(noc):
            print(f'{my_list[i][j]: > 4}', end=' ')
        print()


def matrix_transposition(my_list: list[list[int]]) -> list[list[int]]:
    a = [[0 for i in range(NUMBER_OF_ROWS)] for j in range(NUMBER_OF_COLUMNS)]
    for i in range(NUMBER_OF_ROWS):
        for j in range(NUMBER_OF_COLUMNS):
            a[j][i] = my_list[i][j]
    return a


b = create_matrix()
print_matrix(b)
print()
print(print_matrix(matrix_transposition(b)))


'''2.Напишите функцию принимающую на вход только ключевые
параметры и возвращающую словарь, где ключ — значение
переданного аргумента, а значение — имя аргумента. Если
ключ не хешируем, используйте его строковое представление.'''

def create_dict_arg(**kwargs):
    arg_dict = {key: value if hash_f(value) else str(value) for key, value in kwargs.items()}
    arg_dict ={value: key for key, value in arg_dict.items()}
    return arg_dict


def hash_f(nam):
    res = True
    try:
        hash(nam)
    except TypeError:
        res = False
    return res


print(create_dict_arg(a=5, b='Hello world!', c=[1, 2, 3], d=('Tom', 'Pit'), e=3.6, f={1, 1, 2, 5}, g=True))



'''3. Напишите программу банкомат. 
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой 
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
Возьмите задачу о банкомате из семинара 2. Разбейте её
на отдельные операции — функции. Дополнительно сохраняйте
все операции поступления и снятия средств в список.'''

MULT = 50
summ = 0.0
count = 0
STEP = 3
PROC_P = 0.03
LIM = 5000000.0
PROC_M = 0.1
PROC_MS = 0.015
MINIM = 30
MAX = 600
def mult_sum(u_sum: float, mult: int) -> bool:
    if u_sum % mult != 0:
        return False
    else:
        return True


def count_proc(summ: float, proc: float) -> float:
    summ += summ * proc
    return summ


def million(summ: float, lim: float, proc: float) -> float:
    if summ >= lim:
        summ = summ - summ * proc
        print(summ)
        return summ
    return summ


def percent_for_with(amount: float, proc: float, minn: int, maxx: int) -> float:
    percent = amount * proc
    return max(minn, min(maxx, percent))


while True:
    if count > STEP:
        summ = count_proc(summ, PROC_P)
        count = 0
    else:
        print('Выберете действие: 1 (снять), 2 (пополнить), 3 (выйти)')
        user_inp = input()
        if user_inp == '1':
            summ = million(summ, LIM, PROC_M)
            print(f'Сумма на счету: {summ}')
            sum_many = float(input('Введите сумму кратную 50, которую планируете снять: '))
            if sum_many > summ:
                print('Вы превысили лимит')
            else:
                if mult_sum(sum_many, MULT):
                    percent = percent_for_with(sum_many, PROC_MS, MINIM, MAX)
                    summ -= sum_many + percent
                    count += 1
                    print(f'Сумма на счету: {summ}')
                else:
                    print('Сумма не кратна 50')
        elif user_inp == '2':
            summ = million(summ, LIM, PROC_M)
            print(f'Сумма на счету: {summ}')
            sum_many = float(input('Введите сумму кратную 50: '))
            if mult_sum(sum_many, MULT):
                summ += sum_many
                count += 1
                print(f'Сумма на счету: {summ}')
            else:
                print('Сумма не кратна 50')
        elif user_inp == '3':
            print(f'Сумма на счету: {summ}')
#             break













