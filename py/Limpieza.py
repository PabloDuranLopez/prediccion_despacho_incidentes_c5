# -*- coding: utf-8 -*-
#%%

import pandas as pd
import numpy as np
import os
ruta_dir = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(ruta_dir,"..", "data", "c5.csv"))
#%%
df.to_parquet(os.path.join(ruta_dir,"..","data","c5.parquet"))
print(df["codigo_cierre"].value_counts(normalize=True))
#%%
df=df.drop(columns=["colonia_catalogo","alcaldia_catalogo","folio","fecha_cierre","hora_cierre","alcaldia_cierre"])
#%%
df.loc[df["codigo_cierre"]=="A", "codigo_cierre"] = 1
df.loc[df["codigo_cierre"].isin(["N","D","F"]), "codigo_cierre"] = 0
df=df[df["codigo_cierre"]!='I']
#%%
df["codigo_cierre"].value_counts(normalize=True)
#%%
df["fecha"]=pd.to_datetime(df["fecha_creacion"])

df["hora_creacion"]=pd.to_datetime(df["hora_creacion"])
df["hora"]=df["hora_creacion"].dt.hour.astype('Int64')
df["mes"]=df["fecha"].dt.month.astype('Int64')

def clasificar(hora):
    if 0 <= hora <= 5:
        return "madrugada"
    elif 6 <= hora <= 10:
        return "mañana"
    elif 11 <= hora <= 17:   # o 10 < hora <= 17
        return "medio día"
    else:                     # 18 a 23
        return "tarde"

df["periodo"] = df["hora"].apply(clasificar)

df["fin_semana"] = (
    df["dia_semana"]
      .isin(["Sábado","Domingo"])
      .astype(int)
)


#%%
df=df.drop(columns=["fecha_creacion","hora_creacion"])
#%%
df.to_parquet(os.path.join(ruta_dir,"..","data","c5_limpio.parquet"))
print("Archivo c5_limpio.parquet guardado en la carpeta data.")