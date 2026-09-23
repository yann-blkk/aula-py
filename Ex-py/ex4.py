assentos = [
    ["L", "L", "L", "L", "L", "L"],
    ["L", "L", "L", "L", "L", "L"],
    ["L", "L", "L", "L", "L", "L"],
    ["L", "L", "L", "L", "L", "L"],
    ["L", "L", "L", "L", "L", "L"]
]

colunas = ["A", "B", "C", "D", "E", "F"]


def mostrarAssentos():
    print("\n    A B C D E F")

    for i in range(5):
        print(i + 1, " ", end="")

        for j in range(6):
            print(assentos[i][j], end=" ")

        print()


def validarAssento(assento):
    if len(assento) != 2:
        return False

    if not assento[0].isdigit():
        return False

    fileira = int(assento[0])
    coluna = assento[1].upper()

    if fileira < 1 or fileira > 5:
        return False

    if coluna not in colunas:
        return False

    return True


def verificarDisponibilidade(assento):
    fileira = int(assento[0]) - 1
    coluna = colunas.index(assento[1].upper())

    return assentos[fileira][coluna] == "L"


def calcularPreco(assento):
    fileira = int(assento[0])

    if fileira == 1:
        return "Executiva", 850.00

    elif fileira == 2 or fileira == 3:
        return "Espaço extra", 600.00

    else:
        return "Econômica", 400.00


def comprarAssento():
    assento = input(
        "Digite o assento desejado (ex: 2C): "
    ).upper()

    if not validarAssento(assento):
        print("Assento inválido.")
        return

    if not verificarDisponibilidade(assento):
        print("O assento", assento, "já está ocupado.")
        return

    categoria, preco = calcularPreco(assento)

    print("\nAssento:", assento)
    print("Categoria:", categoria)
    print(f"Valor: R$ {preco:.2f}")

    confirmacao = input("Confirmar compra? (S/N): ").upper()

    if confirmacao == "S":
        fileira = int(assento[0]) - 1
        coluna = colunas.index(assento[1])

        assentos[fileira][coluna] = "O"

        print("Compra realizada com sucesso.")
        print("O assento", assento, "agora está indisponível.")

    else:
        print("Compra cancelada.")


def consultarAssento():
    assento = input("Digite o assento: ").upper()

    if not validarAssento(assento):
        print("Assento inválido.")
        return

    if verificarDisponibilidade(assento):
        print("O assento", assento, "está livre.")
    else:
        print("O assento", assento, "está ocupado.")


def mostrarResumo():
    livres = 0
    ocupados = 0
    faturamento = 0

    vendas = {
        "Executiva": 0,
        "Espaço extra": 0,
        "Econômica": 0
    }

    for i in range(5):
        for j in range(6):

            if assentos[i][j] == "L":
                livres += 1

            else:
                ocupados += 1

                assento = str(i + 1) + colunas[j]
                categoria, preco = calcularPreco(assento)

                faturamento += preco
                vendas[categoria] += 1

    percentual = (ocupados / 30) * 100

    print("\n--- RESUMO DO VOO ---")
    print("Assentos livres:", livres)
    print("Assentos ocupados:", ocupados)
    print("Percentual de ocupação:", round(percentual, 2), "%")
    print(f"Faturamento total: R$ {faturamento:.2f}")

    print("\nVendas por categoria:")
    print("Executiva:", vendas["Executiva"])
    print("Espaço extra:", vendas["Espaço extra"])
    print("Econômica:", vendas["Econômica"])


while True:
    print("\n--- MENU ---")
    print("1 - Visualizar assentos")
    print("2 - Comprar assento")
    print("3 - Consultar assento")
    print("4 - Mostrar resumo do voo")
    print("5 - Encerrar")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        mostrarAssentos()

    elif opcao == "2":
        comprarAssento()

    elif opcao == "3":
        consultarAssento()

    elif opcao == "4":
        mostrarResumo()

    elif opcao == "5":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")