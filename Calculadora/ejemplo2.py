# Calculadora con Python
"""
(1) suma
(2) resta
(3) multi
(4) division
(5) raiz cuadrada
"""

print ('Bienvenido a la calculadora de Axel, espero que cumpla su función' .center(50,'-'))
print(' Opcion 1 Suma',('\n'),'Opcion 2 Resta',('\n'),'Opcion 3 Multiplicacion',('\n'),'Opcion 4 Division',('\n'),'Opcion 5 Raiz cuadrada')

variable1 = int(input('Primer valor''\n'))
variable2 = int(input('Segundo valor''\n'))


def calculadora (num1, num2, opcion):

    opcion = int(input("Elige una opcion" '\n'))
    if opcion == 1:
        print(f'El resultado de la suma de {num1} + {num2}: {num1 + num2}')
    elif opcion == 2:
            print(f'El resultado de la resta de {num1} - {num2}: {num1 - num2}')
    elif opcion == 3:
        print(f'El resultado de la multiplicacion de {num1} * {num2}: {num1 * num2}')  

    elif opcion == 5:
        print(f'El resultado de la raiz cuadrada es {num1} y {num1} : {num1 / 2}')

    elif opcion == 4: 
        if num2 == 0:
            print("Error: No se puede dividir  entre cero. ")
        else: 
            print(f"El resultado de la division es: {num1 / num2}")
            continuar = input("¿Quieres realizar otra operacion (si/no):").lower()

        if continuar != "si":
            print("Fin del programa")
            return 0; 
    
        si = True
        no = False
        
        if si:
            calculadora(num1, num2, opcion)
        

        """else:
            while True:
                num2 = input("Pon un numero")
                # Solicitamos la entrada al usuario
                if num2.isdigit():
                    num2 = int(opcion)
                    print(f"Numero invalido: {opcion}")
                    break
            else:
                print("Entrada invalida, solo admite números")
        """

    else: 
        print('Te equivocaste de opcion')

calculadora(variable1,variable2,2,)

print('Finalizada la operacion, gracias por utilizar mi servicio')
