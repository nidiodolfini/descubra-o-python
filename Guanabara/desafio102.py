def fatorial(num=1, show=True):
    if show:
        fat = num
        for i in range(1, num + 1):
            if fat != 1:
                print(f'{fat}', end=' x ')
            else:
                print(f'{fat}', end=' = ')

            fat -= 1
    for i in range(1, num):
        num *= i
    print(f'{num}')


fatorial(5, True)
