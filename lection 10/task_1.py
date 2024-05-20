# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random


# Здесь пишем код
def generate_random_name():
    random_name = ""

    for i1 in range(2):
        # генерируем 2 слова случайной длины из случайных символов ASCII
        # можно также составить список символов и выбирать из него случайный символ random.choince(lst)
        for i2 in range(random.randint(1, 15)):
            random_name += chr(random.randint(97, 122))
        random_name += " "

    return random_name[:-1]


print(generate_random_name())
