#1
nombre = 'thiago vergara'
print(nombre)

#2
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print(f'la suma es:{suma}')
print(f'la resta es:{resta}')
print(f'la multiplicacion es:{multiplicacion}')
print(f'la division es:{division}')

#3
edad = int(input("Ingrese la edad: "))

if edad >= 18:
    print("Podes pasar")
else:
    (print("vuelve a casa"))

#4
lista = ["manzana", "banana", "pan", "leche", "huevos"]
for i in range(len(lista)):
    print(f"{i}. {lista[i]}") 
#5
lista_usuarios = []

def agregar_usuario(nombre, edad):
    usuario = {
        'nombre': nombre,
        'edad': int(edad)
    }
    lista_usuarios.append(usuario)

nom = input("Ingrese su nombre: ")
ed = input("Ingrese su edad: ")

for _ in range(1):
    nom = input("Ingrese su nombre: ")
    ed = input("Ingrese su edad: ")
    agregar_usuario(nom, ed)


print(lista_usuarios)

#6
for usuario in lista_usuarios:
    if usuario['edad'] > 18:
        print(f"{usuario['nombre']} puede pasar.")
    else:
        print(f"{usuario['nombre']} debe volver a casa.")







