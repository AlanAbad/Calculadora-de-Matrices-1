print ("Calculadora de Matrices")
print (" - Suma \n - Resta \n - Multiplicación \n - Determinante ")
operacion = str (input("Ingrese la operación a realizar : "))
print()

# Parte SUMA

if operacion == ("Suma"):
    R1 = int (input(" Ingrese el número de renglones de la primera Matriz: "))
    C1 = int (input(" Ingrese el número de columnas de la primera Matriz: "))
    print()

    R2 = int (input(" Ingrese el número de renglones de la segunda Matriz: "))
    C2 = int (input(" Ingrese el número de columnas de la segunda Matriz: "))
    print()

# Valores que el usuario va a ingresar   
 
    Matriz1 = []
    Matriz2 = []
    print(" Ingrese los valores de la primera Matriz: ")
    for r in range (R1):
        Matriz1.append([])
        for c in range (C1):
            valor = float(input(" Renglón{}, Columna{} : ".format(r+1,c+1)))
            Matriz1[r].append(valor)

    print(" Ingrese los valores de la segunda Matriz: ")
    for r in range (R2):
        Matriz2.append([])
        for c in range (C2):
            valor = float(input(" Renglón{}, Columna{} : ".format(r+1,c+1)))
            Matriz2[r].append(valor)

# Muestra los valores de las Matrices  
          
    print()
    print(" primera Matriz")        
    for R1 in Matriz1:
        print("[",end=" ")
        for elemento in R1:
            print("{:8.2f}".format(elemento),end=" ")
        print("]")
        print()

    print()
    print(" segunda Matriz")        
    for R2 in Matriz2:
        print("[",end=" ")
        for elemento in R2:
            print("{:8.2f}".format(elemento),end=" ")
        print("]")
        print() 

# SUMA
        
    def Suma(M1,M2):
        if len (M1) == len (M2) and len (M1[0]) == len (M2[0]):
            M3 = []
            for r in range (len(M1)):
                M3.append ([])
                for c in range (len(M1[0])):
                    M3[r].append (M1[r][c] + M2[r][c])
            return M3
        else:
            return None
    MatrizS = Suma(Matriz1,Matriz2)
    if MatrizS == None:
        print(" No se pueden sumar")
        print()
    else:
        print(" Producto Suma")
        for r in MatrizS:
            print("[", end=" ")
            for elemento in r:
                print("{:8.2f}".format(elemento),end=" ")
            print("]")
            print()

# Parte RESTA

elif operacion == ("Resta"):
    R1 = int (input(" Ingrese el número de renglones de la primera Matriz: "))
    C1 = int (input(" Ingrese el número de columnas de la primera Matriz: "))
    print()

    R2 = int (input(" Ingrese el número de renglones de la segunda Matriz: "))
    C2 = int (input(" Ingrese el número de columnas de la segunda Matriz: "))
    print()

# Valores que el usuario va a ingresar   
 
    Matriz1 = []
    Matriz2 = []
    print(" Ingrese los valores de la primera Matriz: ")
    for r in range (R1):
        Matriz1.append([])
        for c in range (C1):
            valor = float(input(" Renglón{}, Columna{} : ".format(r+1,c+1)))
            Matriz1[r].append(valor)

    print(" Ingrese los valores de la segunda Matriz: ")
    for r in range (R2):
        Matriz2.append([])
        for c in range (C2):
            valor = float(input(" Renglón{}, Columna{} : ".format(r+1,c+1)))
            Matriz2[r].append(valor)

# Muestra los valores de las Matrices  
          
    print()
    print(" primera Matriz")        
    for R1 in Matriz1:
        print("[",end=" ")
        for elemento in R1:
            print("{:8.2f}".format(elemento),end=" ")
        print("]")
        print()
    print()
    print(" segunda Matriz")        
    for R2 in Matriz2:
        print("[",end=" ")
        for elemento in R2:
            print("{:8.2f}".format(elemento),end=" ")
        print("]")
        print() 

