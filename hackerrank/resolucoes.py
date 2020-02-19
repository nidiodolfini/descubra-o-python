n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

numSwaps = 0
for i in range(len(a)-1,0,-1):
    for j in range(i):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            numSwaps += 1
print('Array sorted in',numSwaps,'swaps')
print('First Element:',a[0])
print('Last Element:',a[-1])