# ШАГ. Д/з по сроку 20/07/2023

import os


def get_operation_template(operation_number: int):
    match operation_number:
        case 1:
            return lambda int1, int2: f'{int1} + {int2} = {int1 + int2}'
        case 2:
            return lambda int1, int2: f'{int1} - {int2} = {int1 - int2}'
        case 3:
            return lambda int1, int2: f'{int1} * {int2} = {int1 * int2}'
        case 4:
            return lambda int1, int2: f'{int1} / {int2} = {int1 / int2}'
        case 5:
            return lambda int1, int2: f'{int1} // {int2} = {int1 // int2}'
        case 6:
            return lambda int1, int2: f'{int1} % {int2} = {int1 % int2}'
        case 7:
            return lambda int1, int2: f'{int1} ** {int2} = {int1 ** int2}'
        case _:
            return lambda int1, int2: f'{int1} ? {int2} = <Операция не определена>'


def print_header() -> None:
    print('-' * 40)
    print('Калькулятор'.center(40, ' '))
    print('-' * 40)
    print("""
    1. +\t(сложение)
    2. -\t(вычитание)
    3. *\t(умножение)
    4. /\t(деление)
    5. //\t(целочисленное деление)
    6. %\t(остаток от деления)
    7. **\t(возведение в степень)\n
    0. ЗАВЕРШИТЬ
    """)
    print('-' * 40)

    return None


def main() -> None:
    while True:
        os.system('cls')
        print_header()
        operation = int(input('Введите операцию калькулятора:'))
        print('-' * 40)
        if 1 <= operation <= 7:
            calculator = get_operation_template(operation)
            number1 = int(input('Введите первое число > '))
            number2 = int(input('Введите второе число > '))
            print('-'*40)
            print(calculator(number1, number2))
            print('-'*40)
            os.system("pause")

        elif operation == 0:
            print('Вычисления завершены.')
            print('-'*40)
            break
        else:
            print('Ошибка!!! Введено неверное имя операции!')
            print('-'*40)
            os.system("pause")


    return None


if __name__ == '__main__':
    main()
