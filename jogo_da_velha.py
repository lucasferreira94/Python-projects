'''
JOGO DA VELHA
'''

# ABAIXO ESTAO AS POSIÇÕES DA CERQUILHA

theBoard = {'top-L':'', 'top-M':'', 'top-R':'', 
            'mid-L':'','mid-M':'', 'mid-R':'',
            'low-L':'', 'low-M':'', 'low-R':''}

print ('Choose one Space per turn')
print()
print(' top-L'+' top-M'+ ' top-R')
print()   
print(' mid-L'+' mid-M'+ ' mid-R')  
print()
print(' low-L'+' low-M'+ ' low-R ')          
print()

# FUNÇÃO PARA PRINTAR A CERQUILHA NA TELA

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] +'|' + board['top-R'])
    print('+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

# O JOGO INICIA PELA VEZ DO 'X'

turn = 'X'

for i in range(9):  
    printBoard(theBoard) 
    print('Turn for ' + turn + '. Move on wich space? ') # INDICA A VEZ DO JOGADOR
    move = input() # O JOGADOR DEVERÁ COLOCAR A POSIÇÃO QUE QUER JOGAR
    theBoard[move] = turn # ASSOCIA A JOGADA AO JOGADOR
    print()
    # CONDICIONAL PARA REALIZAR A MUDANÇA DE JOGADOR
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard) 
