X1 = int(input())
Y1 = int(input())
W1 = int(input())
Z1 = int(input())
X2 = int(input())
Y2 = int(input())
W2 = int(input())
Z2 = int(input())

horas1 = X1 + (Y1/60)
tempo1 = W1/Z1
soma1 = horas1 + tempo1

horas2 = X2 + (Y2/60)
tempo2 = W2/Z2
soma2 = horas2 + tempo2

if soma1 > horas2:
    print(False)
elif soma2 > 11:
    print(False)
else:
    print(True)



