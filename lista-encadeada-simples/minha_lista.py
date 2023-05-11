class No:
    def __init__(self, valor):        
        self.valor: object = valor
        self.proximo: 'No' = None
    
class MinhaLista:
    #INICIALIZADOR 
    def __init__(self, *args):
        self.primeiro = None        
        if args:    
            self.preencher(args)
    
    #MÉTODOS AUXILIARES
    def preencher(self, valores):
        if not valores:
            return
                 
        self.primeiro = No(valores[0])     
        atual = self.primeiro
        for i in range(1,len(valores)):
            atual.proximo = No(valores[i])
            atual = atual.proximo            	                    
                                                                       
    #CRUD
    def adicionar(self, valor):                       
        novo = No(valor)
        if self.primeiro is None:
            self.primeiro = novo
        else:
            atual = self.primeiro
            while atual.proximo != None:
                atual = atual.proximo        
            atual.proximo = novo
        
        
    def obter(self, indice):
        atual = self.primeiro
        i = 0
        while atual is not None:    
            if indice == i:
                return atual.valor        
            atual = atual.proximo 
            i += 1
        return None
    
    
    def buscar(self, valor):                                
        atual = self.primeiro
        indice = 0
        while atual is not None:         
            if atual.valor == valor:
                return indice
            atual = atual.proximo 
            indice += 1                
        return -1
    
        
    def atualizar(self, indice, valor):       
        atual = self.primeiro
        i = 0
        while atual is not None:    
            if indice == i:
                atual.valor = valor
            atual = atual.proximo 
            i += 1 
                  
    
    def remover(self, indice):
        if indice < 0:
            return None        
        
        if indice == 0:
            removido = self.primeiro
            self.primeiro = removido.proximo
            return removido.valor                    
        
        atual = self.primeiro        
        i = 1
        while atual is not None and i < indice :            
            atual = atual.proximo 
            i += 1             
        
        if atual is None or atual.proximo is None:
            return None        
        
        removido = atual.proximo
        atual.proximo = removido.proximo
        return removido.valor
    
    def contem(self, valor):
        atual = self.primeiro
        while atual is not None:
            if atual.valor == valor:
                return True
            atual = atual.proximo
        return False
        
    
    def contar(self):
        atual = self.primeiro
        contador = 0
        while atual is not None:
            contador += 1
            atual = atual.proximo
        return contador

    #MÉTODOS ESPECIAIS
    def __str__(self, nome_da_estrutura="MinhaLista"):
        lista = []
        atual = self.primeiro
        while atual is not None:
            lista.append(atual.valor)
            atual = atual.proximo        
                                
        lista = str(lista)
        return f"Lista{lista}"
        
    def __iter__(self):
        no = self.primeiro
        tamanho = self.contar()
        i = 0
        while no is not None:                               
            yield no.valor 
            no = no.proximo
                                                                   
    def __len__(self):
        return self.contar()
    
    def __getitem__(self, indice):
        if isinstance(indice, slice):
            inicio, fim, intervalo = indice.indices(len(self))
            lista = MinhaLista()
            for i in range(inicio, fim, intervalo):
                lista.adicionar(self.obter(i))
            return lista
        else:
            return self.obter(indice)
    
    def __setitem__(self, indice, valor):
        self.atualizar(indice, valor)


