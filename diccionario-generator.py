import os
import random
import time
import itertools
from itertools import permutations
from colorama import Fore, Style, init

init(autoreset=True)

def limpiar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_banner():
    banner = f"""
{Fore.CYAN}██████╗ ██╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗ █████╗ ██████╗ ██╗   ██╗  
██╔══██╗██║██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║██╔══██╗██╔══██╗╚██╗ ██╔╝  
██║  ██║██║██║        ██║   ██║██║   ██║██╔██╗ ██║███████║██████╔╝ ╚████╔╝   
██║  ██║██║██║        ██║   ██║██║   ██║██║╚██╗██║██╔══██║██╔══██╗  ╚██╔╝    
██████╔╝██║╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║██║  ██║██║  ██║   ██║     
╚═════╝ ╚═╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝     
                                                                             
 ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                             
{Fore.MAGENTA}██╗   ██╗     ██╗    ██████╗                                                 
██║   ██║    ███║   ██╔═████╗                                                
██║   ██║    ╚██║   ██║██╔██║                                                
╚██╗ ██╔╝     ██║   ████╔╝██║                                                
 ╚████╔╝      ██║██╗╚██████╔╝                                                
  ╚═══╝       ╚═╝╚═╝ ╚═════╝                                    by Saimonch16\n\n\n\n
    """
    print(banner)

def solicitar_datos():
    datos = {}
    datos["nombre"] = input("Ingresa un nombre (deja en blanco si no aplica) -> ")
    datos["apellido"] = input("Ingresa un apellido (deja en blanco si no aplica)-> ")
    datos["dni"] = input("Ingresa un DNI (deja en blanco si no aplica)-> ")
    datos["fecha_nacimiento"] = input("Ingresa una fecha de nacimiento (formato YYYYMMDD, deja en blanco si no aplica)-> ")
    datos["direccion"] = input("Ingresa una dirección (deja en blanco si no aplica)-> ")
    datos["otra_palabra"] = input("Ingresa alguna palabra clave adicional (deja en blanco si no aplica)-> ")
    datos["nombre_mascota"] = input("Ingresa un nombre de una mascota (deja en blanco si no aplica)-> ")
    datos["color_favorito"] = input("Ingresa un color favorito (deja en blanco si no aplica)-> ")
    datos["lugar_nacimiento"] = input("Ingresa un lugar de nacimiento (deja en blanco si no aplica)-> ")

    datos = {k: v for k, v in datos.items() if v}
    return datos

def generar_variaciones(datos):
    palabras = list(datos.values())
    variaciones = set()
    caracteres_especiales = ["!", "@", "#", "$", "%", "&", "*"]

    for palabra in palabras:
        variaciones.add(palabra)
        variaciones.add(palabra.lower())
        variaciones.add(palabra.upper())
        variaciones.add(palabra.capitalize())

    for r in range(2, len(palabras) + 1):
        for comb in permutations(palabras, r):
            combinacion = "".join(comb)
            variaciones.add(combinacion)
            variaciones.add("-".join(comb))
            variaciones.add("".join([word.capitalize() for word in comb]))
            for char in caracteres_especiales:
                for _ in range(3):
                    random_number = str(random.randint(10, 999))
                    variaciones.add(combinacion + char + random_number)
                    variaciones.add("-".join(comb) + char + random_number)
                    variaciones.add("".join([word.capitalize() for word in comb]) + char + random_number)
    
    for char in caracteres_especiales:
        variaciones.update({
            datos.get("nombre", "") + "123" + char,
            datos.get("nombre", "") + "2024" + char,
            datos.get("apellido", "") + "123" + char,
            datos.get("apellido", "") + "2024" + char,
        })
        for _ in range(3):
            random_number = str(random.randint(10, 999))
            variaciones.add(datos.get("nombre", "") + random_number + char)
            variaciones.add(datos.get("apellido", "") + random_number + char)

    variaciones = {v for v in variaciones if v}
    
    return variaciones

def animacion_carga():
    spinner = itertools.cycle(["|", "/", "-", "\\"])
    print(Fore.YELLOW + "\nGenerando diccionario, espera un momento...", end=" ", flush=True)
    for _ in range(20):
        print(next(spinner), end="\r", flush=True)
        time.sleep(0.2)

def guardar_diccionario(variaciones, archivo="diccionario.txt"):
    animacion_carga()
    with open(archivo, "w") as f:
        for variacion in variaciones:
            f.write(variacion + "\n")
    print(f"\n{Fore.GREEN}\n✓ Diccionario generado con éxito en '{archivo}' con {len(variaciones)} contraseñas.")

def main():
    limpiar_terminal()  
    mostrar_banner()
    print(Fore.CYAN + "->->->->-> Bienvenido al generador de diccionarios de contraseñas <-<-<-<-<-\n\n")
    datos = solicitar_datos()
    variaciones = generar_variaciones(datos)
    guardar_diccionario(variaciones)

if __name__ == "__main__":
    main()
