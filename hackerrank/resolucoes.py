# def jumpingOnClouds(c):
#     jumps = 0
#     for i in range(n):
#         if c[i] == 0:
#             jumps += 1
#
#     return jumps - 1


def jumpingOnClouds(c):
    count=0
    jump=0
    for i in c:
        if i==0:
            count+=1
        else:
            jump=jump+count//2+1
            count=0
    if count>1:
        jump=jump+count//2
    return jump

n = int(input())

c = list(map(int, input().rstrip().split()))
result = jumpingOnClouds(c)

print(result)
