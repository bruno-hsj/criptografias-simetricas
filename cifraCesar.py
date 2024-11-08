#Código para criptografar e descriptografar a Cifra de César

def criptografarCesar (mensagem, chave):
    chave = int(chave)
    alfabetoMin = 'abcdefghijklmnopqrstuvwxyz'
    alfabetoMai = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    textoCifrado =''

    for i in mensagem:
        if (i == ' '):
            textoCifrado += " "
        elif (i.isupper() and i.isalpha()):
            posicao = (ord(i) - ord('A') + chave) % 26
            textoCifrado += alfabetoMai[posicao]
        elif(i.islower and i.isalpha()):
            posicao = (ord(i) - ord('a') + chave) % 26
            textoCifrado += alfabetoMin[posicao]
        else:
            textoCifrado += i

    toString = 'Mensagem original: {} --- Mensagem cifrada: {}'.format(mensagem, textoCifrado)
    return toString
def descriptografarCesar(mensagem, chave):
    chave = int(chave)
    alfabetoMin = 'abcdefghijklmnopqrstuvwxyz'
    alfabetoMai = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    textoDescriptografado = ''

    for i in mensagem:
        if (i == ' '):
            textoDescriptografado += " "
        elif (i.isupper() and i.isalpha()):
            posicao = (ord(i) - ord('A') - chave) % 26
            textoDescriptografado += alfabetoMai[posicao]
        elif (i.islower and i.isalpha()):
            posicao = (ord(i) - ord('a') - chave) % 26
            textoDescriptografado += alfabetoMin[posicao]
        else:
            textoDescriptografado += i

    toString = 'Mensagem cifrada: {} --- Mensagem original: {}'.format(mensagem, textoDescriptografado)
    return toString
def descriptografarBruto(mensagem):
    alfabetoMin = 'abcdefghijklmnopqrstuvwxyz'
    alfabetoMai = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    textoDescriptografado = ''
    possiveisMensagens = []

    for i in range (0, 26):
        for j in mensagem:
            if (j == ' '):
                textoDescriptografado += " "
            elif (j.isupper() and j.isalpha()):
                posicao = (ord(j) - ord('A') - i) % 26
                textoDescriptografado += alfabetoMai[posicao]
            elif (j.islower() and j.isalpha()):
                posicao = (ord(j) - ord('a') - i) % 26
                textoDescriptografado += alfabetoMin[posicao]

        possiveisMensagens.append((i, textoDescriptografado))
        textoDescriptografado = ''
    toString = 'Mensagem cifrada: {} --- Quebra com FORÇA BRUTA: {}'.format(mensagem, possiveisMensagens)
    return toString
def descriptografarFrequencia(mensagem):
    alfabetoMin = 'abcdefghijklmnopqrstuvwxyz'
    alfabetoMai = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    textoDescriptografado = ''
    maxPalavras = 0
    palavrasComuns = ['que', 'ent', 'nte', 'ado', 'ade', 'ode', 'ara', 'est', 'res', 'con']
    letrasComuns = ['a', 'e', 'o', 's', 'r']

    frequeciaLetra = {}
    for letra in mensagem:
        if letra in alfabetoMin or letra in alfabetoMai:
            if letra in frequeciaLetra:
                frequeciaLetra[letra] += 1
            else:
                frequeciaLetra[letra] = 1

    letraMaisFrequente = max(frequeciaLetra, key=frequeciaLetra.get)

    for letraAlvo in letrasComuns:
        chave = (ord(letraMaisFrequente) - ord(letraAlvo)) % 26

        for j in mensagem:
            if (j == ' '):
                textoDescriptografado += " "
            elif (j.isupper() and j.isalpha()):
                posicao = (ord(j) - ord('A') - chave) % 26
                textoDescriptografado += alfabetoMai[posicao]
            elif (j.islower() and j.isalpha()):
                posicao = (ord(j) - ord('a') - chave) % 26
                textoDescriptografado += alfabetoMin[posicao]
            else:
                textoDescriptografado += j

        qtdPalavrasCorretas = 0
        qtdPalavrasCorretas = sum(palavra in textoDescriptografado.lower() for palavra in letrasComuns)

        if (qtdPalavrasCorretas > maxPalavras):
            maxPalavras = qtdPalavrasCorretas
            melhorMensagem = textoDescriptografado
            melhorChave = chave

        textoDescriptografado = ''

    toString = 'Mensagem cifrada: {} --- Quebra com Distribuição de Frequências: {} --- Chave: {}'.format(mensagem, melhorMensagem, melhorChave)
    return toString
def menu():
    while (True):
        print('--- Algoritmo de Criptografia de Cesar ---')
        op = int(input('Menu:\n (1) Criptografar Mensagem \n (2) Descriptografar Mensagem \n (3) Descriptografar FORÇA BRUTA \n'
                       ' (4) Descriptografar Melhor Frequência \n (0) Encerrar '))
        if(op == 1):
            textoClaro = input('Informe o texto em claro: ')
            chave = input('Informe a chave da cifra: ')
            print(criptografarCesar(textoClaro, chave))

        elif(op == 2):
            mensagemCifrada = input('Informe o texto CIFRADO: ')
            chave = input('Informe a chave da cifra: ')
            print(descriptografarCesar(mensagemCifrada, chave))

        elif(op == 3):
            mensagemCifrada = input('Informe o texto CIFRADO: ')
            print(descriptografarBruto(mensagemCifrada))

        elif (op == 4):
            mensagemCifrada = input('Informe o texto CIFRADO: ')
            print(descriptografarFrequencia(mensagemCifrada))

        elif(op == 0):
            break

        else:
            print('Opção Inválida')

menu()

