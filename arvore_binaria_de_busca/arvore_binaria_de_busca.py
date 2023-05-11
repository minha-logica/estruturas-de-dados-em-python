"""
    Exemplo de implementação de uma Árvore Binária 
    de Busca.
"""
class No:
    def __init__(self,valor=None):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinariaDeBusca:
    
    def __init__(self):
        self.no_raiz = None 
                                   
                
    def esta_vazia(self):
        return self.no_raiz == None
    
    def adicionar(self, valor, no="RAIZ"):
        
        if self.esta_vazia():
            self.no_raiz = No(valor)
                               
        if no == "RAIZ":
            no = self.no_raiz  
            
        if no == None:            
            no = No(valor)                 
                                  
        if valor < no.valor:            
            no.esquerda = self.adicionar(valor,no=no.esquerda)
        
        if valor > no.valor:
            no.direita = self.adicionar(valor,no=no.direita) 
        
        if no != self.no_raiz:
            return no

                       
    def buscar_menor_valor_na_subarvore_direita(self, no="RAIZ"):              
        if no == "RAIZ":            
            no = self.no_raiz.direita
        else:
            pai = no
            no = no.direita
        
        while no != None and no.esquerda != None:
            pai = no
            no = no.esquerda
                
        return no, pai       
    
    def buscar_no(self, valor):                               
        pai = None
        no = self.no_raiz         
        while no != None:
            if no.valor == valor:
                break            
                            
            pai = no                       
            if valor < no.valor:
                no = no.esquerda
            else:
                no = no.direita
        
        return no, pai        
        
        
    def remover(self, valor):
        if self.esta_vazia(): return
        
        filho, pai = self.buscar_no(valor)
        
        if filho is None: return
        
        substituto = None
        pai_substituto = None
        
        if filho.direita is None or filho.esquerda is None:
            if filho.direita is None:
                substituto = filho.esquerda 
            else:
                substituto = filho.direita 
            pai_substituto = filho 
        else:
            substituto, pai_substituto = self.buscar_menor_valor_na_subarvore_direita(no=filho)
            
            if pai_substituto == filho:
                substituto.esquerda = filho.esquerda
            else:                
                pai_substituto.esquerda = substituto.direita
                substituto.esquerda = filho.esquerda 
                substituto.direita = filho.direita
        
        if pai is None:
            self.no_raiz = substituto 
        else:                              
            if valor < pai.valor:
                pai.esquerda = substituto
            else:
                pai.direita = substituto
                                                                                                                                                                                                   
                                                                            
    def ler(self, no="RAIZ"):
        if self.esta_vazia():
            print("()")
        
        if no == "RAIZ":
            no = self.no_raiz
        
        print(no.valor,end=" ")
        
        if no != None:
            print("(", end="")           
            if no.esquerda != None:
                self.ler(no=no.esquerda)                         
            if no.direita != None:
                self.ler(no=no.direita)                
            print(")",end="")  
        
    def contem(self, valor, no="RAIZ"):
                            
        if no == "RAIZ":          
            no = self.no_raiz
        
        if no == None:
            return False
                                                                                            
        if no.valor > valor:
            return self.contem(valor, no=no.esquerda)
        
        if no.valor < valor:
            return self.contem(valor, no=no.direita)
        
        return no.valor == valor
        
    def contar(self, no=No()):
        
        if no == None:
            return 0
        
        if no.valor == None:
            no = self.no_raiz
        
        return (self.contar(no.esquerda)
        	       + 	1 +
        	       self.contar(no.direita))
                            
if __name__ == "__main__":                

    ab = ArvoreBinariaDeBusca()
        
    ab.adicionar(10)
    ab.adicionar(5)
    ab.adicionar(15)
    ab.adicionar(3)
    ab.ler()    
    ab.remover(10)
    print()
    ab.ler()
    print()
    print(ab.contar())
    print(ab.contem(15))
    
