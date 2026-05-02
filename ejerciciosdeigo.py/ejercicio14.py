# 14. Factorial de un Número

numero = int(input("Ingrese un número entero: "))

factorial = 1

for i in range(1, numero + 1):
    factorial *= i

print("El factorial de", numero, "es:", factorial) 