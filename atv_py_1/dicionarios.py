dicionario = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 1964
}

#slide 147 - exec 1 -------------------------------------
print("\nMostrar a chave \"modelo\" no dicionário abaixo:\ncarro = {\n   \"marca\": \"Ford\", \n   \"modelo\": \"Mustang\", \n   \"ano\": \"1964\"\n}\n")
print("\nResposta: ", dicionario["modelo"])
print("\n-------------------------------------------------\n")

#slide 147 - exec 2 -------------------------------------
print("\nMudar ano para \"2020\" no dicionário abaixo:\ncarro = {\n   \"marca\": \"Ford\", \n   \"modelo\": \"Mustang\", \n   \"ano\": \"1964\"\n}\n")
dicionario["ano"] = 2020
print("\nResposta: ", dicionario)
print("\n-------------------------------------------------\n")

#slide 149 - exec 1 -------------------------------------
print("\nAdicionar o par \"cor\":\"vermelho\" no dicionário abaixo:\ncarro = {\n   \"marca\": \"Ford\", \n   \"modelo\": \"Mustang\", \n   \"ano\": \"1964\"\n}\n")
dicionario = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 1964
}

dicionario["cor"] = "vermelho"
print("\nResposta: ", dicionario)
print("\n-------------------------------------------------\n")