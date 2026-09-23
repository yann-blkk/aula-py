def calcularTotalGols(gols):
    return sum(gols)


def calcularMediaGols(gols):
    return sum(gols) / len(gols)


def encontrarArtilheiros(jogadores, gols):
    maior = max(gols)
    artilheiros = []

    for i in range(len(gols)):
        if gols[i] == maior:
            artilheiros.append(jogadores[i])

    return artilheiros


def mostrarRelatorio(jogadores, gols):
    total = calcularTotalGols(gols)
    media = calcularMediaGols(gols)
    artilheiros = encontrarArtilheiros(jogadores, gols)

    print("\n--- RELATÓRIO ---")

    for i in range(len(jogadores)):
        print(jogadores[i], "-", gols[i], "gols")

    print("Total de gols:", total)
    print("Média de gols:", round(media, 2))

    print("\nJogadores acima da média:")
    for i in range(len(jogadores)):
        if gols[i] > media:
            print(jogadores[i])

    print("\nArtilheiro(s):", ", ".join(artilheiros))

    if len(artilheiros) > 1:
        print("Houve empate na artilharia.")
    else:
        print("Não houve empate na artilharia.")


jogadores = ["Lucas", "Gabriel", "Rafael", "Pedro", "André"]
gols = [4, 7, 2, 7, 5]

mostrarRelatorio(jogadores, gols)