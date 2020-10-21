def next_letter(leter, step):
    return chr((ord(leter) - 97 + step) % 26 + 97)




def encript(text, step):
    encrypted_text = ""
    for letter in text:
        encrypted_text += next_letter(leter=letter, step=step)
    return encrypted_text