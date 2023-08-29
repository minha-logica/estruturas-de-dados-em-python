
""" Tabela de dispersão ou hash table em Python """

def funcao_de_espalhamento(chave,tamanho_lista):
    # uma função boa de espalhamento
    return chave % tamanho_lista

def criar_tabela_de_dispersao(tamanho):# hash table
    T = 2 * tamanho - 1 # seria legal implementar pra ser o primo mais próximo de 2*tamanho  

    lista = [[None, None] for i in range(T)]

    def buscar(chave: int):
        posicao = funcao_de_espalhamento(chave, T)
        if chave == lista[posicao][0]:
            return lista[posicao][1]
        return -1
    
    def inserir(chave: int, valor = None):
        
        if chave < T: print(f"Informe uma chave maior que {T}"); return 0
        
        posicao = funcao_de_espalhamento(chave, T)
        if buscar(chave) == -1:
            lista[posicao][0] = chave
            lista[posicao][1] = valor
        else:
            # TODO: resolver conflitos de chaves com resto(posições) iguais
            # A lista já tem a chave ou tem o mesmo resto;
            # Se só tiver o mesmo resto tem que adicionar o valor na 
            # próxima posição vazia.
            pass
        
    def exibir_lista():
        print(lista)

    return buscar, inserir, exibir_lista


tamanho = 8# tamanho do conjunto de dados

buscar, inserir, exibir = criar_tabela_de_dispersao(tamanho)

inserir(758, "Maçã")
inserir(43, "Tomate")
inserir(25, "Banana")
inserir(199, "Limão")
print(buscar(199))
exibir()


