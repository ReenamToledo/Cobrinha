#Acessar elementos
vetor = ["a", "b", "c", 1, 2, 3]
primeiro = vetor[0] # "a"

#Fatiamento (slicing)
#Pega uma faixa de elementos
sub_vetor = vetor[1:4]
print(sub_vetor)

#Adicionar elementos
vetor.append("d") #Adiciona elemento ao final do vetor
print(vetor)

#Acionar vários elementos de uma vez
vetor.extend([4,5])


#Remover elementos
vetor.remove("b")

#Remover elemento ppor indice(posição)
del vetor[2]