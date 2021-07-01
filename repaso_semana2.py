'''
# Ejecución de condicionales
x = 10
if x > 0 :
    print('x es positivo')

# Ejecución alternativas
x = 10
if x%2 == 0 :
    print('x es par')
else :
    print('x es inpar')

# Condicionales encadenados
x = float(input('Digite un numero: '))
y = float(input('Digite un numero: '))
if x < y:
    print('"x" es menor que "y"')
elif x > y:
    print('"x" is mayor que "y"')
else:
    print('"x" y "y" sons iguales')

# Condicionales anidadas
x = float(input('Digite un numero: '))
y = float(input('Digite un numero: '))
if x == y:
    print('x y y son iguales')
else:
    if x < y:
        print('x es menos que y')
    else:
        print('x es mayor que y')
'''
'''
# DICCIONARIO
diccionario = {"total": 55, "descuento": True, 15: "15"}
print(diccionario)

diccionarioEjemploExcel ={"nombre":5+2,"telefono":3363692, "edad":33, "ciudad":"Pereira"}
print(diccionarioEjemploExcel)



diccionario = dict(total= 55, descuento= True, subtotal= 15)
print(diccionario)

secuencia = ('python', 'zope', 'plone')
print(secuencia)
versiones = dict.fromkeys(secuencia)
print("Nuevo Diccionario : %s" %  str(versiones))
# print("Nuevo Diccionario : {}".format(str(versiones)))

'''
'''
Estudiantes = {  'Alumno1': {'nombre':'Daniel', 'edad':11, 'estatura':1.75, 'grado':'Master'},
                 'Alumno2': {'nombre':'David', 'edad':32, 'estatura':1.85, 'grado':'Doctor'}
                 }

#print(Estudiantes)

if Estudiantes['Alumno1']['nombre'] == Estudiantes['Alumno2']['nombre']:
    print("Los nombres son iguales")
else:
    print('Los nombres son diferentes')

if Estudiantes['Alumno1']['edad'] > Estudiantes['Alumno2']['edad']:
    print(str(Estudiantes['Alumno1']['nombre']) + ' es mayor') 
    mayor = {'nombremayor':Estudiantes['Alumno1']['nombre'], 'edadmayor':Estudiantes['Alumno1']['edad'] }    
elif Estudiantes['Alumno1']['edad'] < Estudiantes['Alumno2']['edad']:
    print(str(Estudiantes['Alumno1']['nombre']) + ' es menor') 
    mayor = {'nombremayor':Estudiantes['Alumno2']['nombre'], 'edadmayor':Estudiantes['Alumno2']['edad'] }

'''

#fruta = ['banana']
#print (fruta [:])
'''
num8 = input("Digite primer numero: ")
num9 = input("Digite segundo numero: ")
try:
    if int(num8) >= -99 and int(num8) <= -10:
        num8 = int(num8) * -1
    if int(num9) >= -99 and int(num9) <= -10:
        num9 = int(num9) * -1

    if (int(num8) >= 10 and int(num8) <= 99) and (int(num9) >= 10 and int(num9) <= 99):
        sumNum8 = int(str(num8[0])) + int(str(num8[1]))
        sumNum9 = int(str(num9[0])) + int(str(num9[1]))
        sum2num = sumNum8 + sumNum9
        print("La sumatoria de los digitos del numero", num8, "es:", sumNum8)
        print("La sumatoria de los digitos del numero", num9, "es:", sumNum9)
        print("La sumatoria de todos los digitos es: ", sum2num)
    else:
        print("Los dos numeros deben ser enteros de dos digitos")
except:
    print("Digite numeros enteros")
'''
""" b = input("Digite un numero de tres cifras: ")
a = list(b)
print(a)
for i in range(len(a)):
    a[i] = int(a[i])
print(sum(a)) """

# Leer un número entero de tres dígitos y determinar en qué posición está el mayor dígito.

""" num = int(input("Digite un numero de tres digitos: "))
x = int(num*0.001)
y = int(num*0.01)
z = int(num*0.1)

if x<y:
    if y<z:
        print(f'{x}<{y}<{z}')
    else:
        print(f'{x}<{z}<{y}')
else:
    if x<z:
        print(f'{y}<{x}<{z}')
    else:
        if y<z:
            print(f'{y}<{z}<{x}')
        else:
            print(f'{z}<{y}<{x}') """

""" num10 = input("Digite numero: ")
try:
    if int(num10) < 0:
        num10 = str(int(num10) * -1)
    if (int(num10) >= 100) and (int(num10) <= 999):
        uno = str(num10[0])
        dos = str(num10[1])
        tres = str(num10[2])
        if (uno > dos) and (uno > tres):
            print("El numero mayor es", uno, "y está en la primera posición")
        elif (dos > uno) and (dos > tres):
            print("El numero mayor es", dos, "y está en la segunda posición")
        elif (tres > uno) and (tres > dos):
            print("El numero mayor es", tres, "y está en la tercera posición")
        else:
            print("No hay un numero mayor")
    else:
        print("Digite numero de 3 digitos")
except:
    print("Digite numeros enteros") """

# Explicacion del error TypeError: ‘dict’ object is not callable

#dictionary = {"key1": "value1"} 
#print(dictionary["key1"])

starling = {"name": "Starling",  "Scientific_name": "Sturnus Vulgaris",
"conservation_status_uk": "Red",
"food": "Invertebrates and fruit" }

print("Name: " + starling["name"]) 
print("Scientific Name: " + starling["Scientific_name"]) 
print("UK Conservation Status: " + starling["conservation_status_uk"]) 
print("What They Eat: " + starling["food"])