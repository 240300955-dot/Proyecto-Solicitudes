# Entrega del proyecto de solicitudes

- **Estudiante:** Derek Monter
- **Fecha y versión de PAD:** [COMPLETAR: fecha de la ejecución y versión que ves en PAD, Ayuda > Acerca de]
- **Flujos y mecanismo de entrega:** Proyecto_RegistroSolicitudes y Proyecto_RegistroSolicitudes_Lote, guardados en PAD. Además dejo en el repositorio las capturas de los elementos de interfaz y los pasos para reconstruirlos, porque los elementos no siempre se transfieren al compartir un flujo.
- **Carpeta del proyecto y archivos de evidencia:** [COMPLETAR: ruta de tu carpeta]. Evidencias: `individual_01.txt`, `resultados_lote_01.csv`, capturas y video en Classroom.
- **Estado inicial:** [COMPLETAR: registro nuevo o historial previo, y el total que mostraba la aplicación antes del ensayo]

## Resultados observados

Anoto solo lo que vi en pantalla. Los folios dependen del historial de la aplicación, así que no los calculé.

| Ensayo | ID o IDs | Folios leídos | Total antes / después | Evidencia | Resultado |
|---|---|---|---|---|---|
| Individual | SOL-500 | [COMPLETAR] | [COMPLETAR] | individual_01.txt + captura | [COMPLETAR] |
| Lote | SOL-001, SOL-002, SOL-003 | [COMPLETAR] | [COMPLETAR] | resultados_lote_01.csv | [COMPLETAR] |
| Movimiento de ventana, solo captura | No corresponde | No corresponde | [COMPLETAR] | [COMPLETAR: captura] | [COMPLETAR] |

## Selectores

| Control | Atributos conservados | Cómo lo distingo de otros controles | Prueba realizada |
|---|---|---|---|
| Solicitante | Identificador `txtSolicitante`, nombre accesible "Solicitante", tipo texto editable, dentro de la ventana `frmSolicitudes` | Es el único cuadro editable con ese identificador. Descarté los identificadores numéricos de los paneles sin nombre porque cambian entre ejecuciones. | [COMPLETAR: qué probaste y qué pasó, por ejemplo mover la ventana] |
| Confirmar | Identificador `btnAceptarDialogo`, nombre "Confirmar", tipo botón, dentro de la ventana `dlgConfirmacion` | El botón Aceptar del diálogo de resultado usa el mismo identificador, así que lo distingo por la ventana que lo contiene y por su nombre accesible. | [COMPLETAR] |
| Folio generado | Identificador `txtFolioDialogo`, tipo texto de solo lectura, dentro de la ventana `dlgResultado` con título "Registro completado" | Las ventanas de error también usan `dlgResultado`, por lo que reviso el título para saber si es éxito, duplicado o dato inválido. | [COMPLETAR] |

## Matriz de pruebas obligatorias

Completo las columnas de estado obtenido, contador, folio y evidencia solo con lo que observé en cada ensayo. Si algo difiere de lo esperado, lo anoto tal cual con la corrección que propongo.

| Prueba | Entrada o preparación | Estado esperado | Estado obtenido | Contador antes / después | Folio | Evidencia |
|---|---|---|---|---|---|---|
| Documento completo y aprobado | [COMPLETAR: filas del CSV usadas] | Llega al formulario y termina con folio real y bitácora | [COMPLETAR] | [COMPLETAR] | [COMPLETAR] | [COMPLETAR] |
| Información ausente en C03 | Script de extracción: C03 no tiene tipo | Se conserva pendiente y no se envía | [COMPLETAR] | [COMPLETAR] | No corresponde | [COMPLETAR: captura de consola] |
| Datos inválidos en el formulario | [COMPLETAR: qué dato alteré] | Reconoce el rechazo y no informa éxito | [COMPLETAR] | [COMPLETAR] | No corresponde | [COMPLETAR] |
| Identificador ya registrado | [COMPLETAR: ID repetido] | Reconoce el duplicado y el contador no aumenta | [COMPLETAR] | [COMPLETAR] | No corresponde | [COMPLETAR] |
| Respuesta lenta y espera suficiente | [COMPLETAR: cómo provoqué la lentitud] | Verifica el registro sin repetir la confirmación | [COMPLETAR] | [COMPLETAR] | [COMPLETAR] | [COMPLETAR] |
| Espera agotada tras confirmar | [COMPLETAR] | Informa pendiente y comprueba después, sin reenviar | [COMPLETAR] | [COMPLETAR] | [COMPLETAR] | [COMPLETAR] |
| Aplicación cerrada al localizarla | App cerrada antes de iniciar el flujo | Agota los reintentos y registra fallo técnico | [COMPLETAR] | No corresponde | No corresponde | [COMPLETAR] |
