def sort(numbers):
    numSwaps = 0
    for i in range(len(numbers)-1,0,-1):
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp
                numSwaps += 1

    print(f'Array sorted in {numSwaps} swaps')
    print(f'First Element: {numbers[0]}')
    print(f'Last Element: {numbers[-1]}')


numbers = [5, 3, 8, 6, 7, 2]
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [1, 2, 3]
numbers3 = [3, 2, 1]
sort(numbers)
sort(numbers1)
sort(numbers2)
sort(numbers3)

