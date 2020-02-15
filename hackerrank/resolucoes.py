def plusMinus(arr):
    negative = 0
    positive = 0
    zero = 0
    for i in range(n):
        if arr[i] == 0:
            zero += 1
        elif arr[i] < 0:
            negative += 1
        else:
            positive += 1
    print(positive / n)
    print(negative / n)
    print(zero / n)


n = int(input())

arr = list(map(int, input().rstrip().split()))

plusMinus(arr)


