# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 05:58:03 2020

@author: Jenni
"""

import os
os.chdir("D:\Jenni\Documents\Data Science\Dados")

import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import numpy as np 

transaction = pd.read_csv('./TransactionsByPerson.csv', delimiter=';')
information = pd.read_csv('./OfferInformation.csv')

from sklearn.cluster import KMeans
from matplotlib import pyplot as plt

dados = transaction.iloc[:, 1:33]
#Para 3 clusters
kmeans = KMeans(n_clusters = 3, #numero de clusters
init = 'k-means++', n_init = 10, #algoritmo que define a posição dos clusters de maneira mais assertiva
max_iter = 5000) #numero máximo de iterações
pred_y = kmeans.fit_predict(dados)

dados['cluster'] = pred_y

sum_cluster3 = pd.DataFrame()
sum_cluster3['A'] = dados.loc[dados['cluster']==0].iloc[:, 0:32].sum() #0, 8
sum_cluster3['B'] = dados.loc[dados['cluster']==1].iloc[:, 0:32].sum() #0, 9
sum_cluster3['C'] = dados.loc[dados['cluster']==2].iloc[:, 0:32].sum() #0, 10

#sum_cluster3.to_csv('Cluster3.csv', mode='w', header=False, sep=';')

#Para 4 clusters
kmeans = KMeans(n_clusters = 4, #numero de clusters
init = 'k-means++', n_init = 10, #algoritmo que define a posição dos clusters de maneira mais assertiva
max_iter = 5000) #numero máximo de iterações
pred_y = kmeans.fit_predict(dados)
dados['cluster'] = pred_y
sum_cluster4 = pd.DataFrame()
sum_cluster4['A'] = dados.loc[dados['cluster']==0].iloc[:, 0:32].sum()
sum_cluster4['B'] = dados.loc[dados['cluster']==1].iloc[:, 0:32].sum()
sum_cluster4['C'] = dados.loc[dados['cluster']==2].iloc[:, 0:32].sum()
sum_cluster4['D'] = dados.loc[dados['cluster']==3].iloc[:, 0:32].sum()
print()

#Para 5 clusters
kmeans = KMeans(n_clusters = 5, #numero de clusters
init = 'k-means++', n_init = 10, #algoritmo que define a posição dos clusters de maneira mais assertiva
max_iter = 5000) #numero máximo de iterações
pred_y = kmeans.fit_predict(dados)
dados['cluster'] = pred_y
sum_cluster5 = pd.DataFrame()
sum_cluster5['A'] = dados.loc[dados['cluster']==0].iloc[:, 0:32].sum()
sum_cluster5['B'] = dados.loc[dados['cluster']==1].iloc[:, 0:32].sum()
sum_cluster5['C'] = dados.loc[dados['cluster']==2].iloc[:, 0:32].sum()
sum_cluster5['D'] = dados.loc[dados['cluster']==3].iloc[:, 0:32].sum()
sum_cluster5['E'] = dados.loc[dados['cluster']==4].iloc[:, 0:32].sum()
sum_cluster5.to_csv('Cluster5.csv', mode='w', header=False, sep=';')
print()