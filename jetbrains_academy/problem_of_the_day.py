guest = []
dot = ''
while dot != '.':
    dot = input()
    if dot == '.':
        break
    guest.append(dot)

print(guest)
print(len(guest))