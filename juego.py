import random

def adivina_el_numero():
    print("¡Bienvenido al juego Adivina el Número!")
    
    # Configurar el rango del número
    min_num = 1
    max_num = 100
    numero_secreto = random.randint(min_num, max_num)
    
    intentos = 0
    adivinado = False
    
    while not adivinado:
        try:
            # Pedir al usuario que adivine
            intento = int(input(f"Adivina un número entre {min_num} y {max_num}: "))
            intentos += 1
            
            # Comprobar el intento
            if intento < numero_secreto:
                print("Demasiado bajo. Intenta de nuevo.")
            elif intento > numero_secreto:
                print("Demasiado alto. Intenta de nuevo.")
            else:
                adivinado = True
                print(f"¡Felicidades! Has adivinado el número {numero_secreto} en {intentos} intentos.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    adivina_el_numero()