import random
from palavras import palavras_lista

def buscar_palavra():
    palavra = random.choice(palavras_lista)
    return palavra.upper()

def jogar(palavra):
    palavra_completa = '_' * len(palavra)
    advinhada = False
    letras_advinhadas = []
    palavras_advinhadas = []
    tentativas = 6
    print('Vamos jogar Forca!')
    print(mostrar_forca(tentativas))
    print(palavra_completa)
    print('\n')
    while not advinhada and tentativas > 0:
        palpite = input('Advinhe uma letra ou palavra: ').upper()
        if len(palpite) == 1 and palpite.isalpha():
            if palpite in letras_advinhadas:
                print(f'Você já tentou essa letra {palpite}')
            elif palpite not in palavra:
                print(f'{palpite} não está na palavra')
                tentativas -= 1
                letras_advinhadas.append(palpite)
            else:
                print(f'Bom trabalho, {palpite} está na palavra!')
                letras_advinhadas.append(palpite)
                lista_de_palavras = list(palavra_completa)
                indices = [i for i, letra in enumerate(palavra) if letra == palpite]
                for indice in indices:
                    lista_de_palavras[indice] = palpite
                    palavra_completa = ''.join(lista_de_palavras)
                    if '_' not in palavra_completa:
                        advinhada = True
        elif len(palpite) == len(palavra) and palpite.isalpha():
            if palpite in palavras_advinhadas:
                print(f'Você já advinhou a palavra {palpite}')
            elif palpite != palavra:
                print(f'{palpite} não está na palavra')
                tentativas -= 1
                palavras_advinhadas.append(palavras_advinhadas)
            else: advinhada = True
            palavra_completa = palavra
        else:
            print('Palpite inválido.')
        print(mostrar_forca(tentativas))
        print(palavra_completa)
        print('\n')
    if advinhada:
        print('Parabéns! você advinhou a palavra! Você venceu!')
    else:
        print(f'Desculpe, suas tentativas acabaram. a palavra era {palavra}, talvez na próxima!')

def mostrar_forca(tentativas):
    estagio = [ """
                 --------
                |       |
                |       O
                |      \\|/
                |       |
                |      / \\
                -
                """,
                """
                 --------
                |       |
                |       O
                |      \\|/
                |       |
                |      / 
                -
                """,
                """
                 --------
                |       |
                |       O
                |      \\|/
                |       |
                |        
                -
                """,
                """
                 --------
                |       |
                |       O
                |      \\|
                |       |
                |        
                -
                """,
                """
                 --------
                |       |
                |       O
                |       |
                |       |
                |        
                -
                """,
                """
                 --------
                |       |
                |       O
                |       |
                |       
                |        
                -
                """,
                """
                 --------
                |       |
                |       O
                |       
                |       
                |        
                -
                """,
                """
                 --------
                |       |
                |       
                |       
                |       
                |        
                -
                """,
    ]
    return estagio[tentativas]


def main():
    palavra = buscar_palavra()
    jogar(palavra)
    while input('Jogar Novamente? (Sim/Não) ').upper() == 'Sim':
        palavra = buscar_palavra()
        jogar(palavra)


if __name__=='__main__':
    main()
