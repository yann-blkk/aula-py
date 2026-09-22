jogadores = ["Lucas", "Gabriel","Rafael", "Pedro", "André"]
gols = [4, 7, 2, 7, 5]

def registro():
    for nome in jogadores:
       return print(nome)
    registro()

def calcularTotalGols():
    somar = 0
    for gol in gols:
        somar = somar + 1
        return(somar)
    calcularTotalGols()

