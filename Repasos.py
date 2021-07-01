""" n = float(input('Digite un numero: '))

if (n > 0): 
    print('El numero es positivo')
if (n < 0): #and len(str(n)) == 4:
    print('El numero es negativo') """


'''
num = int(input("digite numero: "))
if num == 0:
    print("El numero no puede ser cero (0)")
elif num < 0:
    print("El numero es negativo")
    if len(str(num)) == 4:
        print("El numero tiene 3 digitos")
else:
    print("El numero es positivo")
    if len(str(num)) == 2:
        print("El numero tiene 2 digitos")
'''

""" oracion = 'Mary entiende muy bien Python'
frases = oracion.split() # convierte a una lista cada palabra
print("La oración analizada es:", oracion, ".\n") #\n es el carácter de salto de línea y se usa para indicar el fin de una línea de texto y el inicio de una línea nueva

for palabra in range(len(frases)):
    print("Palabra: {0}, en la frase su posición es: {1}".format(frases[palabra], palabra)) """

""" datos_basicos = {
    "nombres":"Leonardo Jose",
    "apellidos":"Caballero Garcia",
    "cedula":"26938401",
    "fecha_nacimiento":"03/12/1980",
    "lugar_nacimiento":"Maracaibo, Zulia, Venezuela",
    "nacionalidad":"Venezolana",
    "estado_civil":"Soltero"
}
clave = datos_basicos.keys()
valor = datos_basicos.values()

cantidad_datos = datos_basicos.items()

for clave, valor in cantidad_datos:
    print(clave + ": " + valor) """

# Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas.
# Luego de realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores de edad (mayores o iguales a 18 años)

""" nombres = list()
edades = list()

for x in range(5):
    nom = "Ingrese el nombre de la persona: " + str(x+1) + "-> "
    nombre = input(nom)
    edad = int(input("Ingrese la edad de la persona: "))
    nombres.append(nombre)
    edades.append(edad)

print("Nombre de de las personas de mayor edad: ")

for x in range(len(edades)):
    if edades[x] >= 18:
        print(nombres[x]) """



