### Modulo de algebra

##Matriz transpuesta
def transponer_matriz(matriz):
    matriz_transpuesta = []
    # Matriz transpuesta
    for i in range(len(matriz[0])):  #esta línea define el iterador sobre el número de columnas de la matriz
        fila_transpuesta = []   #fila vacía auxiliar para el resultado
        #se podría pensar que esto funciona como una especie de método de inserción haciendo analogía con métodos de ordenamiento.
        for fila in matriz:   
            fila_transpuesta.append(fila[i])  #acá se agregan los elementos correspondientes a la matríz final.
        matriz_transpuesta.append(fila_transpuesta)
    return matriz_transpuesta

##Producto vectorial
#Acá se definirá una función que permita realizar el producto vectorial de dos vectores
def producto_cruz(A, B):
    if len(A) == len(B) == 3:
        resultado = [0,0,0]
        resultado[0] = A[1] * B[2] - A[2] * B[1]
        resultado[1] = A[2] * B[0] - A[0] * B[2]
        resultado[2] = A[0] * B[1] - A[1] * B[0]
    elif len(A) == len(B) == 2:
        resultado = [0]
        resultado[0] = A[0] * B[1] - A[1] * B[0]
    return resultado

##Multiplicación de matrices
def multiplicacion_de_matrices(matriz_1, matriz_2):
    #Se define una lista vacía para la siguiente matriz
    matriz_multiplicada = []
    for i in range(len(matriz_1)):  #acá se define el iterable para las filas de la matriz_1
        fila_resultante = []    #se define una lista vacía donde se guardarán los resultados
        for j in range(len(matriz_2[0])):   #acá se define el iterable para las columnas de la matriz_2
            #recordemos que la multiplicación de matrices se hace fila_de_matriz_1 x columna_de_matriz_2
            #por eso se define el ciclo for de esa manera.
            #se hace necesario definir un acumulador para ir sumando resultado a resultado.
            elemento = 0  # acá se define un contador para los elementos que se están multiplicando.
            # es necesario ya que se sumarán varios valores al multiplicar elemento a elemento fila x columna.
            for k in range(len(matriz_2)):   #iterable para la matriz_2
                elemento += matriz_1[i][k] * matriz_2[k][j]  #literalmente, elemento gana valores mientras se multiplica fila x columna.
            fila_resultante.append(elemento)  #se agregan los elementos a la fila resultante
        matriz_multiplicada.append(fila_resultante)  #y estos valores se agregan a la matriz multiplicada
    return matriz_multiplicada

##Determinante de la matriz
## Acá se definirá una función capaz de calcular el determinante de una función 3x3 y 2x2
def determinante_matriz(A):
    ##matriz 3x3
    acumulador = 0
    if len(A) == 3:
        x = 0
        for i in range(len(A)):
            if i == 0:
                acumulador = acumulador + A[x][i]*((A[1][1]*A[2][2])-(A[2][1]*A[1][2]))
            elif i == 1:
                acumulador = acumulador - A[x][i]*((A[1][0]*A[2][2])-(A[2][0]*A[1][2]))
            elif i == 2:
                acumulador = acumulador + A[x][i]*((A[1][0]*A[2][1])-(A[2][0]*A[1][1]))
    ##matriz 2x2
    elif len(A) == 2:
        acumulador = A[0][0]*A[1][1] - A[0][1]*A[1][0]
    return acumulador

## Inversa Gauss-Jordan
def inversa_gauss_jordan(matriz):
    n = len(matriz)
    identidad = []
    #A continuación, se crea la matriz identidad 
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(float(i == j))  #esto crea una lista con un 1 si i==j y 0 si i!=j
        identidad.append(fila)
    #Acá se realizan las operaciones necesarias para llevar la matriz original a la forma requerida (escalonada reducida)
    for fila_pivote in range(n):
        elemento_pivote = matriz[fila_pivote][fila_pivote]
        if elemento_pivote == 0:
            raise ValueError("La matriz es singular")  #si es singular, no tiene inversa... Si el determinante es 0 tambien se sabe que es singular.
        for fila_a_modificar in range(n):  
            if fila_a_modificar != fila_pivote:
                coeficiente = matriz[fila_a_modificar][fila_pivote] / elemento_pivote
                for columna in range(n):
                    matriz[fila_a_modificar][columna] -= coeficiente * matriz[fila_pivote][columna]
                    identidad[fila_a_modificar][columna] -= coeficiente * identidad[fila_pivote][columna]
    #Acá se normalizan los valores de la matriz original reducida
    for fila in range(n):
        diagonal = matriz[fila][fila]
        for columna in range(n):
            matriz[fila][columna] /= diagonal
            identidad[fila][columna] /= diagonal
    return identidad

##Resolución de sistemas de ecuaciones
# Para resolver sistemas de ecuaciones, se usará el método de eliminación gaussiana
def resolver_sistema_ecuaciones(matriz, vector): 
    n = len(matriz)
    for i in range(n):
        #acá se busca el mayor elemento en la columna i
        mayor = abs(matriz[i][i])
        fila_maximo_valor = i
        for j in range(i + 1, n):
            if abs(matriz[j][i]) > mayor:
                mayor = abs(matriz[j][i])
                fila_maximo_valor = j
        #acá se intercambia la fila con el mayor elemento determinado en el paso anterior
        for k in range(i, n):
            temp = matriz[fila_maximo_valor][k]
            matriz[fila_maximo_valor][k] = matriz[i][k]
            matriz[i][k] = temp
        temp = vector[fila_maximo_valor]
        vector[fila_maximo_valor] = vector[i]
        vector[i] = temp
        #acá se resuelve para hacer 0 todos los elementos bajo la diagonal
        for j in range(i + 1, n):
            a = -matriz[j][i] / matriz[i][i]
            for k in range(i, n):
                if i == k:
                    matriz[j][k] = 0
                else:
                    matriz[j][k] += a * matriz[i][k]
            vector[j] += a * vector[i]
    #Acá se resuelve la triangular superior
    x = [0 for i in range(n)]  #esto crea una lista de n elementos 0
    i = n - 1
    while i >= 0:
        diagonal = matriz[i][i]
        x[i] = vector[i] / diagonal
        j = i - 1
        while j >= 0:
            coeficiente = matriz[j][i] / diagonal
            vector[j] -= coeficiente * vector[i]
            matriz[j][i] = 0
            j -= 1
        i -= 1
    return x
##Resolución de sistemas de ecuaciones
#Se usará el método de la inversa
def resolver_sistema_ecuaciones_inversa(matriz, vector):
    n = len(matriz)
    #acá se calcula la inversa como antes
    inversa = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(float(i == j)) 
        inversa.append(fila)       
    for fila_pivote in range(n):
        elemento_pivote = matriz[fila_pivote][fila_pivote]
        if elemento_pivote == 0:
            raise ValueError("La matriz es singular")
        for fila_a_modificar in range(n):  
            if fila_a_modificar != fila_pivote:
                coeficiente = matriz[fila_a_modificar][fila_pivote] / elemento_pivote
                for columna in range(n):
                    matriz[fila_a_modificar][columna] -= coeficiente * matriz[fila_pivote][columna]
                    inversa[fila_a_modificar][columna] -= coeficiente * inversa[fila_pivote][columna]
    for fila in range(n):
        diagonal = matriz[fila][fila]
        for columna in range(n):
            matriz[fila][columna] /= diagonal
            inversa[fila][columna] /= diagonal
    solucion = []
    for i in range(n):
        fila = inversa[i]
        producto_punto = sum([fila[j] * vector[j] for j in range(n)])
        solucion.append(producto_punto)
    return solucion
    
    