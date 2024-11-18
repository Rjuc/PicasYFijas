import random

def Chancer():
    print("¡Bienvenido a Chancer!")
    print("Adivina si el próximo número será mayor, menor o exacto para ganar fichas.")
    print("Comienzas con 10 fichas.\n")

    # Configuración inicial, iniciando con 10 fichas, y numeros para adivinar del 1 al 9
    totalFichas = 10
    rangoMin, rangoMax = 1, 9
    numeroActual = random.randint(rangoMin, rangoMax)
    rondaActual = 1

    while totalFichas > 0:
        print(f"Ronda {rondaActual}:")
        print(f"El número actual es: {numeroActual}")
        print(f"Fichas actuales: {totalFichas}")
        print(f"Rango de números: {rangoMin} - {rangoMax}\n")

        # El bloque try-except me asegura que el input será válido, ro si no lo és, no acabará el juego, simplemente informará que no es válido
        try:
            apuesta = int(input(f"¿Cuántas fichas quieres apostar? (1 - {totalFichas}): "))
            if apuesta < 1 or apuesta > totalFichas:
                print("Cantidad de fichas no válida. Inténtalo de nuevo.\n")
                continue
        except ValueError:
            print("Entrada inválida. Debes ingresar un número.\n")
            continue

        # se toma el intento d eprediccion, se eliminan espacios y mayúsculas
        prediccion = input("¿Qué predices? (mayor/menor/exacto): ").strip().lower()
        if prediccion not in ["mayor", "menor", "exacto"]:
            print("Predicción inválida. Debes elegir 'mayor', 'menor' o 'exacto'.\n")
            continue

        # Este es el número que debieron adivinar, se genera también aleatoriamente
        numeroSiguiente = random.randint(rangoMin, rangoMax)
        print(f"\nEl siguiente número es: {numeroSiguiente}")

        # El siguiente bloque evaluará que tan acertada fue la predicción en base a el número que segeneró
        if prediccion == "mayor" and numeroSiguiente > numeroActual:
            ganancia = apuesta * 2
            totalFichas += ganancia
            print(f"¡Correcto! Ganaste {ganancia} fichas.\n")
        elif prediccion == "menor" and numeroSiguiente < numeroActual:
            ganancia = apuesta * 2
            totalFichas += ganancia
            print(f"¡Correcto! Ganaste {ganancia} fichas.\n")
        elif prediccion == "exacto" and numeroSiguiente == numeroActual:
            # Como las ganacias deben ir aumentando dependiendo de la dificultad esta condicional utilizando el operador ternario, realiza el cálculo
            multiplicador = 5 if rangoMax <= 9 else (10 if rangoMax <= 99 else (50 if rangoMax <= 999 else 100))
            ganancia = apuesta * multiplicador
            totalFichas += ganancia
            print(f"¡Increíble! Adivinaste el número exacto y ganaste {ganancia} fichas.\n")
        elif prediccion == "exacto" and rangoMax > 999 and abs(numeroSiguiente - numeroActual) <= rangoMax * 0.05:
            print("¡Cerca! No acertaste el número exacto, pero estabas dentro del 5% del valor. No pierdes fichas.\n")
        else:
            totalFichas -= apuesta
            print(f"Incorrecto. Perdiste {apuesta} fichas.\n")

        # Actualizar el número actual y avanzar de ronda
        numeroActual = numeroSiguiente
        rondaActual += 1

        # Cada 3 rondas, el número de cifras posible
        if rondaActual % 3 == 0:
            rangoMax = rangoMax * 10 + 9
            print(f"¡El rango ha aumentado! Ahora es de {rangoMin} a {rangoMax}.\n")

        # El juego debe tener una opción para retirarse, se retirará sólo si la respuesta es lieralmente "si", cualquier otra respuesta continuará el juego para no ahcer el código tan largo en esta ocasión
        retirar = input("¿Quieres retirarte? (si/no): ").strip().lower()
        if retirar == "si":
            break

    # EMnsajes de salida si tienes 0 fichas o te retiras
    print("\n--- Fin del juego ---")
    if totalFichas < 10:
        print("Parece que la suerte no estuvo de tu lado.")
    elif 10 <= totalFichas <= 20:
        print("Un desempeño decente, ¡pero puedes hacerlo mejor!")
    elif 20 < totalFichas <= 50:
        print("¡Buen trabajo! Tienes madera.")
    else:
        print("¡Increíble! Eres un maestro de la suerte y el riesgo.")

# Ejecutar el juego
Chancer()