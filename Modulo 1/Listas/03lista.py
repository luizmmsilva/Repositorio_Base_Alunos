nomes = ["Joaquim", "Maria" , "Ana"]

print("Lista inicial:" ,nomes)
# print(f"Lista Inicial:{nomes}")

# adicionar elementos em uma lista
nomes.append("Carlos")
print(nomes)

nomes.insert(1,"Fernanda") # adiciona em uma posição especifica
print("Após insert,",nomes)

# modificar elementos
nomes[2]= "Marcos"
print(nomes)

# remover elementos
nomes.remove("Marcos")
print(nomes)

removido =  nomes.pop(2) # remove e retorna o elemento no indice 2
print(f"Após pop(removido '{removido}'):", nomes)

nomes.clear() # esvazia a lista
print("após clear:", nomes)
