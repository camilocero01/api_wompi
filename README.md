# Procesador de Transacciones (Transaction Summary Generator)
Este proyecto contiene un script en Python del RETO PRÁCTICO para la prueba técnica de WOMPI para el cargo Ingeniero de datos.

El archivo esta diseñado para procesar un archivo de transacciones financieras en formato JSON, tranformarlo y finalmente  exportar los resultados a un archivo optimizado en formato Parquet garantizando idempotencia.

# Descripción del Reto
El objetivo es transformar datos crudos de transacciones para obtener una vista de resumen que permita analizar el comportamiento de las trasacciones aprobadas.

# El proceso realiza lo siguiente:

1. Lee el archivo de entrada transactions_50k.jsonl.

2. Filtra y procesa las transacciones.

3. Agrupa los datos por BIN  y Día.

4. Calcula: Cantidad de transacciones aprobadas.

5. Calcula: Monto total aprobado.

6. Exporta el resultado a formato Parquet.

# Requisitos Previos
- Python 3.8 o superior.
- Gestor de paquetes pip.

# Instalación y Configuración
- Clonar el repositorio (o descargar los archivos):

`git clone <https://github.com/camilocero01/api_wompi/>`
`cd <API_WOMPI>`

# Instalar dependencias: El proyecto requiere pandas para el procesamiento de datos y pyarrow (o fastparquet) para manejar el formato Parquet.

`pip install -r requirements.txt`


# Ejecución
Asegúrese de que el archivo de datos transactions_50k.jsonl se encuentre en la carpeta raíz '/input'.

Ejecute el script principal:

`python main.ipynb`

Al finalizar, se generará un archivo llamado agrupacion_bin_fecha.parquet en el directorio '/output'.

# Supuestos 
- Transacciones Aprobadas: Se asume que existe un campo status o authorized que debe ser validado. Solo se suman y cuentan las transacciones cuyo estado es "aprobado" (o true).
- Datos faltantes: Si una transacción no tiene monto o fecha válida, se descarta del cálculo para mantener la integridad del resumen.

# Idempotencia
El script está diseñado para ser idempotente. 
El script no esta realizando ningún tipo de appends, por lo tanto cada que se ejecuta sobreescribe el archivo de salida