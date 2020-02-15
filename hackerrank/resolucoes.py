def miniMaxSum(arr):
    total = sum(arr)
    totalDiminuido = []
    for i in arr:
        totalDiminuido.append(total - i)
    print(f'{min(totalDiminuido)} {max(totalDiminuido)}')

arr = list(map(int, input().rstrip().split()))

miniMaxSum(arr)
