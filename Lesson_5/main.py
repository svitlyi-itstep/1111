def input_int(message):
    while True:
        try:
            result = int(input(message))
        except ValueError:
            print('Введено некоректне значення! Спробуйте ще раз.')
        except:
            print('Щось пішло не так!')
        else:
            return result


num1 = input_int('Введіть перше число:')
num2 = input_int('Введіть друге число:')

try:
    print(f'{num1} / {num2} = {num1 / num2}')
except ZeroDivisionError:
    print('Ділити на нуль не можна!')
except:
    print('Щось пішло не так!')

'''
    Переписати функцію input_int. Використовуючи цю функцію попросити користувача ввести 2 числа, 
    після чого вивести результат складання, віднімання, множення та ділення цих чисел.

'''