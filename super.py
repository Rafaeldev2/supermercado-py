escolha = 5
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
                  
                   1 - BANANA: R$ 5.00
                   2 - MAÇÃ: R$ 3.00
                   3 - BERGAMOTA: R$ 4.00
                   4 - UVA: R$ 5.00
                   5 - PÃO: R$ 2.50
                   6 - LEITE: R$ 7.00
                   7 - MEL: R$ 6.90
                   8 - SALAME: R$ 10.00
                   9 - QUEIJO: R$ 9.50
                  10 - PRESUNTO: R$ 8.50

            """)


            while True:                
                #Garantir que o usuário vai digitar uma opção válida
                try:         
                    xc = int(input("Escolha o ID do produto: "))
                    
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

            quantidade=input("Escolha a quantidade do produto:")
            sacola.append(["",xc,quantidade,0])


    if x == 2: #MENU do carrinho
        while True:
            print("""
                ============ CARRINHO ===============
            
            Olá colaborador, o que deseja?

            1- Verificar itens da compra
            
            2- Continuar comprando

            3- Voltar
            
            """)
            contador=0
            for produto in sacola:

                print(contador,"#",produto[0]," ",produto[1],"-",produto[2])
                contador=contador+1
        
            while True:            
                #Garantir que o usuário vai digitar uma opção válida
                try:         
                    xf = float(input("Digite aqui: "))
                            
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
