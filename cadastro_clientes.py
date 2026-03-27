clientes = []

def cadastrar():
    nome = input("Digite o seu nome: ")
    idade = input("Digite a sua idade: ")
    email = input("Digite o seu email: ")

    cliente = {
        "nome": nome,
        "idade": idade,
        "email": email
    }

    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")


def listar():
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return

    for i, cliente in enumerate(clientes):
        print(f"{i+1} - {cliente['nome']} | {cliente['idade']} | {cliente['email']}")
    print()


def buscar():
    nome_busca = input("Digite seu nome para buscar: ")

    for cliente in clientes:
        if cliente["nome"].lower() == nome_busca.lower():
            print(f"Encontrado: {cliente}")
            return

    print("Cliente não encontrado.")


while True:
    print("=== MENU ===")
    print("1 - Cadastrar cliente")
    print("2 - Listar cliente")
    print("3 - Buscar cliente")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        buscar()
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")