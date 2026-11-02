# Proyecto de registro automatizado de solicitudes

## Integrantes
- Derek Monter

## Herramientas y versiones
- Power Automate Desktop: [COMPLETAR versión]
- Windows: [COMPLETAR versión]
- Python: [COMPLETAR versión], solo con las bibliotecas estándar `csv` y `os`
- Aplicación Solicitudes RPA, escenario Base

## Qué hace
Un script de Python separa las solicitudes completas de las pendientes y exporta solo las aprobadas a `datos/solicitudes_base.csv`. Después, un flujo de PAD lee ese CSV y, por cada fila, captura los cinco campos en el formulario, confirma el registro, lee el folio real de la interfaz y guarda en una bitácora el identificador, el folio y el estado.

La extracción es una **simulación declarada**: los datos de C01, C02 y C03 están escritos en el script y no hay OCR ni modelo real. C03 no tiene tipo, por eso queda pendiente y no pasa al CSV.

## Rutas configurables
En los flujos de PAD las rutas están en variables al inicio, para cambiarlas sin tocar el resto:
- `RutaIndividual`: archivo de resultado del ensayo individual (debe ser un nombre nuevo).
- `RutaCsv`: ruta a `datos/solicitudes_base.csv`.
- `RutaResultados`: archivo de resultados del lote (también debe ser nuevo).

En `extraccion_fase1.py`, la variable `ruta_csv` indica dónde se escribe el CSV. Hay que adaptarla a cada equipo.

## Preparación y ejecución
1. Extraer el paquete completo en una carpeta con permiso de escritura.
2. Ejecutar `python extraccion_fase1.py` para generar el CSV.
3. Abrir `aplicacion/iniciar.cmd`, dejar el escenario Base y una sola instancia abierta.
4. Abrir PAD con el mismo usuario y nivel de privilegios que la aplicación.
5. Ajustar las tres rutas anteriores y ejecutar primero `Proyecto_RegistroSolicitudes` y después `Proyecto_RegistroSolicitudes_Lote`.
6. Para repetir un ensayo con los mismos IDs, cerrar la aplicación y renombrar manualmente la carpeta `runtime`; además usar nombres nuevos para los archivos de resultados.

## Limitaciones conocidas
- Los flujos de PAD no son importables por sí solos: los elementos de interfaz se capturan en cada equipo y dejo capturas para reconstruirlos.
- Si el flujo se detiene después de confirmar, no se repite a ciegas, porque la solicitud pudo haberse guardado. Hay que revisar el registro antes de volver a intentar.
- [COMPLETAR: cualquier otra limitación que hayas encontrado]

## Reflexión
En cada iteración del bucle cambia la fila actual de la tabla y, con ella, las cinco variables: identificador, solicitante, área, tipo y descripción. Todo lo demás del recorrido, como las esperas, los clics y las comprobaciones, se mantiene igual. Para evitar registrar datos incorrectos reviso el CSV antes de cargarlo, mantengo C03 como pendiente porque no tiene tipo y detengo el flujo si algo no coincide. El guardado no lo doy por hecho por pulsar un botón: espero a que aparezca la ventana de registro completado, leo el folio del cuadro del diálogo y lo comparo con el Último folio de la ventana principal; además verifico que el total aumente. Por eso el folio nunca se escribe ni se calcula de antemano: depende del historial de la aplicación y solo la interfaz sabe cuál asignó. Tampoco todas las acciones se pueden repetir. Volver a localizar una ventana es seguro porque no cambia nada, pero repetir la confirmación después de que se agotó la espera podría crear un duplicado si la solicitud ya se guardó. En ese caso conservo el estado pendiente y primero compruebo qué ocurrió en la aplicación.
