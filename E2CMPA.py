from rich.console import Console
console = Console()

import pyfiglet
from colorama import Fore, init
init(autoreset=True)
banner = pyfiglet.figlet_format("Cristhian Pocon")
print(Fore.CYAN + banner)

# 👤 Diccionario de datos personales en Python
nombre = input("📝 ¿Cómo te llamas?: ")
edad = input("🎂 ¿Cuántos años tienes?: ")
direccion = input("🏠 ¿Cuál es tu dirección?: ")
telefono = input("📱 ¿Cuál es tu número de teléfono?: ")

# 📖 Se guardan los datos en un diccionario
persona = {
    'nombre': nombre,
    'edad': edad,
    'direccion': direccion,
    'telefono': telefono
}
# 🔑 Pregunta al usuario qué clave desea consultar
clave = input("🔍 ¿Qué dato deseas consultar? (nombre, edad, direccion, telefono): ")
# 📢 Verifica si la clave existe en el diccionario
if clave in persona:
    print("✅ El valor de", clave, "es:", persona[clave])
else:
    print("⚠️ La clave no existe en el diccionario.")
# 📋 Muestra el mensaje completo con los datos ingresados
print(
    "\n📌", persona['nombre'],
    "tiene", persona['edad'], "años, vive en",
    persona['direccion'],
    "y su número de teléfono es",
    persona['telefono']
)