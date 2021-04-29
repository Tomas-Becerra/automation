#1. Crear un nuevo repositorio
#2. Tomar de base el la tarea de la clase 2
#3. Si es menor de edad, vamos a venderle juguetes
#3.1: preguntarle si es electrónico, color, camina
#4. Si es mayor de edad, vamos a venderle ropa
#4.1: preguntarle si es camisa o pantalon, color y el talle
#5. Si es jubilado vamos a venderle pasajes
#5.1 Preguntarle si quiere viajar a Federación, Cataratas o Santa Teresita
#Mostrar por pantalla los datos de la persona y el producto seleccionado

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