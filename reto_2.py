paciente = {"id_diagnostico" : "d-001", 
"diag_ta" : "No", #Si / Si / No
"diag_pa" : "No", #No / No / No
"diag_do" : "No", #No / No / No
"diag_dg" : "No"  #Si / No / No
}

# 1 = Presenta Sintomas
# 0 = No tiene sintomas

def diagSintoma(paciente)->dict:
    
    if (paciente["diag_ta"]) == "Si" and (paciente["diag_pa"]) == "Si" and (paciente["diag_do"]) == "Si" and (paciente["diag_dg"]) == "Si":
        return ({"id_diagnostico": (paciente["id_diagnostico"]), "resultado": "Dengue", "estado": True})
    if (paciente["diag_ta"]) == "Si" and (paciente["diag_pa"]) == "No" and (paciente["diag_do"]) == "No" and (paciente["diag_dg"]) == "No":
        return ({"id_diagnostico": (paciente["id_diagnostico"]), "resultado": "Presencia de síntomas" , "estado": False})
    if (paciente["diag_ta"]) == "Si" and (paciente["diag_pa"]) == "Si" and (paciente["diag_do"]) == "No":
        return ({"id_diagnostico": (paciente["id_diagnostico"]), "resultado": "Presencia de síntomas" , "estado": False})
    if (paciente["diag_ta"]) == "Si" and (paciente["diag_pa"]) == "Si" and (paciente["diag_do"]) == "Si" and (paciente["diag_dg"]) == 'No':
        return ({"id_diagnostico": (paciente["id_diagnostico"]), "resultado": "Presencia de síntomas", "estado": False})
    if (paciente["diag_ta"]) == "Si" and (paciente["diag_pa"]) == "No" and (paciente["diag_do"]) == "Si":
        return ({"id_diagnostico": (paciente["id_diagnostico"]), "resultado": "Presencia de síntomas" , "estado": False})
    if (paciente["diag_ta"]) == "Si" and (paciente["diag_pa"]) == "No" and (paciente["diag_do"]) == "No" and (paciente["diag_dg"]) == 'Si':
        return ({"id_diagnostico": (paciente["id_diagnostico"]), "resultado": "Gripa", "estado": True})
    if (paciente["diag_ta"]) == "No" and (paciente["diag_pa"]) == "Si" and paciente["diag_do"] == "Si" and (paciente["diag_dg"]) == 'Si':
        return ({"id_diagnostico": (paciente["id_diagnostico"]), "resultado": "Otitis", "estado": True})
    if (paciente["diag_ta"]) == "No" and (paciente["diag_pa"]) == "Si" and (paciente["diag_do"]) == "No":
        return ({"id_diagnostico": (paciente["id_diagnostico"]), "resultado": "Presencia de síntomas", "estado": False})
    if (paciente["diag_ta"]) == "No" and (paciente["diag_pa"]) == "Si" and (paciente["diag_do"]) == "Si" and (paciente["diag_dg"]) == 'No':
        return ({"id_diagnostico": (paciente["id_diagnostico"]), "resultado": "Presencia de síntomas", "estado": False})
    if (paciente["diag_ta"]) == "No" and (paciente["diag_pa"]) == "No" and (paciente["diag_do"]) and (paciente["diag_dg"]) == "Si":
        return ({"id_diagnostico": (paciente["id_diagnostico"]), "resultado": "Presencia de síntomas", "estado": False})
    if (paciente["diag_ta"]) == "No" and (paciente["diag_pa"]) == "No" and (paciente["diag_do"]) or (paciente["diag_dg"]) == "No":
        return ({"id_diagnostico": (paciente["id_diagnostico"]), "resultado": "No tiene síntomas", "estado": False})
print (diagSintoma(paciente))

