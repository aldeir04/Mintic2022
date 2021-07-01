import pandas as pd


ventas = pd.Series([15,12,21], index = ["Ene", "Feb", "Mar"])
#print(ventas)

datos = { 'manzanas' : [ 3 , 2 , 0 , 1 ], 'naranjas' : [ 0 , 3 , 7 , 2 ] }
compras = pd.DataFrame( datos )
#print(compras)

elementos = { 
    "Numero atómico":[1, 6, 47, 88],
    "Masa atómica":[1.008, 12.011, 107.87, 226],
    "Familia":["No metal", "No metal", "Metal", "Metal"]
}
#print(elementos)

tabla_periodica = pd.DataFrame(elementos)
#print(tabla_periodica)

tabla_periodica = pd.DataFrame(elementos,
                               index = ["H", "C", "Ag", "Ra"],
                               columns = ["Familia", "Numero atómico", "Masa atómica"]
)
print(tabla_periodica)

import numpy as np

unidades_Datos = np.array([[2, 5, 3, 2],
                         [4, 6, 7, 2], 
                          [3, 2, 4, 1]])
#print(unidades_Datos)

unidades = pd.DataFrame(unidades_Datos)
#print(unidades)

unidades = pd.DataFrame(unidades_Datos, index = [2015, 2016, 2017], columns = ["Ag", "Au", "Cu", "Pt"])
unidades.index.name = 'Años'
unidades.columns.name = 'Elementos'

#print(unidades)



unidades_2015 = {"Ag":2, "Au":5, "Cu":3, "Pt":2}
unidades_2016 = {"Ag":4, "Au":6, "Cu":7, "Pt":2}
unidades_2017 = {"Ag":3, "Au":2, "Cu":4, "Pt":1}

unidades = pd.DataFrame([unidades_2015, unidades_2016, unidades_2017],
                       index = [2015, 2016, 2017])
#print(unidades)


entradas = pd.Series([11, 18, 12, 16, 9, 16, 22, 28, 31, 29, 30, 12],
            index = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago",
             "sep", "oct", "nov", "dic"])
#print(entradas)

salidas = pd.Series([9, 26, 18, 15, 6, 22, 19, 25, 34, 22, 21, 14],
            index = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago",
             "sep", "oct", "nov", "dic"])
#print(salidas)

almacén = pd.DataFrame({"entradas": entradas, "salidas": salidas})
almacén["neto"] = almacén.entradas - almacén.salidas
#print(almacén)