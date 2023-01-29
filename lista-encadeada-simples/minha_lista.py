class No:        
    valor: object = None
    proximo: 'No' = None
    
class MinhaLista:
    #INICIALIZADOR 
    def __init__(self, *args):
        self.no_raiz = No()
        self.tamanho = 0 #self._tamanho()      
        self._adicionar_itens(*args)
    #MÉTODOS AUXILIARES
    def _buscar_no(self, indice):
        no = self.no_raiz.proximo
        for i in range(self.tamanho):
            if i  == indice:
                return no
            no = no.proximo
        return 
    def _adicionar_itens(self,*args):
        if len(args) != 0:
            for i in range(len(args)):
                item = args[i]
                self.adicionar(item)
    
    def _tamanho(self):
        no = self.no_raiz
        contador = 0
        while no.proximo != None:
            no = no.proximo
            contador += 1
        return contador 
                            
    #CRUD
    def adicionar(self, valor):                        
        no = self.no_raiz
        ultimo_no = None        
        for i in range(self.tamanho+1):
            if no.proximo == ultimo_no:

                novo_no = No()
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
        no = self.no_raiz
        for i in range(self.tamanho):
            if no.proximo != None: 
                if i == indice:          
                    proximo = no.proximo                    
                    no.proximo = proximo.proximo
                    self.tamanho -= 1                   
                    return self                                                
            no = no.proximo                                
        return
    #MÉTODOS ESPECIAIS
    def __str__(self):
        string = "MinhaLista["                
        no = self.no_raiz.proximo
        if no == None:
            string += "]"
            return string
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

