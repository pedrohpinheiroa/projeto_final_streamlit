from typing import Literal

def vazao(A:float, C:float, h:float) -> float:
    '''
    Calcula a vazão do aspersor pela equação derivada do teorema de Torricelli.

    Parâmetros
    ----------
    A: float 
        área do orifício de saída.  
        Unidade: m²
    C: float 
        coefi ciente de descarga do aspersor.  
        Unidade: unidimensional
    h: float 
        Carga hidráulica ou pressão.  
        Unidade: m (mca)
        
    Retorno
    -------
    q: float
        Equação Utilizada: q = 4,4272 . A . C . h^(0,5)
        Unidade: m³/s
    '''

    return 4.4272 * A * C * (h**(0.5))

def alcance_jato_agua(d:float, h:float, tipo:Literal["fixo", "rotativo"] = "fixo") -> float:
    '''
    Calcula alcance do jato de água.

    Parâmetros
    ----------
    d: float
        diâmetro do bocal.
        Unidade: mm
    h: float 
        Carga hidráulica ou pressão.  
        Unidade: m (mca)
    tipo: {'fixo', 'rotativo'}, padrão 'fixo'
        Parâmetro que define se o aspersor é fixo ou rotativo.  

    Retorno
    -------
    R: float
        Equação Utilizada para tipo fixo: R = 1,35 . d^(0,6) . h^(0,4)
        Equação Utilizada para tipo rotativo: R = 1,35 . (d) . h
        Unidade: m
    '''

    if tipo not in ["fixo", "rotativo"]:
        raise ValueError(f'\n\tO tipo "{tipo}" não está na lista dos valores aceitos pela função "alcance_jato_agua".')
    
    if tipo == "fixo":
        return 1.35 * (d**(0.6)) * (h**(0.4))
    
    return 1.35 * (d**(1/2)) * h

def intensidade_aplicacao_agua(q:float, E1:float, E2:float) -> float:
    '''
    Calcula a lâmina de água aplicada sobre uma superfície por um determinado tempo.

    Parâmetros
    ----------
    q: float
        Vazão do aspersor.
        Unidade: L.s⁻¹
    E1: float 
        Espaçamento entre aspersores na mesma linha.  
        Unidade: m
    E2: float
        Espaçamento entre linhas de aspersores.  
        Unidade: m

    Retorno
    -------
    I: float
        Equação Utilizada: I = [(q . 3600) ÷ (E1 . E2)]
        Unidade: mm.h⁻¹
    '''

    return ((q * 3600) / (E1 * E2))

def eficiencia(R:float, h:float) -> float:
    '''
    Calcula a eficiência do aspersor e do sistema de aspersão, podendo variar de 75% a 85%.

    Parâmetros
    ----------
    R: float
        Raio de cobertura.
        Unidade: m
    h: float 
        Carga hidráulica ou pressão.  
        Unidade: m (mca)

    Retorno
    -------
    Ef: float
        Equação Utilizada: Ef = (R ÷ h) . 100
        Unidade: %
    '''

    return (R / h) * 100
