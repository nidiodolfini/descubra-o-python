def utopianTree(n):
    # tree = 1
    # for i in range(n+1):
    #     if n == 0:
    #         break
    #     elif i % 2 == 0 and i > 1:
    #         tree += 1
    #     elif (i % 3 == 0 and n >= 1) or (i % 5 == 0):
    #         tree = tree * 2
    # return tree
    res = 1
    for i in range(n):
        res = res * 2 if i % 2 == 0 else res + 1
    return res

print(utopianTree(9))
print(utopianTree(7))
print(utopianTree(10))
print(utopianTree(8))
