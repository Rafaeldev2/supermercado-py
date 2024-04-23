while True:
    #Início do programa
    print("""
            ============ MENU ===============
        
        Olá, seja bem vindo ao mercadinho Seu Zé

        Antes de começarmos, você é cliente ou funcionário? (Por favor, digite apenas números: )

        1- Cliente
        
        2- Funcionário

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
                ============ CLIENTE ===============
            
            Olá cliente, o que deseja?

            1- Comprar
            
            2- Ver minha lista

            3- Voltar
            
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
                ============ FUNCIONÁRIO ===============
            
            Olá colaborador, o que deseja?

            1- Verificar estoque
            
            2- Aumentar estoque

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
