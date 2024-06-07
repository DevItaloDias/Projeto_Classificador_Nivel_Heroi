def cabecalho():
    print("-"*30)
    print("Bem-vindo ao Buscador de Heroi")
    print("-"*30)

def informacoes_xp(xp):
    if xp < 1000:
        nivel = "Ferro"
    elif xp <= 2000:
        nivel = "Bronze"
    elif xp <= 5000:
        nivel = "Prata"
    elif xp <= 7000:
        nivel = "Ouro"
    elif xp <= 8000:
        nivel = "Platina"
    elif xp <= 9000:
        nivel = "Ascendente"
    elif xp <= 10000:
        nivel = "Imortal"
    else:
        nivel = "Radiante"
    return nivel

cabecalho()
print("")
n=1

while(n==1):
    nome=input("Digite o nome do seu Heroi")
    xp=int(input("Digite a quantidade de XP do Herói: "))
    nivel=(informacoes_xp(xp))
    print("O Heroi de nome {} esta no nivel {}".format(nome,nivel))
    print("")
    n=int(input("Deseja saber o nivel de outro Heroi ? 1-SIM / 2-NAO"))
    
    if (n==2):
        break