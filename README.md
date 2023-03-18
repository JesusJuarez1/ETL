
Gestor de datos
Componente responsable de ejecutar el proceso de extracción, transformación y carga de datos

Estructura del proyecto

    ├── assets                          # carpeta con datos fuente
    │  ├── source.zip                   # archivo de datos fuente
    ├── result                          # carpeta temporal de procesamiento
    ├── src                             # código fuente del sistema
    │  ├── extractors                   # extractores de datos
    │        ├── csv_extractor.py       # extractor de datos de archivos CSV
    │        ├── htm_extractor.py       # extractor de datos de archivos HTM
    │        ├── xml_extractor.py       # extractor de datos de archivos XML
    │  ├── helpers                      # archivos auxiliares
    │        ├── provider.py            # definición de la interacción con la base de datos
    │        ├── processor.py           # definición de procesamiento de respuestas 
    │        ├── queries.py             # definición de consultas utilizadas en la base de datos
    │  ├── readers                      # lectores de datos
    │        ├── zip_extractor.py       # lector de datos de archivos ZIP
    │  ├── transformers                 # transformadores de datos
    │        ├── csv_transformer.py     # transformador de datos de archivos CSV
    │        ├── htm_transformer.py     # transformador de datos de archivos HTM
    │        ├── xml_transformer.py     # transformador de datos de archivos XML
    ├── .gitignore                      # exclusiones de git
    ├── README.md                       # este archivo
    ├── requirements.txt                # dependencias del sistema



#### Prerequisitos

Para ejecutar este componente es necesario contar con la ejecución de Dgraph, parea ello utilizamos el siguiente comando:
<hr>
docker run -it -p 5080:5080 -p 6080:6080 -p 8080:8080 -p 9080:9080 --name dgraph dgraph/standalone:latest



El comando anterior instanciará los componentes Dgraph Zero (componente encargado de gestionar nodos Dgraph dentro de un cluster balanceando los datos almacenados en los nodos) y Dgraph Alpha (componente encargado de almacenar y gestionar los datos así como los indices y los predicados de consulta).
Adicionalmente existe un componente que permite la interacción visual con Dgraph llamado Dgraph Ratel, para ello podemos utilizar el siguiente comando:

docker run --name ratel  -d -p "8000:8000" dgraph/ratel:latest


#### Para acceder a este componente e interactuar con Dgraph nos podemos dirigir a http://localhost:8000 desde cualquier navegador

Instalación
Descarga el código del repositorio utilizando el siguiente comando:
git clone https://gitlab.com/tareas-arquitectura-de-software-curso/flujo-de-datos/gestor-de-datos.git
accede a la carpeta del componente:
cd gestor-de-datos
construye la imagen de Docker

docker build -t gestor-de-datos .



#### Ejecución
Para ejecutar el componente y correr el proceso de extracción, transformación y carga de datos, utiliza el comando:

docker run --rm --name gestor-de-datos --link dgraph:dgraph gestor-de-datos
