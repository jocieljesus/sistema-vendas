import os
import time


def vizualizar_estoque(estoque_produtos):
    print("-"*50)
    print("  Estoque de Produtos Atual")
    print("-" * 50)
    for chave, valor in estoque_produtos.items():
        print(f"{chave} : {valor}")



def adicionar_item_carrinho(estoque_produto, carrinho):

    vizualizar_estoque(estoque_produto)

    id  = int(input("Digite o id do produto: "))
    if id in estoque_produto:
        qtd = int(input("Qual a quantidade que você gostaria: "))
        if qtd <= estoque_produto[id]["quantidade"]:
            estoque_produto[id]["quantidade"] -= qtd
            carrinho[id] = {
                "nome" : estoque_produto[id]["nome"],
                "quantidade" : qtd,
                "preco" :  estoque_produto[id]["preco"],
                "total" :  qtd * estoque_produto[id]["preco"]
            }
            print(F"{qtd} {estoque_produto[id]["nome"]} foram adicionados ao carrinho")
        else:
            print(f"Estoque Insuficiente. Estoque atual {estoque_produto[id]["quantidade"]}")
    else:
        print("Identificador inexistente")


def vizualizar_carrinho(carrinho):
    subtotal = 0
    print("-"*50)
    print("  Carrinho Atual ")
    print("-" * 50)
    if len(carrinho) == 0:
        print("Carrinho Vazio")
    else:
        for chave, valor in carrinho.items():
            subtotal += valor["total"]
            print(f"{valor["quantidade"]}  { valor["nome"]}  no valor de R${valor["preco"]:.2f} (und)  ->  total {valor["total"]:.2f}")
    print(f"Subtotal =  {subtotal:.2f}")
    return  subtotal



def finalizar_compra(carrinho, estoque):
    subtotal = 0
    desconto = 0
    for chave, valor in carrinho.items():
        subtotal += valor["total"]
    cupom = input("Você possui um cupom de desconto? ")
    if cupom == "DEV10":
        desconto = subtotal*0.1
    elif cupom == "DEV20":
        desconto = subtotal*0.2
    else:
        print("Cupom Inválido ou Expirado")

    print(f"Valor total sem desconto: R${subtotal:.2f}")
    print(f"Valor do desconto: R${desconto:.2f}")
    print(f"Valor total a pagar: R${subtotal-desconto:.2f}")

    pagamento = input("Deseja finalizar o pagamento ? (s/n)")
    if pagamento == "s":
        print("Processando pagamento.")
        for i in range(5):
            print("."*i)
            time.sleep(1)
            os.system("cls")
        print("Compra Realizada com Sucesso!")
    else:
        for k,v in carrinho.items():
            estoque[k]["quantidade"] += v["quantidade"]
        print("Compra Cancelada!")


def menu ():
    print("""
    BEM VINDO A TN STORE
    
    [1] Visualizar Estoque
    [2] Adicionar Item ao Carrinho
    [3] Visualizar Carrinho
    [4] Finalizar Compra
    [0] Sair do Sistema 
    
    """)

