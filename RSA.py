import random
import math


def is_prime(number):
    """Перевіряє, чи є число простим."""
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def generate_prime():
    """Генерує велике просте число."""
    while True:
        num = random.randint(100, 100000)  # Задаємо діапазон для генерації великого числа
        if is_prime(num):
            return num


def gcd(num1, num2):
    """Функція для знаходження найбільшого спільного дільника"""
    while num2:
        num1, num2 = num2, num1 % num2
    return num1


p = generate_prime()
q = generate_prime()
n = p * q
euler = (p - 1) * (q - 1)


def mod_inverse(a, mod):
    """Функція для знаходження оберненого за модулем числа"""

    def extended_gcd(num1, num2):
        """Функція для розширеного алгоритму Евкліда"""
        if num2 == 0:
            return num1, 1, 0
        else:
            g, x, y = extended_gcd(num2, num1 % num2)
            return g, y, x - (num1 // num2) * y

    nod, value_x, value_y = extended_gcd(a, mod)
    if nod != 1:
        raise ValueError("Оберненого за модулем числа не існує")
    return value_x % mod if value_x > 0 else value_x + mod


# Вибір випадкового числа e, такого, що 1 < e <= eluer і gcd(e, euler) = 1
def finding_e(euler_fun):
    """Функція для знаходження чисел e"""
    while True:
        public = random.randint(2, euler_fun - 1)
        if gcd(public, euler_fun) == 1:
            break
    return public


# Обчислюємо значення секретного ключа d, що задовольняє умові e * d = 1 (mod (euler))
def finding_d(public, euler_fun):
    secret = mod_inverse(public, euler_fun)
    return secret


def encrypt_message(sms, public):
    list_index = []
    for letter in sms:
        list_index.append(ord(letter))
    list_encrypt = []
    for m in list_index:
        list_encrypt.append(pow(m, public, n))
    return list_encrypt


def decryption_message(encrypt_sms, secret):
    list_decrypt = []
    for c in encrypt_sms:
        list_decrypt.append(pow(c, secret, n))
    list_letter = []
    for element in list_decrypt:
        list_letter.append(chr(element))
    return list_letter


print(f"{'=' * 50}\n{' ' * 23}RSA\n{'=' * 50}")
print(f"Просте число: p = {p}")
print(f"Просте число: q = {q}\n{'-' * 50}")
print(f"Добуток p * q: n = {n}")
print(f"Функція Ейлера: f(n) = {euler}\n{'-' * 50}")
e = finding_e(euler)
print(f"Значення е = {e}")
d = finding_d(e, euler)
print(f"Значення d = {d}\n{'-' * 50}")
public_key = n, e
private_key = n, d
print(f"Публічний ключ: {public_key}")
print(f"Приватний ключ: {private_key}\n{'-' * 50}")
message_encrypt = encrypt_message("Spring", e)
print(f"Зашифроване повідомлення -> {' '.join(str(el) for el in message_encrypt)}")
message_decrypt = decryption_message(message_encrypt, d)
print(f"Розшифроване повідомлення -> {' '.join(str(el) for el in message_decrypt)}\n{'-' * 50}")
