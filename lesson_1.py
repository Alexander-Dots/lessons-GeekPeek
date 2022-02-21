# Задание № 1 - Поработать с переменными
a = 3
b = 'hello'
c = True
print(a, b, c)
d = int(input('Введите целое число '))
print(a + d)
print(a + c)
text = input('Введите название фильма: ')
some_text = input('введите оценку этого фильма от 0 до 10: ')
print(f'Фильм с названием "{text}" независимые экперты оценивают в {some_text} баллов! (по шкале от 0 до 10)')

# Задание № 2 - Ввести время в секундах и перевести в формат чч:мм:cc
time_in_seconds = int(input('Ведите любое время в секундах: '))
time_hour = time_in_seconds // 3600
time_minute = (time_in_seconds - time_hour * 3600) // 60
time_second = time_in_seconds - time_hour * 3600 - time_minute * 60
print(f'Введённое время в формате чч:мм:сс составляет {time_hour:02}:{time_minute:02}:{time_second:02}')

# Задание № 3 - Узнайте у пользователя число и найти сумму чисел n + nn + nnn =

some_number = input('Введите число ')
print(f'{some_number} + {some_number * 2} + {some_number*3} = {int(some_number) + int(some_number * 2) + int(some_number*3)}')

# Задание № 4 - Запрашивается чило. Найти наибольшую цифру в этом числе
counter_numer = 0
number_2 = int(input('Введите какое-то число '))
while number_2 > 0:
    if number_2 % 10 > counter_numer:
        counter_numer = number_2 % 10
    number_2 //= 10
print(f'Максимальная цифра в введённом числе - {counter_numer}')

# Задание № 5 - Вычислить финансовый результат компании
proceeds = int(input('Введите цифру выручки компании '))
costs = int(input('Введите цифру издержек компании '))
if proceeds > costs:
    print(f'Прибыль компании составила {proceeds - costs}$')
    print(f'Рентабельность выручки  = {(proceeds - costs) / proceeds}$')
    employees = int(input("Введите число сотрудников "))
    print(f'Прибыль на каждого сотрудника составляет {(proceeds - costs) / employees}$')
elif proceeds < costs:
    print(f'Убытки компании составили {costs - proceeds}$')
else:
    print('Компания закончила отчётный период с "нулевой прибылью" ')

# Задание № 6 - Задача про спортсмена с данными за первый день и через сколько он выйдет на заданное кол-во км

a = int(input('Сколько км прошёл спортсмен в первый день? '))
b = int(input('Какое количество км до финиша? '))
cnt = 1
print(f'{cnt}-й день: {a}км')
while a < b:
    a += a*0.1
    cnt += 1
    print(f'{cnt}-й день: {a:.2f}км')