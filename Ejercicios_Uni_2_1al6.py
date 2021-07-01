# 1. Determinar si dado un entero, éste termina en 4
'''
Tenemos que responder 3 cosas
1ro. Que el dato sea un número. TRY - EXCEPT
2do. Que se un número entero. Toca recibir el dato como Tipo INT
3ro. Que este termine en 4. Verificar bajo un IF (si termina en 4)


a = input('ingrese un número entero: ')  # Recibe el dato por consola

if a[-1]=="4":
    print('Termina en 4')
else:
    print('No termina en 4')

'''
# 2. Determine si dado un número, éste tiene 3 dígitos
'''
b = input('Ingrese un número: ')

if len(b)==3:
    print('Tiene 3 dígitos')
else:
    print('No tiene 3 dígitos')
'''

# 3. Determine si dado un número, tiene 2 cifras y si ambas cifras son pares.
""" 
c = int(input('Ingrese un número: '))

if ((c>=10) and (c<100)) or ((c<=-10) and (c>-100)):
    if c%2==0 and int(c*0.1)%2==0:
        print('Ambas dígitos son pares')
    else:
        print('Alguno de los 2 no es par')
else:
    print('No es de 2 dígitos')
 """

# 4. Determine si un número menor que 20 es primo
'''
c = int(input('Ingrese un número menor que 20: '))

if c<20:
    if((c==2) or(c==3) or (c==5) or (c==7) or (c==11) or (c==13) or (c==17) or (c==19)):
        print(f'{c} es un número primo')
    else:
        print('{c} no es primo')
else:
    print(f'¿En qué quedamos? Menor que 20')
'''
# 5. Veamos si es Primo, de 2 cifras y negativo negativo
'''
d = int(input('Ingrese un número: '))

def es_primo(d, n=2):
    if n >= d:
        print("Es primo, negativo y de 2 dígitos")
        return True
    elif d % n != 0:
        return es_primo(d, n + 1)
    else:
        print(f"{d} no es primo y {n} es divisor")
        return False

if ((d>-100) and (d<-9)):
    print(es_primo(d*-1))
else:
    print(f'{d} no es Negativo o de 2 dígitos')
'''

# 6. Leer un número entero de dos dígitos y determinar si los dos dígitos son iguales. 
'''
c = int(input('Ingrese un número: '))

if (c>9) and (c<100):
    if int(c*0.1)==int(str(c)[-1]):
        print('Tiene 2 cifras y son iguales')
    else:
        print('Nada')
else:
    print('No tiene 2 cifras')
'''
# 7. Leer dos números enteros y determinar cuál es el mayor.
'''
a = input("ingrese un numero : ")
b = input("ingrese un numero : ")
print(type(b))

if b > a:
    print(f"{b} es mayor que {a}")
else:
    print(f"{a} es menor que {b}")
'''
# 8. Leer dos números enteros de dos dígitos y determinar a cuánto es igual la suma de todos los dígitos.

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
""" b = input("ingrese numero entero: ")   #repasar estructuras iterativas while y for
a = list(b)
print(a)
for i in range(len(a)):
    a[i] = int(a[i])
print(sum(a)) """

# 9. Leer un número entero de tres dígitos y determinar en qué posición está el mayor dígito.

""" b = input("ingrese numero entero: ")   #repasar estructuras iterativas while y for
a = list(b)
print(a)
for i in range(len(a)):
    a[i] = int(a[i])
print(sum(a))

b = '12'
a = list(b)
c= '32'
d = list(c)
print(a)
print(d)
for i in range(len(a)):
    a[i] = int(a[i])
print(sum(a))
for j in range(len(d)):
    d[j] = int(d[j])
print(sum(d))
print(sum(a)+sum(d)) """
""" 
num = int(input("ingrese un numero de tres digitos: "))
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
            print("el numero mayor es", uno, "y está en la primera posición")
        elif (dos > uno) and (dos > tres):
            print("el numero mayor es", dos, "y está en la segunda posición")
        elif (tres > uno) and (tres > dos):
            print("el numero mayor es", tres, "y está en la tercera posición")
        else:
            print("No hay un numero mayor")
    else:
        print("Digite numero de 3 digitos")
except:
    print("Digite numeros enteros") """

""" 
vowels = ['a', 'e', 'i', 'o', 'u']

# index of'p' is vowels
index = vowels.index('a')
print('The index of a:', index) """

# 10. Leer un número entero de tres dígitos y determinar si algún dígito es múltiplo de los otros.

