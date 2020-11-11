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

def ls(ruta=getcwd()):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]

lista_archivos=ls()

lista_xls=[]

def filtrar_xls(archivo):
    archivo_ext=archivo.split('.')[1]
    if archivo_ext=='xls':
        lista_xls.append(archivo)

for arch in lista_archivos:
    filtrar_xls(arch)

print('tachan')



def convertir_extension(fichero):
    separar=fichero.split('.')
    solucion=separar[0]+'.xlsx'
    return solucion

for convertir in lista_xls:
    wb=xw.Book(convertir)
    bien=convertir_extension(convertir)
    wb.save(bien)
    wb.close()
    
    

    
    








