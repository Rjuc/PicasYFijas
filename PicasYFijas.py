#para correr el programa, es necesario tener instalada la librería random
import random

def NumClave():
    # vamos a generar un número CLAVE de cuatro cifras aleatoriamente sin repetir decimales. 
    opciones = list(range(10))
    # es posible generar los 4 números aleatorios utilizando random.sample, peroie sta vez, he decicdo simplemente generar una lista de números del 1 al 10, luego reorganizarlos aleatoriamente, y tomar 4 de los números de esa lista.
    random.shuffle(opciones)
    #se realiza la conversión a cadenas de "texto" de los primeros cuatro valores de la lista
    clave = ''.join(str(d) for d in opciones[:4])
    return clave

def calcularPicasYFijas(clave, intento):
    fijas = 0
    picas = 0
    
    # Este bucle for, tiene el objetivo de mirar cada uno de los números de la clave, y compararlo con cada uno de los números de el número que nos da el jugador, y calcula si existen fijas o picas. Esta función se repetirá con cada intento, y nos dirá que tal fue el intento
    for i in range(len(clave)):
        if intento[i] == clave[i]:
            fijas += 1
        elif intento[i] in clave:
            picas += 1
    
    return picas, fijas

def jugarPicasYFijas():
    print("¡Vamos a jugar Picas y Fijas como en clase!")
    #ahora ya nestá todo preparado para jugar
    clave = NumClave()
    intentos = 0
    maxIntentos = 12

    #En este bloque while, se pide que se itnente adivenar, también se hace énfasis en que debe ser un número de 4 dígitos únicos entre si, o volverá a pedir el número.
    while intentos < maxIntentos:
        intento = input(f"Intento {intentos + 1}/{maxIntentos}. Ingresa un número de 4 dígitos: ")

        # Validar que el intento sea correcto, también podríamos agregar que l el número a ingresar sea de 4valores únicos, pero eso podría arruinar algunas estratégias
        if len(intento) != 4 or not intento.isdigit():
            print("El valor ingresado debe ser un número, y debe contener 4 dígitos")
            continue

        intentos += 1

        # Se utiliza la función para calcular que tal fué en el intento
        picas, fijas = calcularPicasYFijas(clave, intento)

        # Mostrar resultados del intento
        print(f"Picas: {picas}, Fijas: {fijas}")

        # En este boque, se entra sòlo si el jugador gana
        if intento == clave:
            #ya que ha gaanado, se define cuantos intentoas le tomó, para mostrar el mensaje adecuado
            match intentos:
                case 1:
                    print("Excelente, eres un maestro estas fuera del alcance de los demás")
                case 2 | 3:
                    print("Muy bueno, puedes ser un gran competidor")
                case 4 | 5 | 6 | 7:
                    print("Bien, estas progresando debes buscar tus límites")
                case 8 | 9:
                    print("Regular, Aún es largo el camino por recorrer")
                case _:
                    print("Resultado inesperado, pero ¡ganaste!")

                
            print(f"Adivinaste el número clave {clave} en {intentos} intentos.")
            return

    print(f"Mal, este juego no es para ti. El número clave era {clave}.")

# la función principal se llama al final para evitar errores de declaración temprana
jugarPicasYFijas()
