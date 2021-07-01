
creditos = { '2015020192098' : {
        'nombres': 'Juan', 
        'apellidos': 'Arias Ruiz', 
        'est_credito': 'Activo', 
        'credito': [ {
                'id_credito': 'C0198238', 
                'cuotas': 24, 
                'valor': 3066936.00, 
                'interes': 0.020, 
                'cuo_vencidas': 8, 
                'cuo_pagadas':10
}
]
}
}

def calcularInforme(creditos)-> list:
    total_pagadas = 0
    total_vencidas = 0
    total_elaboradas = 0
    sms2 = ""
    lista_salida = []

    for x, y in creditos.items():                             # sacar id e iniciales de los nombres...

        if y["est_credito"] == "Activo":                          # solo entran creditos cuyo estado es activo

            inicial_nombre = y["nombres"][0]                   # inicial del nombre
            inicial_apellido = y["apellidos"][0]                 # inicial del apellido 
        
            acum = y["credito"][0]["valor"]              # valor total del credito
            n_cuotas = y["credito"][0]["cuotas"]             # numero de cuotas
            vlr_cuota = (acum / n_cuotas)                         # cuota fija
            interes = y["credito"][0]["interes"]            # los intereses
            cuotas_pagas = y["credito"][0]["cuo_pagadas"]        # cuotas ya pagas
            cuota_vencida = y["credito"][0]["cuo_vencidas"]       # cuotas vencidas 

            sms = x +"-"+ inicial_nombre +"-"+ inicial_apellido +"-" # cadena con los codigos y las iniciales
            sms2 += sms

            for x in range(n_cuotas):                                  # ciclo hasta el numero de cuotas
                vlr_pagar = acum * interes                             # valor a pagar valos total mas los intereses
                acum -= vlr_cuota                                      # valor total menos valor a pagar cada vuelta se decrementa
                cta = vlr_cuota + vlr_pagar                             #  valor de la cuota fija mas valor a pagar 

                if x < cuotas_pagas :
                    total_pagadas += cta
                if x >= cuotas_pagas and x < cuotas_pagas + cuota_vencida :
                    total_vencidas += cta
                if x >= cuotas_pagas + cuota_vencida:
                    total_elaboradas += cta
            
        

    sms_tupla = (round(total_pagadas,2),round(total_vencidas,2),round(total_elaboradas,2))
    lista_salida.append(sms2[:-1])                                # añadircadena a la lista de salida
    lista_salida.append(sms_tupla)
        
    return(lista_salida)



        

