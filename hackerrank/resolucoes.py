casesTests = int(input())


def separapalavras(palavra):
    evenIndexed = ''
    oddIndexed = ''
    for i in range(len(palavra)):
        if i % 2 == 0:
            evenIndexed += palavra[i]
        else:
            oddIndexed += palavra[i]
    print(evenIndexed, oddIndexed)


for i in range(casesTests):
    s = input()
    separapalavras(s)
