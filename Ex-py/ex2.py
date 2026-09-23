def registrarTentativas():
    tentativas = []

    for i in range(10):
        while True:
            try:
                valor = int(input(
                    f"Digite o resultado da tentativa {i + 1} (0, 1, 2 ou 3): "
                ))

                if valor in [0, 1, 2, 3]:
                    tentativas.append(valor)
                    break
                else:
                    print("Valor inválido. Digite apenas 0, 1, 2 ou 3.")

            except ValueError:
                print("Digite apenas números inteiros.")

    return tentativas


def calcularPontuacao(tentativas):
    return sum(tentativas)


def calcularAproveitamento(tentativas):
    convertidos = 0

    for tentativa in tentativas:
        if tentativa > 0:
            convertidos += 1

    return (convertidos / len(tentativas)) * 100


def encontrarCestaMaisFrequente(tentativas):
    maior_quantidade = 0
    cesta_frequente = []

    for valor in [0, 1, 2, 3]:
        quantidade = tentativas.count(valor)

        if quantidade > maior_quantidade:
            maior_quantidade = quantidade
            cesta_frequente = [valor]

        elif quantidade == maior_quantidade:
            cesta_frequente.append(valor)

    return cesta_frequente


tentativas = registrarTentativas()

convertidos = 0

for tentativa in tentativas:
    if tentativa > 0:
        convertidos += 1

print("\n--- RESULTADO ---")
print("Tentativas:", tentativas)
print("Pontuação total:", calcularPontuacao(tentativas))
print("Arremessos convertidos:", convertidos)
print("Arremessos errados:", tentativas.count(0))
print("Aproveitamento:", round(calcularAproveitamento(tentativas), 2), "%")

cestas = encontrarCestaMaisFrequente(tentativas)

if len(cestas) == 1:
    print("Tipo de cesta mais frequente:", cestas[0])
else:
    print("Houve empate entre:", cestas)