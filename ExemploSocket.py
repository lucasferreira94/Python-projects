# -*- coding: utf-8 -*-
#!/usr/bin/python
import socket
import sys

while True:
    ip = raw_input("informe o IP: ")
    porta = input("Informe a porta: ")

    meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    resp = meusocket.connect_ex((ip, porta))  # se a conexão for bem sucedida, ele irá retornar 0

    if (resp == 0):
        print("Porta aberta\n")
    elif (resp != 0):
        print("Porta fechada\n")
  
    cont = input("Deseja continuar com o teste?, digite 1 para (SIM) e 2 para (NÃO) \n")

    if(cont == 1):
        continue
        
    elif(cont == 2):
        print("Script encerrado!")
        break 
    
    elif(cont !=1 or cont != 2):
        print("Argumento inválido!\n")
    
         