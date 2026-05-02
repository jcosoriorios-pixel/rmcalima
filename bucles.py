#ejemplo de for 
for i in range(3,8):
    print(f"hola {i}")

#iteracion de una cadena de texto
palabra="colombia"
for letra in palabra:
    print(letra)

#iteracion de una lista
nombres=["julio","alfonso","luisax2","tamara","alexander","daniela"]
for nombre in nombres:
    print(nombre)
    break 
    

#ejemplo de while
i=0
while i<5:
    print(f"hola {i}")
    i+=1

#ejemplo de pass
clave="1234"
clave_ingresada=input("ingrese la clave: ")
while clave_ingresada!=clave:
    print("clave incorrecta, intente de nuevamente")    
    clave_ingresada=input("ingrese la clave: ") 
print("clave correcta, bienvenido")
