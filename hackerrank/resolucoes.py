names = []
N = int(input().strip())
for a0 in range(N):
    firstName, emailID = input().strip().split(' ')
    if '@gmail.com' in emailID:
        names.append(firstName)
print(*sorted(names), sep='\n')