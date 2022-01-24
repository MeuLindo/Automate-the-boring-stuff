modeloTabuleiro = {
    'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
    'low-L': ' ', 'low-M': ' ', 'low-R': ' ',
}

def printTabuleiro(tabuleiro):
    print('|' + tabuleiro['top-L'] + '|' + tabuleiro['top-M'] + '|' + tabuleiro['top-R'] + '|')
    print('-+-+')
    print('|' + tabuleiro['mid-L'] + '|' + tabuleiro['mid-M'] + '|' + tabuleiro['mid-R'] + '|')
    print('-+-+')
    print('|' + tabuleiro['low-L'] + '|' + tabuleiro['low-M'] + '|' + tabuleiro['low-R'] + '|')


printTabuleiro(modeloTabuleiro)

turn = 'X'

for i in range(9):
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    modeloTabuleiro[move] = turn
    if turn =='X':
        turn = 'O'
    else:
        turn = 'X'

printTabuleiro(modeloTabuleiro)