""" k = list("923")
x = int(k[0]) 
y = int(k[1])
z = int(k[2])

if (x % y == 0) or (y % x ==0): 
    print(f'{x} es un multiplo o divisor de {y}' )
else:
    if (x % z == 0) or (z % x == 0):
        print(f'{x} es un multiplo o divisor de {z}')
    else:
        if (y % z == 0) or (z % y == 0):
            print(f'{y} es un multiplo o divisor de {z}')
        else:
            print("los digitos no son ni divisores ni multiplos entre sí")
 """

# 11. Leer tres números enteros de dos dígitos cada  uno y determinar en cuál de ellos se encuentra
#el mayor dígito.
""" a='39'
b='28'
c='76'
victor1=list(a)
victor1.extend(b)
victor1.extend(c)
print(victor1)
for i in range(len(victor1)):
    victor1[i]=int(victor1[i])

print(victor1)
p=victor1.index(max(victor1))
print("el dígito más grande es ",max(victor1))
if p<2:
    print("proviene del número ",a)
elif p<4:
    print("proviene del número ",b)
else: 
    print("proviene del número ",c) """

# 12. leer un número entero de suma de los otros dos

# 13. Leer un número entero menor que 50 y positivo y determinar si es un número primo.
""" a = int(input("ingrese un numero entero menor que 50 y positivo: "))

if (a < 50 and a >=1):
    def es_primo(a, n=2):
        if n >= a:
            print("es primo")
            return True
        elif a % n != 0: 
            return es_primo(a, n + 1)
        else:
            print(f"{a} no es primo y {n} es divisor")
            return False

    es_primo(a)  """

# 14. Leer un número entero de cuatro dígitos y determinar si el segundo dígito es igual al
#penúltimo
""" a='3224'
diana1=list(a)
if diana1[1]==diana1[2]:
    print('sí son igualitos')
else:
    print('no son lojmijmoj') """

# 15. Leer un número entero y determinar si es múltiplo de 7
""" a=int(input('ingrese un número '))
if a % 7==0:
    print(f'{a} si es múltiplo de 7')
else: 
    print(f'{a} no es múltiplo de 7') """

# 16. Leer un número entero menor que mil y determinar cuántos dígitos tiene.
""" a=int(input('ingrese numero entero menor que mil: '))

if a>1000 or a<0:
    print("el numero debe ser menor que mil")
else:
    print(f'{a}, tiene', len(str(a)), ' dígitos')  """

# 17. Leer un número entero de 4 dígitos y determinar si tiene mas dígitos pares o impares.

""" num = (input("Digite un número de 4 dígitos: "))

if (int(num) >= 1000) and (int(num) <= 9999):
    p1 = int(num[0])
    p2 = int(num[1])
    p3 = int(num[2])
    p4 = int(num[3])
    
    if (int(p1%2 == 0)) and (int(p2%2 == 0)) and (int(p3%2 == 0)) and (int(p4%2 == 0)):
        print(f"En el número {num}, todos sus dígitos son pares")
    elif ((int(p1%2 == 0)) and (int(p2%2 != 0)) and (int(p3%2 == 0)) and (int(p4%2 == 0))) or (int(p1%2 == 0)) and (int(p2%2 == 0)) and (int(p3%2 != 0)) and (int(p4%2 == 0)) or (int(p1%2 == 0)) and (int(p2%2 == 0)) and (int(p3%2 == 0)) and (int(p4%2 != 0)) or (int(p1%2 != 0)) and (int(p2%2 == 0)) and (int(p3%2 == 0)) and (int(p4%2 == 0)):
        print(f"En el número {num}, hay mas dígitos pares (3) que impares (1)")
    elif ((int(p1%2 == 0)) and (int(p2%2 != 0)) and (int(p3%2 != 0))) and (int(p4%2 == 0)) or (int(p1%2 != 0)) and (int(p2%2 == 0)) and (int(p3%2 != 0)) and (int(p4%2 == 0)) or (int(p1%2 != 0)) and (int(p2%2 == 0)) and (int(p3%2 == 0)) and (int(p4%2 != 0)) or (int(p1%2 != 0)) and (int(p2%2 != 0)) and (int(p3%2 == 0)) and (int(p4%2 == 0)) or (int(p1%2 == 0)) and (int(p2%2 != 0)) and (int(p3%2 == 0)) and (int(p4%2 != 0)) or (int(p1%2 == 0)) and (int(p2%2 == 0)) and (int(p3%2 != 0)) and (int(p4%2 != 0)):
        print(f"En el número {num}, hay igual dígitos pares e impares")
    elif ((int(p1%2 == 0)) and (int(p2%2 != 0)) and (int(p3%2 != 0))) and (int(p4%2 != 0)) or (int(p1%2 != 0)) and (int(p2%2 == 0)) and (int(p3%2 != 0)) and (int(p4%2 != 0)) or (int(p1%2 != 0)) and (int(p2%2 != 0)) and (int(p3%2 == 0)) and (int(p4%2 != 0)) or (int(p1%2 != 0)) and (int(p2%2 != 0)) and (int(p3%2 != 0)) and (int(p4%2 == 0)):
        print(f"En el número {num}, hay mas dígitos impares (3) que pares (1)")
    else:
        print(f"En el número {num}, todos sus dígitos son impares")
        
else:
    print("Digite un número de 4 digitos")
 """ 

