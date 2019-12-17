def fatorial(num = 1, show = True):
    for i in range(1, num):
        num *= i
    print(num)


fatorial(0, True)