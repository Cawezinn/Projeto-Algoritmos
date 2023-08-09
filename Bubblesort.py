def bubble_sort(lista):
    elementos = len(lista)-1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1],lista[i]
                ordenado = False        
                print(lista)
    return lista

n = int(input())
list_ = input().split(' ')
participants = []
#Criacão da lista com as tuplas
for string in list_:
  tupla = (string[0], int(string[1]))
  participants.append(tupla)

bubble_sort(participants)