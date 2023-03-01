#Questão 1 - Escreva um programa em Python para somar todos os itens de uma lista.

def questao1():
    lista = [20,35,67,10,-50]

    soma = 0

    for numero in lista:

        soma = soma + numero

    print(soma)

#Questão 2 - Escreva um programa em Python para multiplicar todos os itens de uma lista.

def questao2():

    lista = [10,30,25,10,85]

    multiplicacao = 1

    for numero in lista:
        multiplicacao = multiplicacao * numero

    print(multiplicacao)


#Questão 3 - Escreva um programa em Python para obter o maior número de uma lista.

def questao3():
    lista = []
    for i in range(5):
        numeroInteiro = int(input("Digite um inteiro"))
        lista.append(numeroInteiro)
    

    maior = lista[0]

    for numero in lista:
        
        if numero > maior:
            maior = numero

    print(maior)

def questao3Alternativo():
    lista = [10,30,25,10,80]

    for i in range(len(lista)):
        if i == 0:
            maior = lista[i]
        else:
            if lista[i] > maior:
                maior = lista[i]

    print(maior)

#Questão 4 - Escreva um programa em Python para obter o menor número de uma lista.

def questao4():

    lista = [10,30,25,10,80]

    menor = lista[0]

    for numero in lista:
        if numero < menor:
            menor = numero
    print(menor)

#Questão 5 - Escreva um programa Python para contar o número de strings de 
# uma determinada lista de strings. O comprimento da string é 2 ou mais e 
# o primeiro e o último caractere são os mesmos. 
# Lista de amostras: ['abc', 'xyz', 'aba', '1221']

def questao5():
    lista = ['abc', 'xyz', 'aba', '1221', '12314141','34242','asddf','as','a']

    contador = 0

    for termo in lista:

        if len(termo) >= 2:
            if termo[0] == termo[-1]:
                contador += 1

    print(contador)

questao5()
