# Crear y escribir en el archivo
archivo = open("log.txt", "w", encoding="utf-8")
archivo.write("Inicio del programa\n")

for i in range(5):
    archivo.write(f"Línea {i} - Timestamp: {os.times()}\n")

archivo.write("Fin del programa\n")
archivo.close()

print("Archivo 'log.txt' creado y cerrado correctamente.")
print("Tamaño del archivo:", os.path.getsize("log.txt"), "bytes")

