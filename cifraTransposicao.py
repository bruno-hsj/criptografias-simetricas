import numpy as np

def codificarRailFence(mensagem, chave):
    if chave < 2:
        chave += 1
    chave = chave % 10
    matriz = [['*' for i in range(len(mensagem))] for j in range(chave)]
    direcao = False
    linha = 0
    coluna = 0
    temp = []
    mensagemCodificada = ''

    for letra in mensagem:
        if(linha == 0 or linha == chave -1):
            direcao = not direcao

        matriz[linha][coluna] = letra

        coluna += 1

        if(direcao):
            linha += 1
        else:
            linha -= 1

    for i in range(chave):
        for j in range(len(mensagem)):
            if (matriz [i][j] != "*"):
                temp.append(matriz[i][j])
    mensagemCodificada = ''.join(temp)

    matrizStr = "\n".join(["".join(linha) for linha in matriz])

    toString = '{} --- Matriz de Cifra \n Mensagem Cifrada: {} \n Mensagem Original: {}'.format(matrizStr, mensagemCodificada, mensagem)

    return toString

def testadorRailFence(mensagem, chave):
    matriz = [['\n' for i in range(len(mensagem))] for j in range(chave)]
    direcao = None
    linha= 0
    coluna = 0

    for i in range(len(mensagem)):
        if linha == 0:
            direcao = True

        if linha == chave - 1:
            direcao = False

        matriz[linha][coluna] = '*'
        coluna += 1

        if (direcao):
            linha += 1
        else:
            linha -= 1

    index = 0
    for i in range(chave):
        for j in range(len(mensagem)):
            if matriz[i][j] == '*' and index < len(mensagem):
                matriz[i][j] = mensagem[index]
                index += 1

    result = []
    linha, coluna = 0, 0
    for i in range(len(mensagem)):
        if linha == 0:
            direcao = True

        if linha == chave - 1:
            direcao = False

        if matriz[linha][coluna] != '*':
            result.append(matriz[linha][coluna])
            coluna += 1

        if (direcao):
            linha += 1
        else:
            linha -= 1

    return "".join(result)

def decodificarRailFence(mensagem):
    for chave in range(2, 11):
        textoDescriptografado = testadorRailFence(mensagem, chave)
        print(f"Chave {chave}: {textoDescriptografado}")
    return 'Lista de Possibilidades - Forca Bruta'

def menu():
    while (True):
        print('--- Algoritmo de Criptografia de Transposição (Rail Fence) ---')
        op = int(input('Menu:\n (1) Criptografar Mensagem \n (2) Descriptografar Mensagem \n (0) Encerrar '))
        if(op == 1):
            textoClaro = input('Informe o texto em claro: ')
            chave = int(input('Informe a chave da cifra: '))
            print(codificarRailFence(textoClaro, chave))

        elif(op == 2):
            mensagemCifrada = input('Informe o texto CIFRADO: ')
            print(decodificarRailFence(mensagemCifrada))

        elif(op == 0):
            print('Fim de Execução.')
            break

        else:
            print('Opção Inválida')

menu()