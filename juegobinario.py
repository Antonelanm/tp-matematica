import random

def decimal_a_binario(n):
    return bin(n)[2:]

def binario_a_decimal(b):
    return int(b, 2)

print("Bienvenidos a ***Adivinanza Binaria***")

while True:
    print("\n========================")
    print("MENÚ PRINCIPAL:")
    print("1. ¿Qué número decimal representa este número binario?")
    print("2. ¿Qué número binario representa este número decimal?")
    print("3. ¿Cuál es el resultado de una operación AND entre estos dos binarios?")
    print("4. Salir")
    print("========================")

    opcion = input("Elegí una opción (1-4): ")

    if opcion == "1":
        numero = random.randint(1, 20)
        binario = decimal_a_binario(numero)
        incorrecto = numero + random.choice([-2, -1, 1, 2])
        while incorrecto == numero or incorrecto < 0:
            incorrecto = numero + random.choice([-2, -1, 1, 2])
        opciones = [numero, incorrecto]
        random.shuffle(opciones)
        print(f"\n¿Qué número decimal representa este binario?: {binario}")
        print(f"a) {opciones[0]}")
        print(f"b) {opciones[1]}")
        respuesta = input("Elegí entre las siguienes opciones : a o b ").lower()
        elegido = opciones[0] if respuesta == "a" else opciones[1]
        if elegido == numero:

            print(" ---------------- Si, correcto!!--------------")
        else:
            print(f" xxxxxxxxxxxxxxx Incorrecto. La respuesta correcta era: {numero} xxxxxxxxxxxx")

    elif opcion == "2":
        numero = random.randint(1, 20)
        binario = decimal_a_binario(numero)
        incorrecto = numero + random.choice([-2, -1, 1, 2])
        while incorrecto == numero or incorrecto < 0:
            incorrecto = numero + random.choice([-2, -1, 1, 2])
        bin_incorrecto = decimal_a_binario(incorrecto)
        opciones = [binario, bin_incorrecto]
        random.shuffle(opciones)

        print(f"\n¿Qué número binario representa este decimal?: {numero}")
        print(f"a) {opciones[0]}")
        print(f"b) {opciones[1]}")
        respuesta = input("Elegí a o b: ").lower()
        elegido = opciones[0] if respuesta == "a" else opciones[1]
        if elegido == binario:
            print("---------------¡Correcto! Felicitaciones :) ---------------")
        else:
            print(f"xxxxxxxxxxxxx Incorrecto :( La respuesta correcta era: {binario} xxxxxxxxxxx")

    elif opcion == "3":
        binario_1 = decimal_a_binario(random.randint(1, 20))
        binario_2 = decimal_a_binario(random.randint(1, 20))
        print(f"\n¿Resultado de la operación AND entre los siguientes binarios?")
        print(f"a) {binario_1}")
        print(f"b) {binario_2}")
        resultado_and = bin(int(binario_1, 2) & int(binario_2, 2))[2:]
        print(f"¿Cuál es el resultado de la operación AND?")
        print(f"a) {resultado_and}")
        print(f"b) {bin(int(binario_1, 2) & int(binario_2, 2) + 1)[2:]}")
        respuesta = input("Elegí a o b: ").lower()
        if respuesta == "a":
            print("---------------------Si! Correcto.-----------------")
        else:
            print(f"xxxxxxxxxxxxxx Incorrecto. La respuesta correcta era: {resultado_and} xxxxxxxxxxxxx")

    elif opcion == "4":
        print("Gracias por jugar. Espero que vuelvas pronto ")
        break

    else:
        print("Opción inválida. Por favor elegí 1, 2, 3 o 4.")
