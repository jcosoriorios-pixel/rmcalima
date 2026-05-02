"""
nombre=( "clase de funciones" )
lista=["azul","rojo","verde","amarillo"]

print("clase de funciones")
print("lista:",lista)

# usar lent
longitud_nombre=len(nombre)
longitud_lista=len(lista)

print("longitud del nombre:",longitud_nombre)
print("longitud de la lista:",longitud_lista)

# usar type
print(type(nombre))
print(type(lista))

# usar upper - convierte a mayúsculas

print("Nombre original:", nombre)
print("Nombre en mayúsculas:", nombre.upper())

# aplicar upper a cada elemento de la lista
print("Lista original:", lista)
lista_mayusculas = [item.upper() for item in lista]
print("Lista en mayúsculas:", lista_mayusculas)

# usar title - capitaliza la primera letra de cada palabra
texto = "hola mundo"
print("Texto original:", texto)
print("Con title():", texto.title())

# aplicar title a cada elemento de la lista
print("\nLista con title():")
lista_title = [item.title() for item in lista]
print(lista_title)


# split con separador específico
texto_csv = "azul,rojo,verde,amarillo"
print("\nTexto CSV:", texto_csv)
print("Separado por coma:", texto_csv.split(","))

edad=(25,12,32,45,65,34,23,56,78,90)
notas=(8.5, 9.0, 7.5, 6.0, 10.0)


# abs con decimales
decimal = -3.14
print("Decimal negativo:", decimal)
print("Con abs():", abs(decimal))

# abs en una lista
numeros = [-5, 10, -8, 3, -12]
print("\nLista original:", numeros)
lista_abs = [abs(num) for num in numeros]
print("Lista con abs():", lista_abs)

# usar round - redondea un número
numero = 3.14159
print("Número original:", numero)
print("Redondeado a 2 decimales:", round(numero, 2))
print("Redondeado a 0 decimales:", round(numero))
"""
# usar max() y min() - valores máximo y mínimo

numeros = [45, 12, 89, 23, 56, 34]
print("Lista:", numeros)
print("Valor máximo:", max(numeros))
print("Valor mínimo:", min(numeros))

# con tuplas
edades = (25, 12, 32, 45, 65, 34, 23, 56, 78, 90)
print("Edades:", edades)
print("Mayor edad:", max(edades))
print("Menor edad:", min(edades))

# usar append() - añade un elemento al final de la lista

colores = ["rojo", "azul", "verde"]
print("Lista original:", colores)
colores.append("amarillo")
print("Después de append('amarillo'):", colores)

colores.append("naranja")
print("Después de append('naranja'):", colores)

