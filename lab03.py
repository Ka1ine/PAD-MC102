nivel = int(input())
ataque = int(input())
defesa = int(input())
moedas = int(input())
moeda_teste = 0
moedas_finais = 0
missao = 0

if ataque >= 30 and defesa >= 10:
    moedas_finais = moedas + 25
    missao = 1

if moedas >= 30 and defesa >= 30:
    moeda_teste = moedas + 10
    if moeda_teste > moedas_finais:
        moedas_finais = moeda_teste
        missao = 2

if nivel >= 3:
    if ataque < defesa and moedas >= 50:
        moeda_teste = moedas + 50
        if moeda_teste > moedas_finais:
            moedas_finais = moeda_teste
            missao = 3

    if moedas >= 20:
        moeda_teste = moedas + 20
        if moeda_teste > moedas_finais:
            moedas_finais = moeda_teste
            missao = 4
    if ataque >= 20 and defesa >= 30:
        moeda_teste = moedas + 40
        if moeda_teste > moedas_finais:
            moedas_finais = moeda_teste
            missao = 4

if nivel >= 5:
    if ataque >= 40 and defesa >= 50 and moedas >= 50:
        moeda_teste = moedas + 80
        if moeda_teste > moedas_finais:
            moedas_finais = moeda_teste
            missao = 5

    if defesa >= 50:
        moeda_teste = moedas + 30
        if moeda_teste > moedas_finais:
            moedas_finais = moeda_teste
            missao = 6

    if defesa >= 50 and ataque >= 50:
        moeda_teste = moedas + 60
        if moeda_teste > moedas_finais:
            moedas_finais = moeda_teste
            missao = 6

print(f"missão escolhida: {missao}")
if missao == 0:
    print(f"moedas de ouro: {moedas}")
else:
    print(f"moedas de ouro: {moedas_finais}")