# RESTA
        
        def Resta(M1,M2):
            if len (M1) == len (M2) and len (M1[0]) == len (M2[0]):
                M3 = []
                for r in range (len(M1)):
                    M3.append ([])
                    for c in range (len(M1[0])):
                        M3[r].append (M1[r][c] - M2[r][c])
                return M3
            else:
                return None
        MatrizS = Resta(Matriz1,Matriz2)
        if MatrizS == None:
            print(" No se pueden restar")
            print()
        else:
            print(" Producto resta")
            for r in MatrizS:
                print("[", end=" ")
                for elemento in r:
                    print("{:8.2f}".format(elemento),end=" ")
                print("]")
                print()  

# Parte MULTIPLICACIÓN

elif operacion == ("Multiplicación"):
    R1 = int (input(" Ingrese el número de renglones de la primera Matriz: "))
    C1 = int (input(" Ingrese el número de columnas de la primera Matriz: "))
    print()

    R2 = int (input(" Ingrese el número de renglones de la segunda Matriz: "))
    C2 = int (input(" Ingrese el número de columnas de la segunda Matriz: "))
    print()

# Valores que el usuario va a ingresar   
 
    Matriz1 = []
    Matriz2 = []
    print(" Ingrese los valores de la primera Matriz: ")
    for r in range (R1):
        Matriz1.append([])
        for c in range (C1):
            valor = float(input(" Renglón{}, Columna{} : ".format(r+1,c+1)))
            Matriz1[r].append(valor)

    print(" Ingrese los valores de la segunda Matriz: ")
    for r in range (R2):
        Matriz2.append([])
        for c in range (C2):
            valor = float(input(" Renglón{}, Columna{} : ".format(r+1,c+1)))
            Matriz2[r].append(valor)

# Muestra los valores de las Matrices  
          
    print()
    print(" primera Matriz")        
    for R1 in Matriz1:
        print("[",end=" ")
        for elemento in R1:
            print("{:8.2f}".format(elemento),end=" ")
        print("]")
        print()
    print()

    print(" segunda Matriz")        
    for R2 in Matriz2:
        print("[",end=" ")
        for elemento in R2:
            print("{:8.2f}".format(elemento),end=" ")
        print("]")
        print() 

# MULTIPLICACiÓN
        
        def Multiplicación(M1,M2):
            if len (M1) == len (M2):
                M3 = []
                for r in range (len(M1)):
                    M3.append ([])
                    for c in range (len(M2[0])):
                        M3[r].append (0)

                for r in range (len(M1)):
                    for c in range (len(M2[0])):
                        for p in range (len(M1[0])):
                            M3 [r][c] += M1 [r][p] * M2 [p][c]
                return M3
            else:
                return None
    MatrizM = Multiplicación(Matriz1,Matriz2) 
    if MatrizM == None:
        print(" No se pueden multiplicar ")
    else:
        print(" Producto Multiplicación ")
        for r in MatrizM:
            print("[",end=" ")
            for elemento in r:
                print("{:8.2f}".format(elemento), end=" ")      
            print("]")
            print()

# Parte DETERMINANTE

elif operacion == (" Determinante "):

    Matriz = []

    def mat(n):
        for i in range (n):
            Matriz.append([])
            for j in range (n):
                Matriz[i].append(0)
        return Matriz
    
    def llenar (n):
        Matriz = mat(n)
        for x in range (n):
            for y in range (n):
                Matriz[x][y] = float(input('Valor de [' + str(x) + '][' + str[y] + '] = '))

# DETERMINANTE POR GAUSS

    def gauss(n):
        for z in range (n-1):
            for x in range(1, n-z):
                if (Matriz[z][z] != 0):
                    p = Matriz[x+z][z] / Matriz[z][z]
                    for y in range (n):
                        Matriz[x+z][y] = Matriz[x+z][y] - (Matriz[z][y]*p)

    def det(n):
        deter = 1
        for x in range (n):
            deter = Matriz[x][x]*deter
            print('\nE1 determinante de la Matriz es = ', deter)

    n = int(input(" Tamaño de la Matriz : "))
    llenar(n)
    gauss(n)
    det(n)                            