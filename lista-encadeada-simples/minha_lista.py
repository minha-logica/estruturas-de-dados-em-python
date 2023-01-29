class No:    
    indice: int = -1    
    valor: object = None
    proximo: 'No' = None
    
class MinhaLista:
    #INICIALIZADOR 
    def __init__(self, *args):
        self.no_raiz = No()
        self.tamanho = 0
        
        self._adicionar_itens(*args)
    #MÉTODOS AUXILIARES
    def _buscar_no(self, indice):
        no = self.no_raiz.proximo
        for i in range(self.tamanho):
            if no.indice  == indice:
                return no
            no = no.proximo
        return 
    def _adicionar_itens(self,*args):
        if len(args) != 0:
            for i in range(len(args)):
                item = args[i]
                self.adicionar(item)

    #CRUD
    def adicionar(self, valor):                        
        no = self.no_raiz
        ultimo_no = None        
        for i in range(self.tamanho+1):
            if no.proximo == ultimo_no:

                novo_no = No()
                novo_no.indice = self.tamanho 
                novo_no.valor  = valor
                
                no.proximo = novo_no
                self.tamanho += 1
                
                return self
            else:
                no = no.proximo                
    def procurar(self, indice):
        no = self._buscar_no(indice)
        if no != None:
            return no.valor
        else:
            print("Posição não está na lista")
        return 
    
    def atualizar(self, indice, valor): 
        no = self._buscar_no(indice)
        if no != None:
            no.valor = valor
            return self
        else:
            print("Posição não está na lista") 
        return
    
    def remover(self, indice):
        no = self.no_raiz.proximo
        nova_lista = MinhaLista()
        for i in range(self.tamanho):
            if no.indice != indice:
                nova_lista.adicionar(no.valor)                                                             
            no = no.proximo
                
        self.no_raiz = nova_lista.no_raiz 
        self.tamanho -= 1
        del nova_lista
        return self
    #MÉTODOS ESPECIAIS
    def __str__(self):
        string = "MinhaLista["                
        no = self.no_raiz.proximo
        for i in range(self.tamanho):
            valor = str(no.valor)
            string += valor
            if no.proximo != None:
                string += ", "
            else:
                string += "]"
                break
            no = no.proximo
        return string        
        
    def __iter__(self):
        no = self.no_raiz
        for i in range(self.tamanho):
            no = no.proximo           
            yield no.valor
    
    def __len__(self):
        return self.tamanho
    
    def __getitem__(self, indice):
        if isinstance(indice, slice):
            inicio, fim, intervalo = indice.indices(len(self))
            lista = MinhaLista()
            for i in range(inicio, fim, intervalo):
                lista.adicionar(self.procurar(i))
            return lista
        else:
            return self.procurar(indice)
    
    def __setitem__(self, indice, valor):
        self.atualizar(indice, valor)


