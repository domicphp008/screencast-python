import random

#random.randrange(start, stop[, step])
"""
Retorna aleatæoriamente um elemeno de range (começo, fim passo).
Isso é equivalente a choice(range(começo, fim, passo)),mas não constroi um
objeto range.
"""
#Exemplo
"""
for i in range(10):
    #x = random.randrange(1,7)
    #x = random.randrange(1, 7, 2)
    print(x)
"""
#####################################################################
#random.randint(a, b)
"""
Retorna um inteiro N de tal forma que a <= N <= b.
Tal como randrange(a, b+1).
"""
#Exemplo

for i in range(10):
    x = random.randint(1,7)
    print(x)

