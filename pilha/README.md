# Pilha

Nesse exemplo, implementamos a estrutura de dados Pilha. Para isso, utilizamos uma lista encadeada (que vimos anteriormente) para estruturar os `nós`. No entanto, você pode usar uma lista já pronta ou outra estrutura (array ou vetor) caso esteja utilizando uma linguagem diferente. Caso você opte por usar um vetor ou estrutura estática é sempre bom implementar um método para verificar se a Pilha está preenchida, tendo assim maior controle sobre a memória. Assim você pode implementar um método para redimencionar o vetor Pilha, por exemplo.

## Instalação 

Clone este repositório e execute o arquivo `minha_pilha.py` dentro do diretório `pilha`

## Entendendo o código
Imagine uma pilha de pratos. Para formar essa pilha adicionamos um prato em cima do outro. Estamos empilhando os pratos. Existe sempre um prato que fica no `topo`. Se tivermos 10 pratos empilhados o 10° prato será o topo. Para acessar o 2° prato, por exemplo, temos que `desempilhar` a Pilha retirando sempre o prato que estiver no `topo` até chegar no 2° prato.

Em outras palavras o último prato adcionado será o primeiro a ser retirado se formos `desempilhar` a pilha de pratos. Esse tipo de estrutura é conhecido como LIFO - Last-In First-Out, ou em português "O Último a Entrar será o Primeiro a Sair".

Dessa forma, criamos uma classe `No` que irá guardar nossos "pratos". Ela possui dois atributos: valor e anterior.

```python
class No:
    def __init__(self, valor = None):
        self.valor: object = valor
        self.anterior: "No" = None

```

A classe `Pilha` irá manipular esses nós através de uma lista encadeada. 
```python
class Pilha:
    def __init__(self):
        self.topo = None
```
O atributo `topo` em `Pilha` guardará o último item inserido e a referencia do item anterior. Assim, para acessar os elementos da Pilha podemos acessar o item anterior a `topo` ou o anterior do anterior a `topo` e assim sucessivamente até que eventualmente não exista um nó anterior(ou seja, `anterior` será None).

### Adicionando itens na Pilha

Para adicionar elementos na Pilha criamos o método `empilhar()`. Nele criamos um novo nó com o valor que queremos adicionar na Pilha. O atributo `anterior` desse novo nó recebe o `topo`. Assim esse novo nó terá a referência de todos os nós anteriores(os pratos que então em baixo, p. ex.). Depois disso, devemos atualizar `topo`, pois esse novo nó também é o último nó que estamos adicionando até esse momento. Agora, o novo nó que adicionamos está no `topo` da Pilha e será o primeiro a ser removido se formos desempilhá-la.

```python
#... Resto do código

class Pilha:

    #... Os outros métodos

    def empilhar(self, valor):
        """Adiciona na última posição da pilha"""          
        novo_no = No(valor)
        novo_no.anterior = self.topo
        #atualiza topo
        self.topo = novo_no  
```

### Removendo itens da Pilha

Antes de remover um item devemos ter certeza que a Pilha não está vazia. Para isso, criamos o método `esta_vazia()` que verifica se `topo` está vazio. 

```python 
# ... Resto do código

class Pilha:

    # ... Os outros métodos
        
    def esta_vazia(self):
        return self.topo == None

```

Depois de certificar que a Pilha tem elementos, podemos remover o item que está no `topo`. Antes disso, é sempre útil informar o elemento que foi removido. Assim, iremos guardar o valor de `topo` em uma variável temporária para retorná-la depois da remoção.

Para remover o item que está no topo basta atualizar `topo` como o nó `anterior` ao `topo`. Assim, `topo` terá a referência do nó anterior(ou do prato anteior ao prato do topo da pilha, p. ex.).

```python
#... Resto do código

class Pilha:

    #... Os outros métodos
    
    def desempilhar(self):
        """Remove da última posição da pilha"""        
        if self.esta_vazia():
            return None
        item = self.topo.valor
        self.topo = self.topo.anterior                 
        return item        

```

Você pode ver o código completo no arquivo `minha_pilha.py` desse diretório.

Caso você tenha lido esse texto talvez este exemplo sobre [Lista Encadeada Simples](https://github.com/minha-logica/estruturas-de-dados-em-python/tree/master/lista-encadeada-simples) seja útil. Também explicamos sobre na nossa página no [Twitter](https://twitter.com/minha_logica/status/1619696743205212160?t=X2U8F7PRZbtQo0Hg_W8XNg&s=19)


