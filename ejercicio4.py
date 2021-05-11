# ENUNCIADO:
# Rehacer ej 3 con lo aprendido en clase 4:
#  listas = [],
#  diccionarios
# 1. Crear un nuevo repositorio
#2. Tomar de base el la tarea de la clase 2
#3. Si es menor de edad, vamos a venderle juguetes
#3.1: preguntarle si es electrónico, color, camina
#4. Si es mayor de edad, vamos a venderle ropa
#4.1: preguntarle si es camisa o pantalon, color y el talle
#5. Si es jubilado vamos a venderle pasajes
#5.1 Preguntarle si quiere viajar a Federación, Cataratas o Santa Teresita
#Mostrar por pantalla los datos de la persona y el producto seleccionado

def edadPersona(valor):
	lista = []
	if valor < 18:
		lista.append('menor')
	elif valor > 18 and valor < 65:
		lista.append('mayor')
	elif valor >= 65 and valor < 120:
		lista.append('jubilado')
	else:
		lista.append('cadaver')
	
	return accionPor(lista)

def accionPor(queHacer):
	if queHacer[0] == 'menor':
		queHacer.append('Que tipo de juguetes quieres: electrónico? de que color? camina?')
	elif queHacer[0] == 'mayor':
		queHacer.append('Que tipo de ropa quiere: camisa o pantalon, color y el talle?')
	elif queHacer[0] == 'jubilado':
		queHacer.append('Que tipo de pasajes desea: Viajar a Federación, Cataratas o Santa Teresita?')
	
	return queHacer


cuantas = int(input('Ingrese cantidad de personas a registrar: '))
for i in range (cuantas):
	edad = int(input('Ingrese Edad: '))
	while (edad < 1 or edad >=121):
		edad = int(input('Ingrese Edad: '))

	nombre = input('Ingrese Nombre: ')
	apellido = input('Ingrese Apellido: ')
	condicionPersona = []
	condicionPersona = edadPersona(edad)
	print("Su nombre es: {} {} y usted es {}. {} ".format(nombre, apellido, condicionPersona[0], condicionPersona[1]))


# TEMAS:
# list = []
# len(list)
# for i in range(0, len(list)): ..
# for value in list: ...
# list.append(new_element_al_final)
# list.insert(position, new_element) -> all the items will move to the next location
# list.pop() -> deletes the last element
# list.pop(index) -> deletes specific location
# list.reverse() -> change the order
# list.sort() -> modify list by alphabetical order
# list.clear() -> empty the list
# list.extend(list2) -> increase the list with another one
# tupla = () -> collection unable to modify, but access by index
# set = {} -> unable to modify, without order, but unique elements at the creation moment
# diccionario = {'key':'valueAnything', ...}
# print (diccionario{key}) ...