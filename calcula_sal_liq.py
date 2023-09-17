
pacote_beneficios = 985.0


def calcula_salario_liquido(colaborador):
    if colaborador >= 0 and colaborador <= 1100.00:
        salario = (colaborador-((colaborador*5)/100)) + pacote_beneficios
    elif colaborador >= 1100.01 and colaborador <= 2500.00:
        salario = (colaborador-((colaborador*10)/100)) + pacote_beneficios
    else:
       salario = (colaborador -((colaborador*15)/100)) + pacote_beneficios
       return salario 
        
    
