# Шифр Вернама
import secrets  # імпортуємо секретний модуль


print(f"{'=' * 30}\n        Шифр Вернама     \n{'=' * 30}")
language = input("Введіть мову en/uk -> ")
uk_alphabet = 'АаБбВвГгҐґДдЕеЄєЖжЗзИиІіЇїЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщьЮюЯя'
en_alphabet = 'AaEeIiOoUuYyBbCcDdFfGgHhJjKLlMmNnPpQqRrSsTtVvWwXxZz'
message = input("Введіть повідомлення -> ")
string_length = len(message)
key = ''
if language == 'uk':
    key = ''.join(secrets.choice(uk_alphabet) for i in range(string_length))
else:
    key = ''.join(secrets.choice(en_alphabet) for i in range(string_length))
print("Згенерований ключ:", key)


def vernam_encrypt(sms, generated_key):
    sms_ascii = []
    for letter in sms:
        sms_ascii.append(ord(letter))
    key_ascii = []
    for letter in generated_key:
        key_ascii.append(ord(letter))
    encrypted_message = []
    for i in range(len(sms_ascii)):
        encrypted_message.append(sms_ascii[i] ^ key_ascii[i])
    return encrypted_message


def vernam_decrypt(encrypted_sms, generated_key):
    key_ascii = []
    for letter in generated_key:
        key_ascii.append(ord(letter))
    xor_key_text = []
    for el in range(len(encrypted_sms)):
        xor_key_text.append(encrypted_sms[el] ^ key_ascii[el])
    decrypted_message = []
    for element in xor_key_text:
        decrypted_message.append(chr(element))
    result = ''
    for j in decrypted_message:
        result += str(j)
    return result


encrypted_text = vernam_encrypt(message, key)
decrypted_text = vernam_decrypt(encrypted_text, key)

while True:
    print("---Меню---")
    numbers = (input("1. Зашифрувати\n2. Розшифрувати\n3. Вихід\n-> "))

    if numbers == '1':
        # Зашифровуємо повідомлення
        text = ''
        for k in range(len(encrypted_text)):
            text += str(encrypted_text[k]) + ' '
        print(f"Зашифроване повідомлення: {text}\n{'~' * 25}")

    elif numbers == '2':
        # Розшифровуємо повідомлення
        print(f"Розшифроване повідомлення: {decrypted_text}\n{'~' * 25}")

    else:
        break
