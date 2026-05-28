from rich.console import Console
console = Console()

import pyfiglet
from colorama import Fore, init
init(autoreset=True)
banner = pyfiglet.figlet_format("Cristhian Pocon")
print(Fore.CYAN + banner)

# 💱 Diccionario de Divisas en Python

monedas = {
    'Euro': '€',
    'Dollar': '$',
    'Yen': '¥',
    'Quetzal': 'Q'
}

# ⌨️ Solicita al usuario el nombre de la divisa
moneda = input("💵 Introduce una divisa: ")

# 🔍 Busca la divisa en el diccionario y muestra el resultado
print(monedas.get(moneda.title(), "⚠️ La divisa no está en el diccionario."))