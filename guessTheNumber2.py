from random import randint

def adv(x):
    men = 1
    mai = x
    resp = ''
    while resp != 'c':
        pcTry = randint(men, mai)
        print(f'{pcTry} é:')
        print('(A) Muito Alto')
        print('(B) Muito Baixo')
        print('(C) Correto')
        resp = input('R.: ').lower().strip()
        print('\n')
        if resp == 'a':
            mai = pcTry - 1
        elif resp == 'b':
            men = pcTry + 1
    print(f'EBA O NÚMERO CORRETO ERA {pcTry}')

adv(1000)
