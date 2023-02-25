# Filas

Neste exemplo, implementamos a estrutura de dados Fila. Para isso, utilizamos uma lista encadeada para estruturar a Fila. No entanto, existem estruturas prontas (listas) que você pode usar para auxiliar na criação dos métodos de Fila. Outra alternativa é utilizar o módulo "queue" do Python. 

## Entendendo Filas

Imagine uma fila de pessoas no caixa de um supermercado. Essas pessoas são atendidas uma após a outra, na ordem em que chegam. Assim, quem chegou primeiro será o primeiro a ser despachado. Já o último da fila, terá que esperar até que todos à sua frente sejam atendidos.

Portanto, o primeiro da fila será o primeiro a ser atendido, enquanto que o último da fila será o último a ser atendido. Esse tipo de estrutura é conhecida como FIFO(First-In First-Out), ou em português "O primeiro a entrar também é o primeiro a sair". 

## Sobre o código

Em nossa classe No, assim como vimos nos exemplos da Lista Ligada e da Pilha, temos:

```python

class No:
    def __init__(self, valor = None):
        self.valor: object = valor
        self.proximo: "No" = None

```

Já a classe Fila terá dois atributos: primeiro e último, que representam o primeiro e o último elemento da Fila, respectivamente.

```python
# ...Resto do código

class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
```

## Adicionando itens na Fila

Para adicionar elementos na fila precisamos criar um novo nó. Caso a fila ainda não tenha elementos, atualizamos a primeira e a última posição com o novo nó. Se já existirem elementos na fila, podemos adicionar um elemento simplesmente fazendo o próximo nó do atributo `ultimo` (que contém a referência do último nó inserido) apontar para o novo nó. Depois atualizamos o atributo `ultimo` com o novo nó para que possamos repetir o mesmo processo na próxima inserção.


```python

# ... Resto do código

class Fila:
    
    # ... Os outros métodos
    def adicionar(self, valor):
        """Adiciona um elemento na última posição da fila"""
        
        novo = No(valor)                                         
        
        if not self.esta_vazia():
            # Adiciona o novo no
            self.ultimo.proximo = novo
        # Atualiza o atributo ultimo com o novo no
        self.ultimo = novo

```

## Removendo itens da Fila 

Na fila devemos remover o primeiro elemento. Caso haja elementos na fila, podemos fazer o atributo `primeiro`(que guarda a referência do primeiro elemento) apontar para o seu próximo nó (que guarda a referência para o segundo nó inserido, caso ele exista). É sempre útil retornar o valor do elemento removido, então antes da remoção armazenamos esse valor em uma variável de retorno temporária. 

```python 
# ... Resto do código

class Fila:
    
    # ... Os outros métodos
    
    def remover(self):
        """Remove um elemento da primeira posição da fila"""
        
        # verifica se há elementos
        if self.esta_vazia():
            return None
            
        # próximo nó da lista caso exista
        segundo = self.primeiro.proximo 
        
        # valor do item que será removido
        item_removido = self.primeiro.valor
       
        # atualiza a primeira posição da Fila 
        # com o que antes era o segundo nó
        self.primeiro = segundo 
               
        return item_removido

```

---

Você pode conferir o código em [minha_fila.py](https://github.com/minha-logica/estruturas-de-dados-em-python/blob/master/Fila/minha_fila.py)

Se você leu esse texto até aqui, talvez goste de ler também sobre a [Lista Ligada](https://github.com/minha-logica/estruturas-de-dados-em-python/tree/master/lista-encadeada-simples) e sobre a [Pilha](https://github.com/minha-logica/estruturas-de-dados-em-python/tree/master/pilha).





