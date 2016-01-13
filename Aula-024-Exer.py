"""
Escreva um programa pra testar se a estatistica proposta no filme
'Quebrando a banca'é verdadeira. Utilize o módulo random para tais testes.
"""
import random

testes = int(input("Olá, bem-vindo ao nosso programa!Vamos ver se você ganhou um carro!: "))

escolha = 0
escolha = 1
for i in range(testes):
    porta = random.randrange(1, 4)
    premio = random.randint(1, 3)

    if porta != premio:
     escolha and 0 or 1
        
print("ganhou o carro Jão %.3g %% das vezes"%(escolha*100/testes))

