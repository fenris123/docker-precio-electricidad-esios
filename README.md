# docker-precio-electricidad-esios
Proyecto personal que automatiza la descarga diaria del precio de la electricidad en el mercado mayorista español (ESIOS) usando Python, Docker y GitHub Actions. 


El contenedor ejecuta un script que consulta la **API oficial de ESIOS**, genera una tabla de datos y una gráfica diaria, y guarda los resultados de forma reproducible.

## 🔧 Tecnologías utilizadas
- Python 3
- Docker
- GitHub Actions
- Pandas
- Matplotlib
- API de ESIOS (REE España)

## 📦 Objetivo
Crear un contenedor que, de forma automatizada, obtenga diariamente el precio de la electricidad, genere un gráfico y almacene los datos, con posibilidad de usarse como parte de un pipeline de datos o para visualización pública.


## 🚧 Estado del proyecto
En desarrollo. 


## Carpeta resultados.
El script genera un archivo CSV con los datos descargados y lo guarda en la carpeta resultados. Por favor, asegúrate de que esta carpeta exista en el directorio raíz del repositorio antes de ejecutar el script, para evitar errores al guardar los archivos.

Si la carpeta no existe, créala manualmente.


## 📄 Licencia
Este proyecto está licenciado bajo la licencia MIT.