# 18. Leer tres números enteros y determinar si el último dígito de los tres números es igual.

""" num1 = (input("Digite el primer número entero: "))
num2 = (input("Digite el segundo número entero: "))
num3 = (input("Digite el tercer número entero: "))

if (0 < int(num1)) and (0 < int(num2)) and (0 < int(num3)):

    p1 = int(num1[-1])# cambiar por rang(-1), creo que es así
    p2 = int(num2[-1])# cambiar por rang(-1), creo que es así
    p3 = int(num3[-1])# cambiar por rang(-1), creo que es así
    if p1 == p2 == p3:
        print(f"De los números: {num1}, {num2} y {num3}, sus últimos dígitos son iguales")
    else:
        print(f"De los números: {num1}, {num2} y {num3}, sus últimos dígitos no son iguales")

else:
    print("Son tres números enteros") """    

# 19. A un trabajador le pagan según sus horas trabajadas por una tarifa de pago por hora. Si la cantidad de horas trabajadas es mayor 40 horas. La tarifa se incrementa en un 50% para las
# horas extras. Calcular el salario del trabajador dadas las horas trabajadas y la tarifa ingresadas por el usuario.

""" HorasTrab = input("Digite cantidad de horas trabajadas: ")
TarifaXhora = input("Digite tarifa por hora: ")
try:
    if int(HorasTrab) > 40:
        HorasExt = int(HorasTrab) - 40
        TarHorExt = int(TarifaXhora) * 50/100
        Salario = (int(TarifaXhora) * int(HorasTrab)) + (TarHorExt * HorasExt)
    else:
        Salario = (TarifaXhora * HorasTrab)
    print("el salario del trabajador es:", Salario)
except:
    print("Digite numeros enteros") """

# 20. Hacer un algoritmo que calcule el total a pagar por la compra de camisas. Si se compran tres camisas o más se aplica un descuento del 20% sobre el total de la compra y si son menos de tres camisas un descuento del 10%

""" numerocamisas= int(input('Digite cantidad de camisas '))
valorcamisa=10
if numerocamisas>=3:
    total=(numerocamisas*valorcamisa*0.8)   
else: 
    total=(numerocamisas*valorcamisa*0.9)
print('el valor a pagar por las camisas es ', total) """

# 21. Hacer un programa que pida al usuario las tres notas de un alumno (deben estar entre 0 y 5 y pueden tener decimales) 
# y calcule el promedio e indique mediante un mensaje si aprobó o no (aprueba con nota mayor a 3). 
# Se debe validar que las notas introducidas estén dentro del rango permitido

# 22. Verificar si un texto que termina en punto es un palíndromo (capicúa). 
# Un texto es palíndromo si se lee lo mismo de izquierda a derecha o de derecha a izquierda. Ej: “Amor a roma”.

# 23. Diseñe una calculadora que sume, reste, multiplique y divida, la cual le pida al usuario mediante input el valor del primer número, 
# el valor del segundo número y la operación a realizar, hay que tener en cuenta la validación de los valores de entrada, por ejemplo: 
# Si el programa pide el primer valor, y el usuario ingresa una letra, combinaciones de números y letras o caracteres no numéricos 
# se debe mostrar un mensaje mediante otro input requiriendo que ingrese nuevamente el numero 
# e indicándole al usuario que el carácter ingresado debe ser numérico.
# En el caso que uno de los valores ingresados sea 0 y el usuario ingrese la opción de División, 
# debe imprimir un mensaje donde se indique que no se pude dividir entre cero o que el cero no puede ser dividido.
# Recomendaciones para la validación: buscar información en Google sobre valores ASCII y tabla ASCII investigue el funcionamiento de la función ord()
