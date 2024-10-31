import os
import random
import time
import itertools
import subprocess
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
    print(Fore.CYAN + "\nPor favor, proporciona los siguientes datos (deja en blanco si no aplica):\n")
    
    datos["nombre"] = input("1. Ingresa un nombre -> ")
    datos["apellido"] = input("2. Ingresa un apellido -> ")
    datos["apodo"] = input("2. Ingresa un apodo -> ")
    datos["dni"] = input("3. Ingresa un DNI -> ")
    datos["fecha_nacimiento"] = input("4. Ingresa una fecha de nacimiento (formato YYYYMMDD) -> ")
    datos["direccion"] = input("5. Ingresa una dirección -> ")
    datos["otra_palabra"] = input("6. Ingresa alguna palabra clave adicional -> ")
    datos["nombre_mascota"] = input("7. Ingresa un nombre de una mascota -> ")
    datos["color_favorito"] = input("8. Ingresa un color favorito -> ")
    datos["lugar_nacimiento"] = input("9. Ingresa un lugar de nacimiento -> ")

    datos = {k: v for k, v in datos.items() if v}
    return datos

def generar_variaciones(datos, incluir_numeros=True, incluir_especiales=False):
    palabras = list(datos.values())
    variaciones = set()
    caracteres_especiales = ["!", "@", "#", "$", "%", "&", "*"]

    for palabra in palabras:
        variaciones.add(palabra)
        variaciones.add(palabra.lower())
        variaciones.add(palabra.upper())
        variaciones.add(palabra.capitalize())

        if incluir_numeros:
            for num in ["123", "2024"]:
                variaciones.add(palabra + num)

    for r in range(2, len(palabras) + 1):
        for comb in permutations(palabras, r):
            combinacion = "".join(comb)
            combinacion_capitalizada = "".join([word.capitalize() for word in comb])
            variaciones.update({combinacion, combinacion_capitalizada})

            if incluir_numeros:
                for num in ["123", "2024"]:
                    variaciones.update({
                        combinacion + num,
                        combinacion_capitalizada + num
                    })

    if incluir_especiales:
        for palabra in palabras:
            for char in caracteres_especiales:
                variaciones.add(palabra + char)
                if incluir_numeros:
                    for num in ["123", "2024"]:
                        variaciones.add(palabra + num + char)
                        variaciones.add(palabra.capitalize() + num + char)

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

def elegir_archivo_salida():
    while True:
        archivo = input("\nIngresa el nombre del archivo de salida (debe terminar en .txt): ")
        if archivo.endswith(".txt"):
            return archivo
        else:
            print(Fore.RED + "\nError: El nombre del archivo debe terminar en .txt. Intenta de nuevo.")

def buscar_palabra_en_diccionario(archivo):
    palabra = input(Fore.YELLOW + "\nIngresa la palabra a buscar en el diccionario: ")
    
    tipo_busqueda = input(Fore.YELLOW + "\n¿Deseas buscar una coincidencia exacta (e) o palabras que incluyan el texto (i)? (e/i): ").strip().lower()
    
    if tipo_busqueda == 'e':
        patron_busqueda = f'^{palabra}$'  
    elif tipo_busqueda == 'i':
        patron_busqueda = palabra 
    else:
        print(Fore.RED + "\nOpción no válida. Se utilizará la búsqueda por defecto (inclusión).")
        patron_busqueda = palabra
    
    try:
        resultados = subprocess.check_output(['grep', '-E', patron_busqueda, archivo]).decode('utf-8')
        if resultados:
            print(Fore.GREEN + f"\nResultados de la búsqueda para '{palabra}':\n")
            print(resultados)
        else:
            print(Fore.RED + f"\nNo se encontraron resultados para '{palabra}'.")
    except subprocess.CalledProcessError:
        print(Fore.RED + f"\nNo se encontraron resultados para '{palabra}'.")


def verificar_dependencias():
    print(Fore.YELLOW + "\nVerificando dependencias...")
    try:
        import colorama
        print(Fore.GREEN + "\n✓ Todas las dependencias están instaladas.")
    except ImportError as e:
        print(Fore.RED + f"Error: {e}. Instala las dependencias necesaria.")

def verificar_actualizaciones():
    print(Fore.YELLOW + "\nVerificando actualizaciones desde el repositorio...")
    resultado = subprocess.run(["git", "pull", "https://github.com/simoncherry9/dictionary-generator.git"], capture_output=True, text=True)
    
    if "Already up to date." in resultado.stdout:
        print(Fore.GREEN + "\n✓ El repositorio ya está actualizado.")
    else:
        print(Fore.GREEN + "\n✓ Repositorio actualizado con éxito.")

def mostrar_menu():
    while True:
        print(Fore.GREEN + "\n******* Generador de contraseñas *******")
        print(Fore.CYAN + "\n\n\nSeleccione una opción:")
        print("\n1. Verificar dependencias")
        print("2. Verificar actualizaciones desde el repositorio")
        print("3. Crear diccionario")
        print("4. Buscar palabra en el diccionario")
        print("5. Salir")
        
        opcion = input("\nOpción: ")

        if opcion == "1":
            verificar_dependencias()
            input(Fore.YELLOW + "\nPresiona Enter para continuar...")
            limpiar_terminal()
            mostrar_banner()
        elif opcion == "2":
            verificar_actualizaciones()
            input(Fore.YELLOW + "\nPresiona Enter para continuar...")
            limpiar_terminal()
            mostrar_banner()
        elif opcion == "3":
            datos = solicitar_datos()
            incluir_numeros = input("¿Incluir números? (s/n): ").lower() == "s"
            incluir_especiales = input("¿Incluir caracteres especiales? (s/n): ").lower() == "s"
            variaciones = generar_variaciones(datos, incluir_numeros, incluir_especiales)
            archivo = elegir_archivo_salida()
            guardar_diccionario(variaciones, archivo)
            input(Fore.YELLOW + "\nPresiona Enter para continuar...")
            limpiar_terminal()
            mostrar_banner()
        elif opcion == "4":
            archivo = input(Fore.YELLOW + "\nIngresa el nombre del archivo de diccionario para buscar (debe terminar en .txt): ")
            buscar_palabra_en_diccionario(archivo)
            input(Fore.YELLOW + "\nPresiona Enter para continuar...")
            limpiar_terminal()
            mostrar_banner()
        elif opcion == "5":
            print(Fore.YELLOW + "\nSaliendo del programa...")
            break
        else:
            print(Fore.RED + "\nOpción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    limpiar_terminal()
    mostrar_banner()
    mostrar_menu()
