class No:
    def __init__(self, valor=None):
        self.valor = valor
        self.proximo: "No" = None
        
class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
    
    def adicionar(self, valor):
        """Adiciona um elemento na última posição da fila"""
        novo = No(valor)                                         
        
        if not self.esta_vazia():
            # Adiciona o novo no
            self.ultimo.proximo = novo
        # Atualiza o atributo ultimo com o novo no
        self.ultimo = novo
        
        if self.esta_vazia():
            self.primeiro = self.ultimo
            
    def remover(self):
        """Remove um elemento da primeira posição da fila"""
        if self.esta_vazia():
            return None
        segundo = self.primeiro.proximo   
        item_removido = self.primeiro.valor  
        self.primeiro = segundo 
               
        return item_removido
    
    def esta_vazia(self):
        """Verifica se a fila está vazia"""
        return self.primeiro == None
            
    def __str__(self):
        """Representação em string da Fila"""
        no = self.primeiro
        
        if self.esta_vazia():
            return "Fila Vazia"
             
        string = "Fila: "
        while no.proximo is not None:
            string += str(no.valor) + " -> "
            no = no.proximo
        string += str(no.valor)
        
        return string

if __name__ == "__main__":
    
    f = Fila()
    f.adicionar(1)
    f.adicionar(2)
    f.adicionar(3)
    
    print(f) # Fila: 1 -> 2 -> 3
    print(f.remover()) # 1
    print(f) # Fila: 2 -> 3
    print(f.remover()) # 2
    print(f.remover()) # 3
    print(f) # Fila Vazia
