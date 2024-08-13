def personal_sum(numbers):
    incorect_data = 0
    result = 0
    summa = 0
    try:
        for i in numbers:
            try:
                summa += i
                result += 1
            except TypeError:
                incorect_data += 1
                print('В numbers записан некорректный тип данных')
    except TypeError:
        incorect_data += 1
        print('В numbers записан некорректный тип данных')
    return result, incorect_data, summa


def calculate_average(numbers):
    result, incorect_data, summa = personal_sum(numbers)
    try:
        try:
            return summa / result
        except TypeError:
            print('В numbers записан некорректный тип данных')
    except ZeroDivisionError:
        print('В numbers записан некорректный тип данных')
        return 0


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать