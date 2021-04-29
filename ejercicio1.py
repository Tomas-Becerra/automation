nombre = input('Ingrese Nombre: ')
apellido = input('Ingrese Apellido: ')
edad = int(input('Ingrese Edad: '))
condicionEdad = 'cadaver'

if edad < 18:
	condicionEdad = 'menor'
elif edad > 18 and edad < 65:
	condicionEdad = 'mayor' 
elif edad >= 65 and edad < 120:
	condicionEdad = 'jubilado'
print("Su nombre es: " + nombre + " " + apellido + " y usted es un " + condicionEdad)
print("Su nombre es: {} {} y usted es un {}".format(nombre, apellido, condicionEdad))