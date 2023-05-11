"""
    Utiliza a implementação da Árvore 
    Binária de Busca de forma
    personalizada.
"""
from arvore_binaria_de_busca import ArvoreBinariaDeBusca

class ArvoreBinariaDeBuscaVisual(ArvoreBinariaDeBusca):            
    def converter_para_lista(self):
        raiz = self.no_raiz
        altura = self.obter_altura()        
        
        def func(no, lista, nivel):                                              
            if nivel < altura: 
                if len(lista) <= nivel:
                    lista.append([])                              
                
                if no is not None:
                    lista[nivel].append(no.valor)
                    func(no.esquerda, lista,nivel+1)
                    func(no.direita, lista, nivel+1)
                else:                   
                    lista[nivel].append(None)
                    func(None,lista,nivel+1)
                    func(None,lista,nivel+1)
            return lista
                                
        return func(raiz, [], 0)      
        
    def obter_altura(self, no="RAIZ",altura=1, geracao=1):
        if no == "RAIZ":
            no = self.no_raiz
        if no is None:
            return 0
        altura_esquerda = self.obter_altura(no=no.esquerda)
        altura_direita  = self.obter_altura(no=no.direita)
        altura = max(altura_esquerda, altura_direita) 
        
        return altura + 1
        
    def buscar_maior_item(self, no="RAIZ"):
        if no == "RAIZ":
            no = self.no_raiz
        
        if no.direita is not None:                               
            return self.buscar_maior_item(no=no.direita)                                        
        return no.valor    
                                    
            
    def exibir_arvore(self):
        arvore = self.converter_para_lista()
        maior_item = self.buscar_maior_item()
        # Unidade de espaço para manter a proporção da arvore
        unidade_de_espaco = len(str(maior_item))

        largura = pow(2, len(arvore))-1      

        for i, nivel_atual in enumerate(arvore):
            # Calcula o número de espaços entre os itens        
            e = (largura) // (2**(i))     
     
            espacamento_entre_itens = e*unidade_de_espaco*" "      
            indentacao_item = (e//2)*unidade_de_espaco*" "               
            itens = "" 
    
            itens += indentacao_item         
   
            for j, item in enumerate(nivel_atual):        
                if item is None:
                    item = unidade_de_espaco*" "            
                else:                                   
                    item = format(item,"0{}d".format(unidade_de_espaco))                                       
                if j == len(nivel_atual) - 1:
                    itens += item            
                else:
                    itens += item + espacamento_entre_itens                       
    
            if i == len(arvore) - 1:
                print(itens)
                break
    
            ramos = ""
            indentacao_ramo = indentacao_item[:-1]
            maior_espaco_entre_um_par_ramos = indentacao_item + 2*unidade_de_espaco*" "
            maior_espaco_entre_pares_de_ramos = espacamento_entre_itens[2:]
                                             
            tamanho_ramo = len(indentacao_ramo)//2+1
            for y in range(tamanho_ramo):
                espaco_entre_um_par_de_ramos = maior_espaco_entre_um_par_ramos[:2*y+unidade_de_espaco]                                    
                espaco_entre_pares_de_ramos = maior_espaco_entre_pares_de_ramos[2*y:] 
                       
                proximo_nivel = arvore[i+1] 
                ramos += indentacao_ramo[y:]    
            
                largura_do_proximo_nivel = len(proximo_nivel)                  
                for x in range(largura_do_proximo_nivel):                                          
                    ramo = ""
                    espacamento_entre_ramos = ""
                
                    if (x+1) % 2 == 1: 
                        ramo = "/"
                        espacamento_entre_ramos = espaco_entre_um_par_de_ramos 
                    else:
                        ramo = "\\" 
                        if x < largura_do_proximo_nivel - 1:                  
                            espacamento_entre_ramos = espaco_entre_pares_de_ramos   
                
                    if proximo_nivel[x] is None: 
                        ramo = " " 
                
                    ramos += ramo + espacamento_entre_ramos                            
                                   
                if y < tamanho_ramo - 1:
                    ramos += "\n"
    
            print(itens)
            print(ramos)
        
    def __str__(self):
        self.exibir_arvore()   
        return "" 
                                             
if __name__ == "__main__":        
    ab = ArvoreBinariaDeBuscaVisual()
    
    ab.adicionar(10)
    ab.adicionar(5)
    ab.adicionar(12)
    ab.adicionar(7)
    ab.adicionar(2)
    ab.adicionar(4)
    ab.adicionar(7)
    ab.adicionar(6)
    ab.adicionar(11)
    ab.adicionar(13)
          
    print(ab.converter_para_lista())
        
    print()
    print("Árvore Binária de Pesquisa: ")
    print(ab)
    print("Remover o item 5: ")
    ab.remover(5)
    print(ab)
    print("Remover o item 10: ")
    ab.remover(10)
    print(ab)
    print("Adicionar o item 9:")
    ab.adicionar(9)
    print(ab)    
    ab.remover(6)
    print("Remover o item 6:")
    print(ab)
    
    
   


