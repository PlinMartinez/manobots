from os import scandir, getcwd
import os
import xlwings as xw


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


print('tachan')
print(lista_xlsx)
prueba = lista_xlsx[0]


import pandas as pd


'''
df = pd.read_excel(prueba)

df.drop(['compuesto'], axis='columns', inplace=True)

columnas = ['nivel', 'componente']
df2 = df[['nivel', 'componente', 'denominación', 'almacen', 'stock', 'cantidad',
          'coste', 'importe_serpa', 'nombre_prov']]

nombre = 'XX' + prueba

# df2.to_excel(nombre)

suma = sum(df['importe_serpa'])

df2 = df2.append(df2.sum(numeric_only=True), ignore_index=True)
df3 = df2[df2['componente'] == 'TM0001']

df2 = df2.append(df3)
df2.to_excel(nombre)
'''


for xlsx in lista_xlsx:
    try:
        df = pd.read_excel(xlsx)

        df.drop(['compuesto'], axis='columns', inplace=True)

        columnas = ['nivel', 'componente']
        df2 = df[['nivel', 'componente', 'denominación', 'almacen', 'stock', 'cantidad',
                  'coste', 'importe_serpa', 'nombre_prov']]

        nombre = 'XX' + prueba

        # df2.to_excel(nombre)
        
        suma = sum(df['importe_serpa'])

        df2 = df2.append(df2.sum(numeric_only=True), ignore_index=True)
        df3 = df2[df2['componente'] == 'TM0001']
        
        df2 = df2.append(df3)
        df2.to_excel(nombre)

        nombre = 'XX' + xlsx
        df2.to_excel(nombre)
        print('bien!!')
    except:
        print('algo peto...')
        print(xlsx)

