def get_allowed_chars(start, stop):
    allowed_chars = list()
    for char in range(start, stop + 1):
        character = chr(char)
        allowed_chars.append(character)

    return allowed_chars

def encrypt(password, encryption_num):
    char_list = get_allowed_chars(48, 57)
    char_list = char_list + get_allowed_chars(65, 90)
    char_list = char_list + get_allowed_chars(97, 122)
    encrypted = ""
    for letter in password:
        current = char_list.index(letter)
        current = current + encryption_num
        if current >= len(char_list):
            current = current % len(char_list)
        new_letter = char_list[current]
        encrypted = encrypted + new_letter
    return encrypted



