import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# crearemos nuestra tabla y la guardaremos con pandas
# Tenemos 5 listas de redes sociales con 4 elementos por lista
fb = ['Facebook', 8833, True, 2006]
twt = ['Twitter', 8575, False, 2008]
ig = ['Instagram', 7575, True, 2010]
wsp = ['Whatsapp', 8828, True, 2009]
tel = ['Telegram', 2992, False, 2010]
lkn = ['Linkdin', 7277, False, 2012]
# Creamos una lista de listas
lista_redes_sociales = [fb, twt, ig, wsp, tel, lkn]
# print(lista_redes_sociales)
# Usar Pandas para organizar la tabla (DataFrame)
# A cada columna le ponemos nombre
df_redes_sociales = pd.DataFrame(lista_redes_sociales,columns=["Nombre","Cantidad","Es_FB","Años",])
print(df_redes_sociales)
# Creamos el archivo csv y lo guardamos en csv
df_redes_sociales.to_csv("redessociales.csv", index=False)
# Crear grafica de lineas 
# Donde X es "Nombre" en el eje horizontal
# Donde Y es "Cantidad" en eje vertical
plt.plot(df_redes_sociales["Nombre"],df_redes_sociales["Cantidad"])
plt.table("Grafica redes sociales 0148")
plt.xlabel("Nombre de la red social")
plt.ylabel("Cantidad de usuarios")
plt.show()
# Creamos una grafica de puntos 
plt.scatter (df_redes_sociales["Nombre"],df_redes_sociales["Cantidad"])
plt.show()
# Grafica de barras
plt.bar (df_redes_sociales["Nombre"],df_redes_sociales["Cantidad"])
# Etiquietas y titulos
plt.title("Redes sociales 0148")
plt.xlabel("las redes")
plt.ylabel("Usuarios")
# Mostrar
plt.show()
# Ordenar la grafiuca de manera descendenmte
# Van de la mas grande a las mas pequeña
df_rs_ordenada = df_redes_sociales.sort_values("Cantidad",ascending=False)
plt.bar(df_rs_ordenada["Nombre"], df_rs_ordenada["Cantidad"])
plt.show()
# Coloreando la grafica 
df_rs_ordenada = df_redes_sociales.sort_values("Cantidad",ascending=False)
plt.bar(df_rs_ordenada["Nombre"], df_rs_ordenada["Cantidad"],
        color = ["b","g","c","m","y","r"])
plt.show()
# Grafica de pastel
# plt.plot(df_redes_sociales["Nombre"],df_redes_sociales["Cantidad"])
plt.pie(df_redes_sociales["Cantidad"], labels=df_redes_sociales["Nombre"])
plt.show()
