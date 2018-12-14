"""
    creación de clases
"""

class Persona(object):
    """
    """
    
    def __init__(self, n, ape, ed, cod, n1, n2):
        """
        """
        self.nombre = n
        self.edad = int(ed)
        self.codigo = int(cod)
        self.apellido = ape
        self.nota1 = int(n1)
        self.nota2 = int(n2)

    def agregar_nombre(self, n):
        """
        """
        self.nombre = n

    def obtener_nombre(self):
        """
        """
        return self.nombre

    def agregar_edad(self, n):
        """
        """
        self.edad = int(n)

    def obtener_edad(self):
        """
        """
        return self.edad
    
    def agregar_codigo(self, n):
        """
        """
        self.codigo = int(n)

    def obtener_codigo(self):
        """
        """
        return self.codigo
    
    def obtener_apellido(self):
        """
        """
        return self.apellido

    
    def agregar_nota1(self, n1):
        """
        """
        self.nota1 = int(n1)

    def obtener_nota1(self):
        """
        """
        return self.nota1

    def agregar_nota2(self, n2):

        self.nota2 = int(n2)  

    
    def obtener_nota2(self):
        """
        """
        return self.nota2   
    
    def __str__(self):
        """
        """
        return "%s - %s - %d - %d - %d - %s" % (self.obtener_nombre(), self.obtener_apellido(),\
                self.obtener_edad(), self.obtener_codigo(), self.obtener_nota1(), self.obtener_nota2())



class OperacionesPersona(object):
    """
    """
    
    def __init__(self, listado):
        """
        """
        self.listado_personas = listado
    #Obtengo el promedio de notas 1 
    def obtener_promedio_n1(self):
        cadena  = ""
        #declaro la suma como entero
        suman1 = 0
        #recorro el listado de personas
        for n in self.listado_personas:
            #calculo la suma de las notas, haciendo referencia ala función que retornar los atributos de nota1
            suman1 = suman1 + n.obtener_nota1()
        #calculo el promedio, con len podemos hacer referencia al tamaño de la lista    
        resultado = suman1 / len(self.listado_personas)
        cadena = "EL promedio de notas 1 es :%s%s" % (cadena, resultado) 
        return cadena

    def obtener_promedio_n2(self):
        cadena = ""
        suman2 = 0
        for n in self.listado_personas:
            suman2 = suman2 + n.obtener_nota2()

        resultado2 = suman2 / len(self.listado_personas)
        cadena = "EL promedio de notas 2 es :%s%s" % (cadena, resultado2) 
        return cadena 

    #Con está función obtengo las personas que tienen notas menores de nota 1
    def obtener_listado_n1(self):
        resultado_n1 = ""
        #recorro la lista con el for
        for n in self.listado_personas:
            #realizo el condicional haciendo referencia a la función de nota1
            if (n.obtener_nota1() < 15):
               #declaro una variable la cuál va a ser igual a los nombres de las personas que tengan calificación menores a 15 
               resultado_n1 = "Los alumnos con notas menores que 15 son:%s%s-%s"%(resultado_n1, n.obtener_nombre(), n.obtener_apellido()) 
        return resultado_n1        
    
    def obtener_listado_n2(self):
        resultado = ""
        for n in self.listado_personas:

            if (n.obtener_nota2() < 15):
                resultado = "Los alumnos con notas menores que 15 son%s%s-%s"%(resultado, n.obtener_nombre(), n.obtener_apellido()) 
        return resultado 
    #con esta función vamos a realizar la compración de nombres que empieen con r y j
    def obtener_listado_personas(self, a, b):
        #Recorro la lista de personas
        lista_personas = []
        cadena_2 = ""
        for n in self.listado_personas:
            #Realizo la comparación de los nombres de las personas haciendo referencia a [0:1] con la posición del nombre que es la primera letra
            if (n.obtener_nombre()[0:1] == a or n.obtener_nombre()[0:1]== b):
               #le agrego a listas_personas le agrego los nombres
               lista_personas.append(n.obtener_nombre())

        return lista_personas    

    def __str__(self):

        cadena = ""
        for n in self.listado_personas:
            cadena = "%s%s %s\n" % (cadena, n.obtener_nombre(), n.obtener_apellido())  

        return cadena    

