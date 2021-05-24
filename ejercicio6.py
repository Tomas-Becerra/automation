# ENUNCIADO:
# Crear una clase persona
# ATRIBUTOS: nombre, apellido, edad, DNI
# Saber los gustos de la persona:
# METODOS: 
# nombrar -> cArlos -> Carlos
# dar apellido -> suarez -> Suarez
# cumplir -> cumplir años  
# gustos de ropa -> 0 y 9 años le va a gustar la moda infantil
# -> 10 y 18 le gusta la ropa juvenil
# -> 19 y 30 ropa informal
# -> 31 y 40 ropa formal
# -> 41 y 50  ropa de crisis de la mediana edad
# -> más de 50 boinas y vestidos floreados
#
# Sitios para practicar:
# DIFICULTAD 
# 1. codeWars
# 2. hackerRank (p/empleos)
# 3. advent of code

class Persona:
    def __init__(self, nombre, apellido, edad, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni
    
    
    def nombrar(self, nombre):
        self.nombre = nombre.lower().capitalize()
    

    def darApellido(self, apellido):
        pass

    def cumplirAnios(self, edad):
        pass

    def gustoRopa(self, edad):
        pass

tom = Persona("toM", "level", 34, 12345678)

variable = nombrar(tom.nombre)
print(variable)
print(tom.nombre)

# TEMAS:
# Como crear una clase ->
#
# class NombreEnMayuscula:
#   def __init__(self):
#       atributo_uno = "se usa solo en esta clase"
#       self.atributo_dos = "con self, se podrá utilizar dentro de otro metodo y se debe agregar como parametro en la clase como def __init__(self, atributo_dos):"
#
# métodos -> 
#
#   def metodoUno(self):
#       pass  
#
#   def metodoDos(self, variableX):
#       self.atributo_dos =+ variableX 
# 
# objeto =  NombreEnMayuscula("valores de los atributos con self.atributos") 
# 
# print (objeto.atributo_uno)  
# print (objeto.metodoUno())
# print (objeto.metodoDos(valor)) 
#
# try:
#   <<bloque de trabajo ideal>>
# except TypeError:
#   <<bloque si hay un envio erroneo de valores>>
# except ValueError:
#   ....
# except:
#   ....
# finally:
#   ....

