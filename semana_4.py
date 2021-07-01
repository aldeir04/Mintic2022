""" from numpy import random as r
#print(r.choice(['Andres','Juan','Pedro', 'Mateo'], size= r.choice([1,2],p=[0.1,0.9]) , p=[0.5,0.2,0.2,0.1], replace=False))

import numpy as np
#a = np.array([34, 25, 7]) 
#print(type(a))
#print(a.shape)

#matriz = np.zeros((3,3))   # Crear una matriz de todos los ceros
#print(matriz)

a = np.array([[1,2,3], [5,6,7], [9,10,11]])
print(a)
b = a[:2, 1:3]
#print(np.fliplr(a))
#c = a[1:3,:2]
#print(c)
#b[1,1] = 1
print(b) """

import numpy as np

a = np.array([[1,2,3], [5,6,7], [9,10,11]])

b = a[:2, 1:3]
print(b)

#1. Utilizar la función incorporada map() para crear una función que retorne una lista con la longitud de 
# cada palabra (separadas por espacios) de una frase. La función recibe una cadena de texto y retornaráuna lista.



