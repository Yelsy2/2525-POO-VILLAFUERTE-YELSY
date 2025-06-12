# Clase que representa las temperaturas de la semana
class ClimaSemanal:
    def __init__(self):
        self.temperaturas = []

    # Método para ingresar temperaturas
    def ingresar_datos(self):
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
            self.temperaturas.append(temp)

    # Método para calcular el promedio
    def calcular_promedio(self):
        total = sum(self.temperaturas)
        promedio = total / len(self.temperaturas)
        return promedio

# Crear objeto y usar métodos
def main():
    print("=== PROMEDIO SEMANAL DEL CLIMA (POO) ===")
    clima = ClimaSemanal()
    clima.ingresar_datos()
    promedio = clima.calcular_promedio()
    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f}°C")

# Ejecutar el programa
main()
