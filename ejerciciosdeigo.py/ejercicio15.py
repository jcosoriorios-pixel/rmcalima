# 15. Adivina el Número

numero_secreto = 7
intento = 0

while intento != numero_secreto:
    intento = int(input("Adivina el número secreto: "))

    if intento == numero_secreto:
        print("¡Correcto! Adivinaste el número.")

    else:
        print("Incorrecto, intenta nuevamente.") 