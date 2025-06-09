class SistemaVendas:
    def __init__(self):
        self.usuarios = []
        self.produtos = []
        self.vendas = []
    # adicionar usuario
    def adicionar_usuario(self):
        nome = input("Digite o nome do vendedor: ")
        usuario = {'id': len(self.usuarios) + 1, 'nome': nome}
        self.usuarios.append(usuario)
        print(f"Usuário '{nome}' adicionado com sucesso!")
# pra edita o usuario
    def editar_usuario(self):
        self.visualizar_usuarios()
        try:
            id_usuario = int(input("Digite o ID do usuário para editar: "))
            usuario = next(u for u in self.usuarios if u['id'] == id_usuario)
            novo_nome = input("Digite o novo nome do vendedor: ")
            usuario['nome'] = novo_nome
            print(f"Usuário {id_usuario} alterado com sucesso!")
        except StopIteration:
            print("Usuário não encontrado!")
# excluir o usuario se caso for excluir
    def excluir_usuario(self):
        self.visualizar_usuarios()
        try:
            id_usuario = int(input("Digite o ID do usuário para excluir: "))
            self.usuarios = [u for u in self.usuarios if u['id'] != id_usuario]
            print(f"Usuário {id_usuario} excluído com sucesso!")
        except ValueError:
            print("ID inválido!")
# ver o usuario
    def visualizar_usuarios(self):
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
        else:
            print("\nLista de Usuários:")
            for usuario in self.usuarios:
                print(f"ID: {usuario['id']} - Nome: {usuario['nome']}")
# dando nome pro usuario adicionar 
    def adicionar_produto(self):
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        produto = {'id': len(self.produtos) + 1, 'nome': nome, 'preco': preco}
        self.produtos.append(produto)
        print(f"Produto '{nome}' adicionado com sucesso!")
    # pedir pro usuario colocar o id 
    def editar_produto(self):
        self.visualizar_produtos()
        try:
            id_produto = int(input("Digite o ID do produto para editar: "))
            produto = next(p for p in self.produtos if p['id'] == id_produto)
            novo_nome = input("Digite o novo nome do produto: ")
            novo_preco = float(input("Digite o novo preço do produto: "))
            produto['nome'] = novo_nome
            produto['preco'] = novo_preco
            print(f"Produto {id_produto} alterado com sucesso!")
        except StopIteration:
            print("Produto não encontrado!")
    #usuario excluir o id
    def excluir_produto(self):
        self.visualizar_produtos()
        try:
            id_produto = int(input("Digite o ID do produto para excluir: "))
            self.produtos = [p for p in self.produtos if p['id'] != id_produto]
            print(f"Produto {id_produto} excluído com sucesso!")
        except ValueError:
            print("ID inválido!")
    # pra visualizar o id do produto
    def visualizar_produtos(self):
        if not self.produtos:
            print("Nenhum produto cadastrado.")
        else:
            print("\nLista de Produtos:")
            for produto in self.produtos:
                print(f"ID: {produto['id']} - Nome: {produto['nome']} - Preço: R${produto['preco']}")
    # funcao de vendas vai dar o id
    def realizar_venda(self):
        self.visualizar_produtos()
        try:
            id_produto = int(input("Digite o ID do produto vendido: "))
            produto = next(p for p in self.produtos if p['id'] == id_produto)
            self.visualizar_usuarios()
            id_usuario = int(input("Digite o ID do vendedor: "))
            usuario = next(u for u in self.usuarios if u['id'] == id_usuario)
            quantidade = int(input("Digite a quantidade vendida: "))
            total = produto['preco'] * quantidade
            venda = {
                'id_venda': len(self.vendas) + 1,
                'usuario': usuario['nome'],
                'produto': produto['nome'],
                'quantidade': quantidade,
                'total': total
            }
            self.vendas.append(venda)
            print(f"Venda registrada: {quantidade} * {produto['nome']} por {usuario['nome']} no total de R${total:.2f}")
        except StopIteration:
            print("Produto ou usuário não encontrado!")

    def visualizar_vendas(self):
        if not self.vendas:
            print("Nenhuma venda registrada.")
        else:
            print("\nLista de Vendas:")
            for venda in self.vendas:
                print(f"ID: {venda['id_venda']} - Produto: {venda['produto']} - Vendedor: {venda['usuario']} - Quantidade: {venda['quantidade']} - Total: R${venda['total']:.2f}")

    def excluir_venda(self):
        self.visualizar_vendas()
        try:
            id_venda = int(input("Digite o ID da venda para excluir: "))
            self.vendas = [v for v in self.vendas if v['id_venda'] != id_venda]
            print(f"Venda {id_venda} excluída com sucesso!")
        except ValueError:
            print("ID inválido!")

    def exibir_menu(self):
        print("\n*** Sistema de Gerenciamento de Vendas ***\n")
        print("1. Gerenciar Usuários")
        print("2. Gerenciar Produtos")
        print("3. Registrar Venda")
        print("4. Excluir Venda")
        print("5. Visualizar Vendas")
        print("6. Sair")

    def executar(self):
        while True:
            self.exibir_menu()
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                self.menu_usuarios()
            elif opcao == "2":
                self.menu_produtos()
            elif opcao == "3":
                self.realizar_venda()
            elif opcao == "4":
                self.excluir_venda()
            elif opcao == "5":
                self.visualizar_vendas()
            elif opcao == "6":
                print("Saindo...")
                break;100
            else:
                print("Opção inválida, tente novamente.")

    def menu_usuarios(self):
        print("\n1. Adicionar Usuário")
        print("2. Editar Usuário")
        print("3. Excluir Usuário")
        print("4. Visualizar Usuários")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            self.adicionar_usuario()
        elif opcao == "2":
            self.editar_usuario()
        elif opcao == "3":
            self.excluir_usuario()
        elif opcao == "4":
            self.visualizar_usuarios()
        else:
            print("Opção inválida!")

    def menu_produtos(self):
        print("\n1. Adicionar Produto")
        print("2. Editar Produto")
        print("3. Excluir Produto")
        print("4. Visualizar Produtos")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            self.adicionar_produto()
        elif opcao == "2":
            self.editar_produto()
        elif opcao == "3":
            self.excluir_produto()
        elif opcao == "4":
            self.visualizar_produtos()
        else:   
            print("Opção inválida!")
    def filtragem_produto(self):
          self.filtragem_produto 
    print =("Filtre o produto!")
sistema = SistemaVendas()
sistema.executar()
        



  
