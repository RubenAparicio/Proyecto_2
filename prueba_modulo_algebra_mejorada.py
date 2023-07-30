import numpy as np    #Numpy solo existe para generar numeros aleatorios acá#
from package_mod.modulo_algebra import transponer_matriz, producto_cruz, multiplicacion_de_matrices, determinante_matriz, inversa_gauss_jordan, resolver_sistema_ecuaciones, resolver_sistema_ecuaciones_inversa

print("\nEste programa probará las funciones definidas en el módulo álgebra.")
print("\nPrimero se esvaluará el producto vectorial de dos vectores.\n")
print(("\nEscoja la dimensión del vector que desea evaluar: "))
print('''
            (1)R2
            (2)R3 ''')

dimension = int(input("--->"))
if not dimension in [1,2]:
    print("Ingrese un valor adecuado para ejecutar su prueba.")
elif dimension == 1:
    vector_aleatorio = np.random.randint(low=-100, high=100, size=2)
    vector_aleatorio_2 = np.random.randint(low=-100, high=100, size=2)
elif dimension == 2:
    vector_aleatorio = np.random.randint(low=-100, high=100, size=3)
    vector_aleatorio_2 = np.random.randint(low=-100, high=100, size=3)

print("\nEstos son sus vectores:")
Vector_aleatorio = vector_aleatorio.tolist()
Vector_aleatorio_copia = vector_aleatorio.tolist()
Vector_aleatorio_2 = vector_aleatorio_2.tolist()

print(Vector_aleatorio)
print(Vector_aleatorio_2)

vector_resultado = producto_cruz(Vector_aleatorio,Vector_aleatorio_2)
print("\nEste es el vector resultado del PRODUCTO CRUZ de ambos vectores:")
print(vector_resultado)

print(("\nEscoja el orden de la matriz que desea evaluar: "))
print('''
            (1)2x2
            (2)3x3 ''')

orden = int(input("--->"))

if orden == 1:
    matriz_aleatoria = np.random.randint(low=-100, high=100, size=(2,2))
    matriz_aleatoria_2 = np.random.randint(low=-100, high=100, size=(2,2))
    vector_aleatorio_sel = np.random.randint(low=-100, high=100, size=2)
elif orden == 2:
    matriz_aleatoria = np.random.randint(low=-100, high=100, size=(3,3))
    matriz_aleatoria_2 = np.random.randint(low=-100, high=100, size=(3,3))
    vector_aleatorio_sel = np.random.randint(low=-100, high=100, size=3)
else:
    print("Ingrese un orden válido para la matriz.")

print("Esta es su matriz aleatoria: ")    
Matriz_aleatoria = [[matriz_aleatoria[i][j] for j in range(len(matriz_aleatoria[0]))] for i in range(len(matriz_aleatoria))]
matriz_aleatoria_copia = [[matriz_aleatoria[i][j] for j in range(len(matriz_aleatoria[0]))] for i in range(len(matriz_aleatoria))]
Matriz_aleatoria_2 = [[matriz_aleatoria_2[i][j] for j in range(len(matriz_aleatoria_2[0]))] for i in range(len(matriz_aleatoria_2))]
print(matriz_aleatoria)

print("\nEste es el DETERMINANTE de su matriz: ")
determinante = determinante_matriz(Matriz_aleatoria)
print(determinante)

print("\nEsta es la TRANSPUESTA de su matriz: ")
matriz_transpuesta = transponer_matriz(Matriz_aleatoria)
print(matriz_transpuesta)

print("\nLa INVERSA de su matriz es: ")
inversa_gauss = inversa_gauss_jordan(Matriz_aleatoria)
inversa_gauss_decimal = np.round(inversa_gauss, decimals=5)
print(inversa_gauss_decimal)

print("\nA continuación, se genera una nueva matriz para realizar la multiplicación matricial. El par de matrices queda así: \n")
print(matriz_aleatoria)
print(f"\n {matriz_aleatoria_2}")

print("\nLa MULTIPLICACION de ambas matrices es: ")
matriz_c = multiplicacion_de_matrices(Matriz_aleatoria,Matriz_aleatoria_2)
print(matriz_c)

print("\nSe propone probar la resolución de ecuaciones por INVERSA.")
print("Para ello se usará un nuevo vector y la primera matriz definida.")
print("\nMatriz:")
print(matriz_aleatoria)
print("\nVector:")
print(vector_aleatorio_sel)
print("\nEl sistema de ecuaciones quedará de este modo: ")

for fila_matriz, elemento_lista in zip(matriz_aleatoria, vector_aleatorio_sel):
    print(fila_matriz, elemento_lista)
resolucion_de_sistema_de_ecuaciones = resolver_sistema_ecuaciones_inversa(matriz_aleatoria_copia,vector_aleatorio_sel)
resolucion_de_sistema_de_ecuaciones_decimal = np.round(resolucion_de_sistema_de_ecuaciones, decimals=5)
print("\nLa SOLUCIÓN DEL SISTEMA DE ECUACIONES es: ")
print(resolucion_de_sistema_de_ecuaciones_decimal)

print("\n¡Gracias por probar nuestro módulo!")

