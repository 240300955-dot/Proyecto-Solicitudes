# Matriz de pruebas - Sesión 6: excepciones y reintentos seguros

**Estudiante:** Eduardo Emiliano Gómez Fernández  
**Fecha:** 13 de octubre de 2026  
**Power Automate Desktop:** 2.72.00183.26250  
**Versión de Microsoft Store:** 11.2609.183.0  
**Aplicación:** Solicitudes RPA | Laboratorio de escritorio

## Flujos

- S06_ClasificarSolicitud: rechazo de datos, duplicado y solicitud nueva cancelada.
- S06_RespuestaLenta: confirmación única y verificación limitada del resultado.
- S06_LocalizarVentana: enfoque de ventana con dos reintentos y salida técnica.
- EsperarDialogo: subflujo común de los dos primeros flujos. Comprueba cuatro títulos; espera un segundo entre sondeos sin respuesta.

## Entradas

En los casos de negocio se usó Área = Administración, Tipo = Equipo y Descripción = Revisar pantalla del equipo de práctica. Solicitante = Ana, excepto P1 de rechazo, en el que quedó vacío. Los campos se prepararon manualmente antes de ejecutar.

## Resultados

Los estados se contrastaron con sesion06.txt. Los contadores corresponden a los resultados reportados durante las ejecuciones y las capturas revisadas. Los nombres de evidencia siguientes son los nombres acordados para organizar la entrega; deben coincidir con los archivos locales.

| Caso | Flujo | ID / preparación | Estado esperado | Estado obtenido | Total antes / después | Folio | Evidencia |
|---|---|---|---|---|---|---|---|
| P1 | S06_ClasificarSolicitud | SOL-701; solicitante vacío; Base | RECHAZADA_DATOS | RECHAZADA_DATOS | 5 / 5 | No aplica | P1_rechazada_datos.png |
| P1 contraste corregido | S06_ClasificarSolicitud | SOL-702; Ana; Base; cancelar manualmente tras finalizar el bot | RESPUESTA_NO_ESPERADA | RESPUESTA_NO_ESPERADA | 6 / 6 | No se generó | P1_contraste_datos_validos.png |
| P2-A | S06_ClasificarSolicitud | SOL-701 existente; Ana; Base | YA_EXISTENTE | YA_EXISTENTE | 6 / 6 | FOL-0006, previo | P2A_dialogo_duplicado.png.png; P2A_resultado_ya_existente.png |
| P2-B | S06_ClasificarSolicitud | SOL-702 libre; Ana; Base | NUEVA_PENDIENTE | NUEVA_PENDIENTE | 6 / 6 | No se generó | P2B_resultado_nueva_pendiente.png |
| P3A corto | S06_RespuestaLenta | SOL-703 libre; demora 4 s; 2 sondeos después de Confirmar | PENDIENTE_VERIFICACION, habitualmente | PENDIENTE_VERIFICACION | 7 / 8, tras comprobar manualmente | FOL-0008 | P3A_corto_resultado.png; P3A_corto_verificacion_manual.png.png |
| P3A largo | S06_RespuestaLenta | SOL-704 libre; demora 4 s; 10 sondeos después de Confirmar | REGISTRADA_VERIFICADA | REGISTRADA_VERIFICADA | 8 / 9 | FolioLeido = FOL-0009 | P3A_largo_resultado.png |
| P3B abierta | S06_LocalizarVentana | NO_APLICA; aplicación abierta | VENTANA_LOCALIZADA | VENTANA_LOCALIZADA | 9 / 9 | No aplica | P3B_ventana_abierta.png |
| P3B cerrada | S06_LocalizarVentana | NO_APLICA; aplicación cerrada | FALLO_TECNICO | FALLO_TECNICO | 9 / 9, comprobado al reabrir | No aplica | P3B_ventana_cerrada.png; P3B_ultimo_error.png |

## Preparaciones y discrepancia observada

1. En el primer contraste P1 con SOL-701, el bot informó RESPUESTA_NO_ESPERADA. Después se pulsó Confirmar manualmente en vez de Cancelar: se guardó SOL-701, folio FOL-0006, y el contador pasó de 5 a 6. Esta alta no fue un éxito automático del bot ni una cancelación correcta. Corrección: repetir el contraste con SOL-702 y cancelar manualmente. El registro existente SOL-701 se aprovechó para P2-A.
2. Antes de P3A se guardó manualmente SOL-705 para capturar los controles Confirmar, Folio generado y Aceptar de Registro completado. Folio FOL-0007; contador 6 a 7. Fue preparación y no uno de los dos ensayos.
3. El ensayo corto terminó pendiente, pero el registro se completó después. Se comprobó manualmente y no se volvió a enviar SOL-703.

