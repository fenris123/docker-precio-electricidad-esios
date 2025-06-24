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
import matplotlib.pyplot as plt



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

fecha = datetime.utcnow().date().isoformat()


params = {
    'start_date': f'{fecha}T00',
    'end_date': f'{fecha}T23'
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
nombre_archivo = f"Resultados_{fecha}.csv"

# Guardar como CSV
df.to_csv(nombre_archivo, index=False)

print(f"Datos guardados en {nombre_archivo}")




# Crear figura y ejes
fig, ax = plt.subplots(figsize=(10, 5))

# Fondo gris moderado para todo el lienzo (figura)
fig.patch.set_facecolor('#c3c3c3')  # gris claro, puedes probar otros tonos (#e0e0e0, #cccccc...)

# Fondo blanco para el área de la gráfica
ax.set_facecolor('white')

# Ajusta márgenes para hacer el área gráfica más pequeña dentro de la figura:
plt.subplots_adjust(left=0.2, right=0.8, top=0.8, bottom=0.2)

# Formatear la hora para que solo muestre la hora (sin fecha)
df['hora_solo'] = df['hora'].dt.strftime('%H:%M')

# Graficar
ax.plot(df['hora_solo'], df['precio'], marker='o', color='royalblue', linestyle='-')

# Títulos y etiquetas
ax.set_title(f"Precio de la electricidad (Mercado diario) - {fecha}", fontsize=16,fontweight='bold')
ax.set_xlabel("Hora del día", fontsize=12)
ax.set_ylabel("Precio (€/MWh)", fontsize=12)

# Quitar los bordes superior e izquierdo
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Crear lista de horas pares
horas_pares = list(range(0, 24, 2))

# Poner ticks solo en esas horas
ax.set_xticks(horas_pares)

# Formatear las etiquetas como 'HH:00'
etiquetas = [f"{h:02d}:00" for h in horas_pares]
ax.set_xticklabels(etiquetas)


# Quitar grid
ax.grid(False)

# Mejorar legibilidad del eje X
plt.xticks(rotation=45)
plt.tight_layout()

# Guardar gráfico
nombre_grafica = f"Grafico_{fecha}.png"
plt.savefig(nombre_grafica)

