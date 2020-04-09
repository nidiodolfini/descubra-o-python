# cafes = []
# while True:
#     cafe = input().split(" ")
#     if cafe[0] == 'MEOW':
#         cafeteira = cafes[0][0]
#         maior = int(cafes[0][1])
#         for i in cafes:
#             if int(i[1]) > maior:
#                 cafeteira = i[0]
#         print(cafeteira)
#         break
#     cafes.append(cafe.copy())
x = 1
y = 2
def swap():
    global x
    global y
    temp = x
    x = y
    y = temp
    print(x,y)
print(x,y)
swap()
print(x,y)

