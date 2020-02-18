# An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
# Implement a function that determines whether a string that contains only letters 
# is an isogram. Assume the empty string is an isogram. Ignore letter case.

def is_isogram(string):
    cont = 0
    word = string.lower()
    for char in word:
        if word.count(char) > 1:
            cont += 1
    if cont > 1 :
        return False
    else:
        return True

def is_isogram(string):
    return len(string) == len(set(string.lower()))


print(is_isogram("Dermatoglyphics"))
print(is_isogram("aba" ))
print(is_isogram("nidio" ))