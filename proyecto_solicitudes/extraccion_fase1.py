import csv
import os

# Simulación declarada con datos que sí coinciden con el formulario de la aplicación
casos = [
    {"archivo": "C01", "id_solicitud": "SOL-001", "solicitante": "Juan Perez", "area": "Administración", "tipo": "Mantenimiento", "descripcion": "Reparar aire acondicionado"},
    {"archivo": "C02", "id_solicitud": "SOL-002", "solicitante": "Maria Lopez", "area": "Docencia", "tipo": "Equipo", "descripcion": "Cambio de equipo de computo"},
    {"archivo": "C03", "id_solicitud": "SOL-003", "solicitante": "Carlos Ruiz", "area": "Biblioteca", "tipo": "", "descripcion": "Revisar facturas"} # C03 sin tipo (se irá a pendiente)
]

aprobados = []
pendientes = []
campos_requeridos = ["id_solicitud", "solicitante", "area", "tipo", "descripcion"]

# Validación: Separar aprobados de pendientes
for caso in casos:
    # Verificamos si todos los campos requeridos tienen texto
    es_valido = all(caso.get(campo) for campo in campos_requeridos)
    
    if es_valido:
        aprobados.append(caso)
    else:
        pendientes.append(caso) # El C03 cae aquí

# Exportar a CSV solo los casos aprobados en la ruta que lee tu PAD
ruta_csv = r"C:\Users\Chino\Downloads\RPA\proyecto_solicitudes_estudiantes\proyecto_solicitudes\datos\solicitudes_base.csv"

# Crea la carpeta de datos si no existe
os.makedirs(os.path.dirname(ruta_csv), exist_ok=True)

with open(ruta_csv, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=campos_requeridos, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(aprobados)

print(f"Extracción completada.")
print(f"Casos aprobados exportados al CSV: {len(aprobados)}")
print(f"Casos pendientes (sin enviar al CSV): {len(pendientes)} - Archivo: {pendientes[0]['archivo']}")