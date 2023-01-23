import random


def jogo():
    pcJog = random.choice(['p', 'r', 's'])
    print('"r" para Pedra; "p" para Papel; "s" para Tesoura;')
    urJog = input('Escolha: ').lower().strip()

    if pcJog == urJog:
        return 'Deu Empate!'
    elif (urJog == 'r' and pcJog == 's') or (urJog == 's' and pcJog == 'p') or (urJog == 'p' and pcJog == 'r'):
        return 'Você Venceu!'
    else:
        return 'Você Perdeu!'


print(jogo())
