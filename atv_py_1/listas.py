
lista = ["maçã", 41, "josé", ['a', 'b']]

#slide 57 - exec 1 -------------------------------------
print("\nImprima o segundo item da lista abaixo:\nlista = [\"maçã\", 41, \"josé\", [\'a\', \'b\']]\n")
print("\nResposta: ", lista[1])
print("\n-------------------------------------------------\n")

#slide 57 - exec 2 -------------------------------------
print("\nMude o valor da lista abaixo de 'José' para 'João':\nlista = [\"maçã\", 41, \"josé\", [\'a\', \'b\']]\n")
lista[2] = 'joão'
print("\nResposta: ", lista)
print("\n-------------------------------------------------\n")

#slide 59 - exec 1 -------------------------------------
print("\nAdicione 'cereja' ao final da lista abaixo:\nlista = [\"maçã\", 41, \"josé\", [\'a\', \'b\']]\n")
lista = ["maçã", 41, "josé", ['a', 'b']]
lista.append('cereja')
print("\nResposta: ", lista)
print("\n-------------------------------------------------\n")

#slide 59 - exec 2 -------------------------------------
print("\nInsira 'limão' como segundo item da lista abaixo:\nlista = [\"maçã\", 41, \"josé\", [\'a\', \'b\']]\n")
lista = ["maçã", 41, "josé", ['a', 'b']]
lista.insert(1, 'limão')
print("\nResposta: ", lista)
print("\n-------------------------------------------------\n")

#slide 62 - exec 1 -------------------------------------
print("\nRemova 'José' da lista abaixo:\nlista = [\"maçã\", 41, \"josé\", [\'a\', \'b\']]\n")
lista = ["maçã", 41, "josé", ['a', 'b']]
lista.remove('josé')
print("\nResposta: ", lista)
print("\n-------------------------------------------------\n")

#slide 62 - exec 2 -------------------------------------
print("\nImprima o ultimo item da lista abaixo:\nlista = [\"maçã\", 41, \"josé\", [\'a\', \'b\']]\n")
print("\nResposta: ", lista[-1])
print("\n-------------------------------------------------\n")

#-----------------------------------------

lista = ["maçã", 41, "josé", ['a', 'b'], 'cereja', 1]

#-----------------------------------------

#slide 64 - exec 1 -------------------------------------
print("Imprima o 2° e 4° itens da lista abaixo:\nlista = [\"maçã\", 41, \"josé\", [\'a\', \'b\'], \"cereja\", 1]\n")
print("\nResposta: ", lista[1], lista[3])
print("\n-------------------------------------------------\n")

#slide 64 - exec 2 -------------------------------------
print("Imprima quantos itens existem entre o 2° e 4° itens da lista abaixo:\nlista = [\"maçã\", 41, \"josé\", [\'a\', \'b\'], \"cereja\", 1]\n")
cont = 0
for x in lista[2:3]:
        cont+=1
print("\nResposta: ", cont)
print("\n-------------------------------------------------\n")

#slide 66 - exec 1 -------------------------------------
print("Imprima quantos itens existem entre o 1° e último itens da lista abaixo:\nlista = [\"maçã\", 41, \"josé\", [\'a\', \'b\'], \"cereja\", 1]\n")
cont = 0

for x in lista:
    cont+=1

print("\nResposta: ", cont-2)
print("\n-------------------------------------------------\n")

#slide 66 - exec 2 -------------------------------------
print("Imprima quantos itens existem na lista abaixo:\nlista = [\"maçã\", 41, \"josé\", [\'a\', \'b\'], \"cereja\", 1]\n")
cont = 0

for x in lista:
    cont+=1

print("\nResposta: ", cont)
print("\n-------------------------------------------------\n")