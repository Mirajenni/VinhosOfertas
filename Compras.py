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
import csv 

transaction = pd.read_csv('./Transactions2.csv', delimiter=';')

lista = [list(row) for row in transaction.values]
# Print list of lists i.e. rows
print(lista)
def findItem(theList, item):
   return [(ind, theList[ind].index(item)) for ind in range(len(theList)) if item in theList[ind]]

transacoes = [] 
for i, j in lista:
    #if current rows 2nd value is equal to input, print that row
   pessoa = i
   oferta = j
   transacao = [0] * 33
   if pessoa in (item for sublist in transacoes for item in sublist):
       ind = (findItem(transacoes, pessoa)) # [(0, 0)]
       ind = ind[0][0]
       transacoes[ind].insert(oferta, "1")
   else:
       transacao.insert(0, pessoa)
       transacao.insert(oferta, "1")
       transacoes.append(transacao) 
   
print(transacoes)
header = ['Pessoa', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21',
    '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32']
    
with open('TransactionsByPerson.csv', 'w',  newline='', encoding='utf-8') as f: 
    # using csv.writer method from CSV package 
    write = csv.writer(f) 
    write.writerow(header) 
    write.writerows(transacoes) 
    
