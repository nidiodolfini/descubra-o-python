vi = []


def resolve_fila():
    # teste = str(vi[0][2])
    # for i in range(int(teste)):
    # print(vi[1])
    print("vi", vi)


def processInput(input):
    "Aqui você deve criar seu algoritmo para processar a entrada e depois retorna-la."
    v = input.split('\n')
    vi.append(v)
    # print('v',vi)

    return input


# Este bloco de código geralmente não precisa ser alterado, a não ser que julgue necessário.
value = input()
while (value):
    print(processInput(value))
    try:
        value = input()
    except EOFError:
        break

resolve_fila()