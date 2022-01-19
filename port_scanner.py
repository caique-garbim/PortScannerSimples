#!/usr/bin/python

import socket
import sys

print (" ")
ip = raw_input("[*] Digite o IP do host: ")
porta_i = input("[*] Digite a porta inicial (min 1): ")
porta_f = input("[*] Digite a porta final (max 65535): ")
print (" ")

for porta in range(porta_i,porta_f):
        meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        resposta = meusocket.connect_ex((ip,porta))
        if resposta==0:
                print ("- PORTA %d ==> ABERTA" %porta)
