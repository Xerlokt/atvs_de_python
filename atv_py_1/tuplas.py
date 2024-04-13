
tupla = ("maçã", "manga", "mamão")

#slide 86 - exec 1 -------------------------------------
print("\nMostre o 1° item da tupla abaixo:\ntupla = (\"maçã\", \"manga\", \"mamão\")\n")
print("\nResposta: ", tupla[0])
print("\n-------------------------------------------------\n")

#slide 86 - exec 2 -------------------------------------
print("\nIndique a quantidade de itens da tupla abaixo:\ntupla = (\"maçã\", \"manga\", \"mamão\")\n")
cont = 0
for x in tupla:
     cont+=1
print("\nResposta: ", cont)
print("\n-------------------------------------------------\n")

#slide 86 - exec 3 -------------------------------------
print("\nMostre o último item da tupla abaixo:\ntupla = (\"maçã\", \"manga\", \"mamão\")\n")
print("\nResposta: ", tupla[-1])
print("\n-------------------------------------------------\n")

#slide 88 - exec 1 -------------------------------------
print("\nMostrar 3°, 4° e 5° itens da tupla abaixo:\ntupla = (\"maçã\", \"manga\", \"mamão\", \"abacaxi\", \"cereja\", \"limão\", \"abacate\")\n")
tupla = ("maçã", "manga", "mamão", "abacaxi", "cereja", "limão", "abacate")
print("\nResposta: ", tupla[2:5])
print("\n-------------------------------------------------\n")