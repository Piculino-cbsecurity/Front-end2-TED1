Alturas = []
Soma = 0
Masculino = 0
Feminino = 0

for i in range(15):
    altura = float(input("Digite a altura: "))
    genero = input("Digite o genero: ").lower()

    Alturas.append(altura)

    if genero == "masculino":
        Soma += altura
        Masculino += 1
    else:
        Feminino += 1

media = int((Soma / Masculino) * 100) / 100

print("Maior altura:", max(Alturas))
print("Menor altura:", min(Alturas))
print("Media dos homens:", media)
print("Quantidade de mulheres:", Feminino)
