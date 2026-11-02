# Entrega del proyecto de solicitudes

- **Estudiante:** Derek Monter

## Resultados observados

Anoto solo lo que vi en pantalla. Los folios dependen del historial de la aplicación, así que no los calculé.

| Ensayo | ID o IDs | Folios leídos |
|---|---|---|
| Individual | SOL-500 | individual_01.txt + captura |
| Lote | SOL-001, SOL-002, SOL-003  resultados_lote_01.csv | 
| Movimiento de ventana, solo captura | No corresponde | No corresponde |

## Selectores

| Control | Atributos conservados | Cómo lo distingo de otros controles |
|---|---|---|
| Solicitante | Identificador `txtSolicitante`, nombre accesible "Solicitante", tipo texto editable, dentro de la ventana `frmSolicitudes` | Es el único cuadro editable con ese identificador. Descarté los identificadores numéricos de los paneles sin nombre porque cambian entre ejecuciones. |
| Confirmar | Identificador `btnAceptarDialogo`, nombre "Confirmar", tipo botón, dentro de la ventana `dlgConfirmacion` | El botón Aceptar del diálogo de resultado usa el mismo identificador, así que lo distingo por la ventana que lo contiene y por su nombre accesible. |
| Folio generado | Identificador `txtFolioDialogo`, tipo texto de solo lectura, dentro de la ventana `dlgResultado` con título "Registro completado" | Las ventanas de error también usan `dlgResultado`, por lo que reviso el título para saber si es éxito, duplicado o dato inválido. |

## Matriz de pruebas obligatorias

Completo las columnas de estado obtenido, contador, folio y evidencia solo con lo que observé en cada ensayo. Si algo difiere de lo esperado, lo anoto tal cual con la corrección que propongo.

| Prueba | Entrada o preparación | Estado esperado |
|---|---|---|
| Documento completo y aprobado |  Llega al formulario y termina con folio real y bitácora |
| Información ausente en C03 | Script de extracción: C03 no tiene tipo | Se conserva pendiente y no se envía | 
| Datos inválidos en el formulario |  Reconoce el rechazo y no informa éxito |
| Identificador ya registrado |  Reconoce el duplicado y el contador no aumenta |
| Respuesta lenta y espera suficiente |  Verifica el registro sin repetir la confirmación | 
| Espera agotada tras confirmar |  Informa pendiente y comprueba después, sin reenviar | 
| Aplicación cerrada al localizarla | App cerrada antes de iniciar el flujo | Agota los reintentos y registra fallo técnico |
