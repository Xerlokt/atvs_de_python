
conjunto = {"maçã", "banana", "cereja"}

#slide 118 - exec 1 -------------------------------------
print("\nVeja se \"maçã\" está no conjunto abaixo:\nfrutas = {\"maçã\", \"banana\", \"cereja\"}\n")
if("maçã" in conjunto):
    print("\nResposta: maçã está no conjunto citado")
else:
    print("\nResposta: maçã não está no conjunto citado")
print("\n-------------------------------------------------\n")

#slide 118 - exec 2 -------------------------------------
print("\nAdicione \"laranja\" ao conjunto abaixo:\nfrutas = {\"maçã\", \"banana\", \"cereja\"}\n")
conjunto.add("laranja")
print("\nResposta: ", conjunto)
print("\n-------------------------------------------------\n")

#slide 118 - exec 3 -------------------------------------
print("\nAdicione mais frutas ao conjunto abaixo:\nfrutas = {\"maçã\", \"banana\", \"cereja\"}\nmais_frutas = {\"laranja\", \"manga\", \"uva\"}\n")
conjunto = {"maçã", "banana", "cereja"}
mais_frutas = {"laranja", "manga", "uva"}

conjunto.update(mais_frutas)
print("\nResposta: ", conjunto)
print("\n-------------------------------------------------\n")

#slide 120 - exec 1 -------------------------------------
print("\nRemova \"banana\" do conjunto abaixo:\nfrutas = {\"maçã\", \"banana\", \"cereja\"}\n")
conjunto = {"maçã", "banana", "cereja"}

conjunto.remove("banana")
print("\nResposta: ", conjunto)
print("\n-------------------------------------------------\n")

#slide 120 - exec 2 -------------------------------------
print("\nRemova \"banana\" do conjunto abaixo, usando outra função, diferente da anterior:\nfrutas = {\"maçã\", \"banana\", \"cereja\"}\n")
conjunto = {"maçã", "banana", "cereja"}

conjunto.discard("banana")
print("\nResposta: ", conjunto)
print("\n-------------------------------------------------\n")

#slide 122 - exec 1 -------------------------------------
print("\nUna os conjuntos abaixo:\nfrutas = {\"maçã\", \"banana\", \"cereja\"}\nmais_frutas = {\"laranja\", \"manga\", \"uva\"}\n")
conjunto = {"maçã", "banana", "cereja"}
mais_frutas = {"laranja", "manga", "uva"}

conjuntos = conjunto.union(mais_frutas)
print("\nResposta: ", conjuntos)
print("\n-------------------------------------------------\n")