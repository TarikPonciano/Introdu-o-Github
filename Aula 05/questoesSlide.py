#Questão 1 - Dado o nome de uma pessoa, 
#retorne o número de letras do nome e a primeira
#letra do nome.
def questao1():
    nome = input("Digite seu nome: ")

    #Modo 1
    numeroLetras = len(nome) - nome.count(" ")

    contadorLetras = 0

    #Modo 2
    for letra in nome:

        if letra != " ":
            contadorLetras += 1

    print("Número de letras", numeroLetras)
    print("Primeira letra", nome[0])

#Questão 2 - Dada uma palavra, retorna a palavra invertida

def questao2():

    palavra = "Coca Cola"
    inverso = ""

    #Modo 1
    print(palavra[::-1])

    for i in range(len(palavra)):

        inverso += palavra[len(palavra)-1-i]

    print(inverso)


questao2()