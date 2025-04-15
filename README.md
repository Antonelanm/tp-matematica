Este es el trabajo integrador de matemática 

1. Importar librería:
import random

Aquí se importa la librería random, que permite generar números aleatorios. Esto es necesario para crear preguntas con números al azar más adelante.


2. Definir funciones:
Función decimal_a_binario:

def decimal_a_binario(n):
    return bin(n)[2:]

Esta función convierte un número decimal (base 10) a binario (base 2).


La función bin(n) convierte el número decimal n a binario, pero la conversión incluye un prefijo ('0b') que indica que es binario. El [2:] elimina ese prefijo.


Función binario_a_decimal:

def binario_a_decimal(b):
    return int(b, 2)

Esta función convierte un número binario (como una cadena de texto) a su valor decimal.


La función int(b, 2) convierte el número binario b (pasado como cadena de texto) a decimal usando la base 2.


3. Inicio del programa y mensaje de bienvenida:

print("Bienvenidos a ***Adivinanza Binaria***")

Se muestra un mensaje de bienvenida en la pantalla al iniciar el programa.



4. Menú de opciones:

while True:
    print("\n========================")
    print("MENÚ PRINCIPAL:")
    print("1. ¿Qué número decimal representa este número binario?")
    print("2. ¿Qué número binario representa este número decimal?")
    print("3. ¿Cuál es el resultado de una operación AND entre estos dos binarios?")
    print("4. Salir")
    print("========================")

Aquí empieza un bucle while que se ejecuta constantemente hasta que el jugador elija salir.


Se muestra un menú con 4 opciones para que el jugador elija qué tipo de pregunta quiere responder.


5. Leer la opción elegida por el jugador:

opcion = input("Elegí una opción (1-4): ")

El jugador ingresa una opción (1, 2, 3 o 4) para elegir qué tipo de pregunta quiere responder.


6. Opción 1 - ¿Qué número decimal representa este número binario?

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
    respuesta = input("Elegí entre las siguientes opciones : a o b ").lower()
    elegido = opciones[0] if respuesta == "a" else opciones[1]
    if elegido == numero:
        print(" ---------------- Si, correcto!!--------------")
    else:
        print(f" xxxxxxxxxxxxxxx Incorrecto. La respuesta correcta era: {numero} xxxxxxxxxxxx")

En esta opción, el programa genera un número decimal aleatorio entre 1 y 20.


Luego convierte ese número a binario y crea una opción incorrecta sumándole o restándole un valor pequeño al número original.


Se muestran dos opciones (una correcta y otra incorrecta) y el jugador debe elegir la respuesta correcta.


Si el jugador elige la opción correcta, se muestra un mensaje de éxito; si no, se muestra un mensaje de error.


7. Opción 2 - ¿Qué número binario representa este número decimal?

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

Similar a la opción 1, pero ahora el programa genera un número decimal y convierte ese número a binario.


Luego crea una opción incorrecta convirtiendo otro número a binario.


El jugador debe elegir cuál de las dos representaciones binarias corresponde al número decimal mostrado.


8. Opción 3 - Resultado de una operación AND entre dos binarios:

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

En esta opción, se generan dos números binarios aleatorios.


Luego se realiza una operación AND entre esos dos números binarios. La operación AND compara bit por bit dos números binarios y devuelve 1 si ambos bits son 1, o 0 en cualquier otro caso.


El jugador debe elegir cuál es el resultado correcto de esa operación entre dos opciones.


9. Opción 4 - Salir:

elif opcion == "4":
    print("Gracias por jugar. Espero que vuelvas pronto ")
    break

Si el jugador elige la opción 4, el programa imprime un mensaje de despedida y luego termina el bucle, saliendo del programa.


10. Opción inválida:

else:
    print("Opción inválida. Por favor elegí 1, 2, 3 o 4.")

Si el jugador ingresa una opción fuera de las opciones válidas (1, 2, 3, o 4), el programa le avisa que la opción es incorrecta y le pide que elija de nuevo.


