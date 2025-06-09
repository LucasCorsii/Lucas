from datetime import datetime


def obter_data_hora():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def calcular_valor_liquido(valor_bruto, desconto=0, imposto=0):
    valor_com_desconto = valor_bruto - (valor_bruto * desconto / 100)
    valor_liquido = valor_com_desconto + (valor_com_desconto * imposto / 100)
    return valor_liquido

def calcular_frete(peso, distancia, tipo_frete="fixo"):
    if tipo_frete == "fixo":
        return 50 
    elif tipo_frete == "por_peso":
        return peso * 5  
    elif tipo_frete == "por_distancia":
        return distancia * 0.1  


def criar_produto():
    nome = input("Nome do produto: ")
    descricao = input("Descrição do produto: ")
    preco = float(input("Preço do produto: R$ "))
    peso = float(input("Peso do produto (kg): "))
    categoria = input("Categoria do produto: ")
    data_criacao = obter_data_hora()
    
    return {
        "nome": nome,
        "descricao": descricao,
        "preco": preco,
        "peso": peso,
        "categoria": categoria,
        "data_criacao": data_criacao
    }


produto = criar_produto()
print(f"\nProduto criado com sucesso: {produto['nome']}")
print(f"Descrição: {produto['descricao']}")
print(f"Preço: R$ {produto['preco']}")
print(f"Peso: {produto['peso']} kg")
print(f"Categoria: {produto['categoria']}")
print(f"Data de criação: {produto['data_criacao']}")


valor_bruto = float(input("\nDigite o valor bruto da venda: R$ "))
desconto = float(input("Digite o desconto (%) aplicado: "))
imposto = float(input("Digite o imposto (%) sobre o valor: "))
valor_liquido = calcular_valor_liquido(valor_bruto, desconto, imposto)
print(f"Valor líquido: R$ {valor_liquido}")


peso_produto = float(input("\nDigite o peso do produto (kg): "))
distancia = float(input("Digite a distância de entrega (km): "))
tipo_frete = input("Tipo de frete (fixo/por_peso/por_distancia): ")
frete = calcular_frete(peso_produto, distancia, tipo_frete)
print(f"Valor do frete: R$ {frete}")
