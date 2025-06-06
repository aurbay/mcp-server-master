# Laboratorio de MCP

## Descripción General del Ejercicio

> Este ejercicio debe ser completado en equipos de hasta 5 miembros. Cada equipo implementará un servidor `MCP` dedicado para abordar al menos uno de los desafíos que se describen a continuación. Se permite el uso de todas las herramientas y recursos necesarios.

### Desafíos

1.  **Recopilación de Datos Arancelarios de EE. UU.**
    *   Objetivo: Generar un archivo `.csv` que detalle todos los aranceles de importación impuestos por el gobierno de los Estados Unidos a otros países.
    *   Referencia: Un archivo de muestra que demuestra el formato correcto está disponible en `data/tariff.csv`.
    *   Dificultad: Estándar

2.  **Identificación de Registros de Compra Inválidos**
    *   Objetivo: Generar un archivo de registro llamado `purchases_wrong.log` que contenga entradas para los registros de compras que sean incorrectos o que no se encuentren en la base de datos SQLite proporcionada.
    *   Referencia: Un ejemplo del formato de salida esperado se puede encontrar en `data/purchases_wrong.log`. La base de datos SQLite para la verificación se encuentra en `data/test_data.db`.
    *   Dificultad: Moderada/Alta

## Directrices de Entrega

Las entregas serán revisadas y discutidas oralmente después de una `pull request`. Después de la discusión, cada entrega será probada en vivo para evaluar la solución y asignar una puntuación.

### Procedimiento de Entrega

1.  **Creación del Directorio del Equipo**: Crear un nuevo directorio dentro de la carpeta `teams`. El nombre del directorio debe ser el nombre de equipo elegido.
2.  **Duplicación del Archivo del Servidor**: Copiar el archivo `server.py` en el directorio de su equipo. **No** modificar el archivo `server.py` original ubicado en el directorio raíz del proyecto.
3.  **Implementación**: Son libres de modificar el archivo `server.py` dentro del directorio de su equipo y utilizar los recursos necesarios para completar la(s) tarea(s) asignada(s).
4.  **Archivos de Salida**: Los archivos de salida generados por su(s) solución(es) (por ejemplo, `tariff.csv`, `purchases_wrong.log`) deben colocarse dentro del directorio de su equipo.