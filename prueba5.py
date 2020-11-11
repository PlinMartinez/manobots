
from os import scandir, getcwd
import os
import xlwings as xw


def ls(ruta=getcwd()):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]


lista_archivos = ls()

lista_xls = []


def filtrar_xls(archivo):
    archivo_ext = archivo.split('.')[1]
    if archivo_ext == 'xls':
        lista_xls.append(archivo)


for arch in lista_archivos:
    filtrar_xls(arch)

print('tachan')
print(lista_xls)
prueba = lista_xls[1]
print(prueba)
wb = xw.Book(prueba)
wb.save('prueba.xlsx')
wb.close()


def convertir_extension(fichero):
    separar = fichero.split('.')
    solucion = separar[0] + '.xlsx'
    return solucion


for convertir in lista_xls:
    wb = xw.Book(convertir)
    bien = convertir_extension(convertir)
    wb.save(bien)
    wb.close()

print('termino todo ok')
