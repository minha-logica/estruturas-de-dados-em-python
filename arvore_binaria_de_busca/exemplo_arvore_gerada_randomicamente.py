from random import sample
from arvore_binaria_de_busca_visual import ArvoreBinariaDeBuscaVisual
from time import sleep

def gerar_arvore_binaria_aleatoria():
    itens = sample(range(1,100),5)
    ab = ArvoreBinariaDeBuscaVisual()
    for item in itens:
        ab.adicionar(item)
    return ab

def loop():
    while True:
        ab = gerar_arvore_binaria_aleatoria()
        print(ab)
        sleep(2)
        
loop()
