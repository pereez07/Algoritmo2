def clasificar_imc(peso, altura):
    if peso <= 0 or altura <= 0:
        raise ValueError("Error: El peso y la altura deben ser mayores que 0.")
        
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        categoria = "Bajo peso"
    elif imc < 25:
        categoria = "Normal"
    else:
        categoria = "Sobrepeso"
        
    return categoria

resultado_1 = clasificar_imc(60, 1.70)
print(f"CLASIFICAR_IMC(60, 1.70) -> {resultado_1}")

resultado_2 = clasificar_imc(80, 1.75)
print(f"CLASIFICAR_IMC(80, 1.75) -> {resultado_2}")