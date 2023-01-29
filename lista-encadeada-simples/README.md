# Lista Encadeada em Python
Este repositório contém a implementação de uma lista encadeada simples em Python.

## Requesitos 
Python 3.x

## Instalação 

Clone este repositório e execute o arquivo `exemplos.py`

## Uso 

A classe `No` representa um nó da lista encadeada, contendo um valor, um indice e um ponteiro para o próximo nó. A classe `MinhaLista` representa a lista encadeada com métodos para inserir, remover, buscar e imprimir os elementos.

Veja um exemplo de uso abaixo:

```python
from minha_lista import MinhaLista

#CRUD
vogais = MinhaLista(1,"e",3,"i","o")
print(vogais.atualizar(0, "a"))
print(vogais.remover(2))
print(vogais.adicionar("u"))
print(vogais.procurar(5))

#Loop For
primos = MinhaLista(2, 3, 5, 7, 11)
for p in primos:
    print(p)

#Slicing 
m = MinhaLista(1,2,3,4,5,6,7)
print(m[1:4]) #MinhaLista[2, 3, 4]

```

## Contribuições 
Todas as contribuições são bem-vindas. Sinta-se à vontade para abrir uma issue ou enviar um pull request.





