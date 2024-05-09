#1 
class Mascota:
    def __init__(self, especie, precio, vacunado, edad):
        self.especie = especie
        self.precio = precio
        self.vacunado = vacunado
        self.edad = edad

    def __str__(self):
        return f"{self.especie} ({self.edad} años) - {'Vacunado' if self.vacunado else 'No vacunado'}: ${self.precio}"
#2 
m1 = Mascota("Perro", 200, True, 3)
m2 = Mascota("Gato", 100, False, 1)
m3 = Mascota("Conejo", 50, True, 2)
m4 = Mascota("Loro", 150, False, 4)
m5 = Mascota("Lagartija", 250, True, 5)

#3
listado_mascotas = [m1, m2, m3, m4, m5]
#4 
def ordenar_por_precio(mascotas):
    return sorted(mascotas, key=lambda mascota: mascota.precio)
#5 
def promedio_edad(mascotas):
    total_edad = sum(mascota.edad for mascota in mascotas)
    return total_edad / len(mascotas)
#6 
def contar_vacunados(mascotas):
    return sum(1 for mascota in mascotas if mascota.vacunado)

print("Listado Ordenado por Precio:")
for mascota in ordenar_por_precio(listado_mascotas):
    print(mascota)

print("Promedio de Edad:", promedio_edad(listado_mascotas))
print("Cantidad de Mascotas Vacunadas:", contar_vacunados(listado_mascotas))
