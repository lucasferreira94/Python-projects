def collatz(number):
        if(number%2 == 0):
            number = (number//2)
        elif(number%2 == 1):
            number = ((number*3)+1)
        return int(number)
cont = 0

while True:
    try:
        print()
        numero = int(input(('Digite um numero inteiro qualquer: ')))
        break
    except ValueError as err:
        print()
        print('Necessário informar um NÚMERO INTEIRO!!')

while True:
    numero = collatz(numero) 
    while True:
        try: 
            print()
            cont = int(input('Deseja continuar? (1) SIM ou (2) NÃO: '))
            break       
        except ValueError as err:
            print('Por gentileza, digite (1) se deseja continuar, ou (2) se deseja encerrar o programa')

    if(cont == 1):
        collatz(numero)
        print(numero) 
        if(numero == 1): 
             break
    elif(cont == 2): 
        break 
    
