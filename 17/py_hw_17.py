def check_text_user_input(text):
    if not text.strip():  # Check if text is empty or only whitespace
        return False
    for char in text:
        if not (char.isalpha() or char.isspace()):
            return False
    return True


def check_number_user_input(number):
    if not str(number).strip():  # Check if text is empty or only whitespace
        return False
    for char in str(number):
        if not char.isdigit():
            return False
    return True


while True:
    user_input = input("Text to Caesar encrypt: ")
    if not check_text_user_input(user_input):
        print("\nPlease enter only letters and spaces.\n")
    else:
        break

while True:
    offset = int(input("Offset: "))
    if not check_number_user_input(offset):
        print("\nPlease enter valid numeric value.\n")
    else:
        break


def caesar_encrypt(text, offset):
    output = ""
    for letter in text:
        if letter.isalpha():
            output += chr(ord(letter) + offset)
        else:
            output += letter
    return output


print("\nEncrypted text:\n")
print(caesar_encrypt(user_input, offset))

user_input_2 = input("Text to Caesar decrypt: ")
offset_2 = int(input("Offset:"))


def caesar_decrypt(text, offset):
    return caesar_encrypt(text, -offset)


print("\nDecrypted text:\n")
print(caesar_decrypt(user_input_2, offset_2))
