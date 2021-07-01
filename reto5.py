#ruta = r'E:\MisiónTic_2021\Programación\Mision-TIC-GRUPO-09-master\Pruebas_SABER_11_220_estudiantes_2020_1.csv'
""" {'Municipio': {0:'BARRANQUILLA', 1: 'CALI', 2: 'PALMIRA', 3: 'PUERTO COLOMBIA', 4: 'SOGAMOSO', 5: 'TUNJA', 6: 'ZIPAQUIRÁ'},
'Promedio': {0: 16.571428571428573, 1: 16.44, 2: 16.0, 3: 16.0, 4: 16.0, 5: 17.0, 6: 16.0}, 
'Mediana': {0: 17, 1: 16, 2: 16, 3: 16, 4: 16, 5: 17, 6: 16},
'Total Estudiantes': {0: 21, 1: 25, 2: 17, 3: 1, 4: 1, 5: 1, 6: 2}} """
#import matplotlib.pyplot as plt 
import pandas as pd

def infoIcfes(rt_archivo):
    

    if rt_archivo.endswith('.csv') == False:
        return('Extensión inválida.') 

    try:
        df = pd.read_csv(rt_archivo, encoding = 'latin-1', engine = 'python')
    except:
        return('Error al leer el archivo de datos.')

    for i in df.columns:
        df_filtar = df.query('16 <= edad_del_estudiante <= 17')
        df_domicilio = df_filtar[['edad_del_estudiante','municipio_de_residencia']]

        d_promedio = df_domicilio.groupby('municipio_de_residencia', as_index=False).mean()
        d_mediana =  df_domicilio.groupby('municipio_de_residencia', as_index=False).median()
        d_totales =  df_domicilio.groupby('municipio_de_residencia', as_index=False).count()

        d_datos = pd.merge(d_promedio,d_mediana, on= 'municipio_de_residencia')
        d_datos = pd.merge(d_datos,d_totales, on= 'municipio_de_residencia')
        d_datos.columns = ['Municipio', 'Promedio', 'Mediana', 'Total Estudiantes']

    return d_datos.to_dict('dict')


#print(infoIcfes(ruta))

# PRUEBA 1
print(infoIcfes('https://raw.githubusercontent.com/IsraelArbona/Mision-TIC-GRUPO-09/master/Pruebas_SABER_11_220_estudiantes_2020_1.csv'))

# PRUEBA 2
print(infoIcfes('https://raw.githubusercontent.com/IsraelArbona/Mision-TIC-GRUPO-09/master/Pruebas_SABER_11_220_estudiantes_2020_1.xlxs'))

# PRUEBA 3
print(infoIcfes('https://raw.githubusercontent.com/IsraelArbona/Mision-TIC-GRUPO-09/master/Pruebas_SABER_11_220_estudiantes_202.csv'))

