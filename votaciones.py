def puede_votar(edad):
    # Comprobar si la entrada es menor o igual a 0
    if edad <= 0:
        raise ValueError("Error: La edad debe ser mayor que 0.")
        
    resultado = (edad >= 18) and (edad < 120)
    return resultado

resultado_1 = puede_votar(25)
print(f"PUEDE_VOTAR(25) -> {resultado_1}")

resultado_2 = puede_votar(15)
print(f"PUEDE_VOTAR(15) -> {resultado_2}")

resultado_3 = puede_votar(130)
print(f"PUEDE_VOTAR(130) -> {resultado_3}")

