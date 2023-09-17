from calcula_sal_liq import calcula_salario_liquido

#definição dos dados cadastrais

Dados_salariais_colaboradores = { "Jose":"1589.59",
                                    "Maria": "5678.05",
                                    "Ana": "9865.59"
                 }

Dados_login_colaboradores = { "Jose": "1234",
                              "Maria": "5678",
                              "Ana": "8910",
                 }



#solicitação dos dados

Login = input("DIGITE SEU LOGIN: ")
Senha = input("DIGITE SUA SENHA: ")

while True:
    if Login in Dados_login_colaboradores and Senha == Dados_login_colaboradores[Login]:
        print("Login bem-sucedido!")
        break
        
    else:
     print("LOGIN OU SENHA INCORRETOS.TENTE NOVAMENTE!")
     Login = input("DIGITE SEU LOGIN: ")
     Senha = input("DIGITE SUA SENHA: ") 
     


while True:
    tela_de_entrada = input("""
   ################## MENU DE OPÇÕES ################
                    [1] CONSULTA DE SALÁRIO LÍQUIDO
                    [2] SAIR
                    
                        """)
    if tela_de_entrada.isdigit():
        tela_de_entrada = int(tela_de_entrada)
        
        if tela_de_entrada == 1:
            if Login in Dados_salariais_colaboradores:
             salario = float(Dados_salariais_colaboradores[Login])
             Login = salario
             salario_liquido = calcula_salario_liquido(Login)
             print(f"Seu salário líquido é R$ {salario_liquido:.2f}") 
            break
        elif tela_de_entrada == 2:
            print("Saiu")
            break
        else:
            print("TENTE NOVAMENTE COM UMA OPÇÃO VÁLIDA!")
    else:
        print("TENTE NOVAMENTE COM UMA OPÇÃO VÁLIDA!")
    






