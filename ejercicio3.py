#1. Crear un nuevo repositorio
#2. Tomar de base el la tarea de la clase 2
#3. Si es menor de edad, vamos a venderle juguetes
#3.1: preguntarle si es electrónico, color, camina
#4. Si es mayor de edad, vamos a venderle ropa
#4.1: preguntarle si es camisa o pantalon, color y el talle
#5. Si es jubilado vamos a venderle pasajes
#5.1 Preguntarle si quiere viajar a Federación, Cataratas o Santa Teresita
#Mostrar por pantalla los datos de la persona y el producto seleccionado

def edadPersona(valor):
	if valor < 18:
		condicionEdad = 'menor'
	elif valor > 18 and valor < 65:
		condicionEdad = 'mayor' 
	elif valor >= 65 and valor < 120:
		condicionEdad = 'jubilado'
	else:
		condicionEdad = 'cadaver'
	
	return condicionEdad

def accionPor(queHacer):
	if queHacer == 'menor':
		ofrecer = 'Que tipo de juguetes quieres: electrónico? de que color? camina?'
	elif queHacer == 'mayor':
		ofrecer = 'Que tipo de ropa quiere: camisa o pantalon, color y el talle?'
	elif queHacer == 'jubilado':
		ofrecer = 'Que tipo de pasajes desea: Viajar a Federación, Cataratas o Santa Teresita?'
	
	return ofrecer




cuantas = int(input('Ingrese cantidad de personas a registrar: '))
for i in range (cuantas):
	edad = int(input('Ingrese Edad: '))
	while (edad < 1 or edad >=121):
		edad = int(input('Ingrese Edad: '))

	nombre = input('Ingrese Nombre: ')
	apellido = input('Ingrese Apellido: ')
	condicionPersona = edadPersona(edad)
	accionPersona = accionPor(condicionPersona)



	#print("Su nombre es: " + nombre + " " + apellido + " y usted es " + condicionPersona)
	print("Su nombre es: {} {} y usted es {}. {} ".format(nombre, apellido, condicionPersona, accionPersona))