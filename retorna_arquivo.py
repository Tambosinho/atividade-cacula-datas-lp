# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 08:30:53 2023

@author: joaod
"""
# Erro de Documento não encontrado
def retorna_arquivo(filename):
    try:
        with open(f"{filename}.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Arquivo '{filename}.txt' não encontrado. Por favor, forneça um arquivo válido.")
        return None
