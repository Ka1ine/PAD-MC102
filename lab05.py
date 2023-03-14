X1 = input()
X2 = input()
Z = float(input())
VP = float(input())
M = float(input())

lista = []
lista_final = []
cashback = 0
milhas = 0

for i in range(12):
    valor = float(input())
    lista.append(valor)
    cashback += valor / 100
    milhas += int(valor / 5)

cartao2 = float(X1) + VP - cashback
vender_milhas = (milhas // 1000) * Z
cartao3_normal = float(X2) + VP - float(vender_milhas)

if milhas - M < 0:
    cartao3 = cartao3_normal
else:
    sobra = (milhas - M)
    vender = (sobra // 1000) * Z
    if vender > 0:
        cartao3_milhas = float(X2) - vender
    else:
        cartao3_milhas = float(X2)

    if cartao3_normal > cartao3_milhas:
        cartao3 = cartao3_milhas
    else:
        cartao3 = cartao3_normal

lista_final.append(VP)
lista_final.append(cartao2)
lista_final.append(cartao3)

print("Cartão Gratuito: {:.2f}".format(VP))
print("Cartão Cashback: {:.2f}".format(cartao2))
print("Cartão Milhas: {:.2f}".format(cartao3))

for i in range(len(lista_final)):
    if min(lista_final) == lista_final[i]:
        if i == 0:
            print("Cartão Gratuito")
        if i == 1:
            print("Cartão Cashback")
        if i == 2:
            print("Cartão Milhas")
