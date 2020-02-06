n = int(input())

arr = list(map(int, input().rstrip().split()))

for i in range(n, 0, -1):
    print(arr[i-1])