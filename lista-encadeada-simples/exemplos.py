from minha_lista import MinhaLista

#CRUD 
vogais = MinhaLista(1,"e",3,"i","o") 
vogais.atualizar(0, "a")
print(vogais.remover(2)) # 3
vogais.adicionar("u")
print(vogais.buscar(5)) # -1
print(vogais) # Lista['a','e','i','o','u']

#Loop For 
primos = MinhaLista(2, 3, 5, 7, 11) 
for p in primos: 
    print(p) 
  
#Slicing  
m = MinhaLista(1,2,3,4,5,6,7) 
print(m[1:4]) #MinhaLista[2, 3, 4]

# Outros métodos
print(m.contar()) # 7
print(m.buscar(7)) # 6
print(m.obter(0)) # 1
print(m.contem(10)) # False
