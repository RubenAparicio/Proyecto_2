### Modulo de encriptación

## En este módulo se plantearan 2 funciones, una que encripte y otra que desencripte un mensaje solicitado
## Es decir, una cadena de caracteres.

# Para esto, aprovecharemos la funcionalidad de los diccionarios.
# Para cada programa, se definirá un diccionario donde se especifiquen los caracteres equivalentes.

#aca se define la función para encriptar. Dependerá del texto que ingrese el usuario y el diccionario definido.

def encriptar_texto(cadena_de_texto, diccionario_encriptado):
    cadena_de_texto = cadena_de_texto.lower()
    texto_encriptado = ""    #acá se acumulará el texto que se vaya encriptando
    for letra in cadena_de_texto:  #para cada letra de la cadena de caracteres...
        if letra in diccionario_encriptado:   #si esta se encuentra dentro del diccionario definido
            texto_encriptado += diccionario_encriptado[letra]   #entonces al texto encriptado se le agregará el value asociado a dicha letra
        else:
            texto_encriptado += letra #Si en algún caso, dicha letra no estuviera en el diccionario, entonces se agrega directamente al cripto.
    return texto_encriptado

def desencriptar_texto(texto_encriptado, diccionario_encriptado):
    desencriptado_diccionario = {}
    
    for key,value in diccionario_encriptado.items():  #Acá se invierten los valores del diccionario. keys in values, and reverse.
        desencriptado_diccionario[value] = key

    texto_desencriptado = ""   #acá se acumulará el texto desencriptado 
    for simbolo in texto_encriptado:  #para cada símbolo en la cadena de caracteres
        if simbolo in desencriptado_diccionario:  #si el símbolo está en el diccionario definido
            texto_desencriptado += diccionario_encriptado[simbolo]  #entonces al texto desencriptado se le agregará el value asociado a dicho simbolo
        else:
            texto_desencriptado += simbolo #Si en algún caso, dicha letra no estuviera en el diccionario, entonces se agrega directamente al cripto.
    return texto_desencriptado