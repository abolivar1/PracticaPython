def devolver_distintos(num1, num2, num3):
    lista_numeros = [num1,num2,num3]
    if sum(lista_numeros) > 15:
        return  max(lista_numeros)
    elif sum(lista_numeros) < 10:
        return min(lista_numeros)
    else:
        lista_numeros.sort()
        return lista_numeros[1]

def transformar_texto(palabra):
    palabra_sin_letras_duplicadas = list(set(palabra.lower()))
    palabra_sin_letras_duplicadas.sort()
    return palabra_sin_letras_duplicadas

def cero_repetido(*args):
    if args.count(0) > 1:
        return True
    else:
        return False

def contar_primos(numero):
    cantidad_primos = 1
    for verificar_numero in range (3, numero+1, 2):
        cantidad_divisores = 1
        for divisor in range(3, verificar_numero+1, 2):
            if verificar_numero % divisor == 0:
                cantidad_divisores += 1
        if cantidad_divisores == 2:
            print(f"El numero {verificar_numero} es primo")
            cantidad_primos += 1
    print(f"El total de numeros primos hasta el numero {numero} es {cantidad_primos}")