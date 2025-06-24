# Imagen base oficial de Python
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /WDIR

# Copiar el archivo requirements.txt (que contiene las dependencias)
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de archivos del proyecto
COPY . .

# Variable de entorno para el token (se establecerá en tiempo de ejecución)
ENV TOKEN_ESIOS=""

# Comando para ejecutar el script
CMD ["python", "app/precio_mercado.py"]
