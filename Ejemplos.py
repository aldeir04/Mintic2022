
'''
num_cuota = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
vlr_cuota = [127789,127789,127789,127789,127789,127789,127789,127789,127789,127789,127789,127789,127789,127789,127789,127789,127789,127789,127789,127789,127789,127789,127789,127789]
vlr_interes = [61338.72,58782.94,56227.16,53671.38,51115.6,48559.82,46004.04,43448.26,40892.48,38336.7,35780.92,33225.14,30669.36,28113.58,25557.8,23002.02,20446.24,17890.46,15334.68,12778.9,10223.12,7667.34,5111.56,2555.78]
vlr_pagar = [189127.72,186571.94,184016.16,181460.38,178904.6,176348.82,173793.04,171237.26,168681.48,166125.7,163569.92,161014.14,158458.36,155902.58,153346.8,150791.02,148235.24,145679.46,143123.68,140567.9,138012.12,135456.34,132900.56,130344.78]
vlr_saldo = [2939147,2811358,2683569,2555780,2427991,2300202,2172413,2044624,1916835,1789046,1661257,1533468,1405679,1277890,1150101,1022312,894523,766734,638945,511156,383367,255578,127789,0]
est_couta = ['Pagada','Pagada','Pagada','Pagada','Pagada','Pagada','Pagada','Pagada','Pagada','Pagada','En Mora','En Mora','En Mora','En Mora','En Mora','En Mora','En Mora','En Mora','Elaborada','Elaborada','Elaborada','Elaborada','Elaborada','Elaborada']
'''

'''
suma1 = sum(vlr_pagar[0:10])
suma2 = sum(vlr_pagar[10:18])
suma3 = round(sum(vlr_pagar[18:]),2)
print(suma1,suma2,suma3)
'''

'''
l = 0
m = 0

posicion = est_couta.index("Elaborada")
#l += 1
pagar = vlr_pagar[posicion]
#m = 1
print(posicion,pagar)
'''

""" alde = {"a" : 22, "b": 11}
for x in alde.values():
    print (x) """


diccionarioEstudiantes = {
    'E3454fdf':{
        'nombres': 'Laura',
        'apellidos': 'Jaramillo',
        'acudientes':[
            {
                'acudiente_uno': 'Andrea',
                'acudiente_dos': 'Juan'
            }
        ],
        'promedio': 5.0
    }
}

#for elemento in diccionarioEstudiantes:
    #print(elemento)

# Obtener todos los acudientes del diccionarioEstudiantes


""" for acudientes in diccionarioEstudiantes.values():
    print(acudientes.get('acudientes')) """


# Obtener todos los acudientes dos del dicionarioEstudiantes


""" for acudientes in diccionarioEstudiantes.values():
    print(acudientes.get('acudientes')[0]['acudiente_dos']) """



""" for codigoEstudiante,infoEstudiantes in diccionarioEstudiantes.items():
    print(infoEstudiantes['acudientes'][0]['acudiente_dos']) """



for codigoEstudiante,infoEstudiantes in diccionarioEstudiantes.items():
    for acu in range(len(infoEstudiantes['acudientes'])):
        print(infoEstudiantes['acudientes'][acu]['acudiente_dos'])


# Obtener los nombres y apellidos que obtuvieron nota mayor a 4 
# eliminar los demas estudiantes del dict 

""" for codigoEstudiante,infoEstudiante in diccionarioEstudiantes.items():
    promedio = infoEstudiante['promedio']
    if promedio > 4:
        print('Estudiante : ' + infoEstudiante['nombres'] + " " +infoEstudiante['apellidos']) """
    #else:
        #del diccionarioEstudiantes[codigoEstudiante]
        #diccionarioEstudiantes.pop(codigoEstudiante)