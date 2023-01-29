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
