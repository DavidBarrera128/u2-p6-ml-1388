import pandas as pd
import numpy as np

serie_amigos = ["Pedro","Morgan","El Adrian","Jesse","Farfan","Eliseo","Mario"]
print("serie instalado de amigos NC = 1388")
amigos = pd.Series(serie_amigos)
print(amigos)

serie_billetes = [20,50,100,200,500,1000]
print("serie instalado valor de billetes MX NC = 1388")
amigos = pd.Series(serie_billetes)
print(amigos)

serie_billetes = [20,50,100,200,500,1000]
serie_bletras = ["veinte","cincuenta","cien","docientos","quinientos","mil"]
print("serie instalado valor de billetes MX NC = 1388")
tablabilletes = pd.Series(serie_bletras, serie_billetes)
print(tablabilletes)
# diccionario DataFrame
# diccionario de valor monedas y nombre
print("Datos de diccionario DataFrame en pandas")
dic_monedas ={
    "serie_billetes":[20,50,100,200,500,1000],
    "serie_nletras":["veinte","cincuenta","cien","docientos","quinientos","mil"]

}

tablabilletes=pd.DataFrame(dic_monedas,index=["A","B","C","D","E","F"])
print(tablabilletes)

print("casa de cambio David Barrera NC = 1388")