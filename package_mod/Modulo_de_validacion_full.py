# Instrucciones generales:

# se crearan las funciones valInt(), valFloat() y valComplex()
# la idea es que este modulo sirva para validar tipos numericos
# en caso de recibir un solo argumento, la funcion 
# debe arrojar TRUE si el argumento coincide con el tipo esperado
# de no coincidir debe arrojar FALSE

# en caso de revibir dos argumentos, se comprueba si es de 
# tipo int, float o complex para las respectivas funciones
# como segundo argumento se espera un tuple o list con dos valores numericos
# esto viene a representar un INTERVALO
# si este segundo argumento (lsita o tuplas) se presenta
# como tupla (eg (3,8)) es un intervalo abierto, los extremos
# no se incluyen
# en caso de que este segundo argumento se pase como lsita []
# se trata d eun intervalo cerrado 

# -----------------------------------------------------------


# funcion para  validar enteros:
# arrojara TRUE si al ingresar un solo argumento el numero es entero
# o si al ingresar dos argumentos el primero es entero y 
# esta dentro del intervalo indicado

# definiendo funcion:

# La funcion recibe dos argumentos: numero e intervalo

# se establece que el argumento intevalo comience en None, en caso de que la funcion reciba un solo argumento
def valInt(numero, intervalo=None):
    # Usaremos la variable validacion como control para mostrar lo que queremos en los returns
    validacion = True
    # Verificamos que si el intervalo es vacio, en este caso solo se ha ingresado a la funcion un numero
    # Procedemos a verificar si es entero haciendo uso de la funcion isinstance
    # con isinstance comprobamos si una variable es de un cirto tipo de clase o subclase
    # devuelve valores booleanos si se cumple es True si no se cumple False
    while intervalo == None:
        if isinstance(numero,int) == False:
            validacion = False
            return validacion
        else:
            return validacion
        
    #ciclo while que se ejecula cuando el intervalo no esta vacio
    while intervalo != None:
        #comprobamos si es una tupla, intervalo abierto ()
        if isinstance(intervalo,tuple):
            # comprobamos que la tupla solo tenga dos elementos
            if len(intervalo) != 2:
                raise ValueError('El intervalo debe tener dos extremos')
            # comprobamos que el intervalo este dado de forma ascendente
            elif intervalo[0] > intervalo[-1]:
                raise ValueError ('El intervalo debe ir de menor a mayor')
            # comprobamos si el numero es menor que el extremo izquierdo o mayor que el derecho
            elif numero <= intervalo[0] or numero >= intervalo[-1] or isinstance(numero,int) ==False:
                validacion = False
            # si noda de lo anterior se cumple, significa que el numero 
            return validacion              
        # En caso de ser tupla comprobamos si es una lista []
        elif isinstance(intervalo,list):
            # comprobamos que la lista solo tenga dos elementos
            if len(intervalo) != 2:
                raise ValueError('El intervalo debe tener dos extremos')
            # comprobamos que el intervalo este dado de forma ascendente
            elif intervalo[0] > intervalo[-1]:
                raise ValueError ('El intervalo debe ir de menor a mayor')
            # comprobamos si el numero es menor que el extremo izquierdo o mayor que el derecho
            elif numero < intervalo[0] or numero > intervalo[-1] or isinstance(numero,int) ==False:
                validacion = False
            
            return validacion
        
        else:
            raise TypeError('El segundo argumento debe ser una tupla o una lista')
    return validacion    

#print(valInt(4,(2,5)))

# ---------------------------------------------------------------------------------------


# funcion para validar valores flotantes (ver si el numero es decimal o no):

#def valFloat ()   

def valFloat (numero, intervalo=None):
    validacion = True
    if intervalo is None:
        if not isinstance(numero, float):
            validacion = False
            
    if intervalo != None:
        if isinstance(intervalo,tuple):
            if len(intervalo) != 2:
                raise ValueError('El intervalo debe tener dos extremos')
            elif intervalo[0] >= intervalo[-1]:
                raise ValueError('El intervalo debe ir de menor a mayor')
            elif numero <= intervalo[0] or numero >= intervalo[-1]:
                validacion = False
        elif isinstance(intervalo, list):
            if len(intervalo) != 2:
                raise ValueError('El intervalo debe tener dos extremos')
            elif intervalo[0] >= intervalo [-1]:
                raise ValueError('El intervalo debe ir de menor a mayor')
            elif numero < intervalo[0] or numero > intervalo[-1]:
                validacion = False
        else:
            raise TypeError('El segundo argumento debe ser una tupla o una lista')            
    return validacion                 

#print(valFloat(4.6))
#-----------------------------------------------------------------------------------

# funcion para validar numeros complejos:

#definiendo fucnion para validad complejos
# valida si el modulo del numero complejo esta
# en el intervalo señalado por la tupla o la lista

def valComplex (numero, intervalo=None):
    validacion = True
    if intervalo is None:
        if not isinstance(numero, complex):
            validacion = False
            #se usa la funcion predefinida de python abs para calcular el modulo del numero complejo
    
    if intervalo != None:
        modulo_complejo = abs(numero)
        if isinstance(intervalo,tuple):
            if intervalo[0] >= intervalo[-1]: 
                raise ValueError('El intervalo debe ir de menor a mayor')
            elif len(intervalo) != 2:
                raise ValueError('El intervalo debe tener dos extremos')    
            elif modulo_complejo <= intervalo[0] or modulo_complejo >= intervalo[-1]:
                validacion = False
        elif isinstance(intervalo,list):
            if intervalo[0] >= intervalo[-1]:
                raise ValueError('El intervalo debe ir de menor a mayor')  
            elif len(intervalo) != 2:
                raise ValueError('El intervalo debe tener dos extremos')
            elif modulo_complejo < intervalo[0] or modulo_complejo > intervalo[-1]:
                validacion = False
        else:
            raise TypeError('El segundo argumento debe ser una tupla o una lista')
    return validacion  

#print(valComplex(3+4j))

#--------------------------------------------------------------------------------------------


# funcion para validar listas

# definiremos una funcion para validar listas
# el primer argumento debe ser una lista
# el segundo argumento puede ser una lista o un entero
# el tercer argumento debe ser una cadena de texto


def valList(lista_1,comparacion=None,texto=None):
    validacion = True
    if comparacion == None and texto == None:
        if not isinstance(lista_1,list):
            validacion = False
    if comparacion != None or texto != None:
        if texto == 'value':
            if isinstance(lista_1, list) and isinstance(comparacion,list):
                 if lista_1 != comparacion:
                     validacion = False
            else:
                validacion = False
        elif texto == 'len':
            if isinstance(comparacion,int):
                if len(lista_1) != comparacion:
                    validacion =False
            elif comparacion != int or comparacion != list:
                
                raise TypeError('El segundo o tercer argumento no son validos')  
            
        else:
            raise ValueError('El tercer agumento solo puede ser len o value')   
    return validacion

#print(valList([1,2,3],[1,2,3],'value'))