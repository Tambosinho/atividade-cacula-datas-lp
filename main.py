# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 07:47:06 2023

@author: joaod
"""

from funcao import calcula_dif
from retorna_arquivo import retorna_arquivo

# Tenta ler as duas opções
datas = input("Forneça o nome do arquivo ou a data desejada:")

if "-" in datas: 
    datas = datas
    
else: 
    datas = retorna_arquivo(datas)


dif_datas = calcula_dif(datas)

# Print days:
print("Número de dias entre as duas datas:", dif_datas)

