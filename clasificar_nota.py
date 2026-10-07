def clasificar_nota(nota):
    if nota < 0 or nota > 10:
        raise ValueError("Error: La nota debe estar entre 0 y 10.")
        
    
    if nota >= 9:
        calificacion = "Sobresaliente"
    elif nota >= 7:
        calificacion = "Notable"
    elif nota >= 5:
        calificacion = "Aprobado"
    else:
        calificacion = "Suspenso"
        
    return calificacion

print(clasificar_nota(8))    # Notable
