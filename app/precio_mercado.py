# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 11:38:06 2025

@author: fenris123
"""



import os
import requests
import json
from datetime import datetime
import pandas as pd


# Obtener el token desde la variable de entorno (seteada en GitHub Secrets)
Token_esios = os.getenv("TOKEN_ESIOS")

if not Token_esios:
    raise ValueError("No se encontró la variable de entorno TOKEN_ESIOS. Asegúrate de configurarla.")


# Headers para la autenticación
headers = {
    'Host': 'api.esios.ree.es',
    'x-api-key': Token_esios
}

# URL base y endpoint
URL_BASE = 'https://api.esios.ree.es/'
ENDPOINT = 'indicators/'


# Obtener la fecha de hoy en formato YYYY-MM-DD


start_date = datetime.utcnow().date().isoformat()
end_date = datetime.utcnow().date().isoformat()

params = {
    'start_date': f'{start_date}T00',
    'end_date': f'{end_date}T23'
}


# ID del indicador
INDICATOR = '600'
url = URL_BASE + ENDPOINT + INDICATOR


# Realizar la solicitud GET
res = requests.get(url, headers=headers, params=params)

# Procesar la respuesta en formato JSON
data = res.json()

# Filtrar los datos para obtener solo los registros de "España" (geo_id = 3)
filtered_data = [record for record in data.get('indicator', {}).get('values', []) if record.get('geo_id') == 3]

# Crear DataFrame a partir de los datos filtrados
df = pd.DataFrame(filtered_data)

# Seleccionar columnas y renombrar
df = df[['datetime', 'value']].rename(columns={'datetime': 'hora', 'value': 'precio'})

# Convertir la columna 'hora' a datetime para asegurarse de que sea reconocida como tal
df['hora'] = pd.to_datetime(df['hora'])

# Formar el nombre del archivo con la fecha introducida
nombre_archivo = f"resultados/Resultados_{fecha}.csv"

# Guardar como CSV
df.to_csv(nombre_archivo, index=False)

print(f"Datos guardados en {nombre_archivo}")
