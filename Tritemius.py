# Шифр Трітеміуса

class Tritemius:

    def __init__(self, language, message, a_coefficient, b_coefficient):
        self.language = language
        self.message = message
        self.a = a_coefficient
        self.b = b_coefficient
        self.uk_alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя `,.!?:'
        self.en_alphabet = 'abcdefghigklmnopqrstwxyz .,!?:'

    def encryption(self, text):
        # k = a * p + b
        text = text.lower()
        position = 1
        encryption_text = ''
        for letter in text:
            step = self.a * position + self.b
            if self.language == 'uk':
                cipher_letter = (self.uk_alphabet.index(letter) + step) % len(self.uk_alphabet)
                encryption_text += self.uk_alphabet[cipher_letter]
                position += 1
            elif self.language == 'en':
                cipher_letter = (self.en_alphabet.index(letter) + step) % len(self.en_alphabet)
                encryption_text += self.en_alphabet[cipher_letter]
                position += 1
            else:
                print("Введіть правильно мову!")
        return encryption_text

    def decryption(self, text):
        text = text.lower()
        position = 1
        decryption_text = ''
        for letter in text:
            step = self.a * position + self.b
            if self.language == 'uk':
                cipher_letter = (self.uk_alphabet.index(letter) - step) % len(self.uk_alphabet)
                decryption_text += self.uk_alphabet[cipher_letter]
                position += 1
            else:
                cipher_letter = (self.en_alphabet.index(letter) - step) % len(self.en_alphabet)
                decryption_text += self.en_alphabet[cipher_letter]
                position += 1
        return decryption_text


print(str("=" * 30) + "\n       ШИФР ТРІТЄМІУСА\n" + str("=" * 30))
input_language = input("1. Введіть мову uk/en -> ")
message = input("2. Введіть повідомлення -> ")
a = int(input("3. Введіть число, a = "))
b = int(input("4. Введіть число, b = "))
user1 = Tritemius(input_language, message, a, b)
print(f'{"-"*30}\n* Зашифроване повідомлення: {user1.encryption(message)}')
print(f'* Розшифроване повідомлення: {user1.decryption(user1.encryption(message))}')

