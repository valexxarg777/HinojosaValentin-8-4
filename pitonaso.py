import webbrowser
import os

print("=== ABRIENDO NAVEGADOR ===")

pid = os.getpid()
print(f"PID del proceso: {pid}")

url = "https://es.pornhub.com/"

print("Abriendo página web...")
webbrowser.open(url)

print("Pági")