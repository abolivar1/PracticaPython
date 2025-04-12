from random import randint
adivino = False
while not adivino:
    numero_a_adivinar = randint(1, 100)
    print("Bueno, Juan, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número")
    for intento in range(1, 9):
        numero_usuario = int(input("Ingresa el numero: "))
        if numero_usuario < 1 or numero_usuario > 100:
            print("Has elegido un numero no permitido")
        elif numero_usuario < numero_a_adivinar :
            print("Respuesta incorrecta. Tu numero es menor al correcto")
        elif numero_usuario > numero_a_adivinar:
            print("Respuesta incorrecta. Tu numero es mayor al correcto")
        else:
            print(f"Has acertado: en el intento numero {intento}. El numero era {numero_a_adivinar}")
            adivino = True
            break
    if not adivino:
        print("Has perdido. Vuelve a intentarlo")