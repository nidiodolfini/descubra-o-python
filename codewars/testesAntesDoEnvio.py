def is_divisible(n,x,y):
    if n % x == 0 and n % y == 0:
        return True
    else:
        return False


print(is_divisible(3,3,4))
print(is_divisible(12, 3, 4))
print(is_divisible(8,3,4))
print(is_divisible(48,3,4))

