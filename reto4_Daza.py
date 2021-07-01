from functools import reduce

lectura = {'501001190001' :{'toma_lectura': [{'lec_anterior': 1232,'lec_actual': 1304,}],'estrato': 1,'estado': 'activo'},
'501002190324' :{'toma_lectura': [{'lec_anterior': 1203,'lec_actual': 1230,}],'estrato': 4,'estado': 'activo'}}

tarifa = {'cargo_basico': 10450,'consumo': 1200.40}

def inforServicio(lectura, tarifa):
	lista=[]
	listalectura=[]
	listaresultado=[]
	calculo=lambda val1=0,val2=0,val3=0:(val1*val2)+val3
	operacion=lambda operacion,val1=0,val2=0,val3=0: operacion(val1,val2,val3)
	for x,y in lectura.items():
		if (y.get('estado')=='inactivo'):
			lista.append('Sin lecturas')
			menoroiguala15=0
			mayora15=0
			listaidytotal=0
			tupla='Sin lecturas'
		elif (y.get('estado')=='activo'):
			for lecturaPredios in y.get('toma_lectura'):
				lecturaActual=lecturaPredios.get('lec_actual')-lecturaPredios.get("lec_anterior")
				listalectura.append(lecturaActual)
				valores=list(tarifa.values())
				if(y.get('estrato')==1):
					listaTarifa=list(map(lambda val1=0:val1*0.6,valores))
					resultado=operacion(calculo, lecturaActual,listaTarifa[1],listaTarifa[0])
				elif(y.get('estrato')==2):
					listaTarifa=list(map(lambda val1=0:val1*0.85,valores))
					resultado=operacion(calculo, lecturaActual,listaTarifa[1],listaTarifa[0])
				elif(y.get('estrato')==3):
					listaTarifa=list(map(lambda val1=0:val1*0.90,valores))
					resultado=operacion(calculo, lecturaActual,listaTarifa[1],listaTarifa[0])
				elif(y.get('estrato')>=4):
					listaTarifa=list(map(lambda val1=0:val1*1.5,valores))
					resultado=operacion(calculo, lecturaActual,listaTarifa[1],listaTarifa[0])
				lista.append(x)
				listaresultado.append(round(resultado,2))
			listafiltrada=list(filter(lambda valor: valor!= 'Sin lecturas',lista))
			listaidytotal=list(zip(listafiltrada,listaresultado))
			menoroiguala15=list(filter(lambda valor:valor <= 15 ,listalectura ))
			mayora15=list(filter(lambda valor:valor > 15 ,listalectura ))
			sumtotal=reduce(lambda acumulador=0,elemento=0: acumulador+elemento,listaresultado)
			tupla=(listaidytotal,menoroiguala15,mayora15,round(sumtotal,2))
	return (tupla)

print(inforServicio(tarifa,lectura))


