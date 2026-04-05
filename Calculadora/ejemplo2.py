# Calculadora con Python
"""
(1) suma
(2) resta
(3) multiplicación
(4) división
(5) raíz cuadrada
"""
print(f'=== Menú ===')
print(f'Bienvenido a la calculadora de Axel, espero que cumpla su función' .center(60,'-'))
print(f'Opcion 1 Suma',('\n'),'Opcion 2 Resta',('\n'),'Opcion 3 Multiplicación',('\n'),'Opcion 4 Division',('\n'))

try:
    variable1 = int(input('Primer valor''\n'))
    variable2 = int(input('Segundo valor''\n'))
except ValueError:
    print(f'Solo admite números')

def calculadora (num1, num2, opcion):

    try:
        opcion = int(input("Elige una opcion"))
    except ValueError:
        print(f'Solo admite números')


    if opcion == 1:
        print(f'El resultado de la suma de {num1} + {num2}: {num1 + num2}')
        continuar = input("¿Quieres seguir utilizando el servicio? (si/no)")
        if continuar != "si":
            print(" Fin del programa")
            return 0
        else:
            print(f'Introduce los valores')
            calculadora(num1, num2,opcion)

    elif opcion == 2:
        print(f'El resultado de la resta de {num1} - {num2}: {num1 - num2}')
        continuar = input("¿Quieres seguir utilizando el servicio? (si/no)")
        if continuar != "si":
            print(" Fin del programa")
            return 0
        else:
            print(f'Introduce los valores')
            calculadora(num1, num2,opcion)    
    elif opcion == 3:
        print(f'El resultado de la multiplicacion de {num1} * {num2}: {num1 * num2}')
        continuar = input("¿Quieres seguir utilizando el servicio? (si/no)")
        if continuar != "si":
            print(" Fin del programa")
            return 0
        else:
            print(f'Introduce los valores')
            calculadora(num1, num2,opcion)
    elif opcion == 4: 
        if num2 == 0:
            print("Error: No se puede dividir  entre cero. ")
        else: 
            print(f"El resultado de la division es: {num1 / num2}")
            continuar = input("¿Quieres realizar otra operacion (si/no):").lower()
            
        if continuar != "si":
            print("Fin del programa")
            return 0
    
        si = True
        no = False
        
        if si:
            calculadora(num1, num2, opcion)
    else: 
        print('Te equivocaste de opción')
        print(f'Inserta otra vez la opción deseada')
        calculadora(num1, num2,opcion)

calculadora(variable1,variable2,2)
print('Finalizada la operación, gracias por utilizar mi servicio')
