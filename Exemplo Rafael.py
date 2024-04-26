escolha = 5
sacola = []
precos = {
    1: 5.00,   # BANANA
    2: 3.00,   # MAÇÃ
    3: 4.00,   # BERGAMOTA
    4: 5.00,   # UVA
    5: 2.50,   # PÃO
    6: 7.00,   # LEITE
    7: 6.90,   # MEL
    8: 10.00,  # SALAME
    9: 9.50,   # QUEIJO
    10: 8.50   # PRESUNTO
}

while True:
    print("""
            ============ MENU ===============
        
        Olá, seja bem vindo ao mercadinho Seu Zé

         (Por favor, digite apenas números: )

        1- Começar uma compra
        
        2- Ir para o carrinho

        3- Sair
        
        """)
    
    while True:
        try:         
            x = int(input("Digite aqui: "))
            
            if x == 1 or x == 2 or x == 3:
                break            
            else:
                print("Opção inválida, por favor tente novamente")
        except ValueError:
            print("Opção inválida, por favor digite um número válido")

    if x == 1:  # MENU do cliente
        while True:
            print("""
                ============ LISTA DE PRODUTOS ===============
            
            Olá cliente, o que deseja?

            Digite o ID do produto que deseja comprar
                  
                  01 - BANANA: R$ 5.00
                  02 - MAÇÃ: R$ 3.00
                  03 - BERGAMOTA: R$ 4.00
                  04 - UVA: R$ 5.00
                  05 - PÃO: R$ 2.50
                  06 - LEITE: R$ 7.00
                  07 - MEL: R$ 6.90
                  08 - SALAME: R$ 10.00
                  09 - QUEIJO: R$ 9.50
                  10 - PRESUNTO: R$ 8.50

                  Para voltar digite '0'

            """)
            try:
                produto_id = int(input("Escolha o ID do produto: "))
                
                if produto_id == 0:
                    break
                elif 1 <= produto_id <= 10:
                    quantidade = int(input("Escolha a quantidade do produto: "))
                    preco_total = precos[produto_id] * quantidade
                    sacola.append([produto_id, quantidade, preco_total])
                else:
                    print("Opção inválida, por favor tente novamente")
            except ValueError:
                print("Opção inválida, por favor tente novamente")

    if x == 2:  # MENU do carrinho
        if not sacola:
            print("O carrinho está vazio. Volte às compras!")
            continue  # Retorna para o menu principal se o carrinho estiver vazio

        while True:
            print("""
                ============ CARRINHO ===============
            
            Olá colaborador, o que deseja?

            1- Verificar itens da compra

            2- Continuar comprando

            3- Pagar e sair

            """)
            total_compra = sum(item[2] for item in sacola)
            for index, item in enumerate(sacola):
                print(f"{index} - Produto ID: {item[0]}, Quantidade: {item[1]}, Preço Total: {item[2]:.2f}")
            print(f"Preço final da compra: {total_compra:.2f}")

            try:
                xf = int(input("Digite aqui: "))

                if xf == 1:
                    continue  # Mostra novamente os itens
                elif xf == 2:
                    break  # Sai deste loop e volta ao menu principal para continuar comprando
                elif xf == 3 and sacola:
                    # Inicia o processo de pagamento
                    break
                else:
                    print("Opção inválida, por favor tente novamente")
            except ValueError:
                print("Opção inválida, por favor digite um número válido")

            if xf == 3:
                senha_correta = input("Digite a senha do cartão de débito: ")
                tentativas = 3
                while tentativas > 0:
                    senha = input("Digite a senha novamente para confirmar: ")
                    if senha == senha_correta:
                        print("Pagamento efetuado com sucesso!")
                        break
                    else:
                        tentativas -= 1
                        print(f"Senha incorreta! Tentativas restantes: {tentativas}")
                        if tentativas == 0:
                            print("Cartão bloqueado! Fim do programa.")
                            exit()
                if senha == senha_correta:
                    break

    if x == 3:  # Esse if é para sair do programa
        break