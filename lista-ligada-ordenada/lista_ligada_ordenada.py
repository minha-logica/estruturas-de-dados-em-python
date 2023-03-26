class No:
    def __init__(self, valor=None):
        self.valor: int = valor
        self.proximo: "No" = None

class ListaLigadaOrdenada:
    
    def __init__(self):
        self.primeiro: "No" = None   
    
    def adicionar(self, valor): 
        """Adiciona elementos na ordem crescente"""      
        novo = No(valor)         
        if self.esta_vazia():
            self.primeiro = novo
        elif valor <= self.primeiro.valor:
            novo.proximo = self.primeiro
            self.primeiro = novo    
        else:
            anterior, proximo = self._buscar_no_anterior_e_proximo(novo.valor)                                                                                              
            novo.proximo = proximo
            anterior.proximo = novo

    def remover(self, valor):
        """Remove um elemento qualquer da lista"""
        if self.esta_vazia():
            return None
        elif valor == self.primeiro.valor:
            self.primeiro = self.primeiro.proximo
        else:
            anterior, encontrado = self._buscar_no_anterior_e_proximo(valor)
            if encontrado != None and valor == encontrado.valor:                            
                anterior.proximo = encontrado.proximo            	      

    
    def esta_vazia(self):
        """Verifica se a lista está vazia"""
        return self.primeiro == None               
    
    # MÉTODO AUXILIAR
          
    def _buscar_no_anterior_e_proximo(self, valor):        
        """Método auxiliar usado na inserção e remoção de elementos"""                
                
        if self.esta_vazia():
            return None, None
                                   
        anterior = self.primeiro        
        fim_da_lista = None   
                            
        while anterior.proximo != fim_da_lista:
            if valor <= anterior.proximo.valor:                                                       
                break
            anterior = anterior.proximo             
         
        return anterior, anterior.proximo                                                                                
                                                                                                                                                                         
    def __str__(self):        
        if self.esta_vazia():
            return "[]"        
        string_da_lista = "["
        atual = self.primeiro
        final_da_lista = None      
        
        while atual != final_da_lista:
            string_da_lista += str(atual.valor) 
            if atual.proximo == final_da_lista:
                string_da_lista += "]"
                break                      
            string_da_lista += ","
            atual = atual.proximo 
                    
        return string_da_lista
        
if __name__ == "__main__":
    l = ListaLigadaOrdenada()
    l.adicionar(2)
    l.adicionar(4)
    l.adicionar(3)
    l.adicionar(1)
    l.adicionar(-4)
    l.remover(4)
    print(l) # [-4,1,2,3]
