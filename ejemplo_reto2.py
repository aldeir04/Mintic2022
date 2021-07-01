
if (diag_ta == 'Si'and diag_pa == 'Si' and diag_do == 'Si' and diag_dg == 'Si'):
    return {'id_diagnostico': id_diagnostico, 'resultado': 'Dengue', 'estado': True}
if (diag_ta == 'Si'and diag_pa == 'No' and diag_do == 'No' and diag_dg == 'No'): #ok
    return {'id_diagnostico': id_diagnostico, 'resultado': 'Presencia de síntomas' , 'estado': False}
if (diag_ta == 'Si'and diag_pa == 'Si' and diag_do == 'No'):
    return {'id_diagnostico': id_diagnostico, 'resultado': 'Presencia de síntomas' , 'estado': False}
if (diag_ta == 'Si'and diag_pa == 'Si' and diag_do == 'Si' and diag_dg == 'No'):
    return {'id_diagnostico': id_diagnostico, 'resultado': 'Presencia de síntomas', 'estado': False}
if (diag_ta == 'Si'and diag_pa == 'No' and diag_do == 'Si'):
    return {'id_diagnostico': id_diagnostico, 'resultado': 'Presencia de síntomas' , 'estado': False}
if (diag_ta == 'Si'and diag_pa == 'No' and diag_do == 'No' and diag_dg == 'Si'): #ok
    return {'id_diagnostico': id_diagnostico, 'resultado': 'Gripa', 'estado': True}
if (diag_ta == 'No'and diag_pa == 'Si' and diag_do == 'Si' and diag_dg == 'Si'):
    return {'id_diagnostico': id_diagnostico, 'resultado': 'Otitis', 'estado': True}
if (diag_ta == 'No'and diag_pa == 'Si' and diag_do == 'No'):
    return {'id_diagnostico': id_diagnostico, 'resultado': 'Presencia de síntomas', 'estado': False}
if (diag_ta == 'No'and diag_pa == 'Si' and diag_do == 'Si' and diag_dg == 'No'):
    return {'id_diagnostico': id_diagnostico, 'resultado': 'Presencia de síntomas', 'estado': False}
if (diag_ta == 'No'and diag_pa == 'No' and diag_do and diag_dg == 'Si'):
    return {'id_diagnostico': id_diagnostico, 'resultado': 'Presencia de síntomas', 'estado': False}
if (diag_ta == 'No'and diag_pa == 'No' and diag_do or diag_dg == 'No'):#ok
    return {'id_diagnostico': id_diagnostico, 'resultado': 'No tiene síntomas', 'estado': False}