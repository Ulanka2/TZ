# 1


# def func(*args):
#     day = 0
#     for day1 in args:
#         day += day1

#     return day


# print(func(12, 10, 5))  # 27


# # 2


# def func(*args):
#     day = 0
#     for day1 in args:
#         day += day1

#     return day


# print(func(1, 2, 3, 4, 5, 6, 7, 8))  # 36


# # 3


# def func(*args):
#     d = 0
#     for day1 in args:
#         d += day1
#     return d


# print(func(13, 15,))  # 28


# Задание 2
# def func_slovar(name, **kwargs):
#     print(f'{name}')
#     for inf, user in kwargs.items():
#         print(f'{inf} - {user}')


# func_slovar('John', age=23, gender='male',
#             favorite_sports=['football', 'tennis'])

# 2 вариант
# def func_slovar(name, **kwargs):
#     print(name)
#     print('age - {}'.format(kwargs["age"]))
#     print('gender - {}'.format(kwargs["gender"]))
#     print('favorite_sports - {}'.format(kwargs["favorite_sports"]))


# func_slovar('John', age=23, gender='male',favorite_sports=['football', 'tennis'])


# def func(name, **kwargs):
#     print(f'{name}')
#     for inf, user in kwargs.items():
#         print(f'{inf} - {user}')


# func('Alice', job='Web developer', country_from='Sweden')

# задание 3


# def func(a, b):
#     spisok = [[0]*b for i in range(a)]
#     return spisok


# print(func(3, 4))


# def func(a, b):
#     spisok = [[0]*b for i in range(a)]
#     return spisok


# print(func(6, 2))


# def func(num):
#     gen1 = {new[i]: num for i in range(1, num) if i % 3 == 0 new[i] = False else  i % 2 == 0 new[i] = False else new[i] = True i +=1}
#     return gen1
#     print(gen1)

# func(10)

# def prostoe_chislo(num):
#     new = {}
#     i = 0 
#     for i in range(1, num):
#         if i % 3 == 0: 
#             new[i] = False
#         elif  i % 2 == 0: 
#             new[i] = False
#         else: 
#             new[i] = True
#     print(new)
# prostoe_chislo(10)
