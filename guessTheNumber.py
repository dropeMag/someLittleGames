from random import randint

def adv(x):
    pcNum = randint(1, x)
    userNum = 0
    while userNum != pcNum:
        userNum = int(input(f'Adivinhe um número entre 1 e {x}: '))
        if userNum < pcNum:
            print('Errou! Chutou muito baixo.')
        elif userNum > pcNum:
            print('Errou! Chutou muito alto.')
    print(f'PARABÉNS, VOCÊ ACERTOU! ERA O NÚMERO {pcNum}.')

adv(15)
