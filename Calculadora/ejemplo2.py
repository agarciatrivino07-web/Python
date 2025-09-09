# ejemplo2
# Calculadora con Python
"""
(1) suma
(2) resta
(3) multi
(4) division
"""
print ('Bienvenido a la calculadora de Axel, espero que cumpla su función' .center(50,'-'))
print  ('Opcion 1 Suma, Opcion 2 Resta, Opcion 3 Multiplicacion, Opcion 4 Division,     ')

variable1 = float(input('Primer valor'))
variable2 = float(input('Segundo valor'))

def calculadora(num1, num2, opcion):
    opcion = int(input("Elige una opcion"))
    if opcion == 1:
        print(f'El resultado de la suma de {num1} y {num2}: {num1 + num2}')
    elif opcion == 2:
        print(f'El resultado de la resta de {num1} y {num2}: {num1 - num2}')
    elif opcion == 3:
        print(f'El resultado de la multiplicacion de {num1} y {num2}: {num1 * num2}')  

    elif opcion == 4: 
        if num2 == 0:
            print("Error: No se puede dividir  entre cero. ")
        else: 
            print(f"El resultado de la division es: {num1 / num2}")
        continuar = input("¿Quieres realizar otra operacion (si/no):").lower() 
        if continuar != "no":
            return 0;
        if continuar != "si":
            print("¡Gracias por usar la calculadora! Hasta luego.")
        while True:
            num2 = input("Pon un numero")
            # Solicitamos la entrada al usuario
            if num2.isdigit():
                num2 = int(opcion)
                print(f"Numero valido: {opcion}")
                break
            else:
                print("Entrada invalida, solo admite numeros")
    
    else: 
        print('Te equivocaste de opcion')

calculadora(variable1,variable2,2,)

print('Finalizada la operacion, gracias por utilizar mi servicio')
