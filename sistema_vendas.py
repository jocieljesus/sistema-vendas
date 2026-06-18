from funcoes_vendas import *

estoque = {
    1 : {
        "nome":"Camisa",
        "preco": 79.90,
        "quantidade": 17
         },
    2 :  {
        "nome":"Tenis",
        "preco": 299.90,
        "quantidade": 22
         },
    3 :  {
        "nome":"Bermuda",
        "preco": 109.90,
        "quantidade": 14
         }
}
carrinho = {}

while True:
    menu()

    opcao = int(input(" Escolha o que deseja fazer: "))

    match opcao:
        case 1:
            vizualizar_estoque(estoque)
        case 2:
            adicionar_item_carrinho(estoque, carrinho)
        case 3:
            vizualizar_carrinho(carrinho)
        case 4:
            finalizar_compra(carrinho, estoque)
        case 0:
            print(" Saindo do Sistema")
            break
        case _:
            print("Opção Inválida.😢Tente Novamente!")



