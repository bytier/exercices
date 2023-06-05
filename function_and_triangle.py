

def is_triangle(a, b, c):
    if a > 0 and b > 0 and c > 0:

        if a + b > c:
            message = 'True'
        elif a + c > b:
            message = 'True'
        elif b + c > a:
            message = 'True'
    else:
        message = 'False'

    return message


def f_in_():
    a = int(input('Enter a - side: '))
    b = int(input('Enter b - side: '))
    c = int(input('Enter c - side: '))
    # можно использовать одно и то же имя переменных т.к. они локальные и я тут не изменяю их
    # использую функцию внутри функции in_()
    message = is_triangle(a, b, c)

    return print(message)


if __name__ == '__main__':
    while 1 > 0:  # чтобы программа не прерывалась после первого выполнения функции
        f_in_()
