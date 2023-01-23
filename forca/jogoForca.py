from palavras import palavras
import random

def titulo(t):
    print('=' * 30)
    print(f'{t.upper():^30}')
    print('=' * 30)


def escolherPalavra():
    escolha = random.choice(palavras)
    return escolha.upper()


def forca():
    global palavra
    palavra = escolherPalavra()
    letras_palavra = set(palavra)
    letras_usadas = list()
    titulo('jogo da forca')
    vidas = 6

    while True:
        lista_letras = [p if p in letras_usadas else '_' for p in palavra]
        letras_escondidas = ''.join(lista_letras)

        if '_' not in letras_escondidas:
            return True
        elif vidas == 0:
            return False

        print(f'ADIVINHE: {letras_escondidas}')

        print('')
        print(f'Vidas: {vidas}')
        print(f'Letras usadas:', ' '.join(letras_usadas),)
        user_letra = input('Escolha uma Letra: ').strip().upper()

        if len(user_letra) > 1 or not user_letra.isalpha():
            print('Escolha uma letra válida.')
        elif user_letra in letras_usadas:
            print('Letra repetida, escolha outra.')
        else:
            letras_usadas.append(user_letra)

            if user_letra in letras_palavra:
                letras_palavra.remove(user_letra)
            else:
                vidas -= 1

        print('-' * 30)


palavra = ''

if forca():
    titulo('parabéns, você venceu!')
    print(f'{f"Você adivinhou: {palavra}":^30}')
else:
    titulo('que pena, você perdeu')
    print(f'{f"Resposta: {palavra}":^30}')

finalizar = input(f"\n{'ENTER PARA FINALIZAR':^30}")
