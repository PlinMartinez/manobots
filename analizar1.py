import shelve


db=shelve.open('datos.db')

lista=db['lista']

print(lista)

prueba1=lista[3]

print(prueba1)


import xlrd
from openpyxl.workbook import Workbook

book_xls = xlrd.open_workbook(prueba1)
book_xlsx = Workbook()
