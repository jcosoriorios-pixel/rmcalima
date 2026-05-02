# 13. Menú Interactivo

opcion = 0

while opcion != 3:
    print("\n--- MENÚ ---")
    print("1. Saludar")
    print("2. Ver fecha")
    print("3. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        print("¡Hola! Bienvenido al programa.")

    elif opcion == 2:
        print("Hoy es un gran día.")

    elif opcion == 3:
        print("Saliendo del programa...")

    else:
        print("Opción no válida")