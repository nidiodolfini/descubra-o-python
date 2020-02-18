#You have to return the digits of this number within an array in reverse order.

def digitize(n):
    return [int(s) for s in str(n)][::-1]

print(digitize(35231))