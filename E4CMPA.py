# Cristhian Pocon

from rich.console import Console
console = Console()

import pyfiglet
from colorama import Fore, init
init(autoreset=True)
banner = pyfiglet.figlet_format("Cristhian Pocon")
print(Fore.CYAN + banner)

