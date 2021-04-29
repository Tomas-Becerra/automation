#1. Crear un nuevo repositorio
#2. Tomar de base el programa de la clase pasada
#3. Vamos a modificar el programa para que solo tome como válidos números entre 1 y 120
# (si pone un número entre -inf y 0 o 121 a inf debe volver a preguntar)
#3. Al inicio del programa preguntar cuantas personas registrar
#4. Hacer que el programa que se hizo se ejecute esas n veces que se pusieron en el punto 3
#5. Subir el programa al repositorio creado

cuantas = int(input('Ingrese cantidad de personas a registrar: '))
for i in range (cuantas):
	edad = int(input('Ingrese Edad: '))
	while (edad < 1 or edad >=121):
		edad = int(input('Ingrese Edad: '))

	nombre = input('Ingrese Nombre: ')
	apellido = input('Ingrese Apellido: ')
	condicionEdad = 'cadaver'

	if edad < 18:
		condicionEdad = 'menor'
	elif edad > 18 and edad < 65:
		condicionEdad = 'mayor' 
	elif edad >= 65 and edad < 120:
		condicionEdad = 'jubilado'
	#print("Su nombre es: " + nombre + " " + apellido + " y usted es " + condicionEdad)
	print("Su nombre es: {} {} y usted es {} ".format(nombre, apellido, condicionEdad))