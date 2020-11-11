# COGE EL FICHERO art23.xlsx con las ventas y saca los valores que son interesantes solamente
# cuando termina genera el fichero de resumen y otro quitando los duplicados con las estructuras a revisar

import pandas as pd

df = pd.read_excel('art23.xlsx')

df2 = df[df['ref_fabricante_productos'] == 23]

df2 = df2.drop('comision', axis=1)


df3 = df2.sort_values(['nombre_albaranes_venta_facturados',
                       'producto'], ascending=[True, True])


df4 = df3[['producto', 'descripcion']]
df5 = df4.drop_duplicates()

df3.to_excel('fichero1.xlsx')
df5.to_excel('estructuras.xlsx')
