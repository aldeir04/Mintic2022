lectura = {
    '501001190001': {
        'toma_lectura': [{'lec_anterior': 1232, 'lec_actual': 1304, }],
        'estrato': 1,
        'estado': 'activo'
    },
    '501002190324': {
        'toma_lectura': [{'lec_anterior': 1203, 'lec_actual': 1230, }],
        'estrato': 4,
        'estado': 'activo'
    }
} 

lectura = {
    '501001190001': {
        'toma_lectura': [{'lec_anterior': 1232, 'lec_actual': 1304,}
        ],
        'estrato': 1,
        'estado': 'inactivo'
    }
} 

lectura = {
    '201501001': {
        'toma_lectura': [
            {
                'lec_anterior': 12,
                'lec_actual': 60,
            }
        ],
        'estrato': 1,
        'estado': 'activo'
    },
    '201501002': {
        'toma_lectura': [
            {
                'lec_anterior': 2,
                'lec_actual': 6,
            }
        ],
        'estrato': 2,
        'estado': 'activo'
    },
    '201501003': {
        'toma_lectura': [
            {
                'lec_anterior': 23,
                'lec_actual': 43,
            }
        ],
        'estrato': 3,
        'estado': 'activo'
    },
    '201501004': {
        'toma_lectura':
        [
            {
                'lec_anterior': 90,
                'lec_actual': 120,
            }
        ],
        'estrato': 1,
        'estado': 'activo'
    },
    '201501005': {
        'toma_lectura': [
            {
                'lec_anterior': 1,
                'lec_actual': 9,
            }
        ],
        'estrato': 1,
        'estado': 'inactivo'
    },
    '201564006': {
        'toma_lectura': [
            {
                'lec_anterior': 10,
                'lec_actual': 20,
            }
        ],
        'estrato': 6,
        'estado': 'activo'
    }
} 


tarifa = {'cargo_basico': 10450, 'consumo': 1200.40}

""" def inforServicio(lectura : dict, tarifa : dict)-> tuple:
    llaves,m15,M15,total = [],[],[],0
    for x in lectura.keys():
        if lectura[x]['estado'] == 'activo':
            lb = lectura[x]['toma_lectura'][0]['lec_anterior']
            lac = lectura[x]['toma_lectura'][0]['lec_actual']
            m3=lac-lb
            if lectura[x]['estrato']==1:
                cons = round(((lac-lb)*tarifa['consumo']+tarifa['cargo_basico'])*0.6,2)
                total = total + cons
            elif lectura[x]['estrato']==2:
                cons = round(((lac-lb)*tarifa['consumo']+tarifa['cargo_basico'])*0.85,2)
                total = total + cons
            elif lectura[x]['estrato']==3:
                cons = round(((lac-lb)*tarifa['consumo']+tarifa['cargo_basico'])*0.9,2)
                total = total + cons
            elif lectura[x]['estrato']>3:
                cons = round(((lac-lb)*tarifa['consumo']+tarifa['cargo_basico'])*1.5,2)
                total = total + cons
            llaves.append((x,cons))
            if m3<=15:
                m15.append(m3)
            else:
                M15.append(m3)
            solucion = (llaves, m15,M15,round(total,2))
        else:
            return 'Sin lecturas'

    return solucion
# ([('501001190001', 58127.28), ('501002190324', 64291.2)], [], [72, 27], 122418.48)
"""




def inforServicio(lectura: dict, tarifa: dict) -> tuple:
    llaves, m15, M15, total = [], [], [], 0
    for x in lectura.keys():
        if lectura[x]['estado'] == 'activo':
            lb = lectura[x]['toma_lectura'][0]['lec_anterior']
            lac = lectura[x]['toma_lectura'][0]['lec_actual']
            m3 = lac-lb
            if lectura[x]['estrato'] == 1:
                cons = round(
                    ((lac-lb)*tarifa['consumo']+tarifa['cargo_basico'])*0.6, 2)
                total = total + cons
            elif lectura[x]['estrato'] == 2:
                cons = round(
                    ((lac-lb)*tarifa['consumo']+tarifa['cargo_basico'])*0.85, 2)
                total = total + cons
            elif lectura[x]['estrato'] == 3:
                cons = round(
                    ((lac-lb)*tarifa['consumo']+tarifa['cargo_basico'])*0.9, 2)
                total = total + cons
            elif lectura[x]['estrato'] > 3:
                cons = round(
                    ((lac-lb)*tarifa['consumo']+tarifa['cargo_basico'])*1.5, 2)
                total = total + cons
            llaves.append((x, cons))
            if m3 <= 15:
                m15.append(m3)
            else:
                M15.append(m3)
            solucion = (llaves, m15, M15, round(total, 2))
    if total<=0:
        solucion = 'Sin lecturas'

    return solucion


print(inforServicio(lectura, tarifa))
