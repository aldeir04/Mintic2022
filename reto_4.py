""" lectura = {
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

tarifa = {'cargo_basico': 10450, 'consumo': 1200.40} """

#Si es así es un error, debe entrar a ese bloque solo si luego de recorrer toodo el diccionario aún no tiene lecturas. 
# Por eso te da para un solo predio sin lecturas pero no cuando hay varios entre los cuales al menos uno no tiene.

def inforServicio(lectura, tarifa):
    sms2 = []
    mayor_15 = []
    menor_15 = []
    total = 0

    for i in lectura:
        if lectura[i]['estado'] == 'activo':
            valor_lec_basi = lectura[i]['toma_lectura'][0]['lec_anterior']
            valor_lec_act = lectura[i]['toma_lectura'][0]['lec_actual']
            metros = valor_lec_act - valor_lec_basi
        
            if lectura[i]['estrato'] == 1:
                consumo = ((metros * tarifa['consumo']) + tarifa['cargo_basico']) * 0.6
                total += consumo
            elif lectura[i]['estrato'] == 2:
                consumo = ((metros * tarifa['consumo']) + tarifa['cargo_basico']) * 0.85
                total += consumo
            elif lectura[i]['estrato'] == 3:
                consumo = ((metros * tarifa['consumo']) + tarifa['cargo_basico']) * 0.9
                total += consumo
            elif lectura[i]['estrato'] > 3:
                consumo = ((metros * tarifa['consumo']) + tarifa['cargo_basico']) * 1.5
                total += consumo
            sms2.append((i, round(consumo, 2)))
            
            if metros <= 15:
                    menor_15.append(metros)    
            else:
                mayor_15.append(metros)
            sms = (sms2, menor_15, mayor_15, round(total, 2))
        if total<=0:
            sms = 'Sin lecturas'
    return(sms)    
#print(inforServicio(lectura,tarifa))

print(inforServicio({
    'OO5010017089' :{
            'toma_lectura':  [
                {
                'lec_anterior': 5400,
                'lec_actual': 5430,
                }
            ],
        'estrato': 3,
        'estado': 'inactivo'
    },
    '005010027089' :{
            'toma_lectura':  [
                {
                'lec_anterior': 6450,
                'lec_actual': 6536,
                }
            ],
        'estrato': 2,
        'estado': 'activo'
    },
    '005010037089' :{
            'toma_lectura':  [
                {
                'lec_anterior': 6700,
                'lec_actual': 6790,
                }
            ],
        'estrato': 3,
        'estado': 'inactivo'
    }
},
{
    'cargo_basico': 10450,
    'consumo': 1200.40
}))
# El esperado es ([('005010027089', 96631.74)], [], [86], 96631.74)