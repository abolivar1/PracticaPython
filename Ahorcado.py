from random import choice

def elegir_palabra(lista_palabras):
    return choice(lista_palabras)

def pedir_letra():
    letra = ''
    while True:
        letra = input("Ingresa una letra: ")
        if letra.isalpha():
            return letra
        else:
            print("Digitaste un valor invalido. Ingresa solo letras")

def buscar_letra_en_palabra(letra, palabra):
    letra_en_palabra = letra in palabra
    posiciones = [i for i, char in enumerate(palabra) if char == letra]
    return letra_en_palabra, posiciones

def guardar_letras_incorrectas(lista_incorrectas, letra):
    lista_incorrectas.append(letra)
    return lista_incorrectas

def restar_vidas(vidas):
    return vidas - 1

def mostrar_progreso(lista_adivinada):
    print(' '.join(lista_adivinada))

def completo_palabra(lista_adivinada):
    return not ('-' in lista_adivinada)

def jugar():
    palabras = ["manzana", "libro", "gato", "cielo", "bicicleta", "flor", "programa", "java", "python", "pelota",
                "ratón", "camisa", "película", "ordenador", "hoja", "zapato", "perro", "coche", "libertad", "jardín"]
    palabra = elegir_palabra(palabras)
    lista_adivinada = ['-'] * len(palabra)
    lista_incorrectas = []
    vidas = 6
    print(f"Vamos a jugar al ahorcado.\nTienes {vidas} vidas, tu palabra tiene {len(palabra)} letras")
    mostrar_progreso(lista_adivinada)
    while vidas > 0:
        letra = pedir_letra()
        letra_en_palabra, posiciones = buscar_letra_en_palabra(letra, palabra)
        if letra_en_palabra:
            for posicion in posiciones:
                lista_adivinada[posicion] = letra
        else:
            lista_incorrectas = guardar_letras_incorrectas(lista_incorrectas, letra)
            print(f"Fallaste.\nLetras incorrectas usadas: {lista_incorrectas}")
            vidas = restar_vidas(vidas)
            print(f"vidas restantes: {vidas}")
        mostrar_progreso(lista_adivinada)
        if completo_palabra(lista_adivinada):
            print("Has ganado")
            break

    if vidas == 0:
        print(f"Perdiste. la palbra era {palabra}")

jugar()