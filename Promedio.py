# Hallar promedio
Total_n = {
    'n_1': float(input("Digite el primer dato: ")),  
    'n_2': float(input("Digite el primer dato: ")),  
    'n_3': float(input("Digite el primer dato: ")),
    'n_4': float(input("Digite el primer dato: ")), 
    }

suma = sum(Total_n.values())
n = len(Total_n)

def calcular_promedio(Total_n):
    resultado = str(suma / n)
    # resultado = round(resultado,1)
    return ('El promedio es: '+ resultado)

print(calcular_promedio(Total_n))

'''

# como realizar un funcion que calcule el promedio de varios datos
# tener como referencia la funciones de python sum() len()

'''