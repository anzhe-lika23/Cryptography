from spellchecker import SpellChecker

# Шифр Цезаря
print("_" * 10, "Шифр Цезаря", "_" * 10)
language_sms = input("1) Введіть мову повідомлення en/uk/ru -> ")
message = input("2) Введіть повідомлення для шифрування -> ")
shift = int(input("3) Введіть крок зсуву - > "))
encrypted_message = ''
decoded_message = ''
spell = SpellChecker()
min_chr = 0
max_chr = 0x110000


# функція дешифрування повідомлення (метод грубої сили)
def decrypted(sms):
    word_list = []
    for step in range(50):
        decrypted_message = ''
        for symbol in sms:
            if (ord(symbol) - step < min_chr) or (ord(symbol) - step > max_chr):
                decrypted_message += chr(abs(max_chr - abs(ord(symbol) + step)))
            else:
                decrypted_message += chr(ord(symbol) - step)
            word_list.append(decrypted_message)
    words_by_length = []
    for words in word_list:
        if len(words) == len(sms):
            if ' ' in words:
                words = words.split(' ')
                for word in words:
                    if word == spell.correction(word):
                        words_by_length.append(word)
            else:
                if words == spell.correction(words):
                    if words.isalpha():
                        words_by_length.append(words)
    result = []
    for el in words_by_length:
        el = el.lower()
        if el not in result:
            result.append(el)
    print(f"Дешифроване повідомлення: {' '.join(result)}\n{'-' * 35}")


while True:
    print("* Меню:")
    print("Оберіть, що зробити з повідомленням (1-3):")
    numbers = (input("1. Зашифрувати\n2. Розшифрувати\n3. Дешифрування\n4. Вихід\n-> "))

    if numbers == '1':
        # Зашифровуємо повідомлення
        for letter in message:
            encrypted_message += chr(ord(letter) + shift)
        print(f"Зашифроване повідомлення: {encrypted_message}\n{'-' * 35}")

    elif numbers == '2':
        # Розшифровуємо повідомлення
        for letters in encrypted_message:
            decoded_message += chr(ord(letters) - shift)
        print(f"Розшифроване повідомлення: {decoded_message}\n{'-' * 35}")

    elif numbers == '3':
        if language_sms == 'en' or 'ru':
            # Дешифрування повідомлення (метод грубої сили)
            print("Зачекайте...")
            decrypted(encrypted_message)

    else:
        break
