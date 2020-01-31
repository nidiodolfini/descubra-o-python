n = 3
def diagonalDifference(arr):
    ans = 0
    for i in range(n):
        ans += arr[i][i] - arr[i][n - i - 1]
    return abs(ans)
arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
print(diagonalDifference(arr))

# for i in range(n, 0, -1):
#     print(i)