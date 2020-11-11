# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 12:38:34 2019

@author: MPAZ

Calcula el PC de todas las estructuras que estan en una carpeta

Paso1 : busca todos los ficheros xls (filtar tambien)
paso2 : abre cada fichero y lo pasa a xlsx (borrar antiguo despues)
paso3 : cierra todo
paso4 : abre desde pandas, mira el campo costes la suma
paso5 : graba un csv con codigo, pc


"""

from os import scandir, getcwd
import os
import xlwings as xw
import pandas as pd


def ls(ruta=getcwd()):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]


lista_archivos = ls()

lista_xlsx = []


def filtrar_xlsx(archivo):
    archivo_ext = archivo.split('.')[1]
    if archivo_ext == 'xlsx':
        lista_xlsx.append(archivo)


for arch in lista_archivos:
    filtrar_xlsx(arch)

'''
prueba=lista_xlsx[0]

df=pd.read_excel(prueba)

df2=df['importe_serpa'].sum()

df3=round(df2,2)

'''
f = open('BOMS.txt', 'w')


'''
f.write(prueba)
f.write(',')
f.write(str(df3))
f.write('\n')
'''


def grabar(codigo, coste):
    f.write(codigo)
    f.write(',')
    f.write(str(coste))
    f.write('\n')


print(lista_xlsx)


for xlsx in lista_xlsx:
    try:

        codigo = xlsx
        df = pd.read_excel(codigo)
        df2 = df['importe_coste'].sum()
        coste = round(df2, 2)
		coste= coste *100
        grabar(codigo, coste)
    except:
        print("algo fallo en fichero " + xlsx)


f.close()
