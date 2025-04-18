import threading
import time

pedidos = {}
id_pedido = 1
LIMITE_PEDIDOS = 5

def exibir_detalhes_pedido(id, pedido):
    #Exibe os detalhes de um pedido
    print(f"Pedido {id}: {pedido['sabor']} ({pedido['tamanho']}) - {pedido['status']}")

def fazer_pedido():
    #Cria um novo pedido
    global id_pedido
    nome_cliente = input("Nome: ")
    endereco = input("Endereço: ")
    sabor = input("Sabor: ")
    tamanho = input("Tamanho (P, M, G): ")
    pedidos[id_pedido] = {"nome": nome_cliente, "endereco": endereco, "sabor": sabor, "tamanho": tamanho, "status": "Em preparo"}
    print(f"Pedido {id_pedido} criado!")
    id_pedido += 1

def processar_pedido(id_pedido):
    #Simula o processamento de um pedido
    print(f"Processando pedido {id_pedido}...")
    time.sleep(5)
    pedidos[id_pedido]["status"] = "Pronto para entrega"
    print(f"Pedido {id_pedido} pronto!")

def iniciar_pedido(id_pedido):
    #Inicia o processamento de um pedido em uma thread
    threading.Thread(target=processar_pedido, args=(id_pedido,)).start()

def acompanhar_pedidos():
    #Exibe o status dos pedidos
    print("\n--- Status dos Pedidos ---")
    for id, pedido in pedidos.items():
        exibir_detalhes_pedido(id, pedido)

def entregar_pedido():
    #Simula a entrega de um pedido
    if not pedidos:
        print("Sem pedidos para entregar.")
        return
    acompanhar_pedidos()
    try:
        id_entrega = int(input("ID do pedido para entregar: "))
        if id_entrega in pedidos:
            pedidos.pop(id_entrega)
            print(f"Pedido {id_entrega} entregue!")
        else:
            print("ID inválido.")
    except ValueError:
        print("Entrada inválida.")

def exibir_menu():
    #Exibe o menu
    menu = {
        "1": "Fazer pedido",
        "2": "Visualizar fila",
        "3": "Entregar pedido",
        "4": "Sair"
    }
    print("\n--- Pizzaria Delivery ---")
    for opcao, descricao in menu.items():
        print(f"{opcao}. {descricao}")

def main():
    #Função principal
    while True:
        exibir_menu()
        opcao = input("Escolha: ")
        if opcao == "1":
            fazer_pedido()
            if len(pedidos) <= LIMITE_PEDIDOS:
                iniciar_pedido(id_pedido - 1)
            else:
                print("Limite de pedidos atingido!")
        elif opcao == "2":
            acompanhar_pedidos()
        elif opcao == "3":
            entregar_pedido()
        elif opcao == "4":
            break
        else:
            print("Opção inválida!")

if _name_ == "_main_":
    main()
#CODIGO-REFATORADO