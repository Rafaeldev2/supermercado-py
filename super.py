sacola = []

while True:
    #Início do programa
    print("""
            ============ MENU ===============
        
        Olá, seja bem vindo ao mercadinho Seu Zé

        Antes de começarmos, você é cliente ou funcionário? (Por favor, digite apenas números: )

        1- Começar uma compra
        
        2- Ir para o carrinho

        3- Sair
        
        """)
    while True:                
        #Garantir que o usuário vai digitar uma opção válida
        try:         
            x = int(input("Digite aqui: "))
            
            if x == 1 or x == 2 or x == 3:
                break            
            else:
                print("Opção inválida, por favor tente novamente")
        except ValueError:
            print("Opção inválida, por favor tente novamente")
            


    if x == 1: #MENU do cliente
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

            """)
            while True:                
                #Garantir que o usuário vai digitar uma opção válida
                try:         
                    xc = int(input("Digite aqui: "))
                    
                    if xc == 1 or xc == 2 or xc == 3:
                        break            
                    else:
                        print("Opção inválida, por favor tente novamente")
                except ValueError:
                    print("Opção inválida, por favor tente novamente")
            if xc == 1:
                1+1
            elif xc == 3:
                break
        


    if x == 2: #MENU do funcionário
        while True:
            print("""
                ============ CARRINHO ===============
            
            Olá colaborador, o que deseja?

            1- Verificar itens da compra
            
            2- Continuar comprando

            3- Voltar
            
            """)
        
            while True:            
                #Garantir que o usuário vai digitar uma opção válida
                try:         
                    xf = int(input("Digite aqui: "))
                            
                    if xf == 1 or xf == 2 or xf == 3:
                        break            
                    else:
                        print("Opção inválida, por favor tente novamente")
                except ValueError:
                    print("Opção inválida, por favor tente novamente")
            if xf == 1:
                1+1
                
            elif xf == 3:
                break
            
    
    if x == 3: #Esse if é para sair do programa
        break


