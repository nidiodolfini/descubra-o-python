def camelcase(s):
    contWord = 1
    for i in s:
        if i.isupper():
            contWord += 1
    print(contWord)


camelcase('saveChangesInTheEditor')
