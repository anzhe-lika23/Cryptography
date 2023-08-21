import random
import math

print(f"{'='*50}\n          АЛГОРИТМ ДІФФІ-ХЕЛЛМАНА\n{'='*50}")


def is_prime(num):
    """Перевіряє, чи є число простим."""
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def generate_prime():
    """Генерує велике просте число."""
    while True:
        num = random.randint(1000, 10000000000)  # Задаємо діапазон для генерації великого числа
        if is_prime(num):
            return num


def diffie_hellman():
    """Моделює обмін ключами між абонентами за схемою Діффі-Хеллмана."""
    # Генеруємо великі прості числа
    p = generate_prime()
    g = generate_prime()
    print("Публічні параметри:")
    print(f"p = {p}")
    print(f"g = {g}\n")

    # Вибираємо випадкове приватне число для кожного абонента
    private_key_a = random.randint(1, p - 1)
    private_key_b = random.randint(1, p - 1)
    print("Приватні ключі абонентів:")
    print(f"Приватний ключ a: {private_key_a}")
    print(f"Приватний ключ b: {private_key_b}\n")

    # Обчислюємо відкритий ключ для кожного абонента
    public_key_a = pow(g, private_key_a, p)
    public_key_b = pow(g, private_key_b, p)
    print("Публічні ключі абонентів:")
    print(f"Публічний ключ A: {public_key_a}")
    print(f"Публічний ключ B: {public_key_b}\n")

    secret_key_a = pow(public_key_b, private_key_a, p)
    secret_key_b = pow(public_key_a, private_key_b, p)
    print("Загальні секретні ключі:")
    print(f"Загальний секретний ключ для a: {secret_key_a}")
    print(f"Загальний секретний ключ для b: {secret_key_b}\n")

    # Перевіряємо, чи спільні секретні ключі співпадають
    if secret_key_a == secret_key_b:
        print("Загальні ключі співпадають:", secret_key_a)
    else:
        print("Помилка: загальні ключі не співпадають")


diffie_hellman()
