# A FUNÇÃO ABAIXO IRÁ VERIFICAR SE O NÚMERO É PAR OU ÍMPAR 
# E REALIZARÁ O CÁLCULO DE ACORDO COM O RESULTADO
def collatz(number):
        if(number%2 == 0):
            number = (number//2)
        elif(number%2 == 1):
            number = ((number*3)+1)
        return int(number)

# INICIANDO A VARIÁVEL COM '0' PARA NÃO HAVER POSSÍVEIS 
# INTERFERÊNCIAS DE MEMÓRIA
cont = 0

# O LAÇO ABAIXO SE TRATA DE UM TRATAMENTO DE ERRO, PARA EVITAR O
# 'INPUT' DE UMA STRING AO INVÉS DE UM NÚMERO INTEIRO
while True:
    try:
        print()
        numero = int(input(('Digite um numero inteiro qualquer: ')))
        break
    except ValueError as err:
        print()
        print('Necessário informar um NÚMERO INTEIRO!!')

while True:
    numero = collatz(numero) # O NÚMERO DIGITADO IRÁ RECEBER O CÁLCULO DA FUNÇÃO
    while True:
        try: # NOVAMENTE UM TRATAMENTO DE ERRO, IGUAL AO DE CIMA
            print()
            cont = int(input('Deseja continuar? (1) SIM ou (2) NÃO: '))
            break       
        except ValueError as err:
            print('Por gentileza, digite (1) se deseja continuar, ou (2) se deseja encerrar o programa')

    if(cont == 1): # SE DIGITADO '1', IRÁ CONTINUAR O CÁLCULO
        collatz(numero) # CHAMA NOVAMENTE A FUNÇÃO E FAZ O CÁLCULO
        print(numero) # EXIBE O NOVO RESULTADO
        if(numero == 1): # SE O NÚMERO CALCULADO ATINGIR O RESULTADO '1', ENCERRA O PROGRAMA
             break
    elif(cont == 2): # IGNORANDO A CONDIÇÃO ACIMA; SE DIIGTADO '2' O PROGRAMA É ENCERRADO APÓS O ÚLTIMO CÁLCULO SOLICITADO
        break 
    
