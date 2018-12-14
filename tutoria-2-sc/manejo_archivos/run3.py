from paquete_archivos.miarchivo import MiArchivo
from paquete_modelo.mimodelo import Persona, OperacionesPersona

m = MiArchivo()
lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]

# print(lista)

lista = lista[1:]
#lista vacia
lista_personas = []

# p = Persona(lista[1][1], lista[1][2], lista[1][3], lista[1][0])
for d in lista:

    p = Persona(d[1], d[2], d[3], d[0], d[4], d[5])
    lista_personas.append(p)
#Creó un objeto tipo OperacionesPersona 
operaciones = OperacionesPersona(lista_personas)
#realizo la impresión del objeto con los métodos que solicita
print(operaciones.obtener_promedio_n1())
print(operaciones.obtener_promedio_n2())
print(operaciones.obtener_listado_n1())
print(operaciones.obtener_listado_n2())
#realizo la impresión de la lista de personas 
print("El listado de personas cuyo nombre empieza con 'R' o 'J' es: %s" %operaciones.obtener_listado_personas("R", "J"))  