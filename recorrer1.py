#consigue una lista con la ruta y los archivos a analizar

import os
import shelve

db=shelve.open('datos.db')




lista_ficheros=[]

rootDir = '.'
for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
    print('Directorio encontrado: %s' % dirName)
    for fname in fileList:
        print('\t%s' % fname)
        lista_ficheros.append(fname)

print(lista_ficheros)

db['lista']=lista_ficheros




