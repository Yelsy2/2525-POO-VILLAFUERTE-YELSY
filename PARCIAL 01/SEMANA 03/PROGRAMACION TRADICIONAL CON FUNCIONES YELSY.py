# Función para pedir las temperaturas de los 7 días
def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio
def calcular_promedio(temperaturas):
    total = sum(temperaturas)
    promedio = total / len(temperaturas)
    return promedio

# Función principal para controlar el flujo del programa
def main():
    print("=== PROMEDIO SEMANAL DEL CLIMA ===")
    temps = ingresar_temperaturas()
    promedio = calcular_promedio(temps)
    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f}°C")

# Ejecutar el programa
main()
