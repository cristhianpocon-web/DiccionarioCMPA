from rich.console import Console
console = Console()

import pyfiglet
from colorama import Fore, init
init(autoreset=True)
banner = pyfiglet.figlet_format("Cristhian Pocon")
print(Fore.CYAN + banner)

# 🍎 Diccionario de frutas en Python
frutas = {
    'Plátano': 1.35,
    'Manzana': 0.80,
    'Pera': 0.85,
    'Naranja': 0.70
}
# 🍉 Solicita la fruta al usuario
fruta = input("🍓 ¿Qué fruta deseas comprar?: ").title()
# ⚖️ Solicita la cantidad de kilos
kg = float(input("⚖️ ¿Cuántos kilos deseas?: "))
# 🔍 Verifica si la fruta existe en el diccionario
if fruta in frutas:

    # 💰 Calcula el precio total
    total = frutas[fruta] * kg

    # 📢 Muestra el resultado
    print("🛒", kg, "kilos de", fruta, "cuestan Q.", round(total, 2))

else:
    # ⚠️ Mensaje si la fruta no existe
    print("❌ Lo sentimos, la fruta", fruta, "no está disponible.")