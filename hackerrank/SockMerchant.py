n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

def sockMerchant(n, ar):
    count = 0
    ar.sort()
    ar.append('#')
    i = 0
    print(ar)
    while i<n:
        if ar[i]==ar[i+1]:
            count = count+1
            i+=2
        else:
            i+=1
    return count


print(sockMerchant(n, ar))