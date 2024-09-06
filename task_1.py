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

pwd = 'text'
res = input('Input password: ')
if res == pwd:
    print('Доступ разрешен')
    my_math = int(input('2 + 2 = '))
    if 2 + 2 == my_math:
        print('Вы в нормальном мире')
    else:
        print('Доступ запрещен')
else:
    print('Доступ запрещен')
print('Работа завершена')
