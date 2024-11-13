
def add_chars(char_list, start, stop):
    for char_num in range(start, stop + 1):
        char_list.append(chr(char_num))
    return char_list

def encrypt(password, cipher_code):
    allowed_chars = list()
    allowed_chars = add_chars(allowed_chars, 48, 57)
    allowed_chars = add_chars(allowed_chars, 65, 90)
    allowed_chars = add_chars(allowed_chars, 97, 122)
    
    encrypted_list = list()
    for letter in password:
        if letter in allowed_chars:
            letter_index = allowed_chars.index(letter)
            encrypted_unicode = letter_index + cipher_code
            encrypted_unicode %= len(allowed_chars)
            encrypted_list.append(allowed_chars[encrypted_unicode])
    encrypted_password = "".join(encrypted_list)
    return encrypted_password








