#Função para guardar os produtos no Estoque.
estoque = []

#Função para limpar a tela.
def limpar_tela ():
    print("\033c", end ="")

#Criação do menu.
def mostrar_menu():
    while True: 
        limpar_tela()
        print("===== Menu =====")
        print("1 = Adicionar produto")
        print("2 = Atualizar produto")
        print("3 = Excluir produto")
        print("4 = Visualizar produto")
        print("5 = Sair do sistema")
        print("===================")

        opcao =input("Escolha uma opção: ")
         
        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            atualizar_produto()
        elif opcao == "3":
            excluir_produto()
        elif opcao == "4":
            visualizar_produto()
        elif opcao == "5":
            limpar_tela()
            print("===== Saindo do sistema =====")
            break
        else:
            print("Opção inválida. Tente novamente.")
            input("Pressione Enter para continuar.")


# Adicionar Produto ao Estoque.
def adicionar_produto():
    limpar_tela()
    print("===== Adicionar Produto =====")
    nome = input("Nome do Produto:  ")
    preco = float(input("Preço do Produto:  "))
    quantidade = int(input("Quantidade no Estoque:  "))

    produto = {
        'nome':nome ,
        'preço':preco ,
        'quantidade':quantidade
    }

    estoque.append(produto)
    print(f"✅ Produto '{nome}' adicionado com sucesso!")
    input("Pressione Enter para continuar... ")


# Atualizar produtos no estoque.
def atualizar_produto():
    limpar_tela()
    print("===== Atualizar Produto ===== \n")
    nome = input("Nome do produto a atualizar: ")
    
    for produto in estoque:
        if produto["nome"] == nome:
            while True:           
                try:
                    novo_preco = float(input("Novo preço do produto: R$ "))
                    break
                except ValueError:
                    print("❌ O preço deve ser um numero decimal...")
                    print("=========================================")
            while True:
                try:
                    nova_quantidade = int(input("Nova quantidade no estoque: "))
                    break
                except ValueError:
                    print("❌ A quantidade deve ser um numero inteiro...")
                    print("==============================================")
            
            produto["preço"] = novo_preco
            produto["quantidade"] = nova_quantidade

            print("✅ Produto atualizado com sucesso!")
            break
    else:
        print("❌ Produto não encontrado.")
    
        input("Pressione Enter para continuar...")


# Função para Excluir produtos do estoque.
def excluir_produto():
    limpar_tela()
    print("===== Excluir Produto =====\n")

    nome = input("Digite o nome do Produto a ser Excluido:  ")
    encontrado = False
    for produto in estoque:
        if produto["nome"] == nome:
                estoque.remove(produto)
                print(f"✅ Produto '{nome}' excluido com sucesso.")
                encontrado = True
                break
    if not encontrado:
            print(" ❌ Produto não Encontrado.")
    input("\nPressione Enter para continuar...")


#Função para visualizar o Estoque.
def visualizar_produto():
    limpar_tela ()
    print("===== Visualizar Estoque =====")
    if not estoque:
        print("Estoque vazio.")
    else:
        print("===== Produtos no Estoque =====")
        for produto in estoque:
            print("==========================================================")

            print(f". Nome: {produto['nome']}, Preço: R${produto['preço']:.2f}, Quantidade: {produto['quantidade']}")
    print("===========================================================")
    input("Pressione Enter para continuar...")

mostrar_menu()