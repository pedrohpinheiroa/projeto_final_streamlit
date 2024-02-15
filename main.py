from src.dimensionamento_sistema import (
    aspersor,
    linhas_lateral
)




# Aspersor
R = None
h = None
q = None
E1 = None
E2 = None
d = None
A = None
C = None

print(aspersor.eficiencia(5, 10))
print(aspersor.intensidade_aplicacao_agua(10,10,10))
print(aspersor.alcance_jato_agua(10,10,"fixo"))
print(aspersor.vazao(10,10,10))


# Linha lateral
# Parei na página 31 do PDF