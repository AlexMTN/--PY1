import random


def get_random_password(n=8) -> str:
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    password = ''.join(random.sample(chars, n))
    return password
    ...  # TODO написать функцию генерации случайных паролей


print(get_random_password())