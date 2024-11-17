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

def calcular_picas_y_fijas(clave, intento):
    fijas = 0
    picas = 0
    
    # Este bucle for, tiene el objetivo de mirar cada uno de los números de la clave, y compararlo con cada uno de los números de el número que nos da el jugador, y calcula si existen fijas o picas. Esta función se repetirá con cada intento, y nos dirá que tal fue el intento
    for i in range(len(clave)):
        if intento[i] == clave[i]:
            fijas += 1
        elif intento[i] in clave:
            picas += 1
    
    return picas, fijas

def jugar_picas_y_fijas():
    """
    Simula el juego de picas y fijas. El jugador tiene 12 intentos
    para adivinar el número clave.
    """
    print("¡Bienvenido al juego de Picas y Fijas!")
    print("Debes adivinar un número de 4 dígitos únicos.")
    print("Tienes un máximo de 12 intentos. ¡Buena suerte!")

    clave = NumClave()
    intentos = 0
    max_intentos = 12

    while intentos < max_intentos:
        intento = input(f"Intento {intentos + 1}/{max_intentos}. Ingresa un número de 4 dígitos: ")

        # Validar que el intento sea correcto
        if len(intento) != 4 or not intento.isdigit() or len(set(intento)) != 4:
            print("El número ingresado debe tener 4 dígitos únicos. Intenta de nuevo.")
            continue

        intentos += 1

        # Calcular picas y fijas
        picas, fijas = calcular_picas_y_fijas(clave, intento)

        # Mostrar resultados del intento
        print(f"Picas: {picas}, Fijas: {fijas}")

        # Verificar si el jugador ganó
        if intento == clave:
            print(f"¡Felicidades! Adivinaste el número clave {clave} en {intentos} intentos.")
            return

    print(f"Lo siento, alcanzaste el máximo de intentos. El número clave era {clave}. ¡Mejor suerte la próxima vez!")

# Inicia el juego
jugar_picas_y_fijas()

    
"""1. Para iniciar el juego el programa debe generar un número CLAVE de cuatro cifras aleatoriamente sin repetir decimales. 
2. El programa debe solicitar y capturar el número que el jugador ingrese (intento de adivinar).
3. Para el valor que ingresa el jugador se debe indicar cuántos dígitos son picas y cuántos dígitos son fijas (Nota: un dígito es pica cuando aparece en el número CLAVE generado, pero en una posición diferente a la del número del intento, y un dígito es una fija cuando está en el número CLAVE en la misma posición del número del intento). 
4. Si el número del intento es igual al número CLAVE, el jugador gana. Si no es igual puede intentar nuevamente teniendo en cuenta las picas y fijas reportadas por el programa.
5. Adicionalmente debe llevar un recuento de cuantos intentos ha realizado el jugador, hasta un máximo de doce intentos. 
6. En cada intento debe mostrar: número de intentos y el número de cifras de picas y fijas.

Los mensajes de salida mostrarán lo siguiente al terminar los intentos:
Si logra tener las 4 fijas con menos de dos intentos: «Excelente, eres un maestro estas fuera del alcance de los demás».
Si logra tener las 4 fijas con menos de cuatro intentos: «Muy bueno, puedes ser un gran competidor».
Si lo logra con menos de ocho intentos: «Bien, estas progresando debes buscar tus límites».
Si lo logra con menos de diez intentos: «Regular, Aún es largo el camino por recorrer».
Si no lo consigue en los doce intentos: «Mal, este juego no es para ti».
 """""