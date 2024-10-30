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
        # Variaciones con números
        for num in ["123", "2024"]:
            variaciones.add(palabra + num)

    for r in range(2, len(palabras) + 1):
        for comb in permutations(palabras, r):
            combinacion = "".join(comb)
            combinacion_capitalizada = "".join([word.capitalize() for word in comb])
            variaciones.update({combinacion, combinacion_capitalizada})

            for num in ["123", "2024"]:
                variaciones.update({
                    combinacion + num,
                    combinacion_capitalizada + num
                })

    for palabra in palabras:
        for num in ["123", "2024"]:
            for char in caracteres_especiales:
                variaciones.update({
                    palabra + num + char,
                    palabra.capitalize() + num + char
                })

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
