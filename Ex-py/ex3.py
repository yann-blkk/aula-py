nomes = ["Dipirona", "Paracetamol", "Loratadina", "Ibuprofeno", "Amoxicilina"]
precos = [12.50, 9.90, 18.75, 15.00, 25.00]
estoques = [20, 15, 8, 4, 2]


def listarMedicamentos():
    print("\n--- MEDICAMENTOS ---")

    for i in range(len(nomes)):
        print(
            i + 1, "-",
            nomes[i],
            "| R$", f"{precos[i]:.2f}",
            "| Estoque:", estoques[i]
        )


def pesquisarMedicamento():
    nome = input("Digite o nome do medicamento: ")

    for i in range(len(nomes)):
        if nomes[i].lower() == nome.lower():
            print("\nMedicamento:", nomes[i])
            print("Preço: R$", f"{precos[i]:.2f}")
            print("Estoque:", estoques[i])
            return

    print("Medicamento não encontrado.")


def registrarVenda():
    nome = input("Digite o nome do medicamento: ")

    for i in range(len(nomes)):
        if nomes[i].lower() == nome.lower():

            while True:
                try:
                    quantidade = int(input("Digite a quantidade: "))

                    if quantidade <= 0:
                        print("A quantidade deve ser maior que zero.")
                    else:
                        break

                except ValueError:
                    print("Digite uma quantidade válida.")

            if quantidade > estoques[i]:
                print("Estoque insuficiente.")
            else:
                estoques[i] -= quantidade
                print("Venda realizada com sucesso.")

            return

    print("Medicamento não encontrado.")


def reporEstoque():
    nome = input("Digite o nome do medicamento: ")

    for i in range(len(nomes)):
        if nomes[i].lower() == nome.lower():

            while True:
                try:
                    quantidade = int(
                        input("Digite a quantidade para reposição: ")
                    )

                    if quantidade <= 0:
                        print("A quantidade deve ser maior que zero.")
                    else:
                        break

                except ValueError:
                    print("Digite uma quantidade válida.")

            estoques[i] += quantidade
            print("Estoque atualizado com sucesso.")
            return

    print("Medicamento não encontrado.")


def verificarEstoqueBaixo():
    print("\n--- ESTOQUE BAIXO ---")

    encontrou = False

    for i in range(len(nomes)):
        if estoques[i] < 5:
            print(nomes[i], "-", estoques[i], "unidades")
            encontrou = True

    if not encontrou:
        print("Nenhum medicamento com estoque baixo.")


while True:
    print("\n--- MENU ---")
    print("1 - Listar medicamentos")
    print("2 - Pesquisar medicamento")
    print("3 - Registrar venda")
    print("4 - Repor estoque")
    print("5 - Mostrar estoque baixo")
    print("6 - Encerrar")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        listarMedicamentos()

    elif opcao == "2":
        pesquisarMedicamento()

    elif opcao == "3":
        registrarVenda()

    elif opcao == "4":
        reporEstoque()

    elif opcao == "5":
        verificarEstoqueBaixo()

    elif opcao == "6":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")