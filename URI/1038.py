pedido = input().split(" ")

preco_cardapio = [0, 4.00, 4.50, 5.00, 2.00, 1.50]

total = preco_cardapio[int(pedido[0])] * int(pedido[1])

print("Total: R$ %0.2f"%total)