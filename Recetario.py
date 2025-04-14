from pathlib import Path
from os import system
import os
import shutil


ruta_recetas = Path("C:\\Users\\Alex Bolivar\\Desktop\\Recetas")

def eliminar_receta(categoria):
    receta = pedir_receta(categoria)
    os.remove(Path(ruta_recetas, categoria, receta + ".txt"))
    print(f"La receta {receta} fue eliminada")

def eliminar_categoria():
    categoria = pedir_categoria()
    shutil.rmtree(Path(ruta_recetas, categoria))
    print(f"La categoria {categoria} fue eliminada")

def crear_categoria():
    nombre_categoria = input("Ingresa el nombre de la categoria: ")
    os.mkdir(Path(ruta_recetas, nombre_categoria))
    print(f"Categoria {nombre_categoria} creada")


def crear_receta(categoria):
    nombre_receta = input("Ingresa el nombre de la receta: ")
    nueva_receta = open(Path(ruta_recetas, categoria, nombre_receta + ".txt"), "w")
    nueva_receta.write(input("Ingresa los pasos de la receta: \n"))
    nueva_receta.close()
    print(f"Receta {nombre_receta} creada")

def mostrar_receta(categoria, receta):
    contenido_receta = open(Path(ruta_recetas, categoria, receta + ".txt"))
    print(f"Receta: {receta}\n{contenido_receta.read()}")

def pedir_receta(categoria):
    ruta_categoria = ruta_recetas / categoria
    recetas = [receta.stem for receta in Path(ruta_categoria).glob("*.txt")]
    print("Elige una receta:")
    for indice, receta in enumerate(recetas):
        print(f"{indice + 1} - {receta}")
    while True:
        receta = input("Ingresa el numero de la receta: ")
        if receta.isnumeric():
            if 0 < int(receta) <= len(recetas):
                receta = int(receta)
                break
        print("Digitaste un valor invalido. Ingresa solo numeros que correspondan con una de las recetas")
    return recetas[receta - 1]

def pedir_categoria():
    categorias = [item.name for item in ruta_recetas.iterdir() if item.is_dir()]
    print("Elige una categoria:")
    for indice, categoria in enumerate(categorias):
        print(f"{indice + 1} - {categoria}")
    while True:
        categoria = input("Ingresa el numero de la categoria: ")
        if categoria.isnumeric():
            if 0 < int(categoria) <= len(categorias):
                categoria = int(categoria)
                break
        print("Digitaste un valor invalido. Ingresa solo numeros que correspondan con una de las categorias")
    return categorias[categoria - 1]


def saludar():
    nombre = input("Ingresa tu nombre: ")
    cantidad_recetas = 0
    for receta in Path(ruta_recetas).glob("**/*.txt"):
        cantidad_recetas += 1
    print(f"Hola {nombre}. En la ruta {ruta_recetas} tenemos {cantidad_recetas} recetas para ti")

def menu():
    menu = ["Buscar receta", "Crear receta", "Crear categoria", "Eliminar receta", "Eliminar categoria", "Salir"]
    for index, item in enumerate(menu):
        print(f"{index + 1} - {item}")
    while True:
        opcion = input("Ingresa la opcion: ")
        if opcion.isnumeric():
            if 0 < int(opcion) <= len(menu):
                opcion = int(opcion)
                break
        print("Digitaste un valor invalido. Ingresa solo numeros que correspondan con una de las opciones del menu")
    return opcion


def navegar(opcion):
    while True:
        match opcion:
            case 0:
                opcion = menu()
            case 1:
                categoria = pedir_categoria()
                receta = pedir_receta(categoria)
                mostrar_receta(categoria, receta)
                opcion = int(input("0 - Volver al menu principal: "))
            case 2:
                categoria = pedir_categoria()
                crear_receta(categoria)
                opcion = int(input("0 - Volver al menu principal: "))
            case 3:
                crear_categoria()
                opcion = int(input("0 - Volver al menu principal: "))
            case 4:
                categoria = pedir_categoria()
                eliminar_receta(categoria)
                opcion = int(input("0 - Volver al menu principal: "))
            case 5:
                eliminar_categoria()
                opcion = int(input("0 - Volver al menu principal: "))
            case 6:
                print("Adios")
                break
        system("cls")



saludar()
navegar(0)

'''
categoria = pedir_categoria(ruta_recetas)
eliminar_receta(ruta_recetas, categoria)
receta = pedir_receta(ruta_recetas,categoria)
mostrar_receta(ruta_recetas, categoria, receta)'''

