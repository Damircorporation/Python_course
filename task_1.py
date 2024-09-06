# name = 'Alex'
# age = None
# a = 42
# print(id(a))
# a = 'Hello world'
# print(id(a))

# print(name, age, a, 456, 'text', sep='(=^.^=)')

# res = input('Print your text: ')
# print('Ты написал ', res)

# age = int(input ('Сколько тебе лет? '))


# pwd = 'text'
# res = input('Input password: ')
# if res == pwd:
#     print('Доступ разрешен')
#     my_math = int(input('2 + 2 = '))
#     if 2 + 2 == my_math:
#         print('Вы в нормальном мире')
#     else:
#         print('Но будьте отсторожны')
# else:
#     print('Доступ запрещен')
# print('Работа завершена')


# color = input('твой любимый цвет: ')
# if color == 'красный':
#     print('Любитель яркого')
# elif color == 'зеленый':
#     print('ты не охотник?')
# elif color == 'синий':
#     print('Ха, класика')
# else:
#     print('Тебя не понять')


# color = input('твой любимый цвет: ')
# match color:
#     case 'красный | оранжевый':
#         print('Любитель яркого')
#     case 'зеленый':
#         print('ты не охотник?')
#     case 'синий | черный':
#         print('Ха, класика')
#     case _:
#         print('Тебя не понять')


# num = float(input('Введите число'))
# count = 0
# while count < num:
#     print(count)
#     count+=2

# data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
# for item in data:
#     print(item)

# num = int(input('Введите число: '))
# for i in range(0, num, 2):
#     print(i)

animals = ['cat', 'dog', 'wolf', 'dragon']
for i, animal in enumerate(animals, start=1):
    print(i, animal)

