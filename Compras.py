# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 20:45:39 2020

@author: Jenni
"""


#Usando os dados de ofertas de vinho no mercado de atacado, defina profiles de
#compras baseando-se nas transações.
#Use o algoritmo K-Means para seguimento os clientes baseado nas
#características de suas compras.

import os
os.chdir("D:\Jenni\Documents\Data Science\Dados")

import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import numpy as np
import csv

transaction = pd.read_csv('./Transactions2.csv')
information = pd.read_csv('./OfferInformation.csv')

#age, spending core
#criar uma nova tabela de information para pessoa e ofertas, com 0 e 1.

print(transaction)

#Criar um csv de 32 colunas (ofertas) pela quantidade de pessoas não repetidas
#ofertas
import csv
pessoas = []
'''with open('TransactionsByPerson.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Pessoa", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21",
    "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32"])
    #writer.writerow([1, "Linus Torvalds", "Linux Kernel"])'''
    
for i in range(len(transaction)):
    pessoa = transaction.values[i][0]
    #x = ['p','y','t','h','o','n']
    #print(x.index('o'))
    #acha o index da pessoa tal e coloca em [index][offer]
    p = pessoa.split(";")[0]
    if not p in pessoas:
        pessoas.append(p)
    offer = pessoa.split(";")[-1]
    #np.insert()
print(pessoas)
    
