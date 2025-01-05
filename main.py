import time

""" 
Resultado hasa 1M:

PC: Intel Core i5-7200U 2.50GHz
Cantidad de números primos hasta 1000000: 78498
Tiempo de ejecución: 3.92 segundos

Raspberry Pi 4: ARM Cortex-A72 1.5GHz
Cantidad de números primos hasta 1000000: 78498
Tiempo de ejecución: 9.77 segundos

Resultado hasa 10M:

PC: Intel Core i5-7200U 2.50GHz
Cantidad de números primos hasta 10000000: 664579
Tiempo de ejecución: 119.63 segundos

Raspberry Pi 4: ARM Cortex-A72 1.5GHz
Cantidad de números primos hasta 10000000: 664579
Tiempo de ejecución: 253.11 segundos

"""
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    limite = 10000000
    contador_primos = 0

    # Inicia la medición de tiempo
    inicio = time.time()

    for i in range(2, limite + 1):
        if es_primo(i):
            contador_primos += 1

    # Termina la medición de tiempo
    fin = time.time()
    duracion = fin - inicio

    print(f"Cantidad de números primos hasta {limite}: {contador_primos}")
    print(f"Tiempo de ejecución: {duracion:.2f} segundos")

if __name__ == "__main__":
    main()
