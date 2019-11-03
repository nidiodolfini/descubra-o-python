vogais = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]

def vogal(caracter):
    for i in vogais:
        if (i == caracter):
            return True
           # break
    return False
