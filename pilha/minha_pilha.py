class No:
    def __init__(self, valor = None):
        self.valor: object = valor
        self.anterior: "No" = None

#Stack
class Pilha:
    def __init__(self):
        self.topo = None
                        
    #push
    def empilhar(self, valor):
        """Adiciona na última posição da pilha"""          
        novo_no = No(valor)
        novo_no.anterior = self.topo
        #atualiza topo
        self.topo = novo_no        
                                               
    #pop
    def desempilhar(self):
        """Remove da última posição da pilha"""        
        if self.esta_vazia():
            return None
        item = self.topo.valor
        self.topo = self.topo.anterior                 
        return item        
        
    def esta_vazia(self):
        return self.topo == None
       
        
    def __str__(self):
        string = "Pilha["
        no = self.topo
        while no.anterior != None:
            string += str(no.valor) + ", "
            no = no.anterior
        else:
            string += str(no.valor)            
            string += "]" 
                     
        return string

if __name__ == "__main__":
    p = Pilha()
    p.empilhar(1)
    p.empilhar(2)
    p.empilhar(3)
    
    print(p)               # Pilha[3, 2, 1]
    print(p.desempilhar()) # 3
    print(p)               # Pilha[2, 1]
    print(p.desempilhar()) # 2
    print(p)               # Pilha[1]
    print(p.desempilhar()) # 1
    print(p.esta_vazia())  # True