Así se explica el total final: 5 solicitudes iniciales + SOL-701 de preparación + SOL-705 de preparación + SOL-703 + SOL-704 = 9.

## Reintentos y manejo técnico

- Acción: Foco en la ventana.
- Búsqueda por título: Solicitudes RPA | Laboratorio de escritorio. Clase vacía.
- Configuración reportada: dos reintentos, intervalo de dos segundos; un intento inicial más dos reintentos.
- Tras agotar los intentos: continuar mediante salto a FALLO_LOCALIZACION.
- En fallo: Obtener el último error, salida UltimoError, borrar error activado; Estado = FALLO_TECNICO.
- En éxito: Estado = VENTANA_LOCALIZADA y salto a SALIDA.
- SALIDA escribe en bitácora y muestra el resultado.
- Mensaje técnico exacto observado en UltimoError: **No se encontró la ventana**.
- En las pantallas revisadas no apareció un campo configurable de tiempo máximo de localización. No se afirma haber establecido un segundo ni se midió la duración total de búsqueda.
- Evidencias de configuración: P3B_configuracion_reintentos.png y P3B_salto_fallo.png.

## Bitácora

Se conserva sesion06.txt original, sin modificar las ejecuciones registradas. Contiene nueve líneas:

1. P1 / SOL-701 / RECHAZADA_DATOS.
2. P1 / SOL-701 / RESPUESTA_NO_ESPERADA.
3. P1 / SOL-702 / RESPUESTA_NO_ESPERADA.
4. P2 / SOL-701 / YA_EXISTENTE.
5. P2 / SOL-702 / NUEVA_PENDIENTE.
6. P3A / SOL-703 / PENDIENTE_VERIFICACION.
7. P3A / SOL-704 / REGISTRADA_VERIFICADA.
8. P3B / NO_APLICA / VENTANA_LOCALIZADA.
9. P3B / NO_APLICA / FALLO_TECNICO.

Las líneas P3A no incluyen un espacio antes del separador después del ID. Es una diferencia de formato; los IDs y estados son legibles.

## Respuestas

**¿Por qué Datos inválidos no es necesariamente un error técnico de PAD?**

La aplicación pudo recibir y validar la solicitud correctamente, pero rechazó un dato que no cumple sus reglas, como el solicitante vacío. PAD puede ejecutar sus acciones sin error; el bot debe reconocer el diálogo mediante una condición.

**¿Por qué dos sondeos agotados no prueban que el guardado falló?**

Solo indican que no se observó el resultado dentro del plazo de consulta. En SOL-703, el bot informó PENDIENTE_VERIFICACION y después la aplicación mostró FOL-0008 y aumentó el contador. Por eso se comprueba el resultado antes de considerar otro envío.

**¿Qué protege de duplicados la aplicación y qué sigue siendo responsabilidad del bot?**

La aplicación evita crear otra solicitud con el mismo ID. El bot debe distinguir YA_EXISTENTE de una alta nueva, conservar el folio previo, informar cada estado y verificar las operaciones inciertas antes de repetirlas. La bitácora anexa cada ejecución: no elimina intentos repetidos ni demuestra idempotencia de todos los archivos de salida.

**¿Por qué enfocar puede reintentarse y confirmar requiere otra estrategia?**

Enfocar una ventana no crea solicitudes; repetirlo conserva ese efecto. Confirmar puede guardar una solicitud aunque la respuesta todavía no se vea. En el flujo se confirma una sola vez y luego se observa y verifica el folio, con estado pendiente si no hay verificación suficiente.

## Reto en pareja y revisión final

Las ejecuciones anteriores documentan las prácticas. La dinámica en pareja del reto final no ha sido confirmada: si el docente la requiere, realizar un caso de negocio y uno técnico, indicar participantes, predicción de rama, resultado y cualquier corrección observada.

Antes de entregar:

- Comprobar que los nombres de las capturas coincidan con esta matriz.
- Adjuntar sesion06.txt y las capturas de resultados, ramas y reintentos.
- Conservar los tres flujos guardados y EsperarDialogo en los dos flujos que lo utilizan, para demostración.
- Evidencias de ramas: P2_ramas_clasificacion.png y P3A_rama_verificacion.png, o capturas divididas equivalentes.
- Subir al espacio de Classroom indicado por el docente.
