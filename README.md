# docker-precio-electricidad-esios
Proyecto personal que permite automatizar la consulta diaria del precio de la electricidad en el mercado mayorista español (ESIOS) usando Python, Docker y GitHub Actions. 


El contenedor ejecuta un script que consulta la **API oficial de ESIOS**, genera una tabla de datos y una gráfica diaria, y guarda los resultados de forma reproducible.

## 🔧 Tecnologías utilizadas
- Python 3
- Docker
- GitHub Actions
- Pandas
- Matplotlib
- API de ESIOS (REE España)

## 📦 Objetivo
Crear un contenedor docker que, obtenga diariamente el precio de la electricidad, genere un gráfico y almacene los datos, con posibilidad de usarse como parte de un pipeline de datos o para visualización pública.  Ademas se ejecutara a diario en GitHub actions que guardara los resultados como artifacts consultables y descargables


## 🚧 Estado del proyecto
Funcional


## Configuración del Token de ESIOS
Para que el script funcione correctamente y pueda acceder a la API de ESIOS, es necesario proporcionar un token de autenticación válido.

### ¿Qué es el token?
El token es una clave personal que obtienes al registrarte en la API de ESIOS y que permite autenticar tu acceso a los datos.

### Cómo configurar el token
En local: debes establecer la variable de entorno TOKEN_ESIOS en tu sistema operativo antes de ejecutar el script. Por ejemplo:

export TOKEN_ESIOS="tu_token_aqui"       # Linux / macOS
set TOKEN_ESIOS=tu_token_aqui            # Windows PowerShell

### En Docker: 
al ejecutar el contenedor, pasa el token como variable de entorno:

docker run -e TOKEN_ESIOS="tu_token_aqui" nombre_del_contenedor


### En GitHub Actions: 
configura el token como un Secret en GitHub y asigna el valor a la variable de entorno TOKEN_ESIOS dentro del workflow.



## Comandos docker en windows (requiere instalar docker desktop) 

Ejecuta docker desktop
Abre el cdm EN MODO ADMINISTRADOR
Ve a la carpeta donde vayas a trabajar y guardar los archivos

### Comandos a ejecutar (WINDOWS): 

Copia y pega lo siguiente en el cmd (REPETIMOS: EN MODO ADMINISTRADOR)
git clone https://github.com/tu-usuario/docker-precio-electricidad-esios   (Cambia el usuario por tu usuario de github, o el mio si lo copias desde el)

cd docker-precio-electricidad-esios   

docker build -t precio-electricidad .    

docker run --rm -e TOKEN_ESIOS="METER AQUI TU TOKEN" -v C:\espaciodocker\docker-precio-electricidad-esios\resultados:/appcode/resultados precio-electricidad



## 📄 Licencia
Este proyecto está licenciado bajo la licencia MIT.
