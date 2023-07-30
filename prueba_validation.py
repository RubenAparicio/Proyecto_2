from package_mod.Modulo_de_validacion_full import valInt,valFloat,valComplex,valList
#from modulo_validatiom import valInt, valFloat, valComplex, valList
import ast
#importar funciones desde el modulo 

print('\n¡Bienvenido! este programa le va a permitir hacer pruebas con el modulo de validación.')
print('Para esto, solo tiene que ingresar el número asociado al nombre de la función tal y como se le proporciona.')
print('''
      (1) = valInt
      (2) = valFloat
      (3) = valComplex
      (4) = valList
      ''')

control_1 = True

while control_1 == True:
    print('Indique el numero de la función que desea probar')
    opcion = input('---> ')
    if opcion == '1':
        print('Va a comenzar a probar la función valInt')
        print('Por favor, ingrese los datos solicitados')
        numero = input('Ingrese un numero: ')
        intervalo = input('Ingrese un intervalo ya sea en forma de tupla usando () o lista con []: ')
        
        if not numero.isdigit():
            print('Dato no válido')
        else:
            numero = int(numero)
            if intervalo == '':
                resultado = valInt(numero)
            else:
                try:
                    intervalo = eval(intervalo)
                    if not isinstance(intervalo,(tuple,list)):
                        raise ValueError
                    resultado = valInt(numero, intervalo)
                except:
                    raise ValueError
                    #print('intervalo invalido')
                    #exit()                        
            print (f'Resultado: {resultado}')            
                         
                       
            
        #intervalo = eval(intervalo)
        #resultado = valInt(numero, intervalo)
        #print(f'Resultado: {resultado}')
        
    elif opcion == '2':
        print('Va a comenzar a probar la funciñon valFloat')
        print('Por favor, ingrese los datos solicitados')
        numero = input('Ingrese un numero: ')
        intervalo = input('Ingrese un intervalo usando () o []: ')
        
        if '.' not in numero:
            print('Dato invalido')
            
        
      
        #if not numero.replace('.' , '').isdigit():
            #print('Dato invalido')
        
        else:
            if '.' in numero:
                numero = float(numero)
                if intervalo == '':
                    resultado = valFloat(numero)
                else:
                    try:
                        intervalo = eval(intervalo)
                        if not isinstance(intervalo, (tuple,list)):
                            raise ValueError
                        resultado = valFloat(numero,intervalo)  
                    except:
                        raise ValueError   
                print(f'Resultado: {resultado}')     
       
        #resultado = valFloat(numero, intervalo)
        #print(f'Resultado: {resultado}')
        
        
    elif opcion == '3':
        print('Va a comenzar a probar la función valComplex')
        print('Por favor, ingrese los datos solicitados')
        numero = input('Ingrese un numero: ')
        intervalo = input('Ingrese un intervalo usando () o []: ')
        
        
        if '+' and 'j' not in numero:
            print('Dato no valido')
        else:
            if '+' and 'j' in numero:
                numero = complex(numero)
                if intervalo == '':
                    resultado = valComplex(numero)
                else:
                    try:
                        intervalo = eval(intervalo)
                        if not isinstance(intervalo, (tuple,list)):
                            raise ValueError
                        resultado = valComplex(numero,intervalo)
                    except:
                        raise ValueError  
                print(f'Resultado: {resultado}')              

                        
    elif opcion == "4":
        print("Para validar valList, se han usado las siguientes configuraciones:")
        print("Estos elementos corresponden a una Lista(1), una Lista(2) y el tercer argumento, que corresponde a 'len' o 'values'")
        print("Esta es la primera configuración:")
        
        lista_1 = [1, 2, 3]
        comparacion = [1, 2, 3]
        texto = "value"
        print(lista_1)
        print(comparacion)
        print(texto)
        resultado = valList(lista_1, comparacion, texto)
        print("Este es el resultado:")
        print(resultado)

        print("\nEsta es la segunda configuración:")
        lista_2 = [1, 2, 3]
        comparacion_2 = 4
        texto_2 = "len"
        print(lista_2)
        print(comparacion_2)
        print(texto_2)
        resultado = valList(lista_2, comparacion_2, texto_2)
        print("Este es el resultado:")
        print(resultado)

        print("\nEsta es la tercera configuración:")
        comparacion_3 = 3
        print(lista_2)
        print(comparacion_3)
        print(texto_2)
        resultado = valList(lista_2, comparacion_3, texto_2)
        print("Este es el resultado:")
        print(resultado)
        
        #value error
        print('\nEsta es la cuarta configuración: ')
        comparacio_4 = 4
        lista_4 = [4, 9, 7]
        texto_4 = 'hola'
        print(f'''
              {lista_4}
              {comparacio_4}
              {texto_4}''')
        resultado = valList(lista_4, comparacio_4,texto_4)
        print('Este es el resultado: ')
        print(resultado)
        
        # type error
        print('\nEsta es la quinta configuracion: ')
        comparacio_5 = 4.5
        print(f'''
              {lista_4}
              {comparacio_5}
              {texto_2}''')
        resultado = valList(lista_4,comparacio_5,texto_2)
        print('Este es el resultado: ')
        print(resultado)
        
        # type error
        print('\nEsta es la sexta configuracion: ')
        comparacio_5 = 4.5
        texto_6 = 100
        print(f'''
              {lista_4}
              {comparacio_5}
              {texto_2}''')
        resultado = valList(lista_4,comparacio_5,texto_2)
        print('Este es el resultado: ')
        print(resultado) 
        
        #resultado = valList(lista_1,comparacion,texto)
        #print(f'Resultado: {resultado}') 
        
        
    else:
        print('No ha ingresado una opción valida')                
        
        #pides los argumentos
        
        #invocas la funcion y relizas la operacion y la guardar en una variable
        # imprimes por pantalla los argumentos y el resultado de la funcion[]