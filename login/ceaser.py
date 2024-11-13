def get_allowed_chars(start, stop):
    allowed_chars = list()
    for char in range(start, stop + 1):
        character = chr(char)
        allowed_chars.append(character)

    return allowed_chars

def encrypt(char_list, password):
    encrypted = ""
    for letter in password:
        current = char_list.index(letter)
        current = current + 1
        if current >= len(char_list):
            current = current % len(char_list)
        new_letter = char_list[current]
        encrypted = encrypted + new_letter
    return encrypted

list_chars = get_allowed_chars(48, 57)
list_chars = list_chars + get_allowed_chars(65, 90)
list_chars = list_chars + get_allowed_chars(97, 122)

password = encrypt(list_chars, "z")
print(password)