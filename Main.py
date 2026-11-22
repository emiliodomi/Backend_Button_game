from config.db import obtener_conexion

try:
    conexion = obtener_conexion()
    if conexion.is_connected():
        print("Conectado exitosamente a MySQL")
        conexion.close()
except Exception as error:
    print("Error al conectar a MySQL:", error)