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