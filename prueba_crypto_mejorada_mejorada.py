
#import modulo_crypto as mc
from package_mod.modulo_crypto import encriptar_texto, desencriptar_texto


diccionario_encriptado = {" ": "º", "a": "*", "b": "#", "c": "$", "d": "%", "e": "&", "f": "/", "g": "(", "h": ")", "i": "=", "j": "?", "k": "+", "l": "-", "m": "*", "n": "ϟ", "o": "ϡ", "p": ";", "q": ":", "r":"!", "s":"@", "t":"#", "u":"$", "v":"%", "w":"^", "x":"&", "y":"*", "z":"(", "0":"~", "1":"`", "2":"|", "3":"^", "4":"[", "5":"{", "6":"'", "7":"<", "8":"_", "9":"]", ".":"ª", ",":"π"}

print("En este programa se probará la encriptación y desencriptación de un texto simple.\n")

continuar = True
while continuar == True:
    print("Por favor, ingrese a continuación el texto a encriptar. Si desea cancelar la ejecución del programa, ingrese el número 0")
    texto = input("---> ")

    if texto == "0":
        print("¡Gracias por probar nuestro programa!")
        break

    elif isinstance(texto,str):

        Texto_encriptado = encriptar_texto(texto, diccionario_encriptado)
        print(f"\nSu texto encriptado es: \n{Texto_encriptado}")

        Texto_desencriptado = desencriptar_texto(texto, diccionario_encriptado)
        print(f"\nSu texto desencriptado es: \n{Texto_desencriptado}")
        
        continuar_2 = True
        while continuar_2 == True:
            nueva_encriptacion = input("¿Desea realizar una nueva encriptación? (si, no): ")
            if nueva_encriptacion.lower() in ["si", "sí"]:
                continuar_2 = False 
                continuar == True
            elif nueva_encriptacion.lower() in ["no"]:
                print("¡Gracias por probar nuestro programa!")
                continuar = False
                break
            else:
                print("Debe responder con sí o no.")
                continuar_2 = True

    else:
        raise ValueError("Ingrese un valor correcto.")