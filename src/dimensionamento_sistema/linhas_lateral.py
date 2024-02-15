def perda_de_carga(Q:float, D:float, C:float, L:float) -> float:
    '''
    Calcula a perda de carga na linha lateral pela equação de Hazen-Willians.

    Parâmetros
    ----------
    Q: float 
        vazão da linha lateral.  
        Unidade: m³/s
    D: float 
        diâmetro interno da tubulação.  
        Unidade: m
    C: float 
        coefi ciente do tipo da parede do tubo.  
        Unidade: adimensional
    L: float 
        comprimento da tubulação.  
        Unidade: m
        
    Retorno
    -------
    hf: float
        Equação Utilizada: hf = 10,67 . (D^(-4,87)) . ((Q ÷ C)^1,852) . L
        Unidade: m (mca)
    '''

    return 10.67 * (D**(-4.87)) * ((Q / C)**1.852) * L

def perda_de_carga_permissivel(PS:float) -> float:
    '''
    Calcula a perda de carga permissível na linha lateral, admitindo-se um valor de até 20% da pressão de serviço.

    Parâmetros
    ----------
    PS: float 
        pressão de serviço.  
        Unidade: mca
        
    Retorno
    -------
    hf: float
        Equação Utilizada: hf = 0,20 . PS
        Unidade: mca
    '''

    return 0.20*PS